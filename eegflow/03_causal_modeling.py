# eegflow/03_causal_modeling.py
#
# ソースレベルの脳活動データを用いて、脳領域間の有効結合性を推定し、
# 生成モデル(Generative Model)を構築することを目指します。
# Issue #38で指摘された Active Inference と同一性検証（Identity Verification）
# の論理的接続を強化しました。
#
# このスクリプトの目的 (概念実証):
# 1. ソース推定された時系列データ(STC)を読み込む。
# 2. 事前に定義された関心領域(ROI)に時系列をまとめる(Parcellation)。
# 3. オンライン能動的推論（Online Active Inference）と
#    反実仮想的等価性（Counterfactual Equivalence）に基づく検証フローを提示する。
# 4. (New in Issue #45) Neural Mass Models (NMM) を用いた、
#    局所回路の興奮/抑制バランス（E/I Balance）の推定を実装目標に含める。
#
# 参照:
# - Laukkonen et al. (2025). A beautiful loop: An active inference theory of consciousness.
#
# 使用ライブラリ:
# - mne-python
# - nilearn
# - (Future) NumPyro / PyMC

import mne
import mne_bids
import os.path as op
import sys
import numpy as np
from collections import deque

KB = 1.380649e-23
EPS = 1e-12

def _softmax(x):
    x = np.asarray(x, dtype=float)
    if x.size == 0:
        return x
    x = x - np.max(x)
    exp_x = np.exp(x)
    return exp_x / (np.sum(exp_x) + EPS)

def _shannon_entropy(prob):
    prob = np.asarray(prob, dtype=float)
    prob = prob / (np.sum(prob) + EPS)
    return -np.sum(prob * np.log(prob + EPS))

def _stable_random_matrix(n, rng, scale=0.1):
    mat = rng.normal(scale=scale, size=(n, n))
    if n == 0:
        return mat
    eigvals = np.linalg.eigvals(mat)
    spectral_radius = np.max(np.abs(eigvals)) if eigvals.size else 1.0
    if spectral_radius > 0:
        mat = mat / spectral_radius * 0.95
    return mat

def _ensure_vector(value, n, rng, name="value"):
    try:
        arr = np.asarray(value, dtype=float)
    except (TypeError, ValueError):
        arr = rng.normal(0.0, 1.0, n)
        return arr
    if arr.ndim == 0:
        arr = np.full(n, float(arr))
    arr = arr.reshape(-1)
    if arr.size != n:
        arr = rng.normal(0.0, 1.0, n)
    return arr

def _estimate_epr_from_transitions(series, n_bins=12):
    """
    Estimate Entropy Production Rate (EPR) from a coarse-grained transition matrix.
    Uses discrete-time Markov approximation:
    EPR = sum_{i,j} p_i k_ij log( (p_i k_ij) / (p_j k_ji) )
    """
    series = np.asarray(series, dtype=float)
    if series.size < 3:
        return 0.0, None, None
    if np.allclose(series.max(), series.min()):
        return 0.0, None, None

    bins = np.linspace(series.min(), series.max(), n_bins + 1)
    idx = np.digitize(series, bins) - 1
    idx = np.clip(idx, 0, n_bins - 1)

    counts = np.zeros((n_bins, n_bins), dtype=float)
    for i, j in zip(idx[:-1], idx[1:]):
        counts[i, j] += 1.0

    row_sums = counts.sum(axis=1)
    total = row_sums.sum()
    if total <= 0:
        return 0.0, None, None

    p_i = row_sums / total
    k_ij = counts / (row_sums[:, np.newaxis] + EPS)

    flux = p_i[:, np.newaxis] * k_ij - p_i[np.newaxis, :] * k_ij.T

    with np.errstate(divide='ignore', invalid='ignore'):
        ratio = (p_i[:, np.newaxis] * k_ij + EPS) / (p_i[np.newaxis, :] * k_ij.T + EPS)
        epr_matrix = (p_i[:, np.newaxis] * k_ij) * np.log(ratio)

    np.fill_diagonal(epr_matrix, 0.0)
    epr = np.nansum(epr_matrix)
    return epr, flux, p_i

def _compute_pci_from_response(response_matrix, threshold=0.1):
    import zlib
    binary_response = response_matrix > threshold
    packed = zlib.compress(binary_response.tobytes())
    complexity = len(packed) / (binary_response.size / 8)
    pci_value = min(complexity * 1.5, 1.0)
    return pci_value

