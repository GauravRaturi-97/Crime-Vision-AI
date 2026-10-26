# CrimeVision AI — Assessor Evaluation & Oral Demonstration Script

**Project Title:** CrimeVision AI — Intelligent Multimodal Forensic Analysis Platform  
**Candidate & AI Architect:** Gaurav Raturi  
**Evaluation Forum:** SmartBridge Experiential Learning Capstone Project  
**Target Duration:** 5 Minutes (Oral + Live Software Walkthrough)  
**Live URL:** `http://localhost:5000` (or `http://127.0.0.1:5000`)  
**Target Audience:** SmartBridge Technical Evaluators, Academic Mentors, Forensic Domain Experts  

---

## 1. Quick Reference Timeline

```
 ┌───────────────┬────────────────────────────────────────────────────────────┐
 │ Timeline      │ Presentation Stage & Visual Focus                          │
 ├───────────────┼────────────────────────────────────────────────────────────┤
 │ 0:00 - 1:00   │ Introduction, Problem Statement & Evidence Ingestion       │
 │               │ [Tab 1: Evidence Ingestion & Cryptographic Locker]        │
 ├───────────────┼────────────────────────────────────────────────────────────┤
 │ 1:00 - 2:00   │ Multimodal Master Timeline & Cross-Modal Corroboration     │
 │               │ [Tab 2: Master Timeline & Discrepancy Matrix]              │
 ├───────────────┼────────────────────────────────────────────────────────────┤
 │ 2:00 - 3:00   │ Interactive 3D Spatial Scene Reconstruction (Three.js)     │
 │               │ [Tab 3: 3D Scene Reconstruction & Trajectory Spline]       │
 ├───────────────┼────────────────────────────────────────────────────────────┤
 │ 3:00 - 4:00   │ Grounded Investigator Copilot & Hallucination Guardrails   │
 │               │ [Tab 4: Investigator Copilot & Groq LPU Interrogation]     │
 ├───────────────┼────────────────────────────────────────────────────────────┤
 │ 4:00 - 5:00   │ Chain of Custody & Court-Admissible PDF Dossier Export     │
 │               │ [Tab 5: Chain of Custody & ReportLab Export]               │
 └───────────────┴────────────────────────────────────────────────────────────┘
```

---

## 2. Step-by-Step Oral Walkthrough

---

### Minute 0:00 – 1:00: Introduction, Problem Statement & Evidence Ingestion
**Screen:** Browser open at `http://localhost:5000` on **Tab 1: Evidence Ingestion**.

#### Spoken Script:
> *"Respected evaluators, good morning/afternoon. My name is **Gaurav Raturi**, and today I am proud to present my SmartBridge Capstone Project: **CrimeVision AI — Intelligent Multimodal Forensic Analysis Platform**.*
>
> *In real-world criminal investigations, forensic detectives are overwhelmed by fragmented evidence: CCTV videos without audio, 911 dispatch calls without visuals, blurry scene photos, and conflicting witness testimonies. Today, human investigators manually review these silos, which leads to cognitive fatigue, missed clues, and evidence thrown out in court due to broken chains of custody.*
>
> *CrimeVision AI solves this fundamentally. Looking at our dashboard, we begin in **Tab 1: Evidence Ingestion**. Here, an investigator uploads multimodal evidentiary artifacts: high-resolution crime scene photographs, 911 dispatch audio recordings, surveillance video footage, and initial witness statements.*
>
> *Notice that the moment an artifact touches our secure intake locker, our backend immediately computes its **cryptographic SHA-256 hash** before running any AI model. This guarantees non-repudiation and strict compliance with the **Federal Rules of Evidence Rule 901**."*

#### Physical Actions:
1. Point to the header banner showing: *"CrimeVision AI | SmartBridge Capstone — Gaurav Raturi"*.
2. Highlight the green badge: *"CHAIN OF CUSTODY VERIFIED (SHA-256)"*.
3. Click or show the pre-populated evidence dropzones for Image, Audio, Video, and Witness Notes.
4. Click the primary button: **"Run Forensic Analysis Pipeline"**.

