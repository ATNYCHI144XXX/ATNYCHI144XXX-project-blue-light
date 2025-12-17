# Bill of Materials (BOM)

**PROJECT BLUE-LIGHT** - High-Speed Standoff Fentanyl Interdiction System

**Document Version**: 1.0  
**Last Updated**: December 2025

---

## Overview

This document lists all major components required to construct a single PROJECT BLUE-LIGHT sensor unit. Costs are estimates based on 2025 commercial/research pricing for low-volume procurement (1-10 units). Significant cost reductions (30-50%) are expected for production volumes of 100+ units.

---

## 1. Optical/Spectroscopy Components

### 1.1 Quantum Cascade Laser (QCL) System

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **QCL Module** | Tunable QCL, 5-7 µm range | Block Engineering | LaserScan-1 | 2 | $18,000 | $36,000 |
| **QCL Module** | Tunable QCL, 7-10 µm range | Block Engineering | LaserScan-2 | 1 | $18,000 | $18,000 |
| **QCL Module** | Tunable QCL, 10-12 µm range | Block Engineering | LaserScan-3 | 1 | $18,000 | $18,000 |
| **QCL Controller** | 4-channel laser control unit | Block Engineering | LC-4000 | 1 | $8,000 | $8,000 |
| **TEC Cooler** | Thermoelectric cooler for QCL | TE Technology | HP-127 | 4 | $450 | $1,800 |
| **Beam Combiner** | Dichroic beam combiner optics | Thorlabs | Custom | 1 | $3,500 | $3,500 |

**Subtotal**: $85,300

### 1.2 MCT Detector System

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **MCT FPA** | 256×256 MCT detector array | Teledyne FLIR | SC8200 | 1 | $45,000 | $45,000 |
| **TEC Controller** | Temperature controller for MCT | Lakeshore | 336 | 1 | $3,200 | $3,200 |
| **Camera Interface** | Camera Link frame grabber | EPIX | PIXCI EB1 | 1 | $2,500 | $2,500 |
| **Optics Assembly** | 50mm f/2 IR lens + mounts | Custom/Janos | IR-50F2 | 1 | $6,500 | $6,500 |

**Subtotal**: $57,200

### 1.3 Terahertz (THz) System (Optional - Phase 2)

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **THz Source** | 0.1-3 THz emitter | TeraView | TPS 3000 | 1 | $35,000 | $35,000 |
| **THz Detector** | Pyroelectric detector array | Gentec-EO | THZ-I-BNC | 1 | $8,000 | $8,000 |

**Subtotal (Optional)**: $43,000

---

## 2. Mass Spectrometry Components

### 2.1 AFT-MS Unit

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **AFT-MS Core** | Atmospheric flow tube MS | PNNL/Custom | AFT-TOF-100 | 1 | $65,000 | $65,000 |
| **Vacuum Pump** | Turbomolecular pump | Pfeiffer | HiPace 80 | 1 | $6,500 | $6,500 |
| **Backing Pump** | Rotary vane pump | Edwards | E2M2 | 1 | $2,200 | $2,200 |
| **Air Inlet System** | High-speed air scoop + heating | Custom Fab | AS-120 | 1 | $4,500 | $4,500 |
| **Gas Manifold** | Reagent gas control system | Swagelok | Custom | 1 | $3,000 | $3,000 |
| **Ionization Source** | RF discharge ion source | Custom | RF-ION-1 | 1 | $5,500 | $5,500 |

**Subtotal**: $86,700

---

## 3. Imaging Components

### 3.1 Thermal Camera

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **LWIR Camera** | 640×480 uncooled microbolometer | FLIR | Boson 640 | 1 | $8,500 | $8,500 |
| **Lens** | 19mm f/1.0 LWIR lens | FLIR | T197415 | 1 | $2,800 | $2,800 |

**Subtotal**: $11,300

