"""
Unit tests for sensor module.

Tests QCL controller, MCT reader, AFT-MS interface, and camera manager.
"""

import pytest
import numpy as np

from src.sensor.qcl_controller import QCLController
from src.sensor.mct_reader import MCTReader
from src.sensor.aftms_interface import AFTMSInterface
from src.sensor.camera_manager import CameraManager


class TestQCLController:
    """Test cases for QCL controller."""
    
    def test_initialization(self):
        """Test QCL controller initialization."""
        controller = QCLController(num_lasers=4)
        assert controller.num_lasers == 4
        assert not controller._connected
        
    def test_wavelength_tuning(self):
        """Test wavelength tuning."""
        controller = QCLController()
        assert controller.tune_wavelength(0, 8.0)
        assert controller._current_wavelengths[0] == 8.0
        
    def test_invalid_wavelength(self):
        """Test that invalid wavelengths raise errors."""
        controller = QCLController()
        with pytest.raises(ValueError):
            controller.tune_wavelength(0, 15.0)  # Out of range
            
    def test_spectral_data_acquisition(self):
        """Test spectral data retrieval."""
        controller = QCLController()
        data = controller.get_spectral_data()
        assert isinstance(data, np.ndarray)
        assert data.shape[1] == 2  # wavelength and intensity


class TestMCTReader:
    """Test cases for MCT detector reader."""
    
    def test_initialization(self):
        """Test MCT reader initialization."""
        reader = MCTReader(resolution=(256, 256))
        assert reader.resolution == (256, 256)
        
    def test_frame_capture(self):
        """Test frame capture."""
        reader = MCTReader()
        frame = reader.capture_frame()
        assert isinstance(frame, np.ndarray)
        assert frame.shape == (256, 256)
        
    def test_hyperspectral_cube(self):
        """Test hyperspectral cube capture."""
        reader = MCTReader()
        cube = reader.capture_hyperspectral_cube(num_spectral_bands=128)
        assert cube.shape == (256, 256, 128)


class TestAFTMSInterface:
    """Test cases for AFT-MS interface."""
    
    def test_initialization(self):
        """Test AFT-MS initialization."""
        interface = AFTMSInterface()
        assert not interface._connected
        
    def test_mass_spectrum_acquisition(self):
        """Test mass spectrum retrieval."""
        interface = AFTMSInterface()
        spectrum = interface.get_mass_spectrum()
        assert spectrum.masses is not None
        assert spectrum.intensities is not None
        
    def test_compound_identification(self):
        """Test compound identification."""
        interface = AFTMSInterface()
        matches = interface.identify_compounds()
        assert isinstance(matches, list)


class TestCameraManager:
    """Test cases for camera manager."""
    
    def test_thermal_capture(self):
        """Test thermal camera capture."""
        manager = CameraManager()
        manager.connect_thermal()
        frame = manager.capture_thermal()
        assert frame.camera_type == 'thermal'
        assert frame.image.shape == (480, 640)
        
    def test_optical_capture(self):
        """Test optical camera capture."""
        manager = CameraManager()
        manager.connect_optical()
        frame = manager.capture_optical()
        assert frame.camera_type == 'optical'
        assert frame.image.shape == (2160, 3840, 3)
