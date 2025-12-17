"""
AI Detection and Classification Module

Provides machine learning models for chemical signature recognition,
spectral analysis, and threat assessment.
"""

from .spectral_classifier import SpectralClassifier
from .mass_spec_analyzer import MassSpecAnalyzer
from .thermal_anomaly_detector import ThermalAnomalyDetector

__all__ = [
    "SpectralClassifier",
    "MassSpecAnalyzer",
    "ThermalAnomalyDetector",
]
