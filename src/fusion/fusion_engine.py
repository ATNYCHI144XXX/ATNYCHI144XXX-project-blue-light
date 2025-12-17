"""
Sensor Fusion Engine

Integrates detections from multiple sensor modalities using Bayesian inference.
"""

import numpy as np
from typing import Optional, List, Dict
from dataclasses import dataclass

from ..ai.spectral_classifier import SpectralDetection
from ..ai.mass_spec_analyzer import MassSpecDetection
from ..ai.thermal_anomaly_detector import ThermalAnalysis


@dataclass
class VehicleInfo:
    """Information about the scanned vehicle."""
    license_plate: Optional[str]
    vehicle_type: str  # 'truck', 'car', 'van', etc.
    speed_mph: float
    timestamp: float
    

@dataclass
class ThreatAssessment:
    """Comprehensive threat assessment result."""
    threat_level: str  # 'HIGH', 'MEDIUM', 'LOW', 'CLEAR'
    confidence: float  # 0.0 to 1.0
    detected_compounds: List[str]
    contributing_factors: Dict[str, float]
    vehicle_info: VehicleInfo
    

class FusionEngine:
    """
    Multi-modal sensor fusion engine.
    
    Combines spectral, mass spectrometry, and thermal data using
    Bayesian inference to generate comprehensive threat assessments.
    """
    
    def __init__(self):
        """Initialize fusion engine."""
        self._base_rates = {
            'truck': 0.001,  # 0.1% base rate for trucks
            'car': 0.0001,   # 0.01% base rate for cars
            'van': 0.0005,   # 0.05% base rate for vans
        }
        
    def fuse_detections(
        self,
        spectral_result: Optional[List[SpectralDetection]],
        mass_spec_result: Optional[List[MassSpecDetection]],
        thermal_result: Optional[ThermalAnalysis],
        vehicle_data: VehicleInfo
    ) -> ThreatAssessment:
        """
        Fuse multi-modal detection results.
        
        Args:
            spectral_result: Spectral classification results
            mass_spec_result: Mass spectrometry detection results
            thermal_result: Thermal anomaly analysis
            vehicle_data: Vehicle information
            
        Returns:
            Comprehensive threat assessment
        """
        # Get base rate (prior probability)
        prior = self._get_base_rate(vehicle_data.vehicle_type)
        
        # Calculate likelihoods from each sensor
        likelihood_spectral = self._spectral_likelihood(spectral_result)
        likelihood_mass_spec = self._mass_spec_likelihood(mass_spec_result)
        likelihood_thermal = self._thermal_likelihood(thermal_result)
        
        # Bayesian fusion
        posterior = self._bayesian_update(
            prior,
            [likelihood_spectral, likelihood_mass_spec, likelihood_thermal]
        )
        
        # Determine threat level
        threat_level = self._classify_threat(posterior)
        
        # Extract detected compounds
        detected_compounds = self._extract_compounds(spectral_result, mass_spec_result)
        
        # Build contributing factors
        factors = {
            'spectral_confidence': likelihood_spectral,
            'mass_spec_confidence': likelihood_mass_spec,
            'thermal_anomaly': likelihood_thermal,
        }
        
        return ThreatAssessment(
            threat_level=threat_level,
            confidence=posterior,
            detected_compounds=detected_compounds,
            contributing_factors=factors,
            vehicle_info=vehicle_data
        )
        
    def _get_base_rate(self, vehicle_type: str) -> float:
        """Get base rate (prior probability) for vehicle type."""
        return self._base_rates.get(vehicle_type, 0.0001)
        
    def _spectral_likelihood(self, results: Optional[List[SpectralDetection]]) -> float:
        """Calculate likelihood from spectral detections."""
        if not results:
            return 0.0
            
        # Average confidence across detections
        confidences = [d.confidence for d in results]
        return sum(confidences) / len(confidences)
        
    def _mass_spec_likelihood(self, results: Optional[List[MassSpecDetection]]) -> float:
        """Calculate likelihood from mass spec detections."""
        if not results:
            return 0.0
            
        # Average confidence across detections
        confidences = [d.confidence for d in results]
        return sum(confidences) / len(confidences)
        
    def _thermal_likelihood(self, result: Optional[ThermalAnalysis]) -> float:
        """Calculate likelihood from thermal analysis."""
        if not result:
            return 0.0
            
        return result.anomaly_score
        
    def _bayesian_update(self, prior: float, likelihoods: List[float]) -> float:
        """
        Perform Bayesian update with multiple likelihoods.
        
        Args:
            prior: Prior probability
            likelihoods: List of likelihood values from each sensor
            
        Returns:
            Posterior probability
        """
        # Simple Bayesian update (assumes independence)
        # P(threat | evidence) = P(evidence | threat) * P(threat) / P(evidence)
        
        # Calculate combined likelihood
        combined_likelihood = np.prod([1 - (1 - l) for l in likelihoods if l > 0])
        
        # Bayes' rule with normalization
        posterior = (combined_likelihood * prior) / (
            combined_likelihood * prior + (1 - combined_likelihood) * (1 - prior)
        )
        
        return float(posterior)
        
    def _classify_threat(self, confidence: float) -> str:
        """Classify threat level based on confidence."""
        if confidence >= 0.90:
            return 'HIGH'
        elif confidence >= 0.70:
            return 'MEDIUM'
        elif confidence >= 0.50:
            return 'LOW'
        else:
            return 'CLEAR'
            
    def _extract_compounds(
        self,
        spectral: Optional[List[SpectralDetection]],
        mass_spec: Optional[List[MassSpecDetection]]
    ) -> List[str]:
        """Extract list of detected compound names."""
        compounds = set()
        
        if spectral:
            compounds.update(d.compound_name for d in spectral)
            
        if mass_spec:
            compounds.update(d.compound_name for d in mass_spec)
            
        return sorted(list(compounds))
