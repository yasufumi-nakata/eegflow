"""
eegflow.signal_processing: Advanced signal processing modules.
Implements Section 4 (Artifact Removal) and Section 5 (Specialized Analysis).
"""

import numpy as np
import mne
from sklearn.cross_decomposition import CCA
from scipy.signal import welch

# Optional imports for advanced features
try:
    from meegkit import asr
    HAS_MEEGKIT = True
except ImportError:
    HAS_MEEGKIT = False

try:
    from mne_icalabel import label_components
    HAS_ICALABEL = True
except ImportError:
    HAS_ICALABEL = False


def apply_asr(raw, sfreq, cutoff=20.0):
    """
    Section 4.1: Artifact Subspace Reconstruction (ASR).
    Requires 'meegkit'.
    
    Parameters
    ----------
    raw : mne.io.Raw
        The raw data (must be loaded).
    sfreq : float
        Sampling frequency.
    cutoff : float
        Standard deviation cutoff for rejection.
        
    Returns
    -------
    raw_clean : mne.io.Raw
        Cleaned data.
    """
    if not HAS_MEEGKIT:
        print("Warning: meegkit not installed. ASR skipped.")
        return raw
        
    data = raw.get_data() # (n_channels, n_times)
    # meegkit expects (n_times, n_channels)
    data = data.T
    
    # Train on "clean" portion? 
    # Standard ASR uses a calibration period. If not provided, it finds one.
    asr_model = asr.ASR(method='euclid')
    
    # Train (using the whole data as calibration for simplicity here, 
    # ideally should use a resting baseline)
    train_idx = int(data.shape[0] * 0.1) # Use first 10% for calibration? Or let ASR find it
    # Ideally: train_data, _ = asr_train(data, sfreq)
    
    # Using fit_transform from meegkit (simplified usage)
    try:
        clean_data, sample_mask = asr_model.fit_transform(data, sfreq)
        
        # Put back into Raw
        raw_clean = raw.copy()
        raw_clean._data = clean_data.T
        return raw_clean
    except Exception as e:
        print(f"ASR failed: {e}")
        return raw

def apply_iclabel_classification(raw, ica):
    """
    Section 4.3: ICA classification using ICLabel.
    
    Parameters
    ----------
    raw : mne.io.Raw
    ica : mne.preprocessing.ICA
    
    Returns
    -------
    labels : dict
        Dictionary of component labels.
    """
    if not HAS_ICALABEL:
        print("Warning: mne-icalabel not installed.")
        return {}
        
    label_dict = label_components(raw, ica, method='iclabel')
    
    # Print summary
    print("ICLabel Results:")
    for i, label in enumerate(label_dict['labels']):
        prob = label_dict['y_pred_proba'][i]
        print(f"  IC #{i}: {label} ({prob:.2f})")
        
    return label_dict

def calculate_barycenter_frequency(raw, fmin=4, fmax=13):
    """
    Section 5.1: Barycenter Frequency (Spectral Centroid) for VR sickness.
    Shift to lower frequencies indicates discomfort.
    
    Returns
    -------
    centroid : float
        Weighted mean frequency.
    """
    psd = raw.compute_psd(fmin=fmin, fmax=fmax)
    psd_data, freqs = psd.get_data(return_freqs=True)
    
    # Average across channels
    mean_psd = np.mean(psd_data, axis=0)
    
    # Calculate centroid: sum(f * p(f)) / sum(p(f))
    numerator = np.sum(freqs * mean_psd)
    denominator = np.sum(mean_psd)
    
    if denominator == 0:
        return 0
    return numerator / denominator

class SSVEP_CCA:
    """
    Section 5.2: Canonical Correlation Analysis for SSVEP.
    """
    def __init__(self, target_freqs, sfreq, n_harmonics=2):
        self.target_freqs = target_freqs
        self.sfreq = sfreq
        self.n_harmonics = n_harmonics
        self.refs = self._generate_refs(target_freqs, sfreq, n_harmonics)
        self.cca = CCA(n_components=1)
        
    def _generate_refs(self, freqs, sfreq, harmonics):
        """Generate sin/cos reference signals."""
        # Refs are generated dynamically in predict based on data length
        # This method might store pre-computed templates if length is fixed,
        # but for flexibility we can keep it empty or return configuration.
        return {}
        
    def predict(self, eeg_data):
        """
        Predict the target frequency from EEG data using CCA.
        
        Parameters
        ----------
        eeg_data: np.ndarray
            (n_channels, n_samples)
            
        Returns
        -------
        predicted_freq : float
        scores : list of float
            Correlation coefficients for each target frequency.
        """
        n_samples = eeg_data.shape[1]
        t = np.arange(n_samples) / self.sfreq
        
        scores = []
        for freq in self.target_freqs:
            # Generate reference for this duration
            Y = []
            for h in range(1, self.n_harmonics + 1):
                Y.append(np.sin(2 * np.pi * h * freq * t))
                Y.append(np.cos(2 * np.pi * h * freq * t))
            Y = np.array(Y).T # (n_samples, 2*n_harmonics)
            X = eeg_data.T    # (n_samples, n_channels)
            
            # Center the data
            X = X - np.mean(X, axis=0)
            Y = Y - np.mean(Y, axis=0)
            
            self.cca.fit(X, Y)
            # Correlation is the score
            # CCA.score returns coefficient of determination R^2, we want correlation.
            # Using transform to get canonical variates
            Xc, Yc = self.cca.transform(X, Y)
            
            # Canonical correlation is the correlation between the first pair of canonical variates
            # Xc and Yc are (n_samples, n_components). We want correlation of column 0.
            corr = np.corrcoef(Xc[:, 0], Yc[:, 0])[0, 1]
            scores.append(corr)
            
        return self.target_freqs[np.argmax(scores)], scores
