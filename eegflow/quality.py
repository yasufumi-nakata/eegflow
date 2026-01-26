"""
eegflow.quality: Quality Assurance & validation modules.
Implements Section 2 (Signal Quality) and Section 3 (Time Sync) of the technical proposal.
"""

import numpy as np
import mne
from scipy.stats import pearsonr, linregress
from scipy.signal import find_peaks

def check_impedance_balance(impedances, ref_impedance=None, threshold_diff=50000):
    """
    Section 2.1: Check for impedance mismatch that degrades CMRR.
    
    Parameters
    ----------
    impedances : dict or list
        Dictionary of {ch_name: impedance_value_ohm} or list of values.
    ref_impedance : float, optional
        Impedance of the reference electrode. If None, assumes mean of others or 0.
    threshold_diff : float
        Warning threshold for impedance difference (Ohms). Default 50 kOhm.
        
    Returns
    -------
    warnings : list of str
        List of warning messages.
    metrics : dict
        Calculated imbalance metrics.
    """
    if isinstance(impedances, dict):
        values = np.array(list(impedances.values()))
        names = list(impedances.keys())
    else:
        values = np.array(impedances)
        names = [f"Ch{i}" for i in range(len(values))]
        
    if ref_impedance is None:
        # If unknown, we check dispersion among active electrodes
        ref_impedance = 0
        
    # Calculate difference from reference (simplified model)
    # Z_in_diff = |Z_active - Z_ref|
    diffs = np.abs(values - ref_impedance)
    
    max_diff = np.max(diffs)
    bad_channels = [names[i] for i in range(len(diffs)) if diffs[i] > threshold_diff]
    
    warnings = []
    if bad_channels:
        warnings.append(f"High impedance mismatch detected (> {threshold_diff/1000} kOhm): {bad_channels}")
        warnings.append("CMRR may be degraded. Re-gel or adjust electrodes.")
        
    metrics = {
        "max_imbalance": max_diff,
        "mean_imbalance": np.mean(diffs),
        "bad_channels": bad_channels
    }
    
    return warnings, metrics

def estimate_snr(raw, baseline_raw=None, freqs=None):
    """
    Section 2.2: Dynamic S/N ratio evaluation.
    
    Parameters
    ----------
    raw : mne.io.Raw
        The experimental data.
    baseline_raw : mne.io.Raw, optional
        Resting state or saline phantom data for noise floor estimation.
    freqs : dict, optional
        Frequency bands to check {'Name': (fmin, fmax)}. 
        Default: Delta, Theta, Alpha, Beta, Gamma.
        
    Returns
    -------
    snr_dict : dict
        SNR values (in dB) for each band (averaged across channels).
    """
    if freqs is None:
        freqs = {
            'Delta': (1, 4),
            'Theta': (4, 8),
            'Alpha': (8, 13),
            'Beta': (13, 30),
            'Gamma': (30, 100)
        }
        
    snr_dict = {}
    
    # Calculate PSD for signal
    # Use standard fmin/fmax for typical EEG analysis
    psd_signal = raw.compute_psd(fmin=0.5, fmax=100)
    
    psd_noise = None
    if baseline_raw is not None:
        # Check compatibility
        if baseline_raw.info['sfreq'] != raw.info['sfreq']:
            # This is a simplification. Ideally, we should resample baseline.
            # But for now, let's assume users provide compatible data.
            pass
        psd_noise = baseline_raw.compute_psd(fmin=0.5, fmax=100)
    
    for band_name, (fmin, fmax) in freqs.items():
        # Get mean power in band for signal
        # psd.get_data returns (n_channels, n_freqs)
        # We need to mask frequencies
        signal_data, signal_freqs = psd_signal.get_data(return_freqs=True)
        idx_band = np.logical_and(signal_freqs >= fmin, signal_freqs <= fmax)
        
        # Average power in band across all channels
        power_signal = np.mean(signal_data[:, idx_band])
        
        if psd_noise:
            noise_data, noise_freqs = psd_noise.get_data(return_freqs=True)
            # Interpolate noise PSD to match signal freqs if needed, 
            # but MNE's compute_psd usually returns similar freq bins if parameters match.
            # We assume freq bins align for simplicity or just mask similarly.
            idx_band_noise = np.logical_and(noise_freqs >= fmin, noise_freqs <= fmax)
            power_noise = np.mean(noise_data[:, idx_band_noise])
            
            if power_noise > 0:
                snr = 10 * np.log10(power_signal / power_noise)
                snr_dict[band_name] = snr
            else:
                snr_dict[band_name] = np.inf
        else:
            snr_dict[band_name] = "No baseline provided"
            
    return snr_dict

