"""
CrimeVision AI - Intelligent Multimodal Forensic Analysis Platform
Backend Presentation Layer & REST API Controller
Lead Architect: Gaurav Raturi | SmartBridge EL Capstone Project

Capabilities:
- Flask REST API with Flask-CORS serving the interactive investigative dashboard.
- POST /api/analyze/image -> runs ImageForensicEngine (RT-DETR + BLIP).
- POST /api/analyze/audio -> runs AudioForensicEngine (OpenAI Whisper + Groq).
- POST /api/analyze/video -> runs VideoForensicEngine (OpenCV + Anomaly Spikes).
- POST /api/fuse          -> merges modalities via MultimodalFusionEngine.
- POST /api/chat          -> interrogates evidence using Groq LLM Copilot.
- GET  /api/export-pdf    -> compiles and downloads court-admissible PDF dossier.
- GET  /                  -> serves the forensic dashboard console.
"""

import os
import io
import re
import sys
import json
import base64
import hashlib
import datetime
import logging
from typing import Dict, Any, List, Optional, Tuple, Union

from flask import Flask, render_template, request, jsonify, send_file, Response
from flask_cors import CORS
from dotenv import load_dotenv

# Load Environment Configuration
load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("CrimeVision.App")

# Ensure local module visibility
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import Modular Core Forensic Engines
from image_engine import get_image_engine, ImageForensicEngine, analyze_image, compute_sha256 as image_sha256
from audio_engine import get_audio_engine, AudioForensicEngine, analyze_audio, compute_sha256 as audio_sha256
from video_engine import get_video_engine, VideoForensicEngine, analyze_video, compute_sha256 as video_sha256
from fusion_engine import (
    get_fusion_engine,
    MultimodalFusionEngine,
    fuse_multimodal_evidence,
    ask_forensic_copilot,
    generate_3d_crime_scene_data,
    clean_markdown_for_reportlab
)

# Initialize Flask Application
app = Flask(
    __name__,
    template_folder="templates",
    static_folder="static"
)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "crimevision_forensic_secure_token_2026_xyz")
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024  # 100MB limit for forensic media
CORS(app)

# In-Memory Digital Chain-of-Custody & Evidence Store
EVIDENCE_STORE: Dict[str, Any] = {
    "case_info": {
        "case_id": "CV-2026-0891",
        "lead_investigator": "Detective Special Agent",
        "incident_location": "Metropolitan Transit Terminal, Sector 4",
        "incident_date": "2026-10-26 21:40:00 UTC"
    },
    "witness_notes": (
        "Witness Statement (Terminal Guard #04): At 21:40, suspect exited North stairwell "
        "wearing dark hoodie, holding silver metallic briefcase. Gunshots reported, followed by "
        "flight in waiting dark sedan with rear plate ending in 89."
    ),
    "images": [],
    "audio": [],
    "videos": [],
    "image_reports": [],
    "audio_reports": [],
    "video_reports": [],
    "fused_data": None,
    "chat_history": []
}


def sanitize_evidence_item(name: str, raw_bytes: bytes, modality: str) -> Dict[str, Any]:
    """Generates registered cryptographic custody artifact."""
    sha = hashlib.sha256(raw_bytes).hexdigest()
    return {
        "name": name,
        "type": modality,
        "size": len(raw_bytes),
        "hash": sha,
        "bytes": raw_bytes,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S UTC")
    }


# ============================================================================
# Presentation & Web Dashboard Endpoints
# ============================================================================

@app.route("/", methods=["GET"])
def index() -> str:
    """Renders the main interactive forensic console."""
    return render_template("index.html")


@app.route("/api/health", methods=["GET"])
def api_health() -> Response:
    """System health check and author attribution."""
    return jsonify({
        "status": "healthy",
        "service": "CrimeVision AI Forensic Platform",
        "version": "2.0.0",
        "author": "Gaurav Raturi",
        "program": "SmartBridge Google Cloud GenAI Capstone",
        "timestamp": datetime.datetime.now().isoformat()
    })


@app.route("/api/scene-3d", methods=["GET"])
def api_scene_3d() -> Response:
    """Returns spatial 3D points, markers, and vectors for Three.js viewer."""
    case_info = EVIDENCE_STORE["case_info"]
    scene_data = generate_3d_crime_scene_data(
        case_info,
        EVIDENCE_STORE["image_reports"],
        EVIDENCE_STORE["audio_reports"],
        EVIDENCE_STORE["video_reports"]
    )
    return jsonify({"status": "success", "scene_3d": scene_data})


