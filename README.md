# CrimeVision AI — Intelligent Multimodal Forensic Analysis Platform

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Python: 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Framework: Flask](https://img.shields.io/badge/Framework-Flask_3.0%2B-green.svg)](https://flask.palletsprojects.com/)
[![Computer Vision: RT--DETR](https://img.shields.io/badge/Computer_Vision-RT--DETR_rtdetr--l-orange.svg)](https://docs.ultralytics.com/models/rtdetr/)
[![Scene Captioning: BLIP](https://img.shields.io/badge/Scene_Captioning-Salesforce_BLIP-yellow.svg)](https://huggingface.co/Salesforce/blip-image-captioning-base)
[![Audio: OpenAI Whisper](https://img.shields.io/badge/Audio_Analysis-OpenAI_Whisper_base-brightgreen.svg)](https://github.com/openai/whisper)
[![GenAI: Groq LPU](https://img.shields.io/badge/GenAI_Inference-Groq_LPU_Llama--3.3-purple.svg)](https://groq.com/)
[![3D: Three.js WebGL](https://img.shields.io/badge/3D_Viewer-Three.js_WebGL-red.svg)](https://threejs.org/)
[![Chain of Custody: SHA--256](https://img.shields.io/badge/Chain_of_Custody-SHA--256_FRE_901-teal.svg)]()
[![Status: Production Ready](https://img.shields.io/badge/Status-Production_Ready_100%25_Pass-success.svg)]()

> **SmartBridge Experiential Learning Capstone Project**  
> **Author & Lead AI Architect:** Gaurav Raturi  
> **Repository:** `CrimeVision-AI`  
> **Deployment Target:** Law Enforcement & Digital Forensic Crime Laboratories  

---

## 1. Executive Summary & Problem Statement

Modern criminal investigations are inundated with heterogeneous, un-synchronized, and siloed digital evidence:
- High-definition crime scene still imagery.
- Multi-angle surveillance camera (CCTV) footage without audio.
- Low-fidelity 911 emergency dispatch calls and acoustic transients.
- Handwritten or interview-based witness testimony.

Human investigators face severe cognitive fatigue during multi-hour manual review, often leading to missed corroboration windows, contradictory witness statements going unnoticed, and evidence exclusion under strict judicial cross-examination.

**CrimeVision AI** addresses this paradigm by providing an end-to-end, privacy-compliant, multimodal forensic intelligence platform. By combining edge-optimized computer vision (RT-DETR), neural vision-language captioning (BLIP), robust speech-to-text audio triage (Whisper), Groq LPU sub-second tensor reasoning (Llama 3.3 70B), interactive WebGL 3D spatial scene reconstruction (Three.js), and automated court-admissible PDF dossier compilation (ReportLab), CrimeVision AI reduces forensic processing time from days to under 60 seconds while preserving an immutable cryptographic chain of custody.

---

## 2. System Architecture & Data Flow

```
                               CRIMEVISION AI PIPELINE FLOW
 ┌────────────────────────────────────────────────────────────────────────────────────────┐
 │                              MULTIMODAL EVIDENCE INTAKE                                │
 │  ┌──────────────────────┐  ┌──────────────────────┐  ┌──────────────────────────────┐  │
 │  │ Forensic Imagery     │  │ 911 Audio Dispatch   │  │ Surveillance CCTV Footage    │  │
 │  │ (.jpg, .png)         │  │ (.wav, .mp3)         │  │ (.mp4, .avi, 2 fps sample)   │  │
 │  └──────────┬───────────┘  └──────────┬───────────┘  └──────────────┬───────────────┘  │
 └─────────────┼─────────────────────────┼─────────────────────────────┼──────────────────┘
               │                         │                             │
               ▼                         ▼                             ▼
 ┌─────────────────────────┐  ┌─────────────────────────┐  ┌───────────────────────────┐
 │   IMAGE FORENSIC ENGINE │  │  AUDIO FORENSIC ENGINE  │  │   VIDEO FORENSIC ENGINE   │
 │  • RT-DETR Detection    │  │  • OpenAI Whisper Base  │  │  • Temporal Frame Sample  │
 │  • Salesforce BLIP      │  │  • Acoustic Key Events  │  │  • RT-DETR Multi-frame    │
 │  • Laplacian Clarity    │  │  • Groq Zero-Shot Triage│  │  • Threat Anomaly Spikes  │
 └─────────────┬───────────┘  └──────────┬──────────────┘  └───────────┬───────────────┘
               │                         │                             │
               └───────────────────┐     │     ┌───────────────────────┘
                                   ▼     ▼     ▼
                        ┌─────────────────────────────────────┐
                        │     MULTIMODAL FUSION ENGINE        │
                        │  • Temporal Sync (±3.5s Window)     │
                        │  • Evidence Confidence Score        │
                        │  • Discrepancy Matrix Analyzer      │
                        │  • Groq LPU Crime Classification    │
                        └──────────────────┬──────────────────┘
                                           │
         ┌─────────────────────────────────┴─────────────────────────────────┐
         ▼                                 ▼                                 ▼
┌───────────────────┐            ┌───────────────────┐            ┌────────────────────┐
│ WEB PRESENTATION  │            │ GROUNDED COPILOT  │            │ COURT-ADMISSIBLE   │
│ • 5-Tab Forensic  │            │ • Groq Llama-3.3  │            │   PDF EXPORT       │
│   Dashboard       │            │ • Anti-Hallucin.  │            │ • ReportLab Dossier│
│ • Three.js 3D Twin│            │   Strict Citation │            │ • SHA-256 Ledger   │
│ • Suspect Spline  │            │ • Real-time Stream│            │ • Sign-off Blocks  │
└───────────────────┘            └───────────────────┘            └────────────────────┘
```

---

## 3. Repository Directory Structure

The repository is structured to strictly adhere to the SmartBridge Experiential Learning 8-phase milestone standards:

```text
CrimeVision-AI/
├── 1. Brainstorming & Ideation/
│   └── project_proposal.md             # Project proposal, societal impact, cost/performance analysis (Groq LPU vs GPU)
├── 2. Requirement Analysis/
│   └── requirements_spec.md            # Software Requirements Specification (FR1-FR6, NFRs, Hardware/Software specs)
├── 3. Project Design Phase/
│   ├── system_architecture.md          # Architectural diagrams, component matrix, 3D Cartesian coordinates
│   └── ui_ux_design_and_3d_specs.md    # UI/UX theme specifications, Three.js lighting & camera presets
├── 4. Project Planning Phase/
│   ├── milestone_schedule.md           # Epics 1 to 6 sprint roadmap, task breakdown & completion metrics
│   └── project_management_plan.md      # Work Breakdown Structure (WBS), risk management matrix
├── 5. Project Development Phase/       # Primary Production Codebase
│   ├── image_engine.py                 # RT-DETR weapon/person detection + BLIP scene captioning + Laplacian blur
│   ├── audio_engine.py                 # OpenAI Whisper speech-to-text + Groq zero-shot acoustic triage
│   ├── video_engine.py                 # OpenCV 2 fps frame sampling + entity detection + threat timeline
│   ├── fusion_engine.py                # Multimodal temporal alignment, Groq case brief, PDF dossier compiler
│   ├── app.py                          # Flask REST API server, CORS routing & endpoints
│   ├── requirements.txt                # Python environment dependencies
│   ├── .env.example                    # Environment variable configuration template
│   ├── uploads/                        # Ingestion evidence locker (.gitkeep)
│   ├── outputs/                        # Processed keyframes, annotated images & PDF exports (.gitkeep)
│   ├── templates/
│   │   └── index.html                  # 5-Tab Forensic Investigative Console with Three.js canvas
│   └── static/
│       ├── css/style.css               # Law-enforcement dark-slate/crimson styling
│       └── js/
│           ├── app.js                  # Frontend REST API client, tab routing & event handlers
│           └── crime_scene_3d.js       # Three.js 3D spatial reconstruction & suspect trajectory spline
├── 6. Project Testing/
│   ├── test_image_engine.py            # Unit tests for RT-DETR, BLIP, Laplacian clarity, SHA-256
│   ├── test_audio_engine.py            # Unit tests for Whisper transcription & acoustic key events
│   ├── test_fusion_engine.py           # Unit tests for temporal fusion, confidence score, discrepancy matrix
│   ├── test_api.py                     # Integration tests for Flask REST endpoints (/api/*)
│   ├── test_suite.py                   # Comprehensive 10-point end-to-end integration test runner
│   ├── run_tests.sh                    # Automated bash test execution script (chmod +x)
│   └── test_results.md                 # Test execution logs and benchmark matrix
├── 7. Project Documentation/
│   ├── user_guide.md                   # Operational manual for investigators & detectives (5-tab workflow)
│   ├── api_documentation.md            # OpenAPI 3.0 REST API specification & curl examples
│   ├── api_reference.md                # Quick-reference endpoint handbook
│   └── chain_of_custody_standard.md   # Federal Rules of Evidence Rule 901 compliance manual
├── 8. Project Demonstration/
│   ├── demo_script.md                  # 5-minute step-by-step oral presentation walkthrough for assessors
│   ├── demonstration_script.md         # Evaluator demonstration sequence
│   └── mock_case_study.md              # Scenario dataset (Metro Transit Armed Robbery CV-2026-0891)
├── .gitignore                          # Repository credential safeguards & ignore rules
└── README.md                           # Master Project Documentation (This File)
```

---

## 4. Key Features & Forensic Modules

### 4.1. Image Forensic Engine (`image_engine.py`)
- **RT-DETR Transformer Detection:** Uses `rtdetr-l.pt` (with automated fallback to `yolov8n.pt`) to detect weapons (firearms, knives), subjects, and tactical items with bounding boxes and confidence metrics.
- **Visual Hypotheses via BLIP:** Leverages `Salesforce/blip-image-captioning-base` to generate natural-language scene descriptions and hypotheses.
- **Laplacian Blur Variance:** Quantifies image clarity to reject substandard evidence before judicial review.
- **Cryptographic Hashing:** Computes SHA-256 digests immediately on raw binary inputs.

### 4.2. Audio Forensic Engine (`audio_engine.py`)
- **OpenAI Whisper Speech-to-Text:** Transcribes 911 dispatch and surveillance audio into timestamped segments.
- **Dynamic FFmpeg Resolution:** Automatically resolves `imageio-ffmpeg` runtime binary and PATH variables.
- **Groq LPU Acoustic Triage:** Scans audio transcripts for high-urgency keywords (*"gunshot"*, *"knife"*, *"scream"*, *"threat"*) and extracts structured forensic key events with speaker distress categorization.

### 4.3. Video Forensic Engine (`video_engine.py`)
- **Uniform Frame Sampling:** Extracts frames at a configurable sample rate (default: 2 fps) to balance computational latency and temporal coverage.
- **Per-Frame Entity Tracking:** Runs RT-DETR on every extracted frame, recording entity presences and flagging threat surges.
- **Keyframe Evidence Isolation:** Automatically exports keyframe stills for timestamps exhibiting critical threat levels.

### 4.4. Multimodal Fusion Engine (`fusion_engine.py`)
- **Temporal Alignment ($\pm 3.5\text{s}$):** Corroborates auditory distress calls with visual weapon detections within temporal boundaries.
- **Evidence Confidence Score:** Computes a normalized confidence index ($0.0 - 1.0$) reflecting cross-modal corroboration.
- **Witness Discrepancy Matrix:** Automatically identifies and highlights contradictions between human witness statements and physical sensor data (e.g. footwear color, weapon type).
- **Court Dossier Generation (ReportLab):** Compiles multi-page PDF reports containing the executive summary, timeline, discrepancies, SHA-256 ledger, and supervisor attestation blocks.

### 4.5. Interactive 3D Spatial Crime Scene (`crime_scene_3d.js`)
- **Three.js WebGL Engine:** Renders an interactive 3D digital twin of the crime scene with orbit controls and tactical camera presets.
- **Spatial Markers:** Pinned coordinates for Entry/Exit points (`EV-01`), acoustic origins (`EV-02`), and physical weapon recovery loci (`EV-03`).
- **Suspect Trajectory Spline:** Renders a 3D spline showing the suspect's escape vector with an animated pulse particle.

### 4.6. Grounded Investigator Copilot (`POST /api/chat`)
- **Groq LPU Acceleration:** Powered by open-weight models (`llama-3.3-70b-versatile`, `DeepSeek`, `Mixtral`) delivering $<800\text{ms}$ query latency.
- **Anti-Hallucination Guardrails:** Constrained to cite only established facts from the fusion graph; explicitly flags uncorroborated assertions.

---

## 5. Technology Stack & Dependencies

| Category | Technology | Version | Purpose |
|---|---|---|---|
| **Web Server** | Flask & Flask-CORS | `^3.0.0` | High-throughput asynchronous REST API routing |
| **Object Detection** | Ultralytics RT-DETR | `^8.1.0` | Real-time transformer-based object/weapon detection |
| **Scene Captioning** | Hugging Face Transformers | `^4.38.0` | BLIP neural scene captioning and hypothesis generation |
| **Speech-to-Text** | OpenAI Whisper | `^20231117` | Multilingual acoustic transcription & timestamp segmentation |
| **Audio Processing** | imageio-ffmpeg & soundfile | `^0.4.9` | Headless dynamic audio decoding |
| **Vision Utilities** | OpenCV Headless & Pillow | `^4.9.0` | Laplacian blur detection, frame difference & bounding box rendering |
| **LPU GenAI** | Groq Python SDK | `^0.9.0` | Ultra-low latency forensic reasoning & Copilot Q&A |
| **PDF Generation** | ReportLab | `^4.1.0` | Standards-compliant court-admissible forensic PDF dossier export |
| **3D Rendering** | Three.js & OrbitControls | `r128` | Client-side WebGL interactive crime scene spatial reconstruction |

---

## 6. Installation & Setup Guide

### 6.1. Prerequisites
- Linux / macOS / Windows WSL2
- Python 3.10, 3.11, or 3.12
- Node.js / Modern Web Browser (Chrome, Firefox, Safari, Edge)

### 6.2. Step 1: Clone Repository
```bash
git clone https://github.com/GauravRaturi/CrimeVision-AI.git
cd CrimeVision-AI
```

### 6.3. Step 2: Virtual Environment Setup
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip setuptools wheel
pip install -r "5. Project Development Phase/requirements.txt"
```

### 6.4. Step 3: Environment Configuration
Create the `.env` file inside `5. Project Development Phase/`:
```bash
cp "5. Project Development Phase/.env.example" "5. Project Development Phase/.env"
```
Populate your configuration values in `5. Project Development Phase/.env`:
```ini
GROQ_API_KEY=gsk_your_groq_api_key_here
FLASK_SECRET_KEY=crimevision_forensic_secure_token_2026_xyz
UPLOAD_FOLDER=uploads
EVIDENCE_OUTPUT_FOLDER=outputs
DEVICE=cpu  # 'cuda' or 'cpu'
PORT=5000
```

### 6.5. Step 4: Launch the Forensic Application
```bash
cd "5. Project Development Phase"
python app.py
```
Open your browser and navigate to:
```
http://127.0.0.1:5000
```

---

## 7. Verification & Automated Test Suite

CrimeVision AI includes a comprehensive automated test suite with unit tests, component tests, and full REST integration tests.

### 7.1. Run Full Automated Test Suite
From the repository root:
```bash
bash "6. Project Testing/run_tests.sh"
```

### 7.2. Run Individual Test Modules
```bash
# Test 1: Image Forensic Engine (RT-DETR, BLIP, Clarity, Hashing)
python "6. Project Testing/test_image_engine.py"

# Test 2: Audio Forensic Engine (Whisper Speech-to-Text, Acoustic Events)
python "6. Project Testing/test_audio_engine.py"

# Test 3: Multimodal Fusion Engine (Temporal Sync, Confidence Score, PDF)
python "6. Project Testing/test_fusion_engine.py"

# Test 4: Flask REST API Endpoints (/api/health, /api/analyze/*, /api/chat)
python "6. Project Testing/test_api.py"

# Test 5: End-to-End Orchestrated Pipeline
python "6. Project Testing/test_suite.py"
```

---

## 8. Assessor Demonstration Guide

For evaluators conducting an academic or technical project assessment, follow the instructions in [`8. Project Demonstration/demo_script.md`](file:///home/gaurav/CrimeVIsion-AI/8.%20Project%20Demonstration/demo_script.md):

| Timeline | Stage | Key Interaction |
|---|---|---|
| **Minute 0–1** | Ingestion & Integrity | Upload imagery & dispatch audio; inspect instant SHA-256 calculation |
| **Minute 1–2** | Master Timeline | Inspect synchronized cross-modal timeline & automated discrepancy matrix |
| **Minute 2–3** | 3D Crime Scene | Orbit the Three.js 3D terminal grid; trigger `EV-01` camera preset & inspect flight spline |
| **Minute 3–4** | Investigator Copilot | Ask: *"Did the suspect possess a firearm?"*; inspect sub-second Groq response & citations |
| **Minute 4–5** | Court-Ready PDF | Click **"Export Court-Ready PDF Dossier"**; inspect the 3-page signed dossier |

---

## 9. Legal Compliance & Chain of Custody Standard

CrimeVision AI operates under strict evidentiary protocols:
1. **Federal Rules of Evidence (FRE) Rule 901:** Strict authentication and identification of evidence items through SHA-256 cryptographic digests computed prior to ingestion.
2. **Deterministic Fallbacks:** Fallback models engage automatically to prevent data loss or server timeouts during field operations.
3. **Immutable Raw Data:** Original evidence media files are marked read-only and strictly isolated from annotated output files.
4. **Audit Trail:** Every transformation, AI confidence score, and timestamp is logged into the output report.

---

## 10. Author & Project Metadata

- **Author / Lead AI Architect:** Gaurav Raturi  
- **Capstone Program:** SmartBridge Experiential Learning Capstone Project  
- **Project Topic:** Intelligent Multimodal Forensic Analysis Platform  
- **Submission Date:** October 2026  
- **Primary Code Directory:** `5. Project Development Phase/`  
- **License:** Apache License 2.0  
