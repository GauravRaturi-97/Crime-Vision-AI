# CrimeVision AI — Forensic User & Operating Manual

**Author:** Gaurav Raturi | SmartBridge EL Capstone Project  
**Target Audience:** Law Enforcement Detectives, Digital Forensics Analysts, Forensic Lab Examiners  
**Version:** 2.0.0  

---

## 1. Quickstart Guide

### Starting the Platform
```bash
# 1. Activate project virtual environment
cd "/home/gaurav/CrimeVIsion-AI"
source .venv/bin/activate

# 2. Launch Flask Forensic Application
cd "5. Project Development Phase"
python app.py
```
Open your browser to: **`http://localhost:5000`**

---

## 2. Step-by-Step Investigative Workflow

### Step 1: Ingesting Case Evidence (Digital Evidence Locker)
1. In the left sidebar under **Digital Evidence Locker**, specify the **Case File Number** (e.g. `CV-2026-0891`) and **Incident Location**.
2. Upload crime scene photography into the **Crime Scene Images** dropzone.
3. Upload 911 call audio or radio dispatch into the **Audio Transmissions** dropzone.
4. Upload surveillance video clips into the **Surveillance Video** dropzone.
5. Paste officer field notes or witness interview statements into the **Witness Statements** text area.
6. Click **"Ingest & Compute SHA-256 Hashes"**. The cryptographic hashes will immediately appear in the **Cryptographic Custody Register**.

### Step 2: Exploring the 3D Crime Scene (Three.js WebGL)
1. In the central 3D viewport, use your mouse to navigate the reconstructed transit facility:
   - **Left Click + Drag:** Rotate scene perspective.
   - **Right Click + Drag:** Pan spatial scene.
   - **Scroll Wheel:** Zoom in/out.
2. Click on preset buttons (**Overview**, **Top-Down**, **Stairwell Egress**, **Loading Bay**) for rapid camera alignment.
3. Click directly on 3D Evidence Pins (**EV-01**, **EV-02**, **EV-03**) to view localized evidence descriptions and timestamps.
4. Observe the animated glowing amber trajectory path illustrating the suspect's flight vector.

### Step 3: Executing Multimodal Forensic Fusion
1. Click the green button: **"Execute Multimodal Forensic Fusion"**.
2. The platform coordinates:
   - `image_engine`: Localizes subjects and weapons using RT-DETR; generates BLIP visual hypotheses.
   - `audio_engine`: Transcribes dispatch audio via OpenAI Whisper and extracts acoustic peaks.
   - `video_engine`: Measures inter-frame motion surges via OpenCV.
   - `fusion_engine`: Groq LLM synthesizes all streams into an authoritative report.
3. View the updated **Crime Classification**, **Severity Rating**, **RT-DETR Detection Gallery**, and **Unified Chronological Master Timeline**.

### Step 4: Interrogating the Evidence (Investigator Copilot)
1. Scroll down to the **Investigator Forensic Copilot** section.
2. Click any suggested query chip (e.g. *Weapons Identified?*, *Contradictions?*, *Getaway Vehicle?*) or enter a custom investigative query.
3. Receive instantaneous, citation-backed answers grounded directly in the ingested case files.

### Step 5: Exporting Court-Admissible Dossier
1. In the left sidebar, click **"Export Court-Admissible Dossier (PDF)"**.
2. The ReportLab engine compiles the case metadata, SHA-256 custody register, master timeline, and attestation sign-off blocks into a standardized PDF report ready for disclosure.
