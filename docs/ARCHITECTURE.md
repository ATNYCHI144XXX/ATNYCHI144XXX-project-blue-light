# System Architecture

**PROJECT BLUE-LIGHT** - High-Speed Standoff Fentanyl Interdiction System

---

## Table of Contents

1. [Architecture Overview](#1-architecture-overview)
2. [Hardware Components](#2-hardware-components)
3. [Software Stack](#3-software-stack)
4. [Data Flow](#4-data-flow)
5. [Integration Points](#5-integration-points)
6. [Network Architecture](#6-network-architecture)
7. [Security & Reliability](#7-security--reliability)

---

## 1. Architecture Overview

### 1.1 System Layers

PROJECT BLUE-LIGHT follows a layered architecture pattern:

```
┌─────────────────────────────────────────────────────────────┐
│                     Layer 5: Presentation                    │
│              (Law Enforcement Dashboards & Alerts)           │
├─────────────────────────────────────────────────────────────┤
│                     Layer 4: Application                     │
│         (Alert Management, Vehicle Tracking, Analytics)      │
├─────────────────────────────────────────────────────────────┤
│                     Layer 3: Fusion Engine                   │
│            (AI Sensor Fusion, Threat Assessment)             │
├─────────────────────────────────────────────────────────────┤
│                     Layer 2: Processing                      │
│    (Spectral Analysis, Mass Spec Processing, Image AI)      │
├─────────────────────────────────────────────────────────────┤
│                     Layer 1: Hardware                        │
│       (QCL-MCT, AFT-MS, Thermal/Optical Cameras)            │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Deployment Model

**Edge Computing Architecture**: Each sensor unit operates as an autonomous edge computing node with local processing and decision-making capabilities.

**Benefits**:
- Sub-second latency (critical for 120 MPH operation)
- Reduced bandwidth requirements
- Continued operation during network outages
- Enhanced privacy (local filtering before transmission)

---

## 2. Hardware Components

### 2.1 Sensor Module

#### Physical Housing
- **Dimensions**: 45cm × 30cm × 25cm
- **Weight**: 15 kg
- **Enclosure Rating**: IP67 (weatherproof, dust-tight)
- **Operating Temperature**: -40°C to +60°C
- **Thermal Management**: Active cooling with redundant fans

#### Component Layout

```
┌──────────────────────────────────────────────────┐
│  Sensor Housing - Exploded View                  │
│                                                   │
│  ┌─────────────────────────────────────────┐    │
│  │  Optical Window (Sapphire, AR-Coated)   │    │
│  └─────────────────┬───────────────────────┘    │
│                    │                             │
│  ┌─────────────────▼───────────────────────┐    │
│  │  QCL Array (4 lasers, 5-12 µm)          │    │
│  │  + MCT Detector (256×256 FPA)           │    │
│  └─────────────────┬───────────────────────┘    │
│                    │                             │
│  ┌─────────────────▼───────────────────────┐    │
│  │  AFT-MS Inlet (Air Scoop + Mass Spec)   │    │
│  └─────────────────┬───────────────────────┘    │
│                    │                             │
│  ┌─────────────────▼───────────────────────┐    │
│  │  Thermal Camera (LWIR, 640×480)         │    │
│  │  Optical Camera (4K, 30 fps)            │    │
│  └─────────────────┬───────────────────────┘    │
│                    │                             │
│  ┌─────────────────▼───────────────────────┐    │
│  │  Edge Computing Unit                     │    │
│  │  - NVIDIA Jetson Thor                    │    │
│  │  - 64GB RAM                              │    │
│  │  - 512GB NVMe SSD                        │    │
│  └─────────────────┬───────────────────────┘    │
│                    │                             │
│  ┌─────────────────▼───────────────────────┐    │
│  │  Power Supply & Comms                    │    │
│  │  - 300W PSU (gantry power)              │    │
│  │  - 5G Modem (backup)                    │    │
│  │  - Fiber Optic Interface (primary)      │    │
│  └──────────────────────────────────────────┘   │
└──────────────────────────────────────────────────┘
```

### 2.2 Component Specifications

#### Quantum Cascade Laser (QCL) System
- **Manufacturer**: Block Engineering / Daylight Solutions
- **Tuning Range**: 5.0 – 12.0 µm (continuous)
- **Pulse Rate**: 1 MHz (femtosecond mode)
- **Power Output**: 50 mW per laser
- **Beam Divergence**: < 2 mrad
- **Spectral Resolution**: 0.1 cm⁻¹

#### MCT Detector
- **Type**: Mercury Cadmium Telluride (MCT) Focal Plane Array
- **Resolution**: 256 × 256 pixels
- **Spectral Response**: 2.5 – 12 µm
- **Frame Rate**: 1000 Hz
- **NETD**: < 20 mK
- **Cooling**: Thermoelectric (no cryogenics)

#### AFT-MS Unit
- **Technology**: Atmospheric Flow Tube Mass Spectrometry
- **Mass Range**: 50 – 500 amu
- **Resolution**: 0.5 amu
- **Sensitivity**: Parts-per-quadrillion (ppq)
- **Analysis Time**: 200 milliseconds
- **Reagent Ion**: H₃O⁺ (proton transfer reaction)

#### Thermal Camera
- **Type**: Long-Wave Infrared (LWIR)
- **Resolution**: 640 × 480 pixels
- **Spectral Range**: 7.5 – 14 µm
- **Frame Rate**: 30 fps
- **NETD**: < 50 mK

#### Optical Camera
- **Resolution**: 4K (3840 × 2160)
- **Frame Rate**: 30 fps
- **Sensor**: 1/2.3" CMOS
- **Features**: Auto-focus, HDR, license plate optimization

### 2.3 Edge Computing Platform

#### Primary Processor
- **Model**: NVIDIA Jetson AGX Thor (or equivalent)
- **GPU**: 2000 CUDA cores
- **AI Performance**: 200 TOPS (INT8)
- **CPU**: ARM Cortex-A78AE (12 cores)
- **RAM**: 64 GB LPDDR5
- **Storage**: 512 GB NVMe SSD

#### Software Acceleration
- **Deep Learning**: TensorRT optimization
- **Computer Vision**: CUDA-accelerated OpenCV
- **Signal Processing**: cuFFT for spectral analysis

---

## 3. Software Stack

### 3.1 Software Architecture Diagram

```
┌────────────────────────────────────────────────────────────┐
│                    Application Layer                        │
│  ┌──────────────┐  ┌──────────────┐  ┌─────────────────┐  │
│  │ Alert System │  │ Dashboard UI │  │ API Gateway     │  │
│  └──────┬───────┘  └──────┬───────┘  └────────┬────────┘  │
├─────────┼──────────────────┼──────────────────┼────────────┤
│         │         AI Fusion Engine             │            │
│  ┌──────▼───────────────────▼──────────────────▼────────┐  │
│  │  Sensor Fusion AI (Multi-Modal Integration)          │  │
│  │  - Threat Assessment                                  │  │
│  │  - Confidence Scoring                                 │  │
│  │  - Alert Decision Logic                               │  │
│  └───────┬───────────┬──────────────┬─────────────┬─────┘  │
├──────────┼───────────┼──────────────┼─────────────┼────────┤
│          │    Processing Services    │             │        │
│  ┌───────▼──┐  ┌────▼─────┐  ┌─────▼────┐  ┌────▼─────┐  │
│  │Spectral  │  │Mass Spec │  │ Image    │  │ Vehicle  │  │
│  │Analysis  │  │Analysis  │  │ Analysis │  │ Tracking │  │
│  └───────┬──┘  └────┬─────┘  └─────┬────┘  └────┬─────┘  │
├──────────┼──────────┼──────────────┼─────────────┼────────┤
│          │    Hardware Abstraction Layer          │        │
│  ┌───────▼──────────▼──────────────▼─────────────▼─────┐  │
│  │  Hardware Interface (Drivers & Control)              │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────────────────────────────────────────┘
```

### 3.2 Software Components

#### Module 1: Sensor Interface Layer (`src/sensor/`)

**Purpose**: Hardware abstraction and data acquisition

**Components**:
- `qcl_controller.py`: QCL laser control and tuning
- `mct_reader.py`: MCT detector data acquisition
- `aftms_interface.py`: Mass spectrometry control and data retrieval
- `camera_manager.py`: Thermal and optical camera management
- `sensor_calibration.py`: Runtime calibration and drift compensation

**Key Functions**:
```python
class QCLController:
    def tune_wavelength(self, wavelength_um: float)
    def pulse_sequence(self, duration_ms: int)
    def get_spectral_data(self) -> np.ndarray

class AFTMSInterface:
    def start_sampling(self)
    def get_mass_spectrum(self) -> MassSpectrum
    def identify_compounds(self) -> List[ChemicalMatch]
```

#### Module 2: AI Detection Layer (`src/ai/`)

**Purpose**: Chemical signature recognition and classification

**Components**:
- `spectral_classifier.py`: Fentanyl signature detection from QCL-MCT data
- `mass_spec_analyzer.py`: AFT-MS spectrum interpretation
- `thermal_anomaly_detector.py`: Hidden compartment detection
- `model_manager.py`: AI model loading and inference
- `training_pipeline.py`: Model retraining infrastructure

**AI Models**:
1. **Spectral CNN**: Convolutional neural network for hyperspectral analysis
   - Input: 256×256×128 (spatial × spectral)
   - Output: Chemical class probabilities
   - Architecture: ResNet-50 backbone with attention

2. **Mass Spectrum Classifier**: 1D CNN for mass spectrometry
   - Input: 1D mass spectrum (50-500 amu)
   - Output: Compound identification
   - Architecture: Custom 1D ResNet

3. **Thermal Anomaly Detection**: Autoencoder for anomaly detection
   - Input: 640×480 thermal image
   - Output: Anomaly heatmap
   - Architecture: U-Net style autoencoder

#### Module 3: Sensor Fusion (`src/fusion/`)

**Purpose**: Multi-modal integration and threat assessment

**Components**:
- `fusion_engine.py`: Core fusion logic
- `confidence_calculator.py`: Bayesian confidence scoring
- `threat_assessor.py`: Risk level determination
- `decision_logic.py`: Alert triggering rules

**Fusion Algorithm**:
```python
def fuse_detections(
    spectral_result: SpectralDetection,
    mass_spec_result: MassSpecDetection,
    thermal_result: ThermalAnalysis,
    vehicle_data: VehicleInfo
) -> ThreatAssessment:
    
    # Bayesian fusion
    prior = get_base_rate(vehicle_data.type)
    
    likelihood_spectral = spectral_result.confidence
    likelihood_mass_spec = mass_spec_result.confidence
    likelihood_thermal = thermal_result.anomaly_score
    
    # Combined probability
    posterior = bayesian_update(
        prior, 
        [likelihood_spectral, likelihood_mass_spec, likelihood_thermal]
    )
    
    return ThreatAssessment(
        confidence=posterior,
        threat_level=classify_threat(posterior),
        contributing_factors=[...]
    )
```

#### Module 4: Alert System (`src/alert/`)

**Purpose**: Alert generation and notification delivery

**Components**:
- `alert_generator.py`: Alert packet creation
- `notification_service.py`: Multi-channel alert delivery
- `alert_logger.py`: Audit trail and logging
- `priority_queue.py`: Alert prioritization

**Alert Channels**:
1. **Primary**: Direct transmission to patrol units (encrypted 5G/fiber)
2. **Secondary**: Command center dashboard update
3. **Tertiary**: Database logging for analytics

---

## 4. Data Flow

### 4.1 Real-Time Detection Pipeline

```
┌──────────────┐
│   Vehicle    │
│  Approaches  │
└──────┬───────┘
       │
       ▼
┌──────────────┐    ┌────────────────────────────────────┐
│     LPR      │───>│  Vehicle Database Lookup           │
│  Detection   │    │  - Known hauler?                   │
└──────┬───────┘    │  - Previous flags?                 │
       │            └────────────────────────────────────┘
       ▼
┌──────────────┐
│ Sensor Wake  │
│   Sequence   │
└──────┬───────┘
       │
       ├────────────┬────────────┬────────────┐
       │            │            │            │
       ▼            ▼            ▼            ▼
┌──────────┐ ┌───────────┐ ┌─────────┐ ┌─────────┐
│   QCL    │ │  AFT-MS   │ │ Thermal │ │ Optical │
│ Scan     │ │  Sample   │ │  Image  │ │  Image  │
└────┬─────┘ └─────┬─────┘ └────┬────┘ └────┬────┘
     │             │            │          │
     └─────────────┴────────────┴──────────┘
                   │
                   ▼
          ┌────────────────┐
          │  Parallel      │
          │  Processing    │
          └────────┬───────┘
                   │
     ┌─────────────┴─────────────┐
     │                           │
     ▼                           ▼
┌──────────┐              ┌────────────┐
│ Spectral │              │ Mass Spec  │
│ Analysis │              │ Analysis   │
└────┬─────┘              └─────┬──────┘
     │                          │
     └────────┬──────────────────┘
              │
              ▼
      ┌──────────────┐
      │ Sensor Fusion│
      │    Engine    │
      └──────┬───────┘
             │
             ▼
      ┌──────────────┐
      │  Confidence  │
      │   > 0.90?    │
      └──────┬───────┘
             │
        YES  │  NO
      ┌──────┴──────┐
      │             │
      ▼             ▼
┌──────────┐  ┌──────────┐
│ Generate │  │  Log &   │
│  Alert   │  │ Discard  │
└────┬─────┘  └──────────┘
     │
     ▼
┌──────────┐
│ Transmit │
│to Patrol │
└──────────┘
```

### 4.2 Data Flow Timing

**Total Pipeline Latency**: < 800 milliseconds

| Stage | Duration | Cumulative |
|-------|----------|------------|
| Vehicle approaches | (500m out) | 0 ms |
| LPR detection & database check | 50 ms | 50 ms |
| Sensor wake & stabilization | 100 ms | 150 ms |
| Active scanning (under gantry) | 600 ms | 750 ms |
| Spectral processing | 150 ms | 900 ms (parallel) |
| Mass spec processing | 200 ms | 950 ms (parallel) |
| Fusion & decision | 50 ms | 300 ms (after sensors) |
| Alert generation | 20 ms | 320 ms |
| Transmission | 30 ms | 350 ms |
| **Total (sensor to alert)** | | **~800 ms** |

---

## 5. Integration Points

### 5.1 External Systems

#### Law Enforcement CAD Systems
- **Interface**: RESTful API / HL7 FHIR
- **Data Exchange**: Alert packets, vehicle information
- **Authentication**: Mutual TLS with certificate pinning

#### License Plate Recognition (LPR) Databases
- **Interface**: Real-time query API
- **Purpose**: Vehicle identification and history lookup
- **Providers**: Vigilant Solutions, ELSAG, local DMV databases

#### NCIC (National Crime Information Center)
- **Interface**: CJIS-compliant secure connection
- **Purpose**: Stolen vehicle checks, warrant lookups
- **Security**: FBI CJIS Security Policy compliance

#### Highway Management Systems
- **Interface**: NTCIP (National Transportation Communications for ITS Protocol)
- **Purpose**: Traffic flow data, incident coordination
- **Integration**: Real-time traffic management center updates

### 5.2 API Specifications

#### Alert Notification API

**Endpoint**: `POST /api/v1/alerts`

**Request**:
```json
{
  "alert_id": "string",
  "timestamp": "ISO8601",
  "location": {
    "gantry_id": "string",
    "gps": [lat, lon],
    "highway": "string"
  },
  "vehicle": {
    "license_plate": "string",
    "state": "string",
    "photo_url": "string"
  },
  "detection": {
    "chemical_match": "string",
    "confidence": float,
    "estimated_mass": "string"
  },
  "threat_level": "HIGH|MEDIUM|LOW"
}
```

**Response**:
```json
{
  "status": "received",
  "alert_id": "string",
  "assigned_unit": "string",
  "eta_to_intercept": "integer (seconds)"
}
```

---

## 6. Network Architecture

### 6.1 Connectivity

#### Primary: Fiber Optic
- **Bandwidth**: 1 Gbps
- **Latency**: < 5 ms to regional hub
- **Reliability**: 99.99% uptime

#### Backup: 5G Cellular
- **Bandwidth**: 100+ Mbps
- **Latency**: < 30 ms
- **Failover**: Automatic within 2 seconds

#### Local: Edge Computing
- **Processing**: 100% local for detection pipeline
- **Transmission**: Only alerts and metadata (not raw sensor data)
- **Storage**: 7 days local retention for forensics

### 6.2 Data Security

#### Encryption
- **In Transit**: TLS 1.3 with AES-256-GCM
- **At Rest**: Full disk encryption (LUKS / BitLocker)
- **Key Management**: Hardware Security Module (HSM)

#### Access Control
- **Authentication**: Multi-factor authentication for administrators
- **Authorization**: Role-based access control (RBAC)
- **Audit**: Complete logging of all system access

---

## 7. Security & Reliability

### 7.1 System Hardening

#### Physical Security
- Tamper-evident enclosure seals
- Accelerometer-based tampering detection
- Secure boot with TPM 2.0

#### Cybersecurity
- Minimal attack surface (no unnecessary services)
- Automatic security updates
- Intrusion detection system (IDS)
- Network segmentation (sensor network isolated from internet)

### 7.2 Reliability & Redundancy

#### Component Redundancy
- **Power**: Dual power supplies
- **Cooling**: Redundant fans with thermal throttling
- **Communications**: Primary (fiber) + backup (5G)

#### Fault Tolerance
- **Watchdog Timer**: Automatic reboot on system hang
- **Health Monitoring**: Continuous self-diagnostics
- **Graceful Degradation**: Operate with reduced capability if sensors fail

#### Maintenance
- **Remote Diagnostics**: SSH access for troubleshooting
- **Predictive Maintenance**: ML-based failure prediction
- **Mean Time Between Failures (MTBF)**: > 50,000 hours

### 7.3 Quality Assurance

#### Calibration
- **Frequency**: Monthly automated calibration
- **Reference Standards**: NIST-traceable spectral references
- **Drift Correction**: Real-time compensation algorithms

#### Performance Monitoring
- **Metrics**: Detection rate, false positive rate, latency
- **Reporting**: Monthly performance reports to operators
- **Continuous Improvement**: Model retraining based on field data

---

## 8. Scalability Considerations

### 8.1 Horizontal Scaling

**Single Unit**: Monitors 1 highway location  
**10-Unit Pilot**: Covers major drug corridor  
**500-Unit Network**: National interstate coverage

**Scaling Characteristics**:
- **Linear Cost**: Each unit operates independently
- **No Central Bottleneck**: Edge computing eliminates centralized processing
- **Distributed Intelligence**: AI models distributed to each unit

### 8.2 Cloud Integration

**Optional Cloud Services**:
- **Centralized Analytics**: Aggregate data for pattern recognition
- **Model Training**: Cloud-based training with distributed deployment
- **Dashboard**: National-level situational awareness

**Architecture**: Hybrid edge-cloud model
- **Edge**: Real-time detection and alerting (latency-critical)
- **Cloud**: Analytics and model improvement (non-latency-critical)

---

## 9. Future Architecture Enhancements

### 9.1 Planned Improvements

1. **Multi-Substance Detection**: Expand beyond fentanyl to other narcotics and explosives
2. **Predictive Analytics**: ML models to identify trafficking patterns
3. **Autonomous Interdiction Coordination**: AI-driven patrol routing
4. **Swarm Intelligence**: Multiple sensors coordinate for convoy tracking

### 9.2 Research Directions

- **Quantum Sensors**: Next-generation detection sensitivity
- **Neuromorphic Computing**: Ultra-low-power edge AI
- **6G Communications**: Enhanced bandwidth and reduced latency
- **Blockchain**: Tamper-proof evidence chain of custody

---

**Document Version**: 1.0  
**Last Updated**: December 2025  
**Classification**: Unclassified
