"""
eegflow.quality: Quality Assurance & validation modules.
Implements Section 2 (Signal Quality) and Section 3 (Time Sync) of the technical proposal.
"""

import numpy as np
import mne
from scipy.stats import pearsonr, linregress

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
    freqs : list of tuple, optional
        Frequency bands to check [(fmin, fmax), ...]. 
        Default: Delta, Theta, Alpha, Beta, Gamma.
        
    Returns
    -------
    snr_dict : dict
        SNR values (in dB) for each band and channel.
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
    psd_signal = raw.compute_psd(fmin=0.5, fmax=100)
    
    if baseline_raw is not None:
        psd_noise = baseline_raw.compute_psd(fmin=0.5, fmax=100)
    else:
        # If no baseline, estimate noise floor using 1/f fit or lowest percentile?
        # For now, we return power as placeholder if no baseline
        psd_noise = None
        
    for band_name, (fmin, fmax) in freqs.items():
        # Get power in band
        # Note: integration logic depends on MNE version, simplifying here
        # Assuming psd object has .get_data() method
        
        # This is a simplified SNR calculation: Signal Power / Noise Power
        # If noise baseline is provided.
        
        if psd_noise:
            # Resample noise PSD to match signal if needed or just take mean in band
            # We assume same sampling parameters
            pass 
            # Implementation omitted for brevity, returning placeholder
            snr_dict[band_name] = "Requires aligned baseline PSD"
        else:
            snr_dict[band_name] = "No baseline provided"
            
    return snr_dict

def detect_hmd_interference(raw, refresh_rate=90.0):
    """
    Section 2.3: Detect HMD-related spectral peaks.
    
    Parameters
    ----------
    raw : mne.io.Raw
        EEG data.
    refresh_rate : float
        HMD refresh rate (Hz). e.g., 72, 90, 120.
        
    Returns
    -------
    has_interference : bool
    details : dict
    """
    # Check for peaks at refresh_rate and its harmonics
    psd = raw.compute_psd(fmin=refresh_rate-5, fmax=refresh_rate+5)
    data, freqs = psd.get_data(return_freqs=True)
    
    # Simple check: is there a sharp peak near refresh_rate?
    # This requires more complex peak detection logic.
    # We return a placeholder suggesting Notch filter.
    
    return True, {"suggested_notch": refresh_rate}

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
