"""
eegflow.bids_utils: Data standardization modules.
Implements Section 6 (BIDS Compliance).
"""

import os
import shutil
import json
import numpy as np
import pandas as pd
from mne_bids import BIDSPath, write_raw_bids

def convert_to_bids(raw, subject_id, session_id, task_name, root_dir, 
                   event_id=None, events=None, overwrite=True):
    """
    Section 6.1: Convert MNE Raw object to BIDS structure.    
    Parameters
    ----------
    raw : mne.io.Raw
    subject_id : str
    session_id : str
    task_name : str
    root_dir : str
    
    Returns
    -------
    bids_path : mne_bids.BIDSPath
    """
    bids_path = BIDSPath(subject=subject_id, session=session_id, task=task_name,
                         root=root_dir)
    
    # Ensure some metadata exists
    if raw.info['line_freq'] is None:
        raw.info['line_freq'] = 60.0 # Default or warn
        
    write_raw_bids(raw, bids_path=bids_path, events_data=events, 
                   event_id=event_id, overwrite=overwrite)
    
    return bids_path

def add_motion_data(bids_path, motion_data, motion_channels, sfreq):
    """
    Section 6.2: Add Motion-BIDS extension data (_motion.tsv).
    
    Parameters
    ----------
    bids_path : mne_bids.BIDSPath
        The existing BIDS path for the recording.
    motion_data : np.ndarray
        (n_samples, n_channels)
    motion_channels : list
        List of channel names (e.g., ['pos_x', 'pos_y', ...])
    sfreq : float
    """
    # Construct motion path
    # According to Motion-BIDS proposal, motion can be in /motion/ or same dir as eeg?
    # Usually replacing suffix 'eeg' with 'motion'
    
    motion_bids_path = bids_path.copy().update(suffix='motion', extension='.tsv')
    
    # Create DataFrame
    df = pd.DataFrame(motion_data, columns=motion_channels)
    
    # Save TSV
    df.to_csv(motion_bids_path.fpath, sep='\t', index=False)
    
    # Save Sidecar JSON
    json_path = bids_path.copy().update(suffix='motion', extension='.json')
    meta = {
        "SamplingFrequency": sfreq,
        "MotionChannelCount": len(motion_channels),
        "TrackingSystemName": "Unity VR",
        "CoordinateSystem": "Unity Left-Handed (Y-up)"
    }
    
    with open(json_path.fpath, 'w') as f:
        json.dump(meta, f, indent=4)
        
    print(f"Motion data saved to {motion_bids_path.fpath}")

def generate_coord_system_json(bids_path, transform_matrix=None):
    """
    Add _coordsystem.json
    """
    coord_path = bids_path.copy().update(suffix='coordsystem', extension='.json')
    
    coords = {
        "EEGCoordinateSystem": "CapTrak",
        "EEGCoordinateUnits": "mm",
        "EEGCoordinateSystemDescription": "RAS orientation",
        "HeadCoilCoordinates": {},
        "DigitizedHeadPoints": "n/a",
        "DeviceCoordinateUnits": "mm"
    }
    
    if transform_matrix is not None:
        coords["UnityToMNITransform"] = transform_matrix
        
    with open(coord_path.fpath, 'w') as f:
        json.dump(coords, f, indent=4)

def add_impedance_to_electrodes_tsv(bids_path, impedance_dict):
    """
    Section 6.3: Add impedance values to electrodes.tsv (Issue #57).
    
    Parameters
    ----------
    bids_path : mne_bids.BIDSPath
        The existing BIDS path.
    impedance_dict : dict
        Dictionary mapping channel names to impedance values (e.g., {'Fp1': '5 kOhm'}).
    """
    electrodes_path = bids_path.copy().update(suffix='electrodes', extension='.tsv')
    
    if not os.path.exists(electrodes_path.fpath):
        print(f"Warning: {electrodes_path.fpath} not found. Cannot add impedance.")
        return
        
    # Read existing TSV
    df = pd.read_csv(electrodes_path.fpath, sep='\t')
    
    # Add 'impedance' column if not exists
    if 'impedance' not in df.columns:
        df['impedance'] = 'n/a'
        
    # Update values
    for ch_name, imp_val in impedance_dict.items():
        if ch_name in df['name'].values:
            df.loc[df['name'] == ch_name, 'impedance'] = imp_val
            
    # Save back
    df.to_csv(electrodes_path.fpath, sep='\t', index=False)
    print(f"Impedance data added to {electrodes_path.fpath}")