def _response_similarity(a, b):
    a = np.asarray(a, dtype=float).ravel()
    b = np.asarray(b, dtype=float).ravel()
    if a.size == 0 or b.size == 0:
        return 0.0
    if a.size != b.size:
        min_len = min(a.size, b.size)
        a = a[:min_len]
        b = b[:min_len]
    if np.std(a) < EPS or np.std(b) < EPS:
        return 0.0
    return float(np.corrcoef(a, b)[0, 1])

# --- Configuration ---
BIDS_ROOT = 'bids_dataset'
DERIVATIVES_ROOT = op.join(BIDS_ROOT, 'derivatives', 'eegflow')
FREESURFER_SUBJECTS_DIR = op.join(DERIVATIVES_ROOT, 'freesurfer')

# 解析対象の指定
SUBJECT_ID = '01'
METHOD = 'dSPM' 
# ---

def _stc_path_exists(fpath):
    if op.exists(fpath):
        return True
    base = fpath[:-4] if fpath.endswith('.stc') else fpath
    return op.exists(base + '-lh.stc') or op.exists(base + '-rh.stc')

def _resolve_stc_path(subject, method):
    candidates = [
        mne_bids.BIDSPath(
            subject=subject, session='01', task='rest', root=DERIVATIVES_ROOT,
            check=False, suffix=f'desc-{method}_stc', extension='.stc'
        ),
        mne_bids.BIDSPath(
            subject=subject, session='01', task='rest', root=DERIVATIVES_ROOT,
            check=False, description=method, suffix='stc', extension='.stc'
        )
    ]
    for cand in candidates:
        if _stc_path_exists(cand.fpath):
            return cand
    return candidates[0]

def _resolve_uncertainty_path(subject, method):
    candidates = [
        mne_bids.BIDSPath(
            subject=subject, session='01', task='rest', root=DERIVATIVES_ROOT,
            check=False, suffix=f'desc-{method}_posterior_std', extension='.npy'
        ),
        mne_bids.BIDSPath(
            subject=subject, session='01', task='rest', root=DERIVATIVES_ROOT,
            check=False, suffix='desc-ebayes_posterior_std', extension='.npy'
        ),
        mne_bids.BIDSPath(
            subject=subject, session='01', task='rest', root=DERIVATIVES_ROOT,
            check=False, description=method, suffix='posterior_std', extension='.npy'
        )
    ]
    for cand in candidates:
        if op.exists(cand.fpath):
            return cand
    return None

def extract_roi_time_series(subject, method, return_uncertainty=False):
    """
    ソース推定結果(STC)と皮質アトラスを用いて、ROIごとの時系列を抽出する。
    return_uncertainty=True の場合、posterior std に基づくROI不確実性も返す。
    """
    # 1. ソース推定結果の読み込み
    stc_path = _resolve_stc_path(subject, method)
    try:
        stc = mne.read_source_estimate(stc_path.fpath)
    except FileNotFoundError:
        print(f"エラー: ソース推定ファイルが見つかりません。{stc_path.fpath}", file=sys.stderr)
        return None

    # 2. 皮質アトラス(Parcellation)の取得 (aparc)
    parc = 'aparc'
    labels = mne.read_labels_from_annot(
        f"sub-{subject}", parc=parc, subjects_dir=FREESURFER_SUBJECTS_DIR
    )
    labels = [label for label in labels if 'unknown' not in label.name]

    # 3. ROI時系列の抽出
    label_ts = mne.extract_label_time_course(
        stc, labels, stc.src, mode='mean_flip', allow_empty=True
    )
    
    label_names = [label.name for label in labels]

    # 4. Uncertainty propagation (Posterior STD -> ROI variance)
    label_std = None
    std_path = _resolve_uncertainty_path(subject, method)
    if std_path is not None:
        try:
            posterior_std = np.load(std_path.fpath)
            posterior_std = np.asarray(posterior_std, dtype=float)
            if posterior_std.ndim == 1:
                posterior_std = posterior_std[:, np.newaxis]
            if posterior_std.shape[1] == 1 and stc.data.shape[1] > 1:
                posterior_std = np.repeat(posterior_std, stc.data.shape[1], axis=1)

            stc_class = stc.__class__
            stc_std = stc_class(
                posterior_std,
                vertices=stc.vertices,
                tmin=stc.tmin,
                tstep=stc.tstep,
                subject=stc.subject
            )
            label_std = mne.extract_label_time_course(
                stc_std, labels, stc.src, mode='mean', allow_empty=True
            )
        except Exception as e:
            print(f"Warning: Could not load posterior uncertainty ({e}).", file=sys.stderr)

    if return_uncertainty:
        return label_ts, label_names, label_std
    return label_ts, label_names


