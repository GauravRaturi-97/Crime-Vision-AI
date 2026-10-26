# CrimeVision AI — OpenAPI & REST API Specification

**Project:** CrimeVision AI — Intelligent Multimodal Forensic Analysis Platform  
**Author / AI Engineer:** Gaurav Raturi  
**Institution:** SmartBridge EL Capstone Project  
**OpenAPI Specification Version:** 3.0.3  
**Base URL:** `http://127.0.0.1:5000` / `http://localhost:5000`  
**License:** Apache 2.0  

---

## 1. Overview & Architecture

CrimeVision AI exposes an asynchronous and synchronous modular REST API for digital forensic laboratories. The API bridges edge computer vision (RT-DETR / YOLOv8), transformer-based audio transcription (OpenAI Whisper), neural vision-language models (BLIP), temporal corroboration engines, Groq LPU inference (Llama-3.3-70B / DeepSeek-R1 / Mixtral-8x7B), and WebGL 3D spatial reconstruction.

All uploaded evidentiary artifacts are cryptographically signed with SHA-256 digests at the ingestion boundary and strictly audited according to the Federal Rules of Evidence Rule 901 standard.

---

## 2. Global Request & Response Conventions

### Headers
- **Content-Type**:
  - `application/json` for structured payloads (fusion, copilot chat, configuration)
  - `multipart/form-data` for file ingestion (images, audio, video)
- **Accept**: `application/json`, `application/pdf`

### Standard Error Envelope
```json
{
  "success": false,
  "error": "Error description message",
  "status_code": 400,
  "timestamp": "2026-10-26T22:15:00.000000+00:00"
}
```

---

## 3. Comprehensive Endpoint Specifications

```
                     CRIMEVISION REST API ENDPOINT MATRIX
 ┌──────────────────────┬────────┬──────────────────────────────────────────────┐
 │ Endpoint             │ Method │ Purpose                                      │
 ├──────────────────────┼────────┼──────────────────────────────────────────────┤
 │ /api/health          │ GET    │ System health check, device, & Groq status   │
 │ /api/upload          │ POST   │ Ingest multiple files & generate SHA-256     │
 │ /api/analyze/image   │ POST   │ RT-DETR object detection + BLIP captioning   │
 │ /api/analyze/audio   │ POST   │ Whisper transcription + Groq sound triage    │
 │ /api/analyze/video   │ POST   │ Temporal sampling, entity & threat timeline  │
 │ /api/fuse            │ POST   │ Cross-modal temporal fusion & Groq synthesis │
 │ /api/analyze         │ POST   │ End-to-end multi-engine execution pipeline   │
 │ /api/chat            │ POST   │ Grounded investigator copilot Q&A            │
 │ /api/scene-3d        │ GET    │ Three.js 3D crime scene coordinates & paths  │
 │ /api/export-pdf      │ GET/POST Generated court-admissible PDF dossier      │
 └──────────────────────┴────────┴──────────────────────────────────────────────┘
```

---

### 3.1. Health Check & Diagnostics
#### `GET /api/health`
Verifies hardware acceleration (CUDA/MPS/CPU), Groq API configuration status, and PDF compilation subsystems.

**Request:**
```bash
curl -X GET http://127.0.0.1:5000/api/health \
  -H "Accept: application/json"
```

**Response (200 OK):**
```json
{
  "status": "healthy",
  "service": "CrimeVision AI Forensic Platform",
  "author": "Gaurav Raturi",
  "device": "cpu",
  "groq_configured": true,
  "reportlab_available": true
}
```

---

### 3.2. Evidence Upload & Cryptographic Hashing
#### `POST /api/upload`
Uploads multimodal physical/digital artifacts into isolated evidence lockers and computes SHA-256 checksums immediately upon receipt.

**Request Type:** `multipart/form-data`

