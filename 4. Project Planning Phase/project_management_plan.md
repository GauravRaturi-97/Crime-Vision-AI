# Project Management Plan (PMP)

**Project Title:** CrimeVision AI — Intelligent Multimodal Forensic Analysis Platform  
**Lead AI Architect:** Gaurav Raturi  
**Program:** SmartBridge EL Capstone Project  
**Date:** October 2026  
**Status:** In Execution / Production-Ready  

---

## 1. Work Breakdown Structure (WBS)

```
CrimeVision AI
├── 1.0 Planning & Requirements Analysis
│   ├── 1.1 Project Charter & Scope Statement
│   ├── 1.2 Multi-modal Forensic Requirements (SRS)
│   └── 1.3 Legal & Chain-of-Custody Compliance Planning
├── 2.0 System & UI Architecture
│   ├── 2.1 Multimodal Pipeline Architecture Design
│   ├── 2.2 Three.js 3D Coordinate Mapping System
│   └── 2.3 ReportLab PDF Template Engine
├── 3.0 Core Engine Implementation
│   ├── 3.1 image_engine (RT-DETR + BLIP + OpenCV)
│   ├── 3.2 audio_engine (OpenAI Whisper + Acoustic Peaks)
│   ├── 3.3 video_engine (OpenCV Motion Tracking + Keyframes)
│   └── 3.4 fusion_engine (Groq Llama-3.3 + Discrepancy Matrix)
├── 4.0 Backend & Dashboard Integration
│   ├── 4.1 Flask REST API Endpoints
│   ├── 4.2 Interactive Three.js 3D WebGL Canvas
│   └── 4.3 Investigator Copilot Conversational Chat
└── 5.0 Verification, Testing & Capstone Delivery
    ├── 5.1 Automated Engine & API Test Suite
    ├── 5.2 Capstone Evaluation Runbook & Demonstration Script
    └── 5.3 Technical Documentation & Source Packaging
```

---

## 2. Sprint Roadmap & Milestones

| Sprint | Focus Area | Deliverables | Status |
|---|---|---|---|
| **Sprint 1** | Ideation & Requirements | `project_proposal.md`, `requirements_spec.md`, environment setup | Completed |
| **Sprint 2** | Architecture & 3D Design | `system_architecture.md`, Three.js 3D coordinate model, UI wireframes | Completed |
| **Sprint 3** | Computer Vision & Audio | `image_engine.py` (RT-DETR/BLIP), `audio_engine.py` (Whisper) | Completed |
| **Sprint 4** | Video Tracking & GenAI Fusion | `video_engine.py` (OpenCV motion), `fusion_engine.py` (Groq LLM) | Completed |
| **Sprint 5** | Flask REST API & 3D WebGL | `app.py`, `templates/index.html`, `static/js/crime_scene_3d.js` | Completed |
| **Sprint 6** | Testing & Documentation | `test_suite.py`, API reference, demonstration script, root `README.md` | Completed |

---

## 3. Risk Mitigation Matrix

| Risk ID | Identified Risk | Impact | Likelihood | Mitigation Strategy |
|---|---|---|---|---|
| **R-01** | High latency or quota limit on cloud LLM APIs | High | Medium | Dual-engine architecture with Groq LPU primary and Google Gemini fallback + local deterministic fallback. |
| **R-02** | Absence of GPU hardware for local model inference | Medium | High | Automatic device detection (`cuda` if available else `cpu`); lazy-loading and OpenCV heuristic fallbacks. |
| **R-03** | Digital evidence tampering allegations in legal review | Critical | Low | Immediate cryptographic SHA-256 calculation upon ingestion with immutable register printed in PDF dossiers. |
| **R-04** | Large video payload handling memory exhaustion | High | Low | Streamlined chunking and OpenCV keyframe downsampling with maximum payload size limits. |
