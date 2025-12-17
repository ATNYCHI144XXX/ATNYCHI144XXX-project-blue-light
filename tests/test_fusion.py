"""
Unit tests for fusion module.

Tests sensor fusion engine and threat assessor.
"""

import pytest
from src.fusion.fusion_engine import FusionEngine, VehicleInfo, ThreatAssessment
from src.fusion.threat_assessor import ThreatAssessor
from src.ai.spectral_classifier import SpectralDetection
from src.ai.mass_spec_analyzer import MassSpecDetection
from src.ai.thermal_anomaly_detector import ThermalAnalysis


class TestFusionEngine:
    """Test cases for sensor fusion engine."""
    
    def test_initialization(self):
        """Test fusion engine initialization."""
        engine = FusionEngine()
        assert engine._base_rates is not None
        
    def test_threat_classification(self):
        """Test threat level classification."""
        engine = FusionEngine()
        assert engine._classify_threat(0.95) == 'HIGH'
        assert engine._classify_threat(0.75) == 'MEDIUM'
        assert engine._classify_threat(0.55) == 'LOW'
        assert engine._classify_threat(0.30) == 'CLEAR'
        
    def test_fusion_with_detections(self):
        """Test multi-modal fusion with detections."""
        engine = FusionEngine()
        
        spectral = [SpectralDetection(
            compound_name="Fentanyl",
            confidence=0.95,
            spectral_peaks=[1004.0],
            spatial_location=(128, 128)
        )]
        
        mass_spec = [MassSpecDetection(
            compound_name="Fentanyl",
            molecular_weight=336.47,
            confidence=0.94,
            concentration_ppq=2.5
        )]
        
        thermal = ThermalAnalysis(
            anomaly_score=0.3,
            anomaly_locations=[],
            temperature_variance=100.0
        )
        
        vehicle = VehicleInfo(
            license_plate="ABC123",
            vehicle_type="truck",
            speed_mph=75.0,
            timestamp=0.0
        )
        
        assessment = engine.fuse_detections(spectral, mass_spec, thermal, vehicle)
        assert isinstance(assessment, ThreatAssessment)
        assert assessment.threat_level in ['HIGH', 'MEDIUM', 'LOW', 'CLEAR']


class TestThreatAssessor:
    """Test cases for threat assessor."""
    
    def test_initialization(self):
        """Test threat assessor initialization."""
        assessor = ThreatAssessor()
        assert assessor._high_risk_compounds is not None
        
    def test_should_alert(self):
        """Test alert decision logic."""
        assessor = ThreatAssessor()
        
        high_threat = ThreatAssessment(
            threat_level='HIGH',
            confidence=0.95,
            detected_compounds=['Fentanyl'],
            contributing_factors={},
            vehicle_info=VehicleInfo("ABC", "truck", 75.0, 0.0)
        )
        
        assert assessor.should_alert(high_threat)
        
    def test_priority_calculation(self):
        """Test alert priority calculation."""
        assessor = ThreatAssessor()
        
        assessment = ThreatAssessment(
            threat_level='HIGH',
            confidence=0.95,
            detected_compounds=['Fentanyl'],
            contributing_factors={},
            vehicle_info=VehicleInfo("ABC", "truck", 75.0, 0.0)
        )
        
        priority = assessor.calculate_priority(assessment)
        assert 1 <= priority <= 5