**Parameters:**
- `case_id` *(string, optional)*: Case reference ID (Default: `CV-AUTO-xxxxxx`)
- `witness_notes` *(string, optional)*: Field notes or witness transcripts
- `images` *(file[], optional)*: Forensic image files (`.jpg`, `.jpeg`, `.png`, `.bmp`)
- `audio` *(file[], optional)*: Audio recording files (`.wav`, `.mp3`, `.ogg`, `.flac`)
- `videos` *(file[], optional)*: Surveillance video footage (`.mp4`, `.avi`, `.mov`, `.mkv`)

**Request Example:**
```bash
curl -X POST http://127.0.0.1:5000/api/upload \
  -F "case_id=CV-2026-0891" \
  -F "images=@crime_scene.jpg" \
  -F "audio=@dispatch_911.wav" \
  -F "witness_notes=Suspect fled north wearing dark hoodie"
```

**Response (200 OK):**
```json
{
  "success": true,
  "case_id": "CV-2026-0891",
  "uploaded_files": {
    "images": [
      {
        "filename": "crime_scene.jpg",
        "stored_filename": "CV-2026-0891_img_0_crime_scene.jpg",
        "path": "5. Project Development Phase/uploads/CV-2026-0891_img_0_crime_scene.jpg",
        "sha256": "3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d",
        "size_bytes": 1048576,
        "mime_type": "image/jpeg"
      }
    ],
    "audio": [
      {
        "filename": "dispatch_911.wav",
        "stored_filename": "CV-2026-0891_aud_0_dispatch_911.wav",
        "path": "5. Project Development Phase/uploads/CV-2026-0891_aud_0_dispatch_911.wav",
        "sha256": "4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a",
        "size_bytes": 524288,
        "mime_type": "audio/wav"
      }
    ],
    "videos": []
  },
  "witness_notes": "Suspect fled north wearing dark hoodie",
  "integrity_status": "LOCKED_AND_VERIFIED"
}
```

---

### 3.3. Modular Image Forensic Analysis
#### `POST /api/analyze/image`
Invokes the `ImageForensicEngine` using RT-DETR/YOLOv8 for object/weapon detection, Laplacian variance for blur/clarity scoring, and BLIP for natural language scene captioning.

**Request Type:** `multipart/form-data` or `application/json`

**Form Parameters:**
- `file` *(file, optional)*: Image binary
- `path` *(string, optional)*: Absolute or relative filepath on server

**Request Example:**
```bash
curl -X POST http://127.0.0.1:5000/api/analyze/image \
  -F "file=@crime_scene.jpg"
```

**Response (200 OK):**
```json
{
  "success": true,
  "engine": "ImageForensicEngine",
  "data": {
    "file_path": "5. Project Development Phase/uploads/temp_image.jpg",
    "sha256": "3e23e8160039594a33894f6564e1b1348bbd7a0088d42c4acb73eeaed59c009d",
    "resolution": {"width": 1920, "height": 1080},
    "clarity": {
      "laplacian_variance": 412.8,
      "assessment": "SHARP"
    },
    "detections": [
      {
        "box": [450, 180, 720, 890],
        "label": "person",
        "confidence": 0.942,
        "threat_category": "PERSON_OF_INTEREST"
      },
      {
        "box": [580, 520, 640, 610],
        "label": "knife",
        "confidence": 0.887,
        "threat_category": "CRITICAL_WEAPON"
      }
    ],
    "detection_count": 2,
    "annotated_image_path": "5. Project Development Phase/outputs/annotated_temp_image.jpg",
    "blip_caption": "a man holding a sharp metallic object near a doorway in low light",
    "visual_hypotheses": [
      "Aggressive brandishing of an edged weapon detected.",
      "High probability of close-quarters altercation near egress point."
    ]
  }
}
```

---

### 3.4. Modular Audio Forensic Analysis
#### `POST /api/analyze/audio`
Invokes the `AudioForensicEngine` utilizing OpenAI Whisper for speech-to-text segmentation and Groq LPU zero-shot intelligence for acoustic event triage and forensic credibility assessment.

**Request Type:** `multipart/form-data` or `application/json`