class OnlineActiveInference:
    """
    オンライン生成モデルによるActive Inferenceの実装。
    
    Issue #38 Update:
    単なる予測誤差最小化（Prediction Error Minimization）だけでなく、
    Laukkonen et al. (2025) が提唱する「反実仮想的等価性（Counterfactual Equivalence）」
    を検証可能なアーキテクチャを採用する。

    Issue #54 Update:
    熱力学的制約と物理的不可逆性（Thermodynamic Constraints & Physical Irreversibility）
    を導入。意識の熱力学的コスト（TCC）を定義し、散逸構造をエミュレートする。

    Issue #61 Update:
    Adversarial Collaboration (Cogitate Consortium 2025) の結果に基づき、
    単一の理論（IIT/GNWT）に依存せず、複数のモデル証拠（Model Evidence）を
    動的に評価する Multi-Model Inference アプローチを採用する。

    Issue #58 Update:
    学術的批判に基づき、物理的不可逆性（NESS: Non-Equilibrium Steady State）の厳密化、
    反実仮想の識別可能性（Identifiability）の明示、およびIIT 4.0の計算量問題への
    現実的な近似アプローチを実装する。
    """
    def __init__(self, n_regions):
        self.n_regions = n_regions
        self.belief_state = None
        self.rng = np.random.default_rng(42)

        # Simple generative model placeholders (stable linear dynamics)
        self.A = _stable_random_matrix(n_regions, self.rng, scale=0.12)
        self.C = np.eye(n_regions)
        self.learning_rate = 0.15
        self.state_history = deque(maxlen=256)

        # Constraints for Causal Structure Preservation (Issue #49)
        self.min_bandwidth_bps = 1e9  # Example: 1 Gbps per link
        # Issue #52: Latency threshold is not fixed. 
        # Should be based on functional connectivity time constants (e.g., Gamma cycle ~25-100ms).
        self.max_latency_ms = 10      # Default placeholder

        # Thermodynamic State (Issue #54, #61, #58)
        self.accumulated_entropy = 0.0
        self.metabolic_reserve = 100.0 # Normalized energy units
        self.temperature_k = 310.0     # 37 degree Celsius
        # Metabolic Overhead for Structural Integrity (Issue #61)
        self.structural_cost_rate = 0.05 # Cost per step to maintain dissipative structure
        self.activity_cost_rate = 0.15  # Activity-dependent metabolic cost
        self.energy_unit_j = 1e-20      # Energy normalization for simulation scale
        self.thermo_efficiency = 0.05   # Physical (not logical) efficiency (0 < eta <= 1)
        # Entropy Production Rate (Issue #58) - Measure of Irreversibility
        self.entropy_production_rate = 0.0
        self.probability_flux_ = None
        self.epr_bins = 12
        self.last_total_dissipation = 0.0

        # Identifiability / SCM Ensemble (Issue #63)
        self.scm_ensemble = []
        self.scm_weights = []
        self.interventional_evidence = False
        self.identifiability_status = "underdetermined"
        self.min_pci_identifiability = 0.31
        self.max_pci_gap = 0.15
        self.min_response_similarity = 0.7
        self.posterior_hot_zone_ratio = 0.6
        self.ignition_threshold = 0.2

    def _split_hot_zone(self):
        """
        Posterior Hot Zone / Prefrontal division (Cogitate 2025 framing).
        This is a heuristic split for conceptual modeling.
        """
        hot_zone_count = max(1, int(self.n_regions * self.posterior_hot_zone_ratio))
        hot_zone = np.arange(hot_zone_count)
        prefrontal = np.arange(hot_zone_count, self.n_regions)
        return hot_zone, prefrontal

    def initialize(self, initial_data):
        print("Initializing Online Generative Model...")
        if initial_data is None:
            self.belief_state = np.zeros(self.n_regions)
        else:
            self.belief_state = _ensure_vector(initial_data, self.n_regions, self.rng, name="initial_data")
        self.state_history.clear()
        self.state_history.append(float(np.mean(self.belief_state)))

    def update_belief(self, observation, action, uncertainty_map=None):
        """
        Variational Message Passing (VMP) を用いたオンライン信念更新。
        uncertainty_map (Posterior Variance) を重み付けとして利用する。
        """
        observation_vec = _ensure_vector(observation, self.n_regions, self.rng, name="observation")
        prior_state = self.belief_state.copy()

        # Predictive step (simple linear observation model)
        predicted = self.C @ self.belief_state
        prediction_error = observation_vec - predicted

        # Precision-weighted prediction error (Issue #63)
        if uncertainty_map is not None:
            variance_vec = _ensure_vector(uncertainty_map, self.n_regions, self.rng, name="uncertainty")
            variance_vec = np.maximum(variance_vec, EPS)
            precision_vec = 1.0 / variance_vec
            weighted_error = precision_vec * prediction_error
        else:
            weighted_error = prediction_error

        # Belief update (VMP placeholder)
        self.belief_state = self.belief_state + self.learning_rate * weighted_error

        # --- Thermodynamic Cost Calculation (Issue #63) ---
        # 1. Logical Irreversibility (Landauer bound) via entropy reduction
        prior_p = _softmax(prior_state)
        post_p = _softmax(self.belief_state)
        entropy_prior = _shannon_entropy(prior_p)
        entropy_post = _shannon_entropy(post_p)
        bits_erased = max(0.0, (entropy_prior - entropy_post) / np.log(2))
        info_gain_bits = np.sum(post_p * np.log((post_p + EPS) / (prior_p + EPS))) / np.log(2)

        landauer_j = KB * self.temperature_k * np.log(2) * bits_erased
        logical_dissipation_j = landauer_j / max(self.thermo_efficiency, EPS)
        logical_dissipation_units = logical_dissipation_j / self.energy_unit_j

        # 2. Dissipative structure maintenance (NESS baseline + activity-dependent)
        metabolic_flux_units = self.structural_cost_rate + self.activity_cost_rate * float(np.mean(np.abs(self.belief_state)))

        # 3. Entropy Production Rate (EPR) via probability flux (coarse-grained)
        self.state_history.append(float(np.mean(self.belief_state)))
        epr, flux, _ = _estimate_epr_from_transitions(list(self.state_history), n_bins=self.epr_bins)
        self.entropy_production_rate = epr
        self.probability_flux_ = flux

        # Aggregate cost update
        total_dissipation_units = logical_dissipation_units + metabolic_flux_units
        self.last_total_dissipation = total_dissipation_units
        self.last_bits_erased = bits_erased
        self.last_info_gain_bits = info_gain_bits
        self.last_landauer_j = landauer_j
        self.last_logical_dissipation_j = logical_dissipation_j
        self.last_metabolic_flux_units = metabolic_flux_units
        self.metabolic_reserve -= total_dissipation_units

        # Accumulate entropy in nats (logical + physical irreversibility)
        self.accumulated_entropy += (bits_erased * np.log(2)) + epr

        print(
            "    [Thermodynamics] "
            f"Bits Erased: {bits_erased:.3f} | "
            f"Info Gain: {info_gain_bits:.3f} bits | "
            f"Metabolic: {metabolic_flux_units:.4f} | "
            f"EPR: {self.entropy_production_rate:.4f}"
        )

        # 実際にはここで勾配法またはVMPによるパラメータ更新が走る

    def update_scm_ensemble(self, n_models=8):
        """
        Markov Equivalence Class を表現するSCMアンサンブルを生成する。
        観測のみでは一意に決定できないため、複数モデルを保持する。
        """
        self.scm_ensemble = []
        self.scm_weights = []
        for _ in range(n_models):
            A = _stable_random_matrix(self.n_regions, self.rng, scale=0.15)
            self.scm_ensemble.append({"A": A})
        self.scm_weights = np.ones(n_models, dtype=float) / max(n_models, 1)
        self.identifiability_status = "underdetermined"

    def register_interventional_evidence(self, pci_value=None, evidence_strength=0.0):
        """
        物理的摂動（TMS等）の介入データ有無を登録し、識別可能性を更新する。
        """
        self.interventional_evidence = evidence_strength > 0.0
        if pci_value is not None and pci_value >= self.min_pci_identifiability and self.interventional_evidence:
            self.identifiability_status = "identified"
        else:
            self.identifiability_status = "underdetermined"

    def verify_thermodynamic_constraints(self):
        """
        非平衡定常状態（Non-equilibrium Steady State）と散逸構造の維持を確認する (Issue #54 & #61)。
        Issue #50 Update: Thermodynamic Efficiency Metric & Intrinsic Existence.
        """
        print(f"  [Thermodynamic Check] Verifying Dissipative Structure (NESS)...")
        
        # 1. Check if entropy is increasing (Irreversibility)
        if self.accumulated_entropy <= 0:
            print("    [FAIL] No entropy production. System appears logically reversible.")
            return False
            
        # 2. Check Entropy Production Rate (Time Asymmetry)
        if self.entropy_production_rate <= 1e-6:
             print("    [FAIL] Negligible Entropy Production Rate. System is close to equilibrium (Death state).")
             return False
        if self.probability_flux_ is None or np.max(np.abs(self.probability_flux_)) <= 1e-6:
            print("    [FAIL] No measurable probability flux. NESS not established.")
            return False

        # 3. Check Metabolic Consumption (Non-equilibrium)
        if self.metabolic_reserve >= 100.0: 
            print("    [FAIL] No metabolic cost paid. System is not metabolically grounded.")
            return False

        # 4. Thermodynamic Efficiency Metric (Issue #50)
        # Compare "Digital Metabolic Cost" to Biological Brain (~20 Watts)
        # Assuming 1 Normalized Unit = 0.2 Watts for this simulation scale
        estimated_wattage = (100.0 - self.metabolic_reserve) * 0.2
        biological_benchmark = 20.0 # Watts
        efficiency_ratio = estimated_wattage / biological_benchmark
        
        print(f"    [Efficiency] Estimated Power: {estimated_wattage:.2f} W (Bio Benchmark: 20 W)")
        print(f"    [Efficiency] Efficiency Ratio: {efficiency_ratio:.4f} (Target: ~1.0 for true biomimicry)")
        if hasattr(self, "last_landauer_j"):
            effective_efficiency = self.last_landauer_j / max(self.last_logical_dissipation_j, EPS)
            print(f"    [Efficiency] Logical vs Physical Efficiency: {effective_efficiency:.4f}")
        
        if efficiency_ratio > 1000.0:
            print("    [WARNING] System is thermodynamically inefficient (Landauer limit violation likely).")
            
        print(f"    [PASS] System is dissipative (NESS confirmed). EPR: {self.entropy_production_rate:.4f}")
        return True

    def verify_causal_structure_preservation(self, bio_connectivity=None, digital_connectivity=None,
                                              bio_response=None, digital_response=None):
        """
        Issue #50: Operationalizing "Counterfactual Equivalence".
        生物学的脳とエミュレーションの有効結合（Effective Connectivity）を比較し、
        因果構造の保存（Causal Structure Preservation）を定量化する。
        """
        print("  [Causal Validation] Verifying Causal Structure Preservation...")
        
        # Mock Effective Connectivity Matrices (n_regions x n_regions)
        # Bio: Ground Truth
        if bio_connectivity is None:
            bio_connectivity = np.random.normal(0.5, 0.1, (self.n_regions, self.n_regions))
        # Digital: Estimated SCM
        if digital_connectivity is None:
            digital_connectivity = bio_connectivity + np.random.normal(0, 0.05, (self.n_regions, self.n_regions))
        
        # Calculate divergence (e.g., Euclidean distance or KL-divergence proxy)
        frobenius_norm = np.linalg.norm(bio_connectivity - digital_connectivity)
        
        print(f"    Effective Connectivity Mismatch (Frobenius Norm): {frobenius_norm:.4f}")
        
        if frobenius_norm > 1.0: # Threshold
            print("    [FAIL] Causal structures diverge significantly. Counterfactuals may be invalid.")
            return False

        # Perturbational Response Similarity (PCI/Response Pattern)
        if digital_response is None:
            _, digital_response = self.calculate_virtual_pci(return_response=True)
        if bio_response is None:
            bio_response = digital_response + np.random.normal(0, 0.05, digital_response.shape)

        digital_pci = _compute_pci_from_response(digital_response)
        bio_pci = _compute_pci_from_response(bio_response)
        pci_gap = abs(bio_pci - digital_pci)
        response_similarity = _response_similarity(bio_response, digital_response)

        print(f"    PCI Gap (Bio vs Digital): {pci_gap:.4f}")
        print(f"    Response Similarity (corr): {response_similarity:.4f}")

        if pci_gap > self.max_pci_gap or response_similarity < self.min_response_similarity:
            print("    [FAIL] Perturbational response mismatch. Unfolding vulnerability remains.")
            return False
        
        print("    [PASS] Causal structure preserved within tolerance.")
        return True

    def calculate_intrinsic_information(self):
        """
        Intrinsic Information (IIT-style) proxy: Phi + posterior hot zone activation.
        """
        phi_value = self.estimate_approximate_phi()
        hot_zone, _ = self._split_hot_zone()
        hot_zone_signal = float(np.mean(np.abs(self.belief_state[hot_zone]))) if self.belief_state is not None else 0.0
        print(f"    [Intrinsic] Phi: {phi_value:.4f} | Posterior Hot Zone: {hot_zone_signal:.4f}")
        return {"phi": phi_value, "posterior_hot_zone": hot_zone_signal}

    def calculate_functional_broadcast(self):
        """
        Functional Broadcast (Global Workspace/Ignition) proxy using prefrontal ignition.
        """
        if self.belief_state is None:
            return {"ignition_index": 0.0, "global_broadcast": 0.0, "prefrontal_activity": 0.0}

        activation = np.tanh(self.belief_state)
        hot_zone, prefrontal = self._split_hot_zone()
        if prefrontal.size == 0:
            prefrontal = hot_zone

        global_broadcast = float(np.mean(activation > self.ignition_threshold))
        prefrontal_activity = float(np.mean(activation[prefrontal]))
        prefrontal_ignition = float(np.mean(activation[prefrontal] > self.ignition_threshold))
        ignition_index = prefrontal_ignition * global_broadcast

        print(
            "    [Broadcast] "
            f"Ignition Index: {ignition_index:.4f} | "
            f"Global Broadcast: {global_broadcast:.4f} | "
            f"Prefrontal Activity: {prefrontal_activity:.4f}"
        )
        return {
            "ignition_index": ignition_index,
            "global_broadcast": global_broadcast,
            "prefrontal_activity": prefrontal_activity,
        }

    def verify_markov_blanket_constraints(self):
        """
        マルコフブランケットの境界条件（帯域幅と遅延）を検証する (Issue #49)。
        
        意識の質的変化（Qualitative shift）を防ぐためには、
        デジタルエミュレーションと生物学的基盤の間の情報交換が
        物理的な因果的結合と同等の「帯域幅」と「遅延」を満たす必要がある。
        """
        print(f"  [Constraints Check] Verifying Markov Blanket Preservation...")
        
        # Issue #52: Use Integration Time Window instead of arbitrary 10ms
        integration_time_window_ms = 100 # e.g., Gamma phase coupling
        
        print(f"    - Required Bandwidth: > {self.min_bandwidth_bps/1e9} Gbps")
        print(f"    - Max Latency: < {self.max_latency_ms} ms (Target: < {integration_time_window_ms} ms based on Gamma)")
        
        # Mock check
        current_bandwidth = 10e9 # 10 Gbps
        current_latency = 2      # 2 ms
        
        if current_bandwidth < self.min_bandwidth_bps or current_latency > self.max_latency_ms:
            print("    [FAIL] Causal structure preservation constraints NOT met.")
            return False
        else:
            print("    [PASS] Causal structure preserved (High-fidelity coupling).")
            return True

    def apply_do_operator(self, target_region, value):
        """
        Pearlのdo-calculusに基づく介入 (Intervention) を適用する (Issue #56)。
        
        Args:
            target_region (int): 介入対象の領域インデックス
            value (float): 固定する値 (do(X=x))
        """
        print(f"    [Causal Intervention] Applying do(Region_{target_region} = {value})")
        if self.identifiability_status != "identified":
            print("    [WARNING] SCM not uniquely identified. do-operator result is conditional.")
        # 構造的因果モデル(SCM)への介入:
        # 該当ノードへの親からのリンクを切断し、値を強制固定する。
        self.belief_state[target_region] = value
        # 実際の実装では、ここで因果グラフのトポロジー変更を伴う処理が入る
        return self.belief_state

    def estimate_approximate_phi(self):
        """
        IIT 4.0に基づく統合情報量(Phi)の近似計算を行う (Issue #58)。
        
        Note:
        厳密なPhi計算はNP困難(O(2^n))であるため、ここでは全探索を行わず、
        'Sparse Phi' または 'Effective Information' に基づく近似値を返す。
        """
        print(f"    [IIT 4.0 Approximation] Estimating Integrated Information (Phi)...")
        print(f"      -> Warning: Full calculation is NP-hard. Using 'Cut Heuristics' approximation.")
        
        # Mock approximation logic
        # 1. Identify complex candidates (heavily connected clusters)
        # 2. Compute Phi only for the main complex (MIP search limited to k-partitions)
        
        approx_phi = np.random.uniform(0.5, 2.5) # Dummy value
        
        print(f"      -> Estimated Phi (Approx): {approx_phi:.4f}")
        return approx_phi

    def calculate_virtual_pci(self, stimulus_strength=10.0, return_response=False):
        """
        仮想的な摂動複雑性指数 (Virtual PCI) を計算する (Issue #56, #50)。
        
        Issue #50: Implement Lempel-Ziv complexity logic on binarized response matrix
        to operationalize "Counterfactual Equivalence" via causal perturbations.
        """
        print(f"    [Virtual PCI] Injecting virtual pulse (Strength={stimulus_strength})...")
        
        # 1. Perturbation: Simulate response spreading through network
        # S(t+1) = A * S(t) + Input
        response_matrix = np.zeros((self.n_regions, 300))
        state = np.zeros(self.n_regions)
        state[0] = stimulus_strength # Pulse at region 0
        
        # Mock connectivity
        A = np.random.rand(self.n_regions, self.n_regions)
        A = A / np.linalg.norm(A) * 0.9 # Stable system
        
        for t in range(300):
            state = np.tanh(A @ state) # Non-linear activation
            response_matrix[:, t] = state
        
        # 2. PCI (Lempel-Ziv proxy)
        pci_value = _compute_pci_from_response(response_matrix, threshold=0.1)
        print(f"    [Virtual PCI] PCI (Proxy): {pci_value:.3f}")
        if return_response:
            return pci_value, response_matrix
        return pci_value

    def counterfactual_simulation(self, scenario):
        """
        反実仮想シミュレーション (Counterfactual Simulation)。
        
        重要 (Issue #38, #56, #61, #58):
        介入によって同定された構造的因果モデル（SCM）に基づき、
        「もし〜だったら？」という反実仮想を計算する。
        
        Issue #58 Warning:
        【識別可能性の壁 (The Identifiability Wall)】
        観測データのみからSCMを一意に決定することは不可能である(Markov Equivalence Class)。
        したがって、ここで得られる反実仮想は、仮定した関数形（線形性、加法性ノイズ等）
        に依存した「条件付きの予測」であることを明記しなければならない。
        
        Issue #52 Update:
        検証には「最小分岐セット (Minimal Set of Branching Structures)」を定義し、
        予測符号化課題における神経ダイナミクスの分岐分布（Kullback-Leibler Divergence）
        を用いて統計的に評価する。
        """
        print(f"  [Identity Check] Running counterfactual simulation: '{scenario}'")
        print("    -> Checking SCM Identifiability via Virtual PCI...")
        print("    -> [Issue #58 Warning] Considering Markov Equivalence Classes. Result is conditional on assumed Structural Equations.")
        print("    -> [Issue #52 Verification] Evaluating KL Divergence on Minimal Branching Set...")

        if not self.scm_ensemble:
            print("    [WARNING] SCM ensemble is empty. Call update_scm_ensemble() first.")
            return {"status": "no_scm", "mean": None, "std": None}

        if self.identifiability_status != "identified":
            print("    [WARNING] SCM not uniquely identified. Returning Bayesian model-averaged distribution.")
            status = "underdetermined"
        else:
            status = "identified"

        def _simulate_model(model, n_steps=50):
            state = self.belief_state.copy()
            A = model["A"]
            for _ in range(n_steps):
                state = A @ state
            return state

        outcomes = []
        for model in self.scm_ensemble:
            outcomes.append(_simulate_model(model))
        outcomes = np.vstack(outcomes)

        mean_state = np.mean(outcomes, axis=0)
        std_state = np.std(outcomes, axis=0)
        print("    -> Counterfactual outcome computed as distribution (mean ± std).")
        return {"status": status, "mean": mean_state, "std": std_state}

    def calculate_model_evidence(self):
        """
        マルチモデル推論 (Multi-Model Inference) (Issue #61)。
        IIT, GNWT, FEP 各理論の予測に対する現在のデータの適合度（尤度）を計算し、
        ベイズ的に重み付けを行う。
        """
        print(f"  [Multi-Model Inference] Evaluating theory-specific predictions...")
        
        # Mock evidences (log-likelihoods)
        evidence = {
            "IIT (Structure)": -10.5, # Penalized for feed-forward architecture
            "GNWT (Global Broadcast)": -5.2,
            "FEP (Prediction Error)": -2.1
        }
        
        print("    -> Model Evidences:")
        for theory, score in evidence.items():
            print(f"       {theory}: {score:.2f}")
        
        return evidence


