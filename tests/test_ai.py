"""
Unit tests for AI module.

Tests spectral classifier, mass spec analyzer, and thermal anomaly detector.
"""

import pytest
import numpy as np

from src.ai.spectral_classifier import SpectralClassifier
from src.ai.mass_spec_analyzer import MassSpecAnalyzer
from src.ai.thermal_anomaly_detector import ThermalAnomalyDetector


class TestSpectralClassifier:
    """Test cases for spectral classifier."""
    
    def test_initialization(self):
        """Test classifier initialization."""
        classifier = SpectralClassifier()
        assert not classifier._model_loaded
        
    def test_preprocessing(self):
        """Test hyperspectral data preprocessing."""
        classifier = SpectralClassifier()
        cube = np.random.random((256, 256, 128))
        processed = classifier.preprocess_hyperspectral_cube(cube)
        assert processed.shape == cube.shape
        
    def test_classification(self):
        """Test chemical classification."""
        classifier = SpectralClassifier()
        cube = np.random.random((256, 256, 128))
        detections = classifier.classify(cube)
        assert isinstance(detections, list)


class TestMassSpecAnalyzer:
    """Test cases for mass spec analyzer."""
    
    def test_initialization(self):
        """Test analyzer initialization."""
        analyzer = MassSpecAnalyzer()
        assert analyzer._spectral_library is not None
        
    def test_spectrum_analysis(self):
        """Test mass spectrum analysis."""
        analyzer = MassSpecAnalyzer()
        masses = np.linspace(50, 500, 450)
        intensities = np.random.random(450)
        detections = analyzer.analyze_spectrum(masses, intensities)
        assert isinstance(detections, list)
        
    def test_library_matching(self):
        """Test spectral library matching."""
        analyzer = MassSpecAnalyzer()
        peaks = [337.0, 188.0, 105.0]
        matches = analyzer.match_to_library(peaks)
        assert isinstance(matches, list)


class TestThermalAnomalyDetector:
    """Test cases for thermal anomaly detector."""
    
    def test_initialization(self):
        """Test detector initialization."""
        detector = ThermalAnomalyDetector()
        assert not detector._model_loaded
        
    def test_thermal_analysis(self):
        """Test thermal image analysis."""
        detector = ThermalAnomalyDetector()
        image = np.random.randint(0, 65535, size=(480, 640))
        analysis = detector.analyze(image)
        assert 0.0 <= analysis.anomaly_score <= 1.0
        
    def test_anomaly_detection(self):
        """Test anomaly location detection."""
        detector = ThermalAnomalyDetector()
        image = np.random.randint(0, 65535, size=(480, 640))
        analysis = detector.analyze(image)
        assert isinstance(analysis.anomaly_locations, list)