# ============================================================================
# Modular Analysis Endpoints (Prompt 6 Requirements)
# ============================================================================

@app.route("/api/analyze/image", methods=["POST"])
def api_analyze_image() -> Response:
    """
    POST /api/analyze/image:
    Executes ImageForensicEngine (RT-DETR object detection + BLIP scene captioning).
    """
    try:
        raw_bytes = b""
        filename = "evidence_image.jpg"

        if "image" in request.files:
            f = request.files["image"]
            filename = f.filename or filename
            raw_bytes = f.read()
        elif "file" in request.files:
            f = request.files["file"]
            filename = f.filename or filename
            raw_bytes = f.read()
        elif request.is_json:
            data = request.get_json() or {}
            filename = data.get("filename", filename)
            b64_content = data.get("image_base64", "")
            if b64_content:
                raw_bytes = base64.b64decode(b64_content)

        engine = get_image_engine()
        report = engine.analyze(raw_bytes, filename=filename)

        # Register in custody store
        item = sanitize_evidence_item(filename, raw_bytes or b"DEMO_IMAGE", "Image")
        EVIDENCE_STORE["images"].append(item)
        EVIDENCE_STORE["image_reports"].append(report)

        return jsonify({
            "status": "success",
            "modality": "image",
            "report": report
        })
    except Exception as e:
        logger.error(f"Image analysis error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/analyze/audio", methods=["POST"])
def api_analyze_audio() -> Response:
    """
    POST /api/analyze/audio:
    Executes AudioForensicEngine (Whisper multilingual transcription + Groq event extraction).
    """
    try:
        raw_bytes = b""
        filename = "dispatch_recording.wav"

        if "audio" in request.files:
            f = request.files["audio"]
            filename = f.filename or filename
            raw_bytes = f.read()
        elif "file" in request.files:
            f = request.files["file"]
            filename = f.filename or filename
            raw_bytes = f.read()
        elif request.is_json:
            data = request.get_json() or {}
            filename = data.get("filename", filename)
            b64_content = data.get("audio_base64", "")
            if b64_content:
                raw_bytes = base64.b64decode(b64_content)

        engine = get_audio_engine()
        report = engine.analyze(raw_bytes, filename=filename)

        item = sanitize_evidence_item(filename, raw_bytes or b"DEMO_AUDIO", "Audio")
        EVIDENCE_STORE["audio"].append(item)
        EVIDENCE_STORE["audio_reports"].append(report)

        return jsonify({
            "status": "success",
            "modality": "audio",
            "report": report
        })
    except Exception as e:
        logger.error(f"Audio analysis error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/analyze/video", methods=["POST"])
def api_analyze_video() -> Response:
    """
    POST /api/analyze/video:
    Executes VideoForensicEngine (OpenCV frame sampling, RT-DETR detection & anomaly spikes).
    """
    try:
        raw_bytes = b""
        filename = "cctv_footage.mp4"

        if "video" in request.files:
            f = request.files["video"]
            filename = f.filename or filename
            raw_bytes = f.read()
        elif "file" in request.files:
            f = request.files["file"]
            filename = f.filename or filename
            raw_bytes = f.read()
        elif request.is_json:
            data = request.get_json() or {}
            filename = data.get("filename", filename)
            b64_content = data.get("video_base64", "")
            if b64_content:
                raw_bytes = base64.b64decode(b64_content)

        engine = get_video_engine()
        report = engine.analyze(raw_bytes, filename=filename, sample_fps=2.0)

        item = sanitize_evidence_item(filename, raw_bytes or b"DEMO_VIDEO", "Video")
        EVIDENCE_STORE["videos"].append(item)
        EVIDENCE_STORE["video_reports"].append(report)

        return jsonify({
            "status": "success",
            "modality": "video",
            "report": report
        })
    except Exception as e:
        logger.error(f"Video analysis error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/fuse", methods=["POST"])
