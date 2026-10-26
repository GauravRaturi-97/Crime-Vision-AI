# Software Requirements Specification (SRS)

**Project Name:** CrimeVision AI — Intelligent Multimodal Forensic Analysis Platform  
**Program:** SmartBridge EL Capstone Project  
**Author / Lead AI Architect:** Gaurav Raturi  
**Version:** 2.0.0  
**Status:** Approved & Verified  

---

## 1. System Scope & Objectives

CrimeVision AI provides law enforcement, forensic investigators, and criminal prosecutors with an automated, multimodal platform to ingest, analyze, temporally synchronize, and spatially reconstruct multi-source digital evidence. The platform unifies Computer Vision (RT-DETR & BLIP), Speech & Acoustic Processing (OpenAI Whisper), GenAI Reasoning (Groq Llama-3.3 70B), and 3D WebGL Spatial Reconstruction (Three.js).

---

## 2. Functional Requirements (FR)

### FR-1: Multimodal Evidence Ingestion & Cryptographic Chain of Custody
- **FR-1.1:** The system shall accept drag-and-drop or programmatic uploads of crime scene images (`.jpg`, `.png`, `.webp`), audio recordings (`.wav`, `.mp3`, `.m4a`, `.flac`), surveillance video clips (`.mp4`, `.avi`, `.mov`), and textual field notes.
- **FR-1.2:** The system shall compute a 256-bit SHA-256 cryptographic hash immediately upon file intake before any processing.
- **FR-1.3:** The system shall maintain an immutable digital chain-of-custody register with file name, byte size, cryptographic checksum, and ingest timestamp.

### FR-2: Computer Vision & Weapon/Entity Detection (`image_engine.py`)
- **FR-2.1:** The system shall execute RT-DETR (`ultralytics rtdetr-l.pt`) with fallback to `yolov8n.pt` to detect persons, lethal weapons (knives, guns, rifles, firearms), and evidentiary items (backpacks, suitcases, cell phones, vehicles).
- **FR-2.2:** The system shall execute Salesforce BLIP (`Salesforce/blip-image-captioning-base`) for zero-shot natural language scene hypothesis generation.
- **FR-2.3:** The system shall compute image clarity via OpenCV Laplacian variance to evaluate motion blur and court admissibility.
- **FR-2.4:** The system shall generate base64-encoded annotated images with color-coded bounding boxes and forensic confidence badges (Red: Weapons, Cyan: Persons, Yellow: Artifacts, Orange: Vehicles).

### FR-3: Speech Transcription & Forensic Acoustic Extraction (`audio_engine.py`)
- **FR-3.1:** The system shall execute OpenAI Whisper (`base`/`small` model) with CPU/CUDA hardware adaptation and dynamic `ffmpeg` path binding for multilingual speech transcription.
- **FR-3.2:** The system shall segment audio feeds into timestamped transcript records with start/end intervals.
- **FR-3.3:** The system shall scan transcripts for high-urgency keywords (*gunshot, scream, help, ran away, red car, threat*) and query Groq LLM to output structured JSON events with timestamps, event types, excerpts, sentiments, and credibility tags.
- **FR-3.4:** The system shall calculate an Acoustic Distress Score from $0.0$ to $1.0$.

### FR-4: Surveillance Video Frame Sampling & Threat Spikes (`video_engine.py`)
- **FR-4.1:** The system shall ingest CCTV video feeds using OpenCV (`cv2.VideoCapture`) at a configurable sampling frequency (`sample_fps=2.0`).
- **FR-4.2:** The system shall compute inter-frame motion magnitude (`cv2.absdiff`) between consecutive grayscale frames to detect visual motion surges.
- **FR-4.3:** The system shall evaluate threat levels for each sampled temporal point:
  - `HIGH`: Triggered on sudden appearance of weapons or ballistic activity.
  - `MEDIUM`: Triggered on sudden clustering of multiple subjects or vehicle departures.
  - `LOW`: Routine baseline surveillance.
- **FR-4.4:** The system shall save annotated keyframe images for anomaly timestamps and compile an annotated highlights video clip (`highlights_<name>.mp4`).

### FR-5: Multimodal Alignment & Groq Forensic Intelligence (`fusion_engine.py`)
- **FR-5.1:** The system shall correlate acoustic events with video frame sequences within a $\pm 3.5\text{s}$ tolerance window (e.g., matching the sound of a gunshot or scream with visual weapon presence or motion bursts).
- **FR-5.2:** The system shall assemble a unified, gap-free Chronological Forensic Master Timeline sorted strictly by timestamp.
- **FR-5.3:** The system shall calculate an Evidence Confidence Score ($0.0\%\text{--}98.0\%$) based on cross-modal corroboration bonuses and sensor coverage.
- **FR-5.4:** The system shall query Groq LLM (`llama-3.3-70b-versatile` with candidate fallback chain) to generate a structured Case Brief containing:
  - `crime_classification`
  - `executive_summary`
  - `sequence_of_events`
  - `investigative_hypotheses` (exactly 3 distinct scenarios)
  - `potential_inconsistencies_or_doubts`