**Form Parameters:**
- `file` *(file, optional)*: Audio binary (`.wav`, `.mp3`)
- `path` *(string, optional)*: Local server filepath

**Request Example:**
```bash
curl -X POST http://127.0.0.1:5000/api/analyze/audio \
  -F "file=@dispatch_911.wav"
```

**Response (200 OK):**
```json
{
  "success": true,
  "engine": "AudioForensicEngine",
  "data": {
    "file_path": "5. Project Development Phase/uploads/dispatch_911.wav",
    "sha256": "4b227777d4dd1fc61c6f884f48641d02b4d121d3fd328cb08b5531fcacdabf8a",
    "language": "en",
    "duration_seconds": 18.5,
    "full_transcript": "He pulled out a knife! Don't come closer! Somebody call the police now!",
    "segments": [
      {
        "id": 0,
        "start": 0.0,
        "end": 3.8,
        "text": "He pulled out a knife!"
      },
      {
        "id": 1,
        "start": 4.1,
        "end": 8.5,
        "text": "Don't come closer! Somebody call the police now!"
      }
    ],
    "audio_events": [
      {
        "timestamp_seconds": 1.2,
        "event_type": "WEAPON_BRANDISHING_SHOUT",
        "statement_excerpt": "He pulled out a knife!",
        "speaker_sentiment": "EXTREME_DISTRESS",
        "credibility_tag": "HIGH"
      },
      {
        "timestamp_seconds": 5.4,
        "event_type": "CALL_FOR_ASSISTANCE",
        "statement_excerpt": "Somebody call the police now!",
        "speaker_sentiment": "PANIC",
        "credibility_tag": "VERIFIED"
      }
    ]
  }
}
```

---

### 3.5. Modular Video Forensic Analysis
#### `POST /api/analyze/video`
Invokes the `VideoForensicEngine` to perform uniform or motion-triggered frame sampling (default: 2 fps), RT-DETR object tracking across frames, entity clustering anomaly computation, and chronological timeline generation.

**Request Type:** `multipart/form-data` or `application/json`

**Form Parameters:**
- `file` *(file, optional)*: Surveillance video file
- `sample_fps` *(float, optional)*: Frames per second to analyze (Default: `2.0`)
- `path` *(string, optional)*: Local server filepath

**Request Example:**
```bash
curl -X POST http://127.0.0.1:5000/api/analyze/video \
  -F "file=@cctv_hallway.mp4" \
  -F "sample_fps=2.0"
```

**Response (200 OK):**
```json
{
  "success": true,
  "engine": "VideoForensicEngine",
  "data": {
    "file_path": "5. Project Development Phase/uploads/cctv_hallway.mp4",
    "sha256": "8f1172a6e9a039912c98d011f0923e445028919bb100d8329a174cda9081a944",
    "total_duration_seconds": 12.0,
    "fps_sampled": 2.0,
    "total_frames_analyzed": 24,
    "timeline": [
      {
        "timestamp": 2.5,
        "frame_idx": 5,
        "detected_entities": ["person", "knife"],
        "threat_level": "HIGH",
        "keyframe_path": "5. Project Development Phase/outputs/keyframe_0005.jpg",
        "motion_score": 0.78
      },
      {
        "timestamp": 6.0,
        "frame_idx": 12,
        "detected_entities": ["person"],
        "threat_level": "MEDIUM",
        "keyframe_path": "5. Project Development Phase/outputs/keyframe_0012.jpg",
        "motion_score": 0.45
      }
    ],
    "high_threat_spikes": 1,
    "highlights_clip_path": "5. Project Development Phase/outputs/highlights_cctv_hallway.mp4"
  }
}
```

---

### 3.6. Cross-Modal Evidence Fusion & Master Timeline
#### `POST /api/fuse`
Executes `MultimodalFusionEngine` over pre-computed image, audio, video, and witness payloads. Corroborates events within a $\pm 3.5\text{s}$ temporal window, calculates a mathematical Evidence Confidence Score, flags testimony discrepancies, and generates a structured Groq LPU case dossier.

**Request Type:** `application/json`

