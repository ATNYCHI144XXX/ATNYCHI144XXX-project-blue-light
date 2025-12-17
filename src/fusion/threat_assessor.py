"""
Threat Assessor

High-level threat assessment logic and decision making.
"""

from typing import Dict, List
from dataclasses import dataclass
from .fusion_engine import ThreatAssessment


@dataclass
class AssessmentReport:
    """Detailed threat assessment report."""
    assessment: ThreatAssessment
    recommended_action: str
    risk_factors: List[str]
    confidence_breakdown: Dict[str, float]
    

class ThreatAssessor:
    """
    High-level threat assessment and decision logic.
    
    Provides actionable recommendations based on fusion results.
    """
    
    def __init__(self):
        """Initialize threat assessor."""
        self._high_risk_compounds = {'Fentanyl', 'ANPP', 'NPP', 'Carfentanil'}
        
    def assess(self, threat_assessment: ThreatAssessment) -> AssessmentReport:
        """
        Generate detailed assessment report.
        
        Args:
            threat_assessment: Threat assessment from fusion engine
            
        Returns:
            Detailed assessment report with recommendations
        """
        # Determine recommended action
        action = self._determine_action(threat_assessment)
        
        # Identify risk factors
        risk_factors = self._identify_risk_factors(threat_assessment)
        
        # Build confidence breakdown
        confidence_breakdown = threat_assessment.contributing_factors.copy()
        confidence_breakdown['overall'] = threat_assessment.confidence
        
        return AssessmentReport(
            assessment=threat_assessment,
            recommended_action=action,
            risk_factors=risk_factors,
            confidence_breakdown=confidence_breakdown
        )
        
    def _determine_action(self, assessment: ThreatAssessment) -> str:
        """Determine recommended action based on threat level."""
        action_map = {
            'HIGH': 'IMMEDIATE_INTERDICTION',
            'MEDIUM': 'SECONDARY_INSPECTION',
            'LOW': 'LOG_FOR_ANALYSIS',
            'CLEAR': 'NO_ACTION'
        }
        return action_map.get(assessment.threat_level, 'NO_ACTION')
        
    def _identify_risk_factors(self, assessment: ThreatAssessment) -> List[str]:
        """Identify specific risk factors from assessment."""
        factors = []
        
        # Check for high-risk compounds
        for compound in assessment.detected_compounds:
            if compound in self._high_risk_compounds:
                factors.append(f"Detected {compound} (controlled substance)")
                
        # Check for high spectral confidence
        spectral_conf = assessment.contributing_factors.get('spectral_confidence', 0)
        if spectral_conf > 0.9:
            factors.append("High spectral signature confidence")
            
        # Check for mass spec confirmation
        mass_conf = assessment.contributing_factors.get('mass_spec_confidence', 0)
        if mass_conf > 0.9:
            factors.append("Mass spectrometry confirmation")
            
        # Check for thermal anomalies
        thermal = assessment.contributing_factors.get('thermal_anomaly', 0)
        if thermal > 0.7:
            factors.append("Thermal anomaly detected (possible hidden compartment)")
            
        # Check vehicle type
        if assessment.vehicle_info.vehicle_type == 'truck':
            factors.append("Commercial vehicle (higher scrutiny)")
            
        return factors
        
    def should_alert(self, assessment: ThreatAssessment) -> bool:
        """
        Determine if an alert should be generated.
        
        Args:
            assessment: Threat assessment
            
        Returns:
            True if alert should be sent
        """
        return assessment.threat_level in ['HIGH', 'MEDIUM']
        
    def calculate_priority(self, assessment: ThreatAssessment) -> int:
        """
        Calculate alert priority (1-5, 5 being highest).
        
        Args:
            assessment: Threat assessment
            
        Returns:
            Priority level
        """
        priority_map = {
            'HIGH': 5,
            'MEDIUM': 3,
            'LOW': 1,
            'CLEAR': 0
        }
        
        base_priority = priority_map.get(assessment.threat_level, 0)
        
        # Boost priority for multiple detections
        if len(assessment.detected_compounds) > 1:
            base_priority = min(base_priority + 1, 5)
            
        return base_priority