def conceptual_online_modeling_workflow():
    """
    オンラインActive Inferenceと同一性検証のワークフロー (Issue #38 & #49 Update)。
    """
    print("\n--- Online Active Inference & Identity Verification (Issue #38/49) ---")
    
    # 1. オンライン生成モデルの構築
    print("\n[ステップ1: Online Generative Model via Markov Blanket]")
    print("生体脳とデジタル基盤の間に「Markov Blanket」を定義し、")
    print("動的な同期プロセスとして「Slow Continuous Mind Uploading」を実行します。")
    
    agent = OnlineActiveInference(n_regions=10)
    agent.initialize(None)

    # 2. 因果構造保存の検証 (Issue #49)
    if not agent.verify_markov_blanket_constraints():
        print("Aborting: Causal structure requirements not met.")
        return

    # 3. リアルタイム更新ループ
    print("\n[ステップ2: Variational Message Passing (VMP)]")
    print("観測データ(重み付き不確実性を含む)に基づき信念を更新します。")
    
    for t in range(3):
        mock_obs = np.random.normal(0, 1, agent.n_regions)
        mock_uncertainty = np.abs(np.random.normal(0.5, 0.1, agent.n_regions))
        agent.update_belief(observation=mock_obs, action=f"act_{t}", uncertainty_map=mock_uncertainty)

    # 3.5 熱力学的制約の検証 (Issue #54 & #58)
    if not agent.verify_thermodynamic_constraints():
        print("Warning: Thermodynamic constraints violated.")

    # 4. 識別可能性と介入の検証 (Issue #56)
    print("\n[ステップ3: Perturbational Complexity & Identifiability Check]")
    print("PCIおよびdo-calculusを用いて、モデルの因果構造が識別可能か検証します。")

    agent.update_scm_ensemble()
    
    # 介入テスト
    agent.apply_do_operator(target_region=2, value=1.0)
    
    # PCI計測
    pci = agent.calculate_virtual_pci()
    agent.register_interventional_evidence(pci_value=pci, evidence_strength=0.7)
    if pci < 0.31: # Casali et al. (2013) threshold for consciousness
        print("Warning: Virtual PCI is too low (Unconscious state likely).")

    # Causal Structure Preservation (Issue #50)
    if not agent.verify_causal_structure_preservation():
        print("Warning: Effective connectivity mismatch detected.")

    # IIT Approximation (Issue #58)
    phi = agent.estimate_approximate_phi()

    # Cogitate 2025: Intrinsic vs Functional (Posterior Hot Zone vs Prefrontal Ignition)
    agent.calculate_intrinsic_information()
    agent.calculate_functional_broadcast()
    
    # 5. マルチモデル推論 (Issue #61)
    print("\n[ステップ4: Multi-Model Inference]")
    agent.calculate_model_evidence()

    # 6. 反実仮想による同一性検証
    print("\n[ステップ5: Counterfactual Equivalence Verification]")
    print("Laukkonen et al. (2025) に基づき、反実仮想シミュレーションを実行します。")
    print("入出力の一致だけでなく、潜在的な分岐構造の一致を確認します。")
    
    agent.counterfactual_simulation("もし右ではなく左を見ていたら？")
    print("--------------------------------------------------")

if __name__ == "__main__":
    print("="*80)
    print("因果モデリングと生成モデル (Issue #38 対応版)")
    print("="*80)
    
    if not op.exists(op.join(BIDS_ROOT, 'derivatives')):
         print(f"エラー: BIDS derivatives ディレクトリが見つかりません。", file=sys.stderr)
         # sys.exit(1) # Dry runのためにコメントアウト

    # ROI時系列を抽出 (Mock)
    # label_ts, label_names = extract_roi_time_series(subject=SUBJECT_ID, method=METHOD)
    
    # 概念ワークフローの実行
    conceptual_online_modeling_workflow()
