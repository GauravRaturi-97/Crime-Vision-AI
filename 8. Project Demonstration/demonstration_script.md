# Capstone Demonstration & Evaluation Script

**Project:** CrimeVision AI — Intelligent Multimodal Forensic Analysis Platform  
**Candidate / AI Architect:** Gaurav Raturi  
**Program:** SmartBridge EL Capstone Project  
**Target Duration:** 5 – 7 Minutes  

---

## 1. Demonstration Outline

| Time | Segment | Focus | Key Screen / Feature |
|---|---|---|---|
| **0:00 - 1:00** | Introduction & Problem Statement | Fragmented evidence, manual review bottlenecks, lack of spatial context | Title banner, Architecture Diagram |
| **1:00 - 2:00** | Digital Evidence Locker & Ingestion | Ingesting CCTV stills, 911 audio, and witness statement; SHA-256 calculation | Left sidebar form, Cryptographic register |
| **2:00 - 3:30** | Interactive 3D Crime Scene (Three.js) | WebGL 3D spatial reconstruction, evidence markers EV-01/02/03, flight path | Three.js canvas, OrbitControls, preset camera |
| **3:30 - 4:45** | Multimodal AI Execution | RT-DETR visual detections, BLIP caption, Whisper transcript, Groq Llama-3.3 | Detections gallery, Master Timeline table |
| **4:45 - 5:45** | Investigator Copilot & Discrepancies | Asking natural language questions, uncovering footwear contradiction | Chat Copilot interface, suggested query chips |
| **5:45 - 6:30** | Official Dossier Export & Conclusion | Generating court-ready PDF dossier with chain of custody & supervisor blocks | ReportLab PDF download, summary review |

---

## 2. Step-by-Step Evaluator Script

### Step 1: Launch Application
```bash
cd "5. Project Development Phase"
python app.py
```
Open **`http://localhost:5000`** in Google Chrome or Firefox.

### Step 2: Highlight System Attribution
- Point to top header: **"CrimeVision AI — Multimodal Forensic Intelligence Platform | SmartBridge Capstone — Gaurav Raturi"**.
- Point to green integrity badge: **"CHAIN OF CUSTODY VERIFIED (SHA-256)"**.

### Step 3: Demonstrate 3D Crime Scene Viewer
- Rotate the camera with left mouse drag to reveal the Metropolitan Transit Terminal and Loading Bay.
- Click **"Stairwell Egress (EV-01)"** to focus the camera on the egress point where the suspect emerged at 21:40 UTC.
- Click marker **EV-02** to reveal the acoustic transient origin.
- Highlight the traveling yellow pulse particle along the suspect's trajectory vector.

### Step 4: Execute Multimodal Forensic Fusion
- Click **"Execute Multimodal Forensic Fusion"**.
- Highlight that the system synchronously triggers:
  1. `image_engine`: RT-DETR identifies weapons and subject; BLIP generates visual scenario hypothesis.
  2. `audio_engine`: OpenAI Whisper transcribes dispatch audio and calculates distress index.
  3. `video_engine`: OpenCV computes motion surges.
  4. `fusion_engine`: Groq LLM evaluates the discrepancy matrix (confirming stairwell egress while flagging the yellow footwear contradiction).

### Step 5: Query Investigator Copilot
- Click the chip: **"⚠️ Contradictions?"**.
- Groq LLM responds in sub-second time, highlighting that the witness claimed yellow sneakers, but CCTV video/spectral analysis verified dark gray shoes.

### Step 6: Export Court-Admissible Dossier
- Click **"Export Court-Admissible Dossier (PDF)"**.
- Open the downloaded PDF: showcase the Case Overview table, SHA-256 hash register, Master Timeline, and examiner attestation sign-offs.