---

### Minute 1:00 – 2:00: Master Timeline & Cross-Modal Corroboration
**Screen:** Switch to **Tab 2: Master Timeline**.

#### Spoken Script:
> *"Once ingested, our backend triggers three specialized neural engines simultaneously:
> 1. Our **ImageForensicEngine** runs an **RT-DETR** transformer to detect weapons and subjects, and **Salesforce BLIP** to generate scene hypotheses.
> 2. Our **AudioForensicEngine** runs **OpenAI Whisper** to transcribe dispatch audio and extract acoustic stress events.
> 3. Our **VideoForensicEngine** samples surveillance footage, detecting weapon brandishing and movement spikes.
>
> *Now, looking at **Tab 2**, our **MultimodalFusionEngine** solves the core challenge: **Temporal Alignment**. It synchronizes the audio timestamp of the witness shouting 'He pulled out a knife!' with the exact video keyframe at 2.5 seconds showing an edged weapon.*
>
> *Notice the **Evidence Confidence Score of 88% (Court Admissible)**. Even more crucially, examine our automated **Discrepancy Matrix**: the witness claimed the suspect was wearing 'bright yellow boots', but our visual detector confirmed 'dark athletic shoes'. CrimeVision AI flags this contradiction instantly for detectives."*

#### Physical Actions:
1. Click on **Tab 2: Master Timeline**.
2. Scroll through the unified chronological cards: Audio scream at 1.2s $\rightarrow$ Video weapon detection at 2.5s $\rightarrow$ Suspect fleeing at 6.0s.
3. Hover over the **Discrepancy Matrix** badge highlighting the footwear contradiction.
4. Point to the **Evidence Confidence Score** dial.

---

### Minute 2:00 – 3:00: Interactive 3D Spatial Crime Scene Reconstruction
**Screen:** Switch to **Tab 3: 3D Scene Reconstruction**.

#### Spoken Script:
> *"Evidence is not just chronological; it is **spatial**. In Tab 3, CrimeVision AI renders an interactive **Three.js WebGL 3D digital twin** of the crime scene.
>
> *Instead of staring at flat photos, detectives can navigate in 3D space using orbital controls. Our platform automatically pins interactive spatial evidence markers:
> - **Marker EV-01** marks the Stairwell Egress Point where the suspect breached the scene.
> - **Marker EV-02** pins the acoustic origin where the 911 emergency call was placed.
> - **Marker EV-03** identifies the recovery locus of the discarded weapon.
>
> *Notice the animated **golden trajectory spline** tracing the suspect's escape vector across the transit terminal grid. When I click preset views—Top-Down Aerial or Tactical Egress—the camera smoothly transitions to provide tactical clarity for prosecuting attorneys and jury panels."*

#### Physical Actions:
1. Click on **Tab 3: 3D Scene Reconstruction**.
2. Left-click and drag the Three.js viewport to rotate the perspective around the terminal grid.
3. Click on the camera preset button: **"Focus Stairwell (EV-01)"** to animate the camera to the egress marker.
4. Point out the animated pulsating particle traveling along the escape trajectory vector.

---

### Minute 3:00 – 4:00: Grounded Investigator Copilot Chat
**Screen:** Switch to **Tab 4: Investigator Copilot**.

#### Spoken Script:
> *"Next, in **Tab 4**, we introduce the **Forensic Investigator Copilot**, powered by **Groq LPU hardware acceleration** running open-weight **Llama-3.3-70B**.
>
> *Generative AI in law enforcement is often dangerous because of hallucinations. We solved this with **Strict Evidence Grounding Guardrails**. The Copilot is mathematically constrained to cite only confirmed evidentiary tokens from our fusion graph.
>
> *Let's test it live. I will ask: 'Did the suspect possess a firearm?'
>
> *Notice the near-instantaneous response time from Groq's LPU. The Copilot answers unequivocally: 'Negative. Visual detection confirms a knife with an 8-inch blade at timestamp 21:40:02 UTC. Audio transcripts corroborate an edged weapon. No firearm was detected.'
>
> *It explicitly cites the source engine and refuses to speculate outside proven facts."*

