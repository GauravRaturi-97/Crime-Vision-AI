"""
CrimeVision AI - Unit & Integration Tests: ImageForensicEngine
Lead Architect: Gaurav Raturi | SmartBridge EL Capstone Project
"""

import os
import sys
import unittest
import numpy as np
import cv2

# Ensure access to Project Development Phase modules
DEV_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "5. Project Development Phase"))
if DEV_DIR not in sys.path:
    sys.path.insert(0, DEV_DIR)

from image_engine import (
    ImageForensicEngine,
    get_image_engine,
    analyze_image,
    compute_sha256,
    compute_forensic_clarity
)


class TestImageForensicEngine(unittest.TestCase):

    def setUp(self):
        self.engine = get_image_engine()

        # Create a synthetic forensic test image
        self.synthetic_img = np.zeros((480, 640, 3), dtype=np.uint8)
        cv2.putText(self.synthetic_img, "SURVEILLANCE CAM-04 (SECTOR 4)", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.rectangle(self.synthetic_img, (180, 120), (320, 420), (200, 200, 200), -1)  # Subject
        cv2.circle(self.synthetic_img, (250, 170), 30, (180, 150, 120), -1)
        cv2.rectangle(self.synthetic_img, (310, 240), (370, 340), (50, 50, 200), -1)   # Backpack

        _, buf = cv2.imencode(".jpg", self.synthetic_img)
        self.sample_bytes = buf.tobytes()

    def test_01_engine_initialization(self):
        """Validates ImageForensicEngine initializes with correct device and detector."""
        self.assertIsNotNone(self.engine)
        self.assertIn(self.engine.device, ["cpu", "cuda"])
        self.assertIsNotNone(self.engine._detector_type)

    def test_02_sha256_cryptographic_hash(self):
        """Validates SHA-256 digital fingerprint generation for chain of custody."""
        sha = compute_sha256(self.sample_bytes)
        self.assertEqual(len(sha), 64)
        self.assertEqual(sha, compute_sha256(self.sample_bytes))

    def test_03_forensic_clarity_laplacian(self):
        """Validates OpenCV Laplacian blur variance and clarity status."""
        clarity = compute_forensic_clarity(self.synthetic_img)
        self.assertIn("blur_score", clarity)
        self.assertIn("clarity_status", clarity)
        self.assertTrue(clarity["blur_score"] >= 0.0)

    def test_04_detect_objects(self):
        """Validates RT-DETR object detection and structured metadata."""
        detections = self.engine.detect_objects(self.synthetic_img)
        self.assertIsInstance(detections, list)
        for d in detections:
            self.assertIn("box", d)
            self.assertIn("label", d)
            self.assertIn("confidence", d)
            self.assertIn("timestamp", d)
            self.assertTrue(0.0 <= d["confidence"] <= 1.0)

    def test_05_generate_caption_blip(self):
        """Validates Salesforce BLIP natural language scene captioning."""
        caption = self.engine.generate_caption(self.synthetic_img)
        self.assertIsInstance(caption, str)
        self.assertTrue(len(caption) > 0)

    def test_06_generate_visual_hypotheses(self):
        """Validates investigative scenario hypotheses synthesis."""
        detections = self.engine.detect_objects(self.synthetic_img)
        hypotheses = self.engine.generate_visual_hypotheses(self.synthetic_img, detections)
        self.assertIsInstance(hypotheses, list)
        self.assertTrue(len(hypotheses) >= 2)

    def test_07_annotate_image(self):
        """Validates bounding box annotation rendering and output."""
        detections = self.engine.detect_objects(self.synthetic_img)
        annotated = self.engine.annotate_image(self.synthetic_img, detections)
        self.assertIsInstance(annotated, np.ndarray)
        self.assertEqual(annotated.shape, self.synthetic_img.shape)

    def test_08_end_to_end_analyze_backwards_compatible(self):
        """Validates top-level analyze_image API for app.py compatibility."""
        rep = analyze_image(self.sample_bytes, "test_scene.jpg")
        self.assertEqual(rep["filename"], "test_scene.jpg")
        self.assertEqual(len(rep["sha256"]), 64)
        self.assertIn("clarity_score", rep)
        self.assertIn("blip_caption", rep)
        self.assertIn("detections", rep)
        self.assertIn("weapons_detected", rep)
        self.assertIn("people_count", rep)
        self.assertIn("annotated_image_base64", rep)


if __name__ == "__main__":
    unittest.main(verbosity=2)