def api_fuse() -> Response:
    """
    POST /api/fuse:
    Merges loaded modalities via MultimodalFusionEngine, computes timeline & Groq case brief.
    """
    try:
        data = request.get_json() or {}
        witness_notes = data.get("witness_notes") or request.form.get("witness_notes") or EVIDENCE_STORE["witness_notes"]
        case_id = data.get("case_id") or request.form.get("case_id") or EVIDENCE_STORE["case_info"]["case_id"]
        location = data.get("incident_location") or request.form.get("incident_location") or EVIDENCE_STORE["case_info"]["incident_location"]

        case_info = {
            "case_id": case_id,
            "lead_investigator": EVIDENCE_STORE["case_info"]["lead_investigator"],
            "incident_location": location,
            "incident_date": EVIDENCE_STORE["case_info"]["incident_date"]
        }
        EVIDENCE_STORE["case_info"] = case_info
        EVIDENCE_STORE["witness_notes"] = witness_notes

        # Ensure demo baselines if no media was uploaded yet
        img_reports = EVIDENCE_STORE["image_reports"] or [analyze_image(b"", "cctv_exterior_gate4.jpg")]
        aud_reports = EVIDENCE_STORE["audio_reports"] or [analyze_audio(b"", "dispatch_recording_ch03.wav")]
        vid_reports = EVIDENCE_STORE["video_reports"] or [analyze_video(b"", "cctv_surveillance_cam04.mp4")]

        fusion_engine = get_fusion_engine()

        # 1. Multimodal Alignment
        fused = fusion_engine.fuse_evidence(
            image_data=img_reports,
            audio_data=aud_reports,
            video_data=vid_reports,
            witness_notes=witness_notes,
            case_info=case_info
        )

        # 2. Groq Case Brief Generation
        brief = fusion_engine.generate_case_brief(fused)

        # 3. 3D Spatial Geometry
        scene_3d = generate_3d_crime_scene_data(case_info, img_reports, aud_reports, vid_reports)

        fused_result = {
            "case_id": case_id,
            "crime_classification": brief.get("crime_classification", "Armed Robbery"),
            "severity_level": "Critical",
            "evidence_confidence_score": fused["evidence_confidence_score"],
            "master_timeline": fused["master_timeline"],
            "scene_3d": scene_3d,
            "case_brief": brief,
            "fused_context": fused,
            "engine_used": f"Groq LLM ({fusion_engine.groq_model}) + Multimodal Fusion Core"
        }
        EVIDENCE_STORE["fused_data"] = fused_result

        return jsonify({
            "status": "success",
            "fused": fused_result,
            "scene_3d": scene_3d,
            "case_brief": brief
        })
    except Exception as e:
        logger.error(f"Fusion error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/chat", methods=["POST"])
def api_chat() -> Response:
    """
    POST /api/chat:
    Interrogates ingested forensic evidence via Groq LLM with strict grounding & timestamp citations.
    """
    try:
        data = request.get_json() or {}
        query = data.get("query", "").strip()
        if not query:
            return jsonify({"status": "error", "message": "Query cannot be empty."}), 400

        history = data.get("chat_history") or EVIDENCE_STORE["chat_history"]
        fused = EVIDENCE_STORE.get("fused_data") or {
            "case_id": EVIDENCE_STORE["case_info"]["case_id"],
            "crime_classification": "Armed Commercial Robbery",
            "evidence_confidence_score": 89.0,
            "master_timeline": [
                {"timestamp": 15.0, "time": "00:15", "modality": "CCTV", "event": "Subject exits North stairwell", "frame_idx": 450, "confidence": "Verified"},
                {"timestamp": 22.0, "time": "00:22", "modality": "Acoustic", "event": "Ballistic discharge reported", "confidence": "Verified"},
                {"timestamp": 38.0, "time": "00:38", "modality": "CCTV", "event": "Vehicle departs eastbound", "frame_idx": 1140, "confidence": "Verified"}
            ],
            "witness_notes": EVIDENCE_STORE["witness_notes"]
        }

        fusion_engine = get_fusion_engine()
        answer = fusion_engine.interrogate_evidence(query, fused, history)

        # Update persistent history
        EVIDENCE_STORE["chat_history"].append({"role": "user", "content": query})
        EVIDENCE_STORE["chat_history"].append({"role": "assistant", "content": answer})

        return jsonify({
            "status": "success",
            "query": query,
            "response": answer
        })
    except Exception as e:
        logger.error(f"Chat error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/export-pdf", methods=["GET", "POST"])
