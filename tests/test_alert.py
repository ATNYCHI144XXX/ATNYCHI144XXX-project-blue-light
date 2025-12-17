"""
Unit tests for alert module.

Tests alert generator and notification service.
"""

import pytest
import json

from src.alert.alert_generator import AlertGenerator
from src.alert.notification_service import NotificationService, NotificationChannel
from src.fusion.fusion_engine import ThreatAssessment, VehicleInfo


class TestAlertGenerator:
    """Test cases for alert generator."""
    
    def test_initialization(self):
        """Test alert generator initialization."""
        generator = AlertGenerator("TEST-001", (39.0, -76.0))
        assert generator.gantry_id == "TEST-001"
        assert generator.gps_coordinates == (39.0, -76.0)
        
    def test_alert_generation(self):
        """Test alert packet generation."""
        generator = AlertGenerator("TEST-001", (39.0, -76.0))
        
        assessment = ThreatAssessment(
            threat_level='HIGH',
            confidence=0.95,
            detected_compounds=['Fentanyl'],
            contributing_factors={'spectral_confidence': 0.95},
            vehicle_info=VehicleInfo("ABC123", "truck", 75.0, 0.0)
        )
        
        alert = generator.generate_alert(
            assessment,
            license_plate="ABC123",
            vehicle_photo_url="http://example.com/photo.jpg",
            recommended_action="IMMEDIATE_INTERDICTION"
        )
        
        assert alert.alert_id is not None
        assert alert.threat_level == 'HIGH'
        assert alert.vehicle['license_plate'] == "ABC123"
        
    def test_json_serialization(self):
        """Test alert JSON serialization."""
        generator = AlertGenerator("TEST-001", (39.0, -76.0))
        
        assessment = ThreatAssessment(
            threat_level='HIGH',
            confidence=0.95,
            detected_compounds=['Fentanyl'],
            contributing_factors={},
            vehicle_info=VehicleInfo("ABC123", "truck", 75.0, 0.0)
        )
        
        alert = generator.generate_alert(assessment, "ABC123", None, "INTERDICTION")
        json_str = generator.to_json(alert)
        
        # Verify it's valid JSON
        parsed = json.loads(json_str)
        assert parsed['alert_id'] == alert.alert_id


class TestNotificationService:
    """Test cases for notification service."""
    
    def test_initialization(self):
        """Test notification service initialization."""
        service = NotificationService()
        assert len(service.get_enabled_channels()) > 0
        
    def test_channel_management(self):
        """Test enabling/disabling channels."""
        service = NotificationService()
        
        # Disable a channel
        service.disable_channel(NotificationChannel.EMAIL)
        assert NotificationChannel.EMAIL not in service.get_enabled_channels()
        
        # Re-enable it
        service.enable_channel(NotificationChannel.EMAIL)
        assert NotificationChannel.EMAIL in service.get_enabled_channels()
        
    def test_alert_sending(self):
        """Test alert sending."""
        service = NotificationService()
        generator = AlertGenerator("TEST-001", (39.0, -76.0))
        
        assessment = ThreatAssessment(
            threat_level='HIGH',
            confidence=0.95,
            detected_compounds=['Fentanyl'],
            contributing_factors={},
            vehicle_info=VehicleInfo("ABC123", "truck", 75.0, 0.0)
        )
        
        alert = generator.generate_alert(assessment, "ABC123", None, "INTERDICTION")
        result = service.send_alert(alert, priority=5)
        
        # Should succeed (even with placeholder implementation)
        assert result
