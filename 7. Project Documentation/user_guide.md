# CrimeVision AI — Investigator User Guide

**Platform:** CrimeVision AI — Intelligent Multimodal Forensic Analysis Platform  
**Author / Lead AI Architect:** Gaurav Raturi | SmartBridge EL Capstone Project  
**Target Audience:** Law Enforcement Detectives, Digital Forensic Analysts, Crime Scene Investigators, Legal Prosecutors  
**Version:** 2.0.0  

---

## 1. Introduction & Mission Overview

**CrimeVision AI** is an advanced multimodal forensic intelligence platform engineered to eliminate information silos across heterogeneous crime scene evidence. By synchronizing Computer Vision (**RT-DETR & BLIP**), Acoustic Analysis (**OpenAI Whisper**), Video Motion Tracking (**OpenCV**), and GenAI Cross-Modal Reasoning (**Groq LPU Llama-3.3 70B**), the platform empowers investigators to:
1. Reconstruct gap-free chronological timelines in seconds.
2. Cross-corroborate witness claims against physical digital media.
3. Interrogate evidence in natural language with strict timestamp and frame citations.
4. Explore 3D spatial reconstructions in an interactive WebGL crime room.
5. Compile court-admissible, cryptographically verified PDF forensic reports.

---

## 2. Navigating the 5-Tab Investigative Console

Access the live dashboard at `http://127.0.0.1:5000` via any modern web browser.

```
+----------------------------------------------------------------------------------------------------+
| [Tab 1: Evidence Ingestion] [Tab 2: Master Timeline] [Tab 3: 3D Scene] [Tab 4: Copilot] [Tab 5: PDF] |
+----------------------------------------------------------------------------------------------------+
```

### Tab 1: Evidence Ingestion
- **Case Information Input:** Fill in the *Case Identifier* (e.g., `CV-2026-0891`) and *Incident Location*.
- **Drag-and-Drop Dropzones:**
  - **Crime Scene Stills:** Upload `.jpg`, `.png`, or `.webp` files. Click **Run Image Forensic Engine** to preview RT-DETR localized weapons/persons and BLIP visual captions.
  - **911 & Dispatch Audio:** Upload `.wav` or `.mp3` recordings. Click **Run Audio Forensic Engine** to transcribe speech and extract acoustic concussive peaks.
  - **CCTV Surveillance Video:** Upload `.mp4` or `.avi` clips. Click **Run Video Forensic Engine** to inspect frame sampling (`sample_fps=2`), motion surges, and threat level classifications.
  - **Witness Statements:** Paste officer field notes, guard logs, or recorded 911 statements.
- **Master Fusion Trigger:** Click **Execute Multimodal Forensic Fusion** to synthesize all loaded streams into a unified master timeline and Groq case brief.

---

### Tab 2: Multimodal Master Timeline
- **Chronological Flow:** View all cross-verified incident events organized strictly by timestamp.
- **Threat Badges:**
  - <span style="color:#ef4444; font-weight:bold;">HIGH</span>: Weapons localized, gunshots reported, or vehicle escape in progress.
  - <span style="color:#f59e0b; font-weight:bold;">MEDIUM</span>: Multiple subjects clustering or elevated acoustic pitch.
  - <span style="color:#10b981; font-weight:bold;">LOW</span>: Baseline routine sector surveillance.
- **Corroboration Annotations:** Review system notes indicating cross-modal corroboration (e.g., *Acoustic event at T+15.0s corroborated by visual CCTV motion at T+15.0s*).
- **Interactive Filtering:** Use the threat level filter buttons (`All`, `High`, `Medium`, `Low`) to isolate critical moments.

---

### Tab 3: Interactive 3D Crime Scene Reconstruction
- **WebGL Wireframe Room:** Powered by Three.js, this viewport places all evidence within a calibrated 3D Cartesian coordinate space ($X, Y, Z$).
- **Camera Presets:**
  - **Overview:** Default angled 3D vantage point (`x=16, y=14, z=18`).
  - **Top-Down:** Direct bird's-eye orthographic view (`x=0, y=28, z=0.1`).
  - **Stairwell Egress (EV-01):** Close-up focus on the North stairwell egress point.
  - **Loading Bay (EV-03):** Focus on the vehicle staging and getaway bay.
- **Evidence Markers:**
  - `EV-01` (Cyan): North stairwell egress coordinate.
  - `EV-02` (Crimson): Ballistic / acoustic transient origin coordinate.
  - `EV-03` (Amber): Loading bay transport location.
- **Click-to-Inspect:** Click any 3D marker to inspect its spatial coordinates, registered modality, and forensic description in the inspector panel below the canvas.
- **Trajectory Pulse:** Observe the dynamic animated spline showing the suspect's movement trajectory from ingress to extraction.

---

### Tab 4: AI Forensic Chatbot (Investigator Copilot)
- **Natural Language Interrogation:** Ask complex cross-modal questions about the crime scene without manual video scrubbing.
- **Quick Query Chips:** Click pre-formulated investigative queries:
  - `🔍 Weapons Identified?`
  - `⚠️ Contradictions vs Media?`
  - `🚗 Getaway Vehicle Details?`
  - `⏱️ Reconstruct Timeline?`
- **Citation-Enforced Grounding:** All copilot answers strictly cite specific timestamps (e.g., `[T+15.0s / 00:15 UTC]`), modality sources, and visual frame IDs. Unverified facts are explicitly asserted as *Indeterminate*.

---

### Tab 5: Chain of Custody & PDF Export
- **Cryptographic Custody Register:** Review unalterable 256-bit SHA-256 digital hashes computed for every uploaded media stream.
- **Groq Case Brief Preview:** Inspect the AI-synthesized statutory crime classification, executive summary, 3 plausible investigative scenarios, and potential alibi inconsistencies.
- **One-Click Court Dossier Export:** Click **Download Official Forensic Report (PDF)** to generate an official court-admissible PDF report complete with supervisor certification sign-off blocks.

---

## 3. Best Practices for Admissible Evidence Intake

1. **Upload Original Media:** Avoid re-encoded or screen-recorded video files to preserve original frame timestamps and pixel clarity.
2. **Review Laplacian Score:** Ensure image clarity reports indicate *Moderate* or *High* clarity ($> 45.0$) before relying on distant license plate optical detections.
3. **Save Master PDF Immediately:** Export the official forensic PDF at the conclusion of intake to establish an early digital chain-of-custody timestamp for judicial presentation.
