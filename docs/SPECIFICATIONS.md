# Technical Specifications

**PROJECT BLUE-LIGHT** - Component-Level Specifications

---

## Table of Contents

1. [Quantum Cascade Laser (QCL) Specifications](#1-quantum-cascade-laser-qcl-specifications)
2. [MCT Detector Specifications](#2-mct-detector-specifications)
3. [AFT-MS Specifications](#3-aft-ms-specifications)
4. [Processing Platform Specifications](#4-processing-platform-specifications)
5. [Detection Thresholds](#5-detection-thresholds)
6. [Target Compound Specifications](#6-target-compound-specifications)
7. [Environmental Specifications](#7-environmental-specifications)
8. [Performance Specifications](#8-performance-specifications)

---

## 1. Quantum Cascade Laser (QCL) Specifications

### 1.1 Laser Array Configuration

**Number of Lasers**: 4 independent QCL modules  
**Coverage**: Combined coverage of 5.0 – 12.0 µm mid-IR spectrum

#### Individual QCL Module Specs

| Parameter | Specification |
|-----------|---------------|
| **Tuning Range** | 2.5 µm (per module) |
| **Wavelength Accuracy** | ±0.5 nm |
| **Wavelength Stability** | ±0.1 nm over 24 hours |
| **Tuning Speed** | 1000 nm/second |
| **Output Power** | 50 mW (continuous wave) |
| **Beam Quality** | M² < 1.3 |
| **Beam Divergence** | < 2 mrad (full angle) |
| **Polarization** | Linear, >100:1 ratio |
| **Operating Temperature** | 15°C – 35°C (TEC-stabilized) |

### 1.2 Pulsing Characteristics

**Operating Modes**:
1. **Continuous Wave (CW)**: For stationary or slow-moving targets
2. **Femtosecond Pulsed**: For high-speed (120 MPH) operation

**Femtosecond Mode Specifications**:

| Parameter | Value |
|-----------|-------|
| **Pulse Duration** | 100 femtoseconds (10⁻¹³ seconds) |
| **Pulse Repetition Rate** | 1 MHz |
| **Peak Power** | 500 W (pulsed) |
| **Average Power** | 50 mW |
| **Duty Cycle** | 0.01% |
| **Timing Jitter** | < 10 femtoseconds |

### 1.3 Spectral Resolution

**Resolution**: 0.1 cm⁻¹ (wavenumber)  
**Accuracy**: ±0.5 cm⁻¹  
**Range**: 800 – 2000 cm⁻¹ (5 – 12.5 µm)

### 1.4 Control Interface

**Protocol**: Modbus TCP/IP  
**Update Rate**: 10 Hz  
**Commands**: Wavelength set, power level, pulse mode, calibration  
**Feedback**: Current wavelength, power output, temperature

---

## 2. MCT Detector Specifications

### 2.1 Focal Plane Array (FPA)

**Type**: Mercury Cadmium Telluride (HgCdTe) photovoltaic detector

| Parameter | Specification |
|-----------|---------------|
| **Array Format** | 256 × 256 pixels |
| **Pixel Pitch** | 30 µm |
| **Active Area** | 7.68 mm × 7.68 mm |
| **Spectral Response** | 2.5 – 12 µm |
| **Peak Quantum Efficiency** | >70% at 8 µm |
| **Cooling** | Thermoelectric cooler (TEC) |
| **Operating Temperature** | 180 K (-93°C) |
| **Temperature Stability** | ±0.1 K |

### 2.2 Performance Characteristics

| Parameter | Specification |
|-----------|---------------|
| **Frame Rate** | Up to 1000 Hz |
| **Integration Time** | 10 µs – 10 ms (adjustable) |
| **NETD** | <20 mK at 300 K, f/2 optics |
| **Dynamic Range** | 14-bit (16,384 levels) |
| **Linearity** | >99.5% |
| **Uniformity** | >98% (after NUC) |
| **Operability** | >99.5% (bad pixels <0.5%) |

### 2.3 Optical System

**Lens Configuration**: 50mm f/2 MCT-compatible optics

| Parameter | Value |
|-----------|-------|
| **Focal Length** | 50 mm |
| **F-Number** | f/2.0 |
| **Field of View** | 8.8° × 8.8° |
| **Working Distance** | 10 – 50 meters |
| **Spot Size at 25m** | 3.85 meters |
| **MTF** | >0.3 at Nyquist frequency |

### 2.4 Data Interface

**Output Format**: 16-bit TIFF or HDF5  
**Data Rate**: 250 MB/s (at 1000 Hz)  
**Interface**: Camera Link or CoaXPress  
**Latency**: <1 ms (detector to computer)

---

## 3. AFT-MS Specifications

### 3.1 Mass Spectrometer Configuration

**Type**: Atmospheric Flow Tube with Time-of-Flight (TOF) Mass Analysis

| Parameter | Specification |
|-----------|---------------|
| **Mass Range** | 50 – 500 amu (atomic mass units) |
| **Mass Resolution** | 0.5 amu (FWHM) |
| **Mass Accuracy** | ±0.1 amu |
| **Sensitivity** | Parts-per-quadrillion (10⁻¹⁵) |
| **Dynamic Range** | 10⁶ |
| **Scan Speed** | 10 Hz (full spectrum) |

### 3.2 Ion Source

**Reagent Ion**: H₃O⁺ (protonated water, for Proton Transfer Reaction)

| Parameter | Value |
|-----------|-------|
| **Ion Source Type** | Radio-frequency (RF) discharge |
| **Reagent Gas** | Water vapor (H₂O) |
| **Flow Rate** | 10 sccm (standard cubic cm per minute) |
| **Pressure** | 2.0 mbar (flow tube) |
| **E/N Ratio** | 120 Td (Townsend) |

### 3.3 Atmospheric Inlet

**Design**: High-speed air scoop with computational fluid dynamics optimization

| Parameter | Specification |
|-----------|---------------|
| **Inlet Type** | Critical orifice |
| **Sample Flow Rate** | 50 mL/min |
| **Response Time** | <200 ms |
| **Aerodynamic Design** | Optimized for 120 MPH vehicle wake capture |
| **Inlet Heating** | 100°C (prevents condensation) |

### 3.4 Detection Limits for Target Compounds

| Compound | Detection Limit (ppqv) | Typical Ambient | Signal-to-Noise |
|----------|------------------------|-----------------|-----------------|
| **Fentanyl** | 0.5 | <0.001 | >500:1 |
| **ANPP** | 0.8 | <0.001 | >300:1 |
| **NPP** | 1.0 | <0.001 | >250:1 |
| **Propionyl Chloride** | 0.3 | <0.001 | >800:1 |
| **Acetic Anhydride** | 0.5 | 0.01 – 0.1 | >100:1 |

### 3.5 Data Output

**Format**: Mass spectrum (mass vs. intensity)  
**Update Rate**: 10 Hz  
**Processing**: Real-time baseline subtraction and peak detection  
**Interface**: Ethernet (TCP/IP)

---

## 4. Processing Platform Specifications

### 4.1 Edge Computing Unit

**Platform**: NVIDIA Jetson AGX Thor or equivalent

| Component | Specification |
|-----------|---------------|
| **GPU** | 2000 CUDA cores (Ampere architecture) |
| **AI Performance** | 200 TOPS (Tera Operations Per Second, INT8) |
| **CPU** | 12-core ARM Cortex-A78AE @ 2.2 GHz |
| **RAM** | 64 GB LPDDR5 @ 6400 MHz |
| **Storage** | 512 GB NVMe SSD (PCIe 4.0) |
| **Power Consumption** | 60W typical, 100W peak |
| **Operating System** | Ubuntu 22.04 LTS (ARM64) |

### 4.2 Software Framework

**Deep Learning**: NVIDIA TensorRT 8.6+ with CUDA 12.0  
**Computer Vision**: OpenCV 4.8+ with CUDA acceleration  
**Signal Processing**: SciPy, NumPy with cuFFT  
**Communication**: gRPC for inter-service communication

### 4.3 AI Model Specifications

#### Spectral Classification Model

| Parameter | Value |
|-----------|-------|
| **Architecture** | ResNet-50 with Attention |
| **Input Dimensions** | 256 × 256 × 128 (H × W × Spectral) |
| **Output Classes** | 50 chemical compounds |
| **Parameters** | 25 million |
| **Inference Time** | 45 ms (TensorRT INT8) |
| **Accuracy** | 97.2% (on validation set) |
| **False Positive Rate** | 0.8% |

#### Mass Spectrum Classification Model

| Parameter | Value |
|-----------|-------|
| **Architecture** | 1D ResNet-34 |
| **Input** | 450 mass bins (50-500 amu) |
| **Output Classes** | 100 compounds |
| **Parameters** | 5 million |
| **Inference Time** | 12 ms |
| **Accuracy** | 98.5% |
| **False Positive Rate** | 0.5% |

---

## 5. Detection Thresholds

### 5.1 Sensitivity Requirements

**Design Goal**: Detect smallest operationally relevant quantities

| Detection Mode | Threshold | Operational Significance |
|----------------|-----------|--------------------------|
| **Surface Residue (QCL)** | 10 ng/cm² | Door handle contamination from handling |
| **Vapor Detection (AFT-MS)** | 0.5 ppqv | Leak from sealed container |
| **Bulk Detection (THz)** | 100 grams | Minimum trafficking quantity |

### 5.2 Confidence Thresholds

**Alert Generation Criteria**:

| Threat Level | Combined Confidence | Action |
|--------------|---------------------|--------|
| **HIGH** | >90% | Immediate interdiction alert |
| **MEDIUM** | 70-90% | Secondary inspection recommendation |
| **LOW** | 50-70% | Logged for analysis, no immediate action |
| **CLEAR** | <50% | No alert |

### 5.3 Multi-Modal Confirmation

**Fusion Logic**:
```
IF (QCL confidence > 95%) AND (AFT-MS confirms) THEN HIGH
ELSE IF (QCL confidence > 80%) OR (AFT-MS confirms) THEN MEDIUM
ELSE IF (Anomaly detected) THEN LOW
ELSE CLEAR
```

---

## 6. Target Compound Specifications

### 6.1 Fentanyl (Primary Target)

**Chemical Formula**: C₂₂H₂₈N₂O  
**CAS Number**: 437-38-7  
**Molecular Weight**: 336.47 g/mol

**Spectroscopic Signatures**:

| Method | Key Features |
|--------|--------------|
| **Mid-IR** | 1004 cm⁻¹ (C=O stretch), 1466 cm⁻¹ (aromatic), 2950 cm⁻¹ (C-H) |
| **Mass Spec** | m/z 337 [M+H]⁺, fragments at 188, 105, 84 |
| **Terahertz** | 1.2 THz, 1.8 THz, 2.5 THz (crystal lattice modes) |

**Detection Range**:
- **Spectral**: 5.4 – 12.8 µm mid-IR range
- **Primary Peak**: 1004 cm⁻¹ (highest confidence)
- **Confirmation Peaks**: 1466, 1572, 2950 cm⁻¹

### 6.2 Precursor Chemicals

#### ANPP (4-Anilino-N-phenethylpiperidine)

**Molecular Formula**: C₁₉H₂₄N₂  
**CAS Number**: 21409-26-7  
**Molecular Weight**: 280.41 g/mol  
**DEA List**: List I Chemical

**Signatures**:
- **Mid-IR**: 3350 cm⁻¹ (N-H), 1610 cm⁻¹ (aromatic)
- **Mass Spec**: m/z 281 [M+H]⁺

#### NPP (N-Phenethyl-4-piperidone)

**Molecular Formula**: C₁₃H₁₇NO  
**CAS Number**: 39742-60-4  
**Molecular Weight**: 203.28 g/mol  
**DEA List**: List I Chemical

**Signatures**:
- **Mid-IR**: 1715 cm⁻¹ (C=O ketone)
- **Mass Spec**: m/z 204 [M+H]⁺

#### Propionyl Chloride

**Molecular Formula**: C₃H₅ClO  
**CAS Number**: 79-03-8  
**Molecular Weight**: 92.52 g/mol  
**Characteristic**: Highly volatile

**Signatures**:
- **Mid-IR**: 1802 cm⁻¹ (C=O acid chloride)
- **Mass Spec**: m/z 93 [M+H]⁺
- **Vapor Pressure**: 276 mmHg at 20°C (excellent for AFT-MS)

---

## 7. Environmental Specifications

### 7.1 Operating Conditions

| Parameter | Specification |
|-----------|---------------|
| **Temperature Range** | -40°C to +60°C |
| **Humidity** | 0 – 100% RH (non-condensing in sealed housing) |
| **Altitude** | Sea level to 3000 meters |
| **Wind Speed** | Up to 100 mph (survival: 150 mph) |
| **Precipitation** | All weather (rain, snow, sleet) |
| **Solar Loading** | Full sun exposure (white/reflective housing) |

### 7.2 Enclosure Protection

**Rating**: IP67 (dust-tight, immersion resistant)  
**Materials**: 
- Housing: Marine-grade aluminum (6061-T6)
- Window: Sapphire with multi-layer AR coating
- Gaskets: EPDM rubber
- Fasteners: Stainless steel (316)

### 7.3 Power Requirements

| Parameter | Specification |
|-----------|---------------|
| **Input Voltage** | 120/240 VAC (50/60 Hz) or 48 VDC |
| **Power Consumption** | 300W typical, 450W peak |
| **Power Factor** | >0.95 |
| **Backup** | Internal battery (15 minutes UPS) |
| **Efficiency** | >90% (80 Plus Gold) |

---

## 8. Performance Specifications

### 8.1 Detection Performance

| Metric | Target | Achieved (Lab) | Achieved (Field) |
|--------|--------|----------------|------------------|
| **True Positive Rate** | >95% | 97.2% | 94.8% |
| **False Positive Rate** | <1% | 0.8% | 1.2% |
| **Detection Range** | 10-50m | 5-60m | 8-55m |
| **Maximum Speed** | 120 MPH | 140 MPH | 125 MPH |
| **Processing Latency** | <1 second | 650 ms | 820 ms |

### 8.2 Reliability

| Metric | Specification |
|--------|---------------|
| **MTBF** | >50,000 hours (5.7 years continuous) |
| **MTTR** | <4 hours (modular replacement) |
| **Availability** | >99.5% (including planned maintenance) |
| **Calibration Interval** | 30 days (automated) |
| **Service Life** | 10 years (design life) |

### 8.3 Data Quality

| Parameter | Specification |
|-----------|---------------|
| **Spectral SNR** | >100:1 for target peaks |
| **Mass Spec SNR** | >500:1 for target compounds |
| **Image Quality** | >0.3 MTF at Nyquist |
| **Timing Accuracy** | ±10 ms (GPS-synchronized) |

### 8.4 Network Performance

| Metric | Specification |
|--------|---------------|
| **Alert Delivery Time** | <100 ms (to patrol unit) |
| **Data Throughput** | 1 Gbps (fiber), 100 Mbps (5G backup) |
| **Network Latency** | <10 ms (fiber), <30 ms (5G) |
| **Packet Loss** | <0.01% |

---

## 9. Compliance & Standards

### 9.1 Safety Standards

- **Laser Safety**: IEC 60825-1 (Class 1 - eye-safe)
- **Electrical**: UL 61010-1, IEC 61010-1
- **EMC**: FCC Part 15 Class A, EN 55032
- **Environmental**: MIL-STD-810G (military environmental testing)

### 9.2 Communication Standards

- **Networking**: IEEE 802.3 (Ethernet), IEEE 802.11 (WiFi backup)
- **Security**: FIPS 140-2 Level 2 (cryptographic module)
- **Time Sync**: IEEE 1588 PTP (Precision Time Protocol)

### 9.3 Data Standards

- **Image Format**: TIFF 6.0, HDF5
- **Spectral Data**: JCAMP-DX, NetCDF
- **Metadata**: EXIF, XMP
- **Alert Format**: JSON (schema-validated)

---

## 10. Vendor Recommendations

### 10.1 Key Component Suppliers

#### QCL Systems
- **Block Engineering** (USA): LaserScan, LaserWarn
- **Daylight Solutions** (Leonardo DRS, USA): MIRcat-QT
- **Thorlabs** (USA): QCL development kits

#### MCT Detectors
- **Teledyne FLIR** (USA): Science-grade MCT FPAs
- **Lynred** (France): SPIDER MCT detectors
- **Leonardo** (UK): High-speed MCT arrays

#### Mass Spectrometry
- **Pacific Northwest National Laboratory (PNNL)**: AFT-MS technology transfer
- **908 Devices** (USA): MX908 portable mass spec
- **Smiths Detection** (UK): IONSCAN 600

#### Edge Computing
- **NVIDIA** (USA): Jetson AGX Thor, AGX Orin
- **Intel** (USA): NUC with Movidius acceleration
- **Google** (USA): Coral Edge TPU

---

**Document Version**: 1.0  
**Last Updated**: December 2025  
**Classification**: Unclassified - Technical Specifications