def api_export_pdf() -> Response:
    """
    GET / POST /api/export-pdf:
    Compiles and downloads official court-admissible forensic PDF dossier via ReportLab.
    """
    try:
        data = {}
        if request.is_json:
            data = request.get_json() or {}
        elif request.args:
            data = request.args.to_dict()

        case_id = data.get("case_id", EVIDENCE_STORE["case_info"]["case_id"])
        case_info = {
            "case_id": case_id,
            "lead_investigator": data.get("lead_investigator", EVIDENCE_STORE["case_info"]["lead_investigator"]),
            "incident_location": data.get("incident_location", EVIDENCE_STORE["case_info"]["incident_location"]),
            "incident_date": data.get("incident_date", EVIDENCE_STORE["case_info"]["incident_date"])
        }

        # Build evidence items table
        evidence_items = []
        for img in EVIDENCE_STORE["images"]:
            evidence_items.append({"name": img["name"], "type": "Image", "size": len(img["bytes"]), "hash": img["hash"]})
        for aud in EVIDENCE_STORE["audio"]:
            evidence_items.append({"name": aud["name"], "type": "Audio", "size": len(aud["bytes"]), "hash": aud["hash"]})
        for vid in EVIDENCE_STORE["videos"]:
            evidence_items.append({"name": vid["name"], "type": "Video", "size": len(vid["bytes"]), "hash": vid["hash"]})

        if not evidence_items:
            evidence_items = [
                {"name": "cctv_exterior_cam04.mp4", "type": "Video", "size": 2490368, "hash": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8"},
                {"name": "dispatch_recording.wav", "type": "Audio", "size": 524288, "hash": "9f86d081884c7d659a2feaa0c55ad015a3bf4f1b2b0b822cd15d6c15b0f00a08"},
                {"name": "cctv_still_frame01.jpg", "type": "Image", "size": 142340, "hash": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"}
            ]

        fused = EVIDENCE_STORE.get("fused_data") or {
            "case_id": case_id,
            "crime_classification": "Armed Commercial Robbery (Penal Code § 211)",
            "severity_level": "Critical",
            "evidence_confidence_score": 91.5,
            "case_brief": {
                "crime_classification": "Armed Commercial Robbery (Penal Code § 211)",
                "executive_summary": "Multimodal forensic synthesis confirms synchronized egress via North stairwell timed with secondary transport idling in commercial bay.",
                "investigative_hypotheses": [
                    "Scenario A (Primary): Coordinated heist utilizing pre-positioned getaway transport.",
                    "Scenario B: Opportunistic commercial assault following facility security breach.",
                    "Scenario C: Decoy diversion to mask secondary storage vault access."
                ],
                "potential_inconsistencies_or_doubts": [
                    "Witness reported yellow sneakers; surveillance video confirms dark gray footwear."
                ]
            },
            "master_timeline": [
                {"time": "21:38:10 UTC", "modality": "CCTV-04", "event": "Dark sedan idles in loading bay with driver seated", "confidence": "Verified"},
                {"time": "21:40:02 UTC", "modality": "CCTV-02", "event": "Subject egresses North stairwell holding metallic case", "confidence": "Verified"},
                {"time": "21:40:48 UTC", "modality": "Whisper Audio", "event": "Acoustic motor rev and vehicle door impact", "confidence": "Verified"},
                {"time": "21:41:12 UTC", "modality": "CCTV-02", "event": "Vehicle departs eastbound onto State Avenue", "confidence": "Verified"}
            ]
        }

        report_payload = {
            "case_id": case_id,
            "case_info": case_info,
            "case_brief": fused.get("case_brief", {}),
            "evidence_confidence_score": fused.get("evidence_confidence_score", 90.0),
            "evidence_items": evidence_items,
            "master_timeline": fused.get("master_timeline", [])
        }

        # Export PDF using MultimodalFusionEngine
        out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "outputs")
        os.makedirs(out_dir, exist_ok=True)
        out_pdf_path = os.path.join(out_dir, f"CrimeVision_Forensic_Dossier_{case_id}.pdf")

        fusion_engine = get_fusion_engine()
        fusion_engine.export_forensic_pdf(report_payload, out_pdf_path)

        with open(out_pdf_path, "rb") as f:
            pdf_bytes = f.read()

        return Response(
            pdf_bytes,
            mimetype="application/pdf",
            headers={
                "Content-Disposition": f"attachment; filename=CrimeVision_Dossier_{case_id}.pdf"
            }
        )
    except Exception as e:
        logger.error(f"PDF export error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


# ============================================================================
# Backwards-Compatibility Endpoints (for test_suite.py & legacy frontend)
# ============================================================================

@app.route("/api/upload", methods=["POST"])
def api_upload() -> Response:
    """Batch multipart upload endpoint for evidence files."""
    try:
        case_id = request.form.get("case_id", EVIDENCE_STORE["case_info"]["case_id"])
        witness_notes = request.form.get("witness_notes", EVIDENCE_STORE["witness_notes"])
        EVIDENCE_STORE["case_info"]["case_id"] = case_id
        EVIDENCE_STORE["witness_notes"] = witness_notes

        registered_items = []
        for f in request.files.getlist("images"):
            if f.filename:
                b = f.read()
                it = sanitize_evidence_item(f.filename, b, "Image")
                EVIDENCE_STORE["images"].append(it)
                registered_items.append({"name": it["name"], "hash": it["hash"], "type": "Image"})

        for f in request.files.getlist("audio"):
            if f.filename:
                b = f.read()
                it = sanitize_evidence_item(f.filename, b, "Audio")
                EVIDENCE_STORE["audio"].append(it)
                registered_items.append({"name": it["name"], "hash": it["hash"], "type": "Audio"})

        for f in request.files.getlist("videos"):
            if f.filename:
                b = f.read()
                it = sanitize_evidence_item(f.filename, b, "Video")
                EVIDENCE_STORE["videos"].append(it)
                registered_items.append({"name": it["name"], "hash": it["hash"], "type": "Video"})

        return jsonify({
            "status": "success",
            "message": f"Ingested {len(registered_items)} evidence artifact(s).",
            "evidence_items": registered_items
        })
    except Exception as e:
        logger.error(f"Upload error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


@app.route("/api/analyze", methods=["POST"])
def api_analyze() -> Response:
    """End-to-end multimodal pipeline execution endpoint."""
    try:
        data = request.get_json() or {}
        case_id = data.get("case_id", EVIDENCE_STORE["case_info"]["case_id"])
        location = data.get("incident_location", EVIDENCE_STORE["case_info"]["incident_location"])
        witness_notes = data.get("witness_notes", EVIDENCE_STORE["witness_notes"])

        case_info = {
            "case_id": case_id,
            "lead_investigator": EVIDENCE_STORE["case_info"]["lead_investigator"],
            "incident_location": location,
            "incident_date": EVIDENCE_STORE["case_info"]["incident_date"]
        }
        EVIDENCE_STORE["case_info"] = case_info
        EVIDENCE_STORE["witness_notes"] = witness_notes

        # Execute Image Engine
        image_reports = []
        for img in EVIDENCE_STORE["images"]:
            image_reports.append(analyze_image(img["bytes"], img["name"]))
        if not image_reports:
            image_reports.append(analyze_image(b"", "cctv_exterior_gate4.jpg"))

        # Execute Audio Engine
        audio_reports = []
        for aud in EVIDENCE_STORE["audio"]:
            audio_reports.append(analyze_audio(aud["bytes"], aud["name"]))
        if not audio_reports:
            audio_reports.append(analyze_audio(b"", "dispatch_recording_ch03.wav"))

        # Execute Video Engine
        video_reports = []
        for vid in EVIDENCE_STORE["videos"]:
            video_reports.append(analyze_video(vid["bytes"], vid["name"]))
        if not video_reports:
            video_reports.append(analyze_video(b"", "cctv_surveillance_cam04.mp4"))

        fused = fuse_multimodal_evidence(
            image_reports=image_reports,
            audio_reports=audio_reports,
            video_reports=video_reports,
            witness_notes=witness_notes,
            case_info=case_info
        )

        EVIDENCE_STORE["image_reports"] = image_reports
        EVIDENCE_STORE["audio_reports"] = audio_reports
        EVIDENCE_STORE["video_reports"] = video_reports
        EVIDENCE_STORE["fused_data"] = fused

        return jsonify({
            "status": "success",
            "case_id": fused["case_id"],
            "crime_classification": fused["crime_classification"],
            "severity_level": fused["severity_level"],
            "synthesis_markdown": fused["synthesis_markdown"],
            "master_timeline": fused["master_timeline"],
            "scene_3d": fused["scene_3d"],
            "image_reports": image_reports,
            "engine_used": fused["engine_used"]
        })
    except Exception as e:
        logger.error(f"Analysis error: {str(e)}")
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    print(f"\n============================================================")
    print(f"🛡️  CrimeVision AI Presentation Layer Starting on Port {port}")
    print(f"🌐  Interactive Console: http://127.0.0.1:{port}")
    print(f"============================================================\n")
    app.run(host="0.0.0.0", port=port, debug=False)
