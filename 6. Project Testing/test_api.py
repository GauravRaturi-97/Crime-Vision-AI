"""
CrimeVision AI - Unit & Integration Tests: Flask Presentation Layer & REST APIs
Lead Architect: Gaurav Raturi | SmartBridge EL Capstone Project
"""

import os
import sys
import unittest

DEV_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "5. Project Development Phase"))
if DEV_DIR not in sys.path:
    sys.path.insert(0, DEV_DIR)

from app import app


class TestFlaskRESTAPIs(unittest.TestCase):

    def setUp(self):
        self.app = app
        self.app.config["TESTING"] = True
        self.client = self.app.test_client()

    def test_01_index_dashboard_route(self):
        """Validates GET / renders the interactive 5-tab console."""
        r = self.client.get("/")
        self.assertEqual(r.status_code, 200)
        self.assertIn(b"CrimeVision AI", r.data)
        self.assertIn(b"Tab 1: Evidence Ingestion", r.data)
        self.assertIn(b"Tab 2: Multimodal Master Timeline", r.data)
        self.assertIn(b"Tab 3: Interactive 3D Scene Viewer", r.data)
        self.assertIn(b"Tab 4: AI Forensic Chatbot", r.data)
        self.assertIn(b"Tab 5: Chain of Custody & PDF Export", r.data)

    def test_02_health_route(self):
        """Validates GET /api/health and author attribution."""
        r = self.client.get("/api/health")
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertEqual(data["status"], "healthy")
        self.assertEqual(data["author"], "Gaurav Raturi")

    def test_03_scene_3d_route(self):
        """Validates GET /api/scene-3d returns 3D evidence coordinates."""
        r = self.client.get("/api/scene-3d")
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertIn("scene_3d", data)
        self.assertIn("evidence_markers", data["scene_3d"])

    def test_04_analyze_image_endpoint(self):
        """Validates POST /api/analyze/image modular endpoint."""
        r = self.client.post("/api/analyze/image")
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["modality"], "image")
        self.assertIn("report", data)

    def test_05_analyze_audio_endpoint(self):
        """Validates POST /api/analyze/audio modular endpoint."""
        r = self.client.post("/api/analyze/audio")
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["modality"], "audio")
        self.assertIn("report", data)

    def test_06_analyze_video_endpoint(self):
        """Validates POST /api/analyze/video modular endpoint."""
        r = self.client.post("/api/analyze/video")
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertEqual(data["status"], "success")
        self.assertEqual(data["modality"], "video")
        self.assertIn("report", data)

    def test_07_fuse_endpoint(self):
        """Validates POST /api/fuse master alignment endpoint."""
        r = self.client.post("/api/fuse", json={"case_id": "CV-TEST-API"})
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertEqual(data["status"], "success")
        self.assertIn("fused", data)
        self.assertIn("master_timeline", data["fused"])

    def test_08_chat_endpoint(self):
        """Validates POST /api/chat copilot interrogation endpoint."""
        r = self.client.post("/api/chat", json={"query": "What weapon was identified?"})
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertEqual(data["status"], "success")
        self.assertIn("response", data)

    def test_09_export_pdf_get_and_post(self):
        """Validates GET and POST /api/export-pdf generates valid PDF bytes."""
        # GET
        r_get = self.client.get("/api/export-pdf")
        self.assertEqual(r_get.status_code, 200)
        self.assertEqual(r_get.mimetype, "application/pdf")
        self.assertTrue(len(r_get.data) > 3000)

        # POST
        r_post = self.client.post("/api/export-pdf", json={"case_id": "CV-TEST-PDF"})
        self.assertEqual(r_post.status_code, 200)
        self.assertEqual(r_post.mimetype, "application/pdf")
        self.assertTrue(len(r_post.data) > 3000)

    def test_10_end_to_end_analyze_pipeline(self):
        """Validates POST /api/analyze end-to-end execution pipeline."""
        r = self.client.post("/api/analyze", json={
            "case_id": "CV-TEST-AUTO",
            "incident_location": "Sector 4",
            "witness_notes": "Suspect fled in dark sedan."
        })
        self.assertEqual(r.status_code, 200)
        data = r.get_json()
        self.assertEqual(data["status"], "success")
        self.assertIn("crime_classification", data)


if __name__ == "__main__":
    unittest.main(verbosity=2)