#### Physical Actions:
1. Click on **Tab 4: Investigator Copilot**.
2. Click the quick-query chip: **"Was a firearm detected?"** or type in the chat box.
3. Press **Send** and demonstrate the sub-second response rendered in the chat stream.
4. Highlight the source citation tags: `[image_engine:det_02]` and `[audio_engine:seg_01]`.

---

### Minute 4:00 – 5:00: Chain of Custody & Court-Admissible PDF Export
**Screen:** Switch to **Tab 5: Custody & Report**.

#### Spoken Script:
> *"Finally, in **Tab 5**, we address the legal finish line: **Court Admissibility**.
>
> *AI analysis is useless if it cannot withstand cross-examination in a court of law. Here, our **Cryptographic Chain of Custody Ledger** displays the full lifecycle of every piece of evidence: ingestion timestamp, original filename, SHA-256 cryptographic digest, and processing engine status.
>
> *With a single click on **'Export Court-Ready PDF Dossier'**, CrimeVision AI uses **ReportLab** to generate an official 3-page forensic dossier.
>
> *This document contains the Executive Summary, the Unified Master Timeline, the Discrepancy Matrix, the complete SHA-256 Ledger, and formal Supervisor Sign-off blocks ready for submission to the District Attorney.
>
> *In summary, CrimeVision AI transforms fragmented, chaotic forensic data into an objective, corroborated, 3D-reconstructed, and legally ironclad prosecution dossier in under 60 seconds.*
>
> *Thank you, and I am now open to your questions and technical evaluation."*

#### Physical Actions:
1. Click on **Tab 5: Custody & Report**.
2. Point to the SHA-256 hash table showing the green verified statuses.
3. Click the **"Export Court-Ready PDF Dossier"** button; show the downloaded PDF opening in the browser or viewer.
4. Conclude presentation with confident posture and slide into Q&A.

---

## 3. Anticipated Assessor Questions & Model Answers

### Q1: *"Why did you choose Groq LPU over standard cloud GPUs like Nvidia A100?"*
> **Answer:** *"Groq's Language Processing Unit (LPU) uses a deterministic Tensor Streaming Architecture. Unlike conventional GPUs that suffer from high batching latency and memory bandwidth bottlenecks, Groq delivers over 450 tokens per second at batch size 1. In high-stress forensic triage or active tactical situations, investigators cannot wait 15 seconds for an LLM response. Furthermore, Groq's inference cost is nearly 90% lower than dedicated cloud GPU instances."*

### Q2: *"How do you prevent the LLM from hallucinating non-existent weapons or evidence?"*
> **Answer:** *"We implement a dual guardrail architecture. First, the LLM is supplied with a strictly structured context window containing only verified JSON objects from the upstream computer vision (RT-DETR) and audio (Whisper) modules. Second, our system prompt enforces forensic rules: any fact not explicitly corroborated by an evidentiary token must be rejected, and witness claims are tagged separately under our Discrepancy Matrix."*

### Q3: *"How does the system ensure evidence integrity under legal cross-examination?"*
> **Answer:** *"We adhere to the Federal Rules of Evidence Rule 901. Immediately upon ingestion, before any decoding or processing, the file's binary stream is hashed via SHA-256. All analytical outputs and intermediate keyframes are linked back to this primary hash in our Chain of Custody Ledger. The original evidence files are treated as immutable and stored in a read-only locker."*

### Q4: *"What happens if the primary RT-DETR weights or Groq API are temporarily unavailable?"*
> **Answer:** *"CrimeVision AI is built with zero single points of failure. If the RT-DETR model weights fail to load, the engine automatically falls back to an embedded YOLOv8 lightweight detector. If the Groq API experiences network latency, our Multimodal Fusion Engine falls back gracefully to a deterministic rule-based heuristic synthesizer."*