**Payload Schema:**
```json
{
  "image_data": { ... },
  "audio_data": { ... },
  "video_data": { ... },
  "witness_notes": "string"
}
```

**Request Example:**
```bash
curl -X POST http://127.0.0.1:5000/api/fuse \
  -H "Content-Type: application/json" \
  -d '{
    "witness_notes": "Suspect fled in yellow boots",
    "image_data": {"detection_count": 2, "blip_caption": "knife on floor"},
    "audio_data": {"audio_events": [{"timestamp_seconds": 1.2, "event_type": "WEAPON_BRANDISHING_SHOUT"}]},
    "video_data": {"timeline": [{"timestamp": 2.5, "threat_level": "HIGH", "detected_entities": ["knife"]}]}
  }'
```

**Response (200 OK):**
```json
{
  "success": true,
  "engine": "MultimodalFusionEngine",
  "data": {
    "evidence_confidence_score": 0.88,
    "confidence_tier": "HIGH (COURT ADMISSIBLE)",
    "master_timeline": [
      {
        "timestamp_seconds": 1.2,
        "modality": "AUDIO",
        "description": "Witness distress cry: 'He pulled out a knife!'",
        "threat_level": "HIGH",
        "corroborated": true
      },
      {
        "timestamp_seconds": 2.5,
        "modality": "VIDEO + IMAGE",
        "description": "Subject wielding weapon captured on CCTV egress",
        "threat_level": "CRITICAL",
        "corroborated": true
      }
    ],
    "discrepancies": [
      {
        "item": "Suspect Footwear",
        "witness_claim": "Yellow boots",
        "forensic_finding": "Dark athletic footwear confirmed in frame 12",
        "severity": "EVIDENTIARY_CONFLICT"
      }
    ],
    "case_brief": {
      "crime_classification": "Aggravated Assault with Deadly Weapon",
      "executive_summary": "At 21:40 UTC, an armed altercation occurred at the transit terminal egress...",
      "sequence_of_events": [
        "21:40:01 - Verbal confrontation begins.",
        "21:40:02 - Edged weapon deployed."
      ],
      "investigative_leads": [
        "Subpoena surveillance cameras along North Egress Corridor.",
        "Recover latent fingerprints from metallic threshold."
      ]
    }
  }
}
```

---

### 3.7. End-to-End Orchestrated Analysis Pipeline
#### `POST /api/analyze`
Executes complete pipeline in one single call: runs all uploaded modalities through their respective engines, triggers multimodal fusion, and updates the shared memory state.

**Request Type:** `application/json`

**Payload:**
```json
{
  "case_id": "CV-2026-0891"
}
```

**Response (200 OK):**
Returns consolidated bundle containing `{ "success": true, "image_result": {...}, "audio_result": {...}, "video_result": {...}, "fused_result": {...} }`.

---

### 3.8. Grounded Investigator Copilot Chat
#### `POST /api/chat`
Interrogates the fused case dossier using the Groq LPU LLM with strict grounding instructions to prevent AI hallucination. Only facts established in evidence may be affirmed; unverified witness claims are explicitly flagged.

**Request Type:** `application/json`

**Request Payload:**
```json
{
  "question": "Was a firearm observed during the incident?",
  "history": [
    {"role": "user", "content": "What weapons were detected?"},
    {"role": "assistant", "content": "A knife with an 8-inch blade was detected with 88.7% confidence."}
  ]
}
```

**Request Example:**
```bash
curl -X POST http://127.0.0.1:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "question": "Did the suspect possess a firearm?"
  }'
```

**Response (200 OK):**
```json
{
  "success": true,
  "question": "Did the suspect possess a firearm?",
  "answer": "Negative. No firearm was identified in the visual or CCTV telemetry. Visual evidence confirms an edged weapon (knife) at 21:40:02 UTC. Audio dispatch reports mention only an edged weapon.",
  "confidence": 0.95,
  "sources_cited": ["image_engine:det_02", "audio_engine:seg_01"],
  "model": "groq:llama-3.3-70b-versatile"
}
```