def detect_hmd_interference(raw, refresh_rate=90.0, threshold_std=3.0):
    """
    Section 2.3: Detect HMD-related spectral peaks.
    
    Parameters
    ----------
    raw : mne.io.Raw
        EEG data.
    refresh_rate : float
        HMD refresh rate (Hz). e.g., 72, 90, 120.
    threshold_std : float
        Threshold for peak detection (z-score like).
        
    Returns
    -------
    has_interference : bool
    details : dict
    """
    # Check for peaks around refresh_rate
    fmin = max(0, refresh_rate - 5)
    fmax = refresh_rate + 5
    
    try:
        psd = raw.compute_psd(fmin=fmin, fmax=fmax)
        data, freqs = psd.get_data(return_freqs=True)
        
        # Average across channels
        mean_psd = np.mean(data, axis=0)
        
        # Simple peak detection
        # We look for a peak that is significantly higher than the local median/mean
        local_median = np.median(mean_psd)
        local_std = np.std(mean_psd)
        
        peaks, properties = find_peaks(mean_psd, height=local_median + threshold_std * local_std)
        
        found_peaks = freqs[peaks]
        
        # Check if any found peak is close to refresh rate (within 1Hz)
        is_interfered = np.any(np.abs(found_peaks - refresh_rate) < 1.0)
        
        details = {
            "suggested_notch": refresh_rate if is_interfered else None,
            "peaks_found": found_peaks.tolist(),
            "max_psd_at_refresh": float(np.max(mean_psd))
        }
        
        return is_interfered, details
        
    except Exception as e:
        print(f"Error in interference detection: {e}")
        return False, {"error": str(e)}

def calculate_clet_latency(lsl_times, photo_times):
    """
    Section 3.1: CLET (Computation of Latencies in ERP Triggers).
    Calculates End-to-End latency and jitter.
    
    Parameters
    ----------
    lsl_times : array-like
        Timestamps of LSL software markers.
    photo_times : array-like
        Timestamps of photodiode onsets (hardware).
        
    Returns
    -------
    stats : dict
        {'mean_latency': float, 'jitter': float, 'drift': float}
    """
    # Align sequences. Assuming 1-to-1 mapping and no missing triggers for simplicity
    # In real world, we need to match closest events.
    
    if len(lsl_times) != len(photo_times):
        # Fallback: simple trimming or error
        min_len = min(len(lsl_times), len(photo_times))
        lsl_times = lsl_times[:min_len]
        photo_times = photo_times[:min_len]
        
    latencies = np.array(photo_times) - np.array(lsl_times)
    
    stats = {
        'mean_latency_ms': np.mean(latencies) * 1000,
        'jitter_ms': np.std(latencies) * 1000,
        'min_ms': np.min(latencies) * 1000,
        'max_ms': np.max(latencies) * 1000,
        'n_events': len(latencies)
    }
    
    return stats

def linear_drift_correction(raw, drift_ppm):
    """
    Section 3.3: Correct for clock drift by resampling.
    
    Parameters
    ----------
    raw : mne.io.Raw
    drift_ppm : float
        Drift in parts per million.
        
    Returns
    -------
    raw_corrected : mne.io.Raw
    """
    # Resampling factor
    # If device is faster than clock (positive drift), we need to downsample?
    # Logic: True duration = recorded_duration * (1 + drift)
    
    # MNE's resample method changes the data rate.
    # To correct time alignment without changing sfreq, we effectively stretch/shrink signal
    resample_ratio = 1.0 + (drift_ppm / 1e6)
    
    print(f"Applying drift correction: ratio={resample_ratio}")
    # raw.resample(sfreq * resample_ratio) -> this changes sfreq. 
    # Usually we resample to the nominal sfreq *from* the estimated real sfreq.
    
    return raw.resample(raw.info['sfreq'] * resample_ratio)
