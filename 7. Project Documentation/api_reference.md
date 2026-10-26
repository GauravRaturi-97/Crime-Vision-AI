# CrimeVision AI — REST API Reference Manual

**Author:** Gaurav Raturi | SmartBridge EL Capstone Project  
**Base URL:** `http://localhost:5000`  
**API Version:** 2.0.0  

---

## Endpoint Summary

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Serves interactive forensic dashboard with Three.js 3D viewer. |
| `GET` | `/api/health` | Health check and device configuration status. |
| `POST` | `/api/upload` | Ingests multimodal files and returns SHA-256 hashes. |
| `POST` | `/api/analyze` | Executes modular pipeline across all engines. |
| `POST` | `/api/chat` | Natural-language forensic Q&A via Groq LLM. |
| `GET` | `/api/scene-3d` | Returns 3D coordinate geometry for Three.js. |
| `POST` | `/api/export-pdf` | Compiles and downloads court-admissible PDF dossier. |

---

## Detailed Endpoint Specifications

### 1. `GET /api/health`
**Description:** Verifies service availability and engine configurations.

**Response (200 OK):**
```json
{
  "author": "Gaurav Raturi",
  "device": "cpu",
  "groq_configured": true,
  "reportlab_available": true,
  "service": "CrimeVision AI Forensic Platform",
  "status": "healthy"
}
```

---

### 2. `POST /api/upload`
**Description:** Multipart form upload accepting crime scene imagery, 911 dispatch audio, surveillance video clips, and witness notes. Computes SHA-256 immediately.

**Form Parameters:**
- `case_id` (string): Case identification number (e.g. `CV-2026-0891`).
- `witness_notes` (string): Officer or witness interview notes.
- `images` (file list): Image files (`.jpg`, `.png`).
- `audio` (file list): Audio files (`.wav`, `.mp3`).
- `videos` (file list): Video files (`.mp4`, `.mov`).

**Response (200 OK):**
```json
{
  "status": "success",
  "message": "Successfully ingested and hashed 3 evidence artifact(s).",
  "evidence_items": [
    {
      "name": "cctv_frame_01.jpg",
      "type": "Image",
      "size": 142340,
      "hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
    }
  ]
}
```

---

### 3. `POST /api/analyze`
**Description:** Executes the full multimodal pipeline.

**Request Payload:**
```json
{
  "case_id": "CV-2026-0891",
  "incident_location": "Metropolitan Transit Terminal, Sector 4",
  "witness_notes": "Witness claims suspect exited North stairwell."
}
```

**Response (200 OK):**
```json
{
  "status": "success",
  "case_id": "CV-2026-0891",
  "crime_classification": "Armed Commercial Robbery (Penal Code § 211)",
  "severity_level": "Critical",
  "synthesis_markdown": "### 1. STATUTORY CRIME CATEGORIZATION...",
  "master_timeline": [
    {
      "time": "21:38:10 UTC",
      "modality": "CCTV Camera-04",
      "event": "Dark sedan arrives in commercial loading bay.",
      "confidence": "Verified"
    }
  ],
  "scene_3d": {
    "evidence_markers": [
      {
        "id": "EV-01",
        "title": "North Stairwell Egress",
        "position": [-6.0, 0.5, 4.0],
        "color": "#38bdf8"
      }
    ],
    "suspect_path": [[-8.0, 0.2, 5.0], [7.0, 0.2, -3.0]]
  },
  "engine_used": "Groq LLM (llama-3.3-70b-versatile)"
}
```

---

### 4. `POST /api/chat`
**Description:** Investigator Copilot natural-language interrogation.

**Request Payload:**
```json
{
  "query": "What weapons were detected across visual and audio evidence?",
  "chat_history": []
}
```

**Response (200 OK):**
```json
{
  "status": "success",
  "response": "Under case record CV-2026-0891: RT-DETR localized a metallic briefcase held by suspect during egress, corroborated by acoustic transient data at 21:40:48 UTC..."
}
```

---

### 5. `POST /api/export-pdf`
**Description:** Compiles and streams a court-admissible PDF forensic report with SHA-256 chain of custody, master timeline, and attestation signatures.

**Response (200 OK):**
Binary stream with `Content-Type: application/pdf`.