### 3.2 Optical Camera

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **4K Camera** | 4K @ 30fps with HDR | Basler | ace 2 Pro | 1 | $1,200 | $1,200 |
| **Lens** | 50mm f/1.4 C-mount | Computar | M5018-MP2 | 1 | $450 | $450 |
| **License Plate Module** | LPR-optimized optics/software | OpenALPR | Custom | 1 | $800 | $800 |

**Subtotal**: $2,450

---

## 4. Computing & Processing

### 4.1 Edge Computing Platform

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **Edge Computer** | NVIDIA Jetson AGX Thor | NVIDIA | 945-13912 | 1 | $3,500 | $3,500 |
| **SSD Storage** | 512GB NVMe M.2 SSD | Samsung | 980 PRO | 1 | $180 | $180 |
| **RAM Expansion** | 64GB LPDDR5 (if not included) | — | — | 1 | $400 | $400 |
| **Carrier Board** | Custom I/O carrier board | Connect Tech | Custom | 1 | $650 | $650 |

**Subtotal**: $4,730

### 4.2 Data Acquisition Hardware

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **DAQ Card** | Multi-channel data acquisition | National Instruments | USB-6343 | 1 | $2,800 | $2,800 |
| **Serial Interface** | 8-port USB-serial adapter | FTDI | FT4222H | 1 | $120 | $120 |

**Subtotal**: $2,920

---

## 5. Power & Cooling

### 5.1 Power System

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **Power Supply** | 500W 80+ Gold PSU, 120/240VAC | Mean Well | RSP-500-48 | 2 | $180 | $360 |
| **Power Distribution** | DC-DC converters, filtering | Custom PCB | PDB-001 | 1 | $450 | $450 |
| **UPS Battery** | 12V 9Ah backup battery | Yuasa | NP9-12 | 2 | $35 | $70 |
| **Battery Management** | UPS controller | APC | Custom | 1 | $220 | $220 |

**Subtotal**: $1,100

### 5.2 Thermal Management

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **Fans** | 120mm high-airflow fan | Noctua | NF-A12x25 | 4 | $35 | $140 |
| **Heat Exchangers** | Aluminum heat sink | Wakefield-Vette | Custom | 2 | $85 | $170 |
| **Thermal Paste** | High-performance TIM | Arctic Silver | AS5 | 1 | $12 | $12 |

**Subtotal**: $322

---

## 6. Enclosure & Mounting

### 6.1 Environmental Enclosure

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **Housing** | IP67 aluminum enclosure | Bud Industries | Custom | 1 | $2,500 | $2,500 |
| **Optical Window** | Sapphire AR-coated window | Edmund Optics | Custom | 1 | $1,800 | $1,800 |
| **Gaskets & Seals** | EPDM environmental seals | Parker | Custom Kit | 1 | $180 | $180 |
| **Cable Glands** | IP67 cable entry connectors | Lapp | SKINTOP | 8 | $25 | $200 |

**Subtotal**: $4,680

### 6.2 Mounting Hardware

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **Gantry Mount** | Universal gantry bracket | Custom Fab | GM-001 | 1 | $850 | $850 |
| **Vibration Isolators** | Anti-vibration mounts | Lord Corp | J-6000 | 4 | $45 | $180 |
| **Fasteners** | Stainless steel hardware kit | McMaster | Custom | 1 | $120 | $120 |

**Subtotal**: $1,150

---

## 7. Communications & Networking

### 7.1 Network Interface

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **Fiber Optic Module** | 1Gbps SFP transceiver | Finisar | FTLF1318P3BTL | 2 | $180 | $360 |
| **Fiber Patch Cable** | Single-mode fiber, 100m | Corning | Custom | 1 | $250 | $250 |
| **5G Modem** | Industrial 5G cellular modem | Sierra Wireless | EM9191 | 1 | $450 | $450 |
| **Antenna** | 5G MIMO antenna | Taoglas | TG.45.8113 | 2 | $75 | $150 |
| **Network Switch** | Managed Ethernet switch | Cisco | IE-3300-8T2S | 1 | $1,200 | $1,200 |

