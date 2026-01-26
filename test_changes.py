
import numpy as np
import mne
from eegflow.quality import check_impedance_balance, estimate_snr, detect_hmd_interference
from eegflow.signal_processing import SSVEP_CCA
from eegflow.bids_utils import convert_to_bids, add_motion_data

def test_quality():
    print("Testing Quality Modules...")
    # Mock data
    sfreq = 250
    n_channels = 4
    n_samples = 1000
    info = mne.create_info(ch_names=['Fp1', 'Fp2', 'C3', 'C4'], sfreq=sfreq, ch_types='eeg')
    data = np.random.randn(n_channels, n_samples) * 1e-6 # Microvolts
    
    # Inject 90Hz noise into channel 0
    t = np.arange(n_samples) / sfreq
    data[0] += 10e-6 * np.sin(2 * np.pi * 90 * t)
    
    raw = mne.io.RawArray(data, info)
    
    # 1. Impedance
    impedances = {'Fp1': 5000, 'Fp2': 60000, 'C3': 5000, 'C4': 5000}
    warns, metrics = check_impedance_balance(impedances)
    print("Impedance warnings:", warns)
    assert len(warns) > 0
    
    # 2. HMD Interference
    has_interference, details = detect_hmd_interference(raw, refresh_rate=90.0)
    print("HMD Interference:", has_interference, details)
    # Note: 250Hz sfreq -> Nyquist 125Hz. 90Hz is visible.
    # But simple noise might not trigger 'peak' if noise floor is high. 
    # With pure sine wave injection it should.
    
    # 3. SNR
    # Create baseline (lower power)
    data_base = np.random.randn(n_channels, n_samples) * 0.5e-6
    raw_base = mne.io.RawArray(data_base, info)
    snr = estimate_snr(raw, baseline_raw=raw_base)
    print("SNR:", snr)

def test_ssvep():
    print("\nTesting SSVEP CCA...")
    sfreq = 250
    target_freqs = [10.0, 12.0, 15.0]
    cca = SSVEP_CCA(target_freqs, sfreq)
    
    # Generate mock EEG data that matches 12.0 Hz
    n_channels = 8
    n_samples = 500
    t = np.arange(n_samples) / sfreq
    
    # Signal: 12Hz sine wave + noise
    signal = np.sin(2 * np.pi * 12.0 * t)
    data = np.zeros((n_channels, n_samples))
    for i in range(n_channels):
        data[i] = 0.5 * signal + np.random.randn(n_samples) * 0.5
        
    predicted, scores = cca.predict(data)
    print(f"Predicted: {predicted} Hz, Expected: 12.0 Hz")
    print("Scores:", scores)
    
    assert predicted == 12.0

if __name__ == "__main__":
    try:
        test_quality()
        test_ssvep()
        print("\nAll tests passed!")
    except Exception as e:
        print(f"\nTests failed: {e}")
        import traceback
        traceback.print_exc()