### FR-6: Interactive Spatial 3D Scene Reconstruction & Grounded Copilot Chatbot
- **FR-6.1:** The system shall project spatial 3D coordinates, suspect trajectory lines, and evidence markers (`EV-01`, `EV-02`, `EV-03`) into a Three.js WebGL canvas with preset camera angles (*Overview*, *Top-Down*, *Egress*, *Loading Bay*).
- **FR-6.2:** The system shall implement a grounded Investigator Copilot chatbot (`POST /api/chat`) that answers natural language inquiries strictly backed by evidence records, citing timestamps (`[00:15 / T+15.0s]`) and frame IDs.
- **FR-6.3:** The system shall export court-admissible forensic PDF reports (`GET /api/export-pdf`) via ReportLab, featuring case metadata, SHA-256 custody tables, master timelines, and supervisory certification sign-offs.

---

## 3. Non-Functional Requirements (NFR)

### NFR-1: Latency & Computational SLAs
- **Groq Inference Throughput:** Token generation speed shall exceed $250\text{ tokens/sec}$ with Time-to-First-Token (TTFT) $< 200\text{ms}$.
- **Video Processing Throughput:** Video frame sampling and detection shall achieve real-time throughput of $\ge 2.0\text{ frames/sec}$ on CPU and $\ge 15\text{ frames/sec}$ with CUDA acceleration.
- **PDF Compilation:** ReportLab dossier compilation shall complete in $< 1.5\text{s}$.

### NFR-2: Precision, Recall & Model Accuracy
- **RT-DETR Object Detection:** Mean Average Precision ($mAP_{50}$) for target forensic classes (`person`, `knife`, `weapon`, `car`) shall exceed $0.75$ on benchmark test sets.
- **Whisper Word Error Rate (WER):** Speech transcription WER shall remain below $12\%$ under ambient commercial and dispatch noise.

### NFR-3: Forensic Chain-of-Custody & Court Admissibility
- **Admissibility Standard:** The system shall comply with Federal Rules of Evidence (FRE) Rule 902(13) and Rule 902(14) regarding self-authenticating digital records generated by automated electronic processes.
- **Cryptographic Hashing:** Every ingested binary artifact shall have an unalterable SHA-256 fingerprint verified against subsequent transformations.
- **Non-Fabrication Assurance:** LLM system instructions shall explicitly forbid speculative fact fabrication; absent data must be flagged as *Indeterminate*.

### NFR-4: Modularity & Zero Circular Dependencies
- All core engine modules (`image_engine`, `audio_engine`, `video_engine`, `fusion_engine`, `app`) shall maintain a strict unidirectional import hierarchy.

---

## 4. Hardware & Software Requirements

### Software Environment:
- **Operating System:** Linux (Ubuntu 22.04 LTS / Debian 12 recommended) or macOS / Windows with WSL2.
- **Runtime:** Python 3.10 to 3.12.
- **Web Server Framework:** Flask 3.0+, Flask-CORS 4.0+.
- **Computer Vision Libraries:** OpenCV 4.9+ (`opencv-python-headless`), Pillow 10.0+, Ultralytics 8.4+ (RT-DETR).
- **Deep Learning Frameworks:** PyTorch 2.2+, Torchvision 0.17+, Hugging Face Transformers 4.44+.
- **Speech & Audio:** OpenAI Whisper (`base`/`small`), `imageio-ffmpeg` static binary distribution.
- **GenAI Reasoning SDK:** Groq SDK 0.9.0+, Google GenAI SDK 0.1.0+ (fallback).
- **Document Export Engine:** ReportLab 4.1+.
- **Frontend Presentation:** HTML5, CSS3, ES6 JavaScript, Three.js r128 (WebGL).

### Minimum Hardware Profile (CPU Execution):
- **Processor:** 4 Cores (Intel Core i5/i7 or AMD Ryzen 5, 2.4 GHz+).
- **RAM:** 8 GB Minimum (16 GB Recommended).
- **Storage:** 5 GB free disk space for model weights (`rtdetr-l.pt`, `yolov8n.pt`, `blip-base`, `whisper-base`).

### Recommended Hardware Profile (CUDA Accelerated):
- **Processor:** 8 Cores (Intel Xeon / Core i7 or AMD Ryzen 7).
- **RAM:** 32 GB.
- **GPU:** NVIDIA RTX 3060 / 4060 / A100 (minimum 8 GB VRAM, CUDA 12.1+).