**Subtotal**: $2,410

### 7.2 Security Module

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **HSM** | Hardware Security Module | Yubico | YubiHSM 2 | 1 | $650 | $650 |
| **TPM** | Trusted Platform Module | Infineon | OPTIGA TPM 2.0 | 1 | $25 | $25 |

**Subtotal**: $675

---

## 8. Sensors & Monitoring

### 8.1 Environmental Sensors

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **GPS Module** | High-precision GNSS | u-blox | NEO-M9N | 1 | $85 | $85 |
| **Temperature Sensors** | Thermocouple array | Omega | Type-K TC | 8 | $15 | $120 |
| **Humidity Sensor** | RH/Temp sensor | Sensirion | SHT85 | 2 | $22 | $44 |
| **Accelerometer** | 3-axis vibration sensor | Analog Devices | ADXL355 | 1 | $35 | $35 |
| **Pressure Sensor** | Barometric pressure | Bosch | BMP390 | 1 | $18 | $18 |

**Subtotal**: $302

---

## 9. Cabling & Interconnects

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **Power Cables** | Industrial AC power cables | Custom | Various | 1 | $180 | $180 |
| **Signal Cables** | Shielded data cables | Belden | Various | 1 | $320 | $320 |
| **Fiber Cables** | Internal fiber patch cords | Corning | Various | 1 | $150 | $150 |
| **Connectors** | Military-spec connectors | Amphenol | Various | 1 | $280 | $280 |

**Subtotal**: $930

---

## 10. Software & Licensing

| Item | Description | Vendor | License Type | Qty | Unit Cost | Total |
|------|-------------|--------|--------------|-----|-----------|-------|
| **OS License** | Ubuntu Pro (LTS support) | Canonical | Annual | 1 | $500 | $500 |
| **AI Framework** | NVIDIA TensorRT license | NVIDIA | Included | — | $0 | $0 |
| **Spectral Library** | NIST Chemistry WebBook | NIST | Public Domain | — | $0 | $0 |
| **Development Tools** | IDEs, debugging tools | Various | Open Source | — | $0 | $0 |

**Subtotal**: $500

---

## 11. Calibration & Test Equipment

| Item | Description | Manufacturer | Part Number | Qty | Unit Cost | Total |
|------|-------------|--------------|-------------|-----|-----------|-------|
| **Reference Standards** | Fentanyl spectral standards | Sigma-Aldrich | Custom | 1 | $2,500 | $2,500 |
| **Calibration Targets** | IR calibration sources | Optronics | OR-20 | 1 | $1,800 | $1,800 |
| **Test Gases** | Certified gas mixtures | Airgas | Custom | 1 | $450 | $450 |

**Subtotal**: $4,750

---

## Cost Summary

### Per-Unit Costs (Single Unit Production)

| Category | Subtotal |
|----------|----------|
| **1. Optical/Spectroscopy** | $85,300 |
| **2. Mass Spectrometry** | $86,700 |
| **3. Imaging** | $13,750 |
| **4. Computing** | $7,650 |
| **5. Power & Cooling** | $1,422 |
| **6. Enclosure & Mounting** | $5,830 |
| **7. Communications** | $3,085 |
| **8. Sensors** | $302 |
| **9. Cabling** | $930 |
| **10. Software** | $500 |
| **11. Calibration** | $4,750 |
| | |
| **Hardware Subtotal** | **$210,219** |
| **Integration Labor (150hrs @ $150/hr)** | **$22,500** |
| **Testing & Validation (80hrs @ $150/hr)** | **$12,000** |
| **Documentation & Training** | **$5,000** |
| | |
| **TOTAL PER UNIT (Prototype)** | **$249,719** |

### Economies of Scale (Production Volume Estimates)

| Volume | Estimated Unit Cost | Total Program Cost |
|--------|---------------------|---------------------|
| **1 unit (Prototype)** | $250,000 | $250,000 |
| **10 units (Pilot)** | $180,000 | $1,800,000 |
| **50 units (Regional)** | $140,000 | $7,000,000 |
| **100 units** | $120,000 | $12,000,000 |
| **500 units (National)** | $95,000 | $47,500,000 |

