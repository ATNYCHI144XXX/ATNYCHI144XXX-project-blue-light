"""
Sensor Fusion Module

Combines data from multiple sensor modalities to generate comprehensive
threat assessments using Bayesian inference and AI integration.
"""

from .fusion_engine import FusionEngine
from .threat_assessor import ThreatAssessor

__all__ = [
    "FusionEngine",
    "ThreatAssessor",
]
