"""
CrimeVision AI - Automated Comprehensive Test Suite
Author: Gaurav Raturi | SmartBridge EL Capstone Project

Validates:
1. image_engine: RT-DETR detection, BLIP captioning, OpenCV clarity, SHA-256, annotation.
2. audio_engine: Whisper transcription, timestamped segments, acoustic peaks.
3. video_engine: OpenCV motion detection, keyframes, FPS/duration.
4. fusion_engine: Groq LLM cross-modal reasoning, 3D coordinate mapping, Copilot Q&A.
5. app.py: Flask REST API endpoints (/api/health, /api/upload, /api/analyze, /api/chat, /api/scene-3d, /api/export-pdf).
"""

import os
import sys
import unittest
import numpy as np
import cv2

# Add development directory to path
DEV_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "5. Project Development Phase"))
sys.path.insert(0, DEV_DIR)

import image_engine
import audio_engine
import video_engine
import fusion_engine
import app


class TestCrimeVisionEngines(unittest.TestCase):

    def setUp(self):
        # Create synthetic test frame
        img = np.zeros((240, 320, 3), dtype=np.uint8)
        cv2.putText(img, "TEST EVIDENCE", (20, 120), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
        _, buf = cv2.imencode(".jpg", img)
        self.sample_image_bytes = buf.tobytes()

        # Synthetic audio bytes (WAV header)
        self.sample_audio_bytes = b"RIFF\x24\x00\x00\x00WAVEfmt \x10\x00\x00\x00\x01\x00\x01\x00\x44\xac\x00\x00\x88\x58\x01\x00\x02\x00\x10\x00data\x00\x00\x00\x00"

    def test_01_image_engine(self):
        """Tests image_engine analysis, SHA-256, and annotation."""
        res = image_engine.analyze_image(self.sample_image_bytes, "test_evidence.jpg")
        self.assertEqual(res["filename"], "test_evidence.jpg")
        self.assertEqual(len(res["sha256"]), 64)
        self.assertIn("clarity_score", res)
        self.assertIn("blip_caption", res)
        self.assertIn("detections", res)
        self.assertIsNotNone(res["annotated_image_base64"])
        print("  [PASS] image_engine verification completed.")

    def test_02_audio_engine(self):
        """Tests audio_engine speech transcription and acoustic peak extraction."""
        res = audio_engine.analyze_audio(self.sample_audio_bytes, "dispatch_recording.wav")
        self.assertEqual(res["filename"], "dispatch_recording.wav")
        self.assertEqual(len(res["sha256"]), 64)
        self.assertTrue(len(res["transcript"]) > 0)
        self.assertTrue(len(res["acoustic_events"]) > 0)
        self.assertTrue(0.0 <= res["distress_score"] <= 1.0)
        print("  [PASS] audio_engine verification completed.")

    def test_03_video_engine(self):
        """Tests video_engine OpenCV processing and motion detection."""
        res = video_engine.analyze_video(b"", "cctv_exterior.mp4")
        self.assertEqual(res["filename"], "cctv_exterior.mp4")
        self.assertIn("fps", res)
        self.assertTrue(len(res["timeline_events"]) > 0)
        print("  [PASS] video_engine verification completed.")

    def test_04_fusion_engine(self):
        """Tests multimodal evidence fusion and 3D coordinate generation."""
        img_rep = image_engine.analyze_image(self.sample_image_bytes, "still.jpg")
        aud_rep = audio_engine.analyze_audio(self.sample_audio_bytes, "audio.wav")
        vid_rep = video_engine.analyze_video(b"", "video.mp4")

        fused = fusion_engine.fuse_multimodal_evidence(
            image_reports=[img_rep],
            audio_reports=[aud_rep],
            video_reports=[vid_rep],
            witness_notes="Witness states suspect fled east.",
            case_info={"case_id": "CV-TEST-UNIT"}
        )
        self.assertEqual(fused["case_id"], "CV-TEST-UNIT")
        self.assertIn("crime_classification", fused)
        self.assertIn("severity_level", fused)
        self.assertTrue(len(fused["master_timeline"]) > 0)
        self.assertIn("scene_3d", fused)
        self.assertTrue(len(fused["scene_3d"]["evidence_markers"]) >= 3)
        print("  [PASS] fusion_engine cross-modal reasoning verified.")

    def test_05_investigator_copilot(self):
        """Tests natural-language investigator copilot grounding."""
        fused = {
            "case_id": "CV-TEST-UNIT",
            "crime_classification": "Armed Commercial Robbery",
            "severity_level": "Critical",
            "synthesis_markdown": "Suspect egressed via North stairwell."
        }
        answer = fusion_engine.ask_forensic_copilot(
            query="Where did the suspect egress?",
            chat_history=[],
            fused_case_data=fused,
            witness_notes="Suspect exited North stairwell."
        )
        self.assertTrue(len(answer) > 20)
        print("  [PASS] investigator_copilot chat verified.")


class TestFlaskRESTAPI(unittest.TestCase):

    def setUp(self):
        self.client = app.app.test_client()

    def test_06_index_route(self):
        """Validates dashboard rendering and Three.js container presence."""
        r = self.client.get("/")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"CrimeVision AI", r.data)
        self.assertIn(b"three-canvas", r.data)
        print("  [PASS] GET / (Dashboard with Three.js canvas) verified.")

    def test_07_health_route(self):
        """Validates /api/health endpoint and author attribution."""
        r = self.client.get("/api/health")
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertEqual(data["author"], "Gaurav Raturi")
        print("  [PASS] GET /api/health verified.")

    def test_08_scene_3d_route(self):
        """Validates /api/scene-3d returns spatial coordinates."""
        r = self.client.get("/api/scene-3d")
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertIn("scene_3d", data)
        print("  [PASS] GET /api/scene-3d spatial vector endpoint verified.")

    def test_09_analyze_route(self):
        """Validates /api/analyze executes multimodal pipeline."""
        r = self.client.post("/api/analyze", json={
            "case_id": "CV-TEST-AUTO",
            "incident_location": "Metropolitan Sector 4",
            "witness_notes": "Suspect observed fleeing east."
        })
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertEqual(data["status"], "success")
        print("  [PASS] POST /api/analyze multimodal pipeline verified.")

    def test_10_export_pdf_route(self):
        """Validates /api/export-pdf generates valid ReportLab PDF bytes."""
        r = self.client.post("/api/export-pdf", json={"case_id": "CV-TEST-AUTO"})
        self.assertEqual(r.status_code, 200)
        self.assertEqual(r.mimetype, "application/pdf")
        self.assertTrue(len(r.data) > 2000)
        print("  [PASS] POST /api/export-pdf ReportLab dossier compilation verified.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
