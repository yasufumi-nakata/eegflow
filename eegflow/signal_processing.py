"""
eegflow.signal_processing: Advanced signal processing modules.
Implements Section 4 (Artifact Removal) and Section 5 (Specialized Analysis).
"""

import numpy as np
import mne
from sklearn.cross_decomposition import CCA
from scipy.signal import welch
import scipy.linalg

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


def apply_asr(raw, sfreq, cutoff=20.0, method='riemann'):
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
    method : str
        Distance metric ('euclid' or 'riemann'). 
        'riemann' is recommended for better handling of non-stationary noise (Anders et al., 2020).
        
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
    asr_model = asr.ASR(method=method)
    
    # Train (using the whole data as calibration for simplicity here, 
    # ideally should use a resting baseline)
    train_idx = int(data.shape[0] * 0.1) # Use first 10% for calibration? Or let ASR find it
    # Ideally: train_data, _ = asr_train(data, sfreq)
    
    # Using fit_transform from meegkit (simplified usage)
    try:
        clean_data, sample_mask = asr_model.fit_transform(data, sfreq, cutoff=cutoff)
        
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

def apply_adaptive_filter(eeg_data, ref_data, filter_type='rls', order=5, forgetting_factor=0.99):
    """
    Section 4.2: Adaptive filtering using motion reference (Sensor Fusion).
    
    Parameters
    ----------
    eeg_data : np.ndarray
        (n_channels, n_samples)
    ref_data : np.ndarray
        (n_ref_channels, n_samples) - Reference noise signals (e.g. IMU).
    filter_type : str
        'rls' (Recursive Least Squares) or 'lms' (Least Mean Squares).
    order : int
        Filter order (number of taps).
    forgetting_factor : float
        For RLS, lambda (0 < lambda <= 1). Closer to 1 means longer memory.
        
    Returns
    -------
    clean_eeg : np.ndarray
        (n_channels, n_samples)
    """
    n_channels, n_samples = eeg_data.shape
    n_ref, n_ref_samples = ref_data.shape
    
    if n_samples != n_ref_samples:
        raise ValueError("EEG and Reference data must have same length.")
        
    clean_eeg = np.zeros_like(eeg_data)
    
    # Simple RLS implementation
    # We treat each EEG channel independently
    # Input vector x(n) is constructed from current and past values of reference channels
    # To simplify, if we have multiple ref channels, the input vector size is n_ref * order
    
    # Initialize RLS variables
    M = n_ref * order # Total weights
    lam = forgetting_factor
    delta = 1.0 # Initial correlation matrix diagonal
    
    # Pre-construct the input matrix X (n_samples, M)
    # Pad reference for delays
    ref_padded = np.pad(ref_data, ((0,0), (order-1, 0)), mode='constant')
    
    X = np.zeros((n_samples, M))
    for i in range(n_samples):
        window = ref_padded[:, i : i+order] # (n_ref, order)
        # Flatten and reverse time so newest is first
        X[i, :] = window[:, ::-1].flatten() 
        
    # Now run RLS for each channel
    for ch in range(n_channels):
        d = eeg_data[ch, :]
        w = np.zeros(M)
        P = (1.0/delta) * np.eye(M)
        
        for n in range(n_samples):
            x_n = X[n]
            
            # RLS update
            Px = P @ x_n
            # Denominator: lam + x^T P x
            denom = lam + x_n @ Px
            g = Px / denom
            
            # A priori error
            alpha = d[n] - w @ x_n
            
            # Update weights
            w = w + g * alpha
            
            # Update P
            # P = (1/lam) * (P - g @ x_n.T @ P) 
            # Note: g is vector, x_n is vector. Outer product.
            # Using Px which is P @ x_n
            P = (1/lam) * (P - np.outer(g, Px))
            
            # The cleaned signal is the error (e)
            # We use a priori error as approximation or compute a posteriori
            clean_eeg[ch, n] = alpha 
            
    return clean_eeg

class SSVEP_TRCA:
    """
    Section 5.2: Task-Related Component Analysis for SSVEP.
    Reference: Nakanishi et al. (2018)
    """
    def __init__(self, target_freqs, sfreq):
        self.target_freqs = target_freqs
        self.sfreq = sfreq
        self.models = {} # Store TRCA weights for each target
        
    def fit(self, eeg_trials, labels):
        """
        Train TRCA spatial filters.
        
        Parameters
        ----------
        eeg_trials : np.ndarray
            (n_trials, n_channels, n_samples)
        labels : np.ndarray
            (n_trials,) - Label (index of target freq) for each trial.
        """
        n_trials, n_channels, n_samples = eeg_trials.shape
        classes = np.unique(labels)
        
        for c in classes:
            # Get trials for this class
            trials_c = eeg_trials[labels == c] # (n_c, n_ch, n_samples)
            
            # S: Inter-trial covariance
            # Concatenate trials -> (n_ch, n_c * n_samples)
            X = np.concatenate(trials_c, axis=1) 
            
            # Q: Covariance of all data
            Q = np.cov(X)
            
            # S: Covariance of the template repeated
            # Template = mean across trials
            template = np.mean(trials_c, axis=0) # (n_ch, n_samples)
            
            S = np.zeros((n_channels, n_channels))
            for i in range(trials_c.shape[0]):
                for j in range(trials_c.shape[0]):
                    x_i = trials_c[i] - np.mean(trials_c[i], axis=1, keepdims=True)
                    x_j = trials_c[j] - np.mean(trials_c[j], axis=1, keepdims=True)
                    S += x_i @ x_j.T
            
            # Solve Generalized Eigenvalue Problem: S w = lambda Q w
            try:
                # eigh for symmetric matrices
                eigvals, eigvecs = scipy.linalg.eigh(S, Q)
                # Sort descending
                idx = np.argsort(eigvals)[::-1]
                w = eigvecs[:, idx[0]] # Best spatial filter
                self.models[c] = (w, template)
            except Exception as e:
                print(f"TRCA fit failed for class {c}: {e}")
                
    def predict(self, eeg_trial):
        """
        Predict class for a single trial.
        
        Parameters
        ----------
        eeg_trial : np.ndarray
            (n_channels, n_samples)
            
        Returns
        -------
        predicted_label
        """
        scores = []
        possible_labels = list(self.models.keys())
        possible_labels.sort()
        
        for c in possible_labels:
            w, template = self.models[c]
            
            # Apply spatial filter
            # s(t) = w^T x(t)
            test_s = w @ eeg_trial
            temp_s = w @ template
            
            # Correlation
            if np.std(test_s) == 0 or np.std(temp_s) == 0:
                scores.append(0)
            else:
                r = np.corrcoef(test_s, temp_s)[0, 1]
                scores.append(r)
            
        return possible_labels[np.argmax(scores)]