---

### 3.9. 3D Spatial Scene Coordinates
#### `GET /api/scene-3d`
Returns calibrated 3D world coordinates, evidence marker loci, suspect trajectory vectors, and camera presets for the WebGL Three.js interactive canvas.

**Request:**
```bash
curl -X GET http://127.0.0.1:5000/api/scene-3d \
  -H "Accept: application/json"
```

**Response (200 OK):**
```json
{
  "success": true,
  "scene_id": "METROPOLITAN_TRANSIT_HALL",
  "grid_dimensions": {"x": 50, "z": 50, "step": 1},
  "evidence_markers": [
    {
      "id": "EV-01",
      "label": "Stairwell Egress Point",
      "position": {"x": -8.5, "y": 0.1, "z": -12.0},
      "color": 16724530,
      "modality": "VIDEO_ANOMALY",
      "details": "Frame #5 weapon detection locus"
    },
    {
      "id": "EV-02",
      "label": "Acoustic Transient Origin",
      "position": {"x": 4.2, "y": 0.1, "z": -2.1},
      "color": 39372,
      "modality": "AUDIO_TRANSIENT",
      "details": "Dispatch distress timestamp 1.2s"
    },
    {
      "id": "EV-03",
      "label": "Discarded Weapon Recovery",
      "position": {"x": 14.0, "y": 0.1, "z": 18.5},
      "color": 16753920,
      "modality": "PHYSICAL_EVIDENCE",
      "details": "Latent print recovery zone"
    }
  ],
  "trajectory_spline": [
    {"x": -8.5, "y": 0.5, "z": -12.0},
    {"x": -2.0, "y": 0.5, "z": -6.0},
    {"x": 4.2, "y": 0.5, "z": -2.1},
    {"x": 9.0, "y": 0.5, "z": 7.0},
    {"x": 14.0, "y": 0.5, "z": 18.5}
  ]
}
```

---

### 3.10. Court-Admissible Forensic PDF Export
#### `GET /api/export-pdf` & `POST /api/export-pdf`
Compiles a forensic PDF dossier utilizing ReportLab. Formatted with executive summary, discrepancy matrix, chain of custody ledger with SHA-256 digests, and supervisor verification signature blocks.

**Query Parameters (for GET):**
- `case_id` *(string, optional)*: Case reference ID (Default: `CV-2026-0891`)

**Request Example:**
```bash
# Direct download via browser or curl
curl -X GET "http://127.0.0.1:5000/api/export-pdf?case_id=CV-2026-0891" \
  -o "Forensic_Dossier_CV-2026-0891.pdf"
```

**Response (200 OK):**
- **Content-Type:** `application/pdf`
- **Content-Disposition:** `attachment; filename="Forensic_Report_CV-2026-0891.pdf"`
- **Binary Stream:** PDF document compliant with ISO 32000-1.

---

## 4. HTTP Status Codes & Troubleshooting

| HTTP Code | Condition | Solution / Action |
|---|---|---|
| `200 OK` | Request completed successfully. | Parse returned JSON or stream binary PDF. |
| `400 Bad Request` | Missing required parameters or empty file upload. | Ensure file fields are populated and JSON is valid. |
| `404 Not Found` | Requested case or engine output does not exist. | Upload evidence files before triggering analysis. |
| `415 Unsupported Media` | File format unsupported (e.g. `.exe`). | Upload valid formats: JPEG, PNG, WAV, MP3, MP4. |
| `500 Internal Error` | Subsystem runtime exception. | Inspect Flask logs; ensure Groq API key is valid. |

---

## 5. Security & Legal Admissibility Notice
All endpoints in CrimeVision AI are architected to enforce:
1. **Chain of Custody:** Immutable SHA-256 digests generated in memory before disk serialization.
2. **Deterministic Fallbacks:** Fallback models engage automatically if cloud LPU services experience transient network delays.
3. **Forensic Integrity:** Evidence files are strictly read-only and never modified during visual annotation.