**Cost Reduction Factors**:
- Volume discounts on components (30-40%)
- Reduced integration labor per unit (economies of learning)
- Optimized supply chain and component substitution
- Custom ASIC development for sensor processing (Phase 3)

---

## Installation Costs (Per Site)

| Item | Description | Cost |
|------|-------------|------|
| **Gantry Access** | Crane/bucket truck rental | $2,500 |
| **Electrical Work** | Power connection to gantry | $3,500 |
| **Fiber Installation** | Fiber optic cable run to command center | $8,000 |
| **Site Survey** | RF/network site analysis | $1,500 |
| **Commissioning** | On-site testing and calibration | $4,000 |
| **Training** | Operator training (3 days) | $5,000 |
| | |
| **Total Installation Cost** | **$24,500** |

**Complete Site Cost** = Unit Cost + Installation Cost

Example (10-unit pilot): $180,000 + $24,500 = **$204,500 per site**

---

## Maintenance & Operating Costs

### Annual Per-Unit Costs

| Item | Description | Annual Cost |
|------|-------------|-------------|
| **Calibration Standards** | Replacement reference materials | $1,500 |
| **Consumables** | Reagent gases, filters, etc. | $800 |
| **Software Updates** | OS and AI model updates | $500 |
| **Preventive Maintenance** | Quarterly service visits | $4,000 |
| **Component Replacement** | 5% failure rate (warranty excludes) | $3,000 |
| **Network Fees** | Cellular data (backup) | $600 |
| **Electricity** | 300W × 24hr × 365d × $0.12/kWh | $315 |
| | |
| **Total Annual Operating Cost** | **$10,715** |

**5-Year Total Cost of Ownership** = Unit Cost + Installation + (5 × Operating Cost)

Example (production unit): $95,000 + $24,500 + $53,575 = **$173,075**

---

## Optional Enhancements

### Advanced Capabilities (Future Phases)

| Enhancement | Description | Additional Cost |
|-------------|-------------|-----------------|
| **Terahertz Imaging** | Add THz subsystem | +$43,000 |
| **Long-Range Mode** | Extended detection range optics | +$12,000 |
| **Multi-Substance Library** | Expanded chemical database | +$5,000 |
| **Weather Station** | Integrated meteorological sensors | +$2,500 |
| **Solar Power Option** | Off-grid solar+battery system | +$18,000 |

---

## Supplier Contact Information

### Primary Vendors

- **Block Engineering** (USA): +1-508-946-4200, sales@blockeng.com
- **Teledyne FLIR** (USA): +1-866-477-3687, sales@flir.com
- **PNNL Technology Transfer**: +1-509-375-2789, commercialization@pnnl.gov
- **NVIDIA**: nvidia.com/jetson (distributor network)
- **Thorlabs** (USA): +1-973-300-3000, sales@thorlabs.com

### Integration Partners

Recommended system integrators with experience in defense/spectroscopy systems:
- Leidos (USA)
- Smiths Detection (UK/USA)
- L3Harris Technologies (USA)
- Battelle Memorial Institute (USA)

---

## Notes

1. **Prices are estimates** based on 2025 commercial pricing and are subject to change.
2. **Volume discounts** available for orders of 10+ units.
3. **Export restrictions** may apply to QCL and MCT components (ITAR/EAR).
4. **Custom components** (air inlet, mounting) require engineering design phase.
5. **Lead times**: 3-6 months for specialized components (QCL, MCT, AFT-MS).
6. **Warranty**: Typically 1-2 years on major components.
7. **Training**: Operator training recommended (included in installation cost).

---

**Document Prepared By**: PROJECT BLUE-LIGHT Engineering Team  
**Review Date**: December 2025  
**Next Review**: Quarterly or upon significant component changes  
**Classification**: Unclassified - Procurement Sensitive
