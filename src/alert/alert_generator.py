"""
Alert Generator

Creates standardized alert packets for law enforcement notification.
"""

import json
import time
from typing import Dict, Optional
from dataclasses import dataclass, asdict

from ..fusion.fusion_engine import ThreatAssessment


@dataclass
class AlertPacket:
    """Standardized alert packet structure."""
    alert_id: str
    timestamp: float
    location: Dict[str, any]
    vehicle: Dict[str, any]
    detection: Dict[str, any]
    threat_level: str
    recommended_action: str
    

class AlertGenerator:
    """
    Generates standardized alert packets.
    
    Creates JSON-formatted alerts conforming to the PROJECT BLUE-LIGHT
    alert specification for law enforcement integration.
    """
    
    def __init__(self, gantry_id: str, gps_coordinates: tuple):
        """
        Initialize alert generator.
        
        Args:
            gantry_id: Unique identifier for this sensor installation
            gps_coordinates: (latitude, longitude) of sensor location
        """
        self.gantry_id = gantry_id
        self.gps_coordinates = gps_coordinates
        self._alert_counter = 0
        
    def generate_alert(
        self,
        assessment: ThreatAssessment,
        license_plate: Optional[str],
        vehicle_photo_url: Optional[str],
        recommended_action: str
    ) -> AlertPacket:
        """
        Generate alert packet from threat assessment.
        
        Args:
            assessment: Threat assessment result
            license_plate: Vehicle license plate (if detected)
            vehicle_photo_url: URL to vehicle photo
            recommended_action: Recommended law enforcement action
            
        Returns:
            AlertPacket ready for transmission
        """
        # Generate unique alert ID
        alert_id = self._generate_alert_id()
        
        # Build location information
        location = {
            "gantry_id": self.gantry_id,
            "gps": list(self.gps_coordinates),
            "highway": self._infer_highway()  # TODO: Implement based on GPS
        }
        
        # Build vehicle information
        vehicle = {
            "license_plate": license_plate or "UNKNOWN",
            "state": "XX",  # TODO: Parse from plate
            "type": assessment.vehicle_info.vehicle_type,
            "speed_mph": assessment.vehicle_info.speed_mph,
            "photo_url": vehicle_photo_url
        }
        
        # Build detection information
        detection = {
            "chemical_match": ", ".join(assessment.detected_compounds) or "None",
            "confidence": assessment.confidence,
            "confidence_breakdown": assessment.contributing_factors,
            "detected_compounds": assessment.detected_compounds,
        }
        
        return AlertPacket(
            alert_id=alert_id,
            timestamp=time.time(),
            location=location,
            vehicle=vehicle,
            detection=detection,
            threat_level=assessment.threat_level,
            recommended_action=recommended_action
        )
        
    def _generate_alert_id(self) -> str:
        """Generate unique alert identifier."""
        self._alert_counter += 1
        timestamp = int(time.time())
        return f"BL-{self.gantry_id}-{timestamp}-{self._alert_counter:04d}"
        
    def _infer_highway(self) -> str:
        """Infer highway name from GPS coordinates."""
        # TODO: Implement reverse geocoding
        return "Unknown Highway"
        
    def to_json(self, alert: AlertPacket) -> str:
        """
        Convert alert packet to JSON string.
        
        Args:
            alert: AlertPacket to serialize
            
        Returns:
            JSON string representation
        """
        return json.dumps(asdict(alert), indent=2)
        
    def to_dict(self, alert: AlertPacket) -> Dict:
        """
        Convert alert packet to dictionary.
        
        Args:
            alert: AlertPacket to convert
            
        Returns:
            Dictionary representation
        """
        return asdict(alert)
