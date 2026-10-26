"""
CrimeVision AI - Unit & Integration Tests: MultimodalFusionEngine
Lead Architect: Gaurav Raturi | SmartBridge EL Capstone Project
"""

import os
import sys
import unittest
import tempfile

DEV_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "5. Project Development Phase"))
if DEV_DIR not in sys.path:
    sys.path.insert(0, DEV_DIR)

from fusion_engine import (
    MultimodalFusionEngine,
    get_fusion_engine,
    fuse_multimodal_evidence,
    ask_forensic_copilot,
    generate_3d_crime_scene_data,
    extract_timeline_rows_from_text
)


class TestMultimodalFusionEngine(unittest.TestCase):

    def setUp(self):
        self.engine = get_fusion_engine()

        self.mock_image = {
            "filename": "surveillance_still.jpg",
            "weapons_detected": ["knife"],
            "people_count": 2,
            "blip_caption": "Two subjects in dark clothing in commercial corridor with knife.",
            "clarity_score": 240.0
        }
        self.mock_audio = {
            "filename": "dispatch_audio.wav",
            "transcript": "Dispatch, gunshot heard! Suspect fleeing east towards loading bay!",
            "distress_score": 0.85,
            "events": [
                {"timestamp_seconds": 15.0, "time": "00:15", "event_type": "Ballistics", "statement_excerpt": "Gunshot heard!", "speaker_sentiment": "Panicked", "credibility_tag": "High"},
                {"timestamp_seconds": 22.0, "time": "00:22", "event_type": "Suspect Flight", "statement_excerpt": "Suspect fleeing east towards loading bay!", "speaker_sentiment": "Urgent", "credibility_tag": "Corroborated"}
            ]
        }
        self.mock_video = {
            "filename": "cam02_bay.mp4",
            "fps": 30.0,
            "duration_sec": 40.0,
            "timeline": [
                {"timestamp": 2.0, "time": "00:02", "frame_idx": 60, "detected_entities": ["car"], "threat_level": "LOW", "anomaly_note": "Dark sedan idles in loading bay"},
                {"timestamp": 15.0, "time": "00:15", "frame_idx": 450, "detected_entities": ["person", "knife"], "threat_level": "HIGH", "anomaly_note": "Subject holding weapon enters stairwell"},
                {"timestamp": 38.0, "time": "00:38", "frame_idx": 1140, "detected_entities": ["person", "car"], "threat_level": "HIGH", "anomaly_note": "Subject boards sedan; vehicle departs eastbound"}
            ]
        }
        self.witness_notes = "Witness observed two males in dark hoodies. Shots heard around 00:15, fled in dark sedan."

    def test_01_fuse_evidence_chronological_timeline(self):
        """Validates cross-modal timeline alignment and strict chronological ordering."""
        fused = self.engine.fuse_evidence(
            image_data=self.mock_image,
            audio_data=self.mock_audio,
            video_data=self.mock_video,
            witness_notes=self.witness_notes,
            case_info={"case_id": "CV-TEST-FUSION"}
        )
        self.assertIn("master_timeline", fused)
        self.assertTrue(len(fused["master_timeline"]) > 0)

        # Check chronological ordering
        timestamps = [t["timestamp"] for t in fused["master_timeline"]]
        self.assertEqual(timestamps, sorted(timestamps))

        # Check Evidence Confidence Score calculation
        self.assertIn("evidence_confidence_score", fused)
        self.assertTrue(50.0 <= fused["evidence_confidence_score"] <= 98.0)

    def test_02_generate_case_brief_structure(self):
        """Validates Groq-powered statutory crime classification and 3 hypotheses."""
        fused = self.engine.fuse_evidence(
            image_data=self.mock_image,
            audio_data=self.mock_audio,
            video_data=self.mock_video,
            witness_notes=self.witness_notes
        )
        brief = self.engine.generate_case_brief(fused)

        self.assertIn("crime_classification", brief)
        self.assertIn("executive_summary", brief)
        self.assertIn("sequence_of_events", brief)
        self.assertIn("investigative_hypotheses", brief)
        self.assertIn("potential_inconsistencies_or_doubts", brief)
        self.assertEqual(len(brief["investigative_hypotheses"]), 3)

    def test_03_interrogate_evidence_grounded_copilot(self):
        """Validates grounded copilot citations to timestamps and evidence markers."""
        fused = self.engine.fuse_evidence(
            image_data=self.mock_image,
            audio_data=self.mock_audio,
            video_data=self.mock_video,
            witness_notes=self.witness_notes
        )
        answer = self.engine.interrogate_evidence("What weapon was detected and what time was the gunshot?", fused)
        self.assertIsInstance(answer, str)
        self.assertTrue(len(answer) > 40)
        self.assertTrue(any(k in answer.lower() for k in ["00:15", "t+", "15", "knife", "gunshot", "ballistic"]))

    def test_04_export_forensic_pdf(self):
        """Validates court-admissible ReportLab PDF dossier generation."""
        fused = self.engine.fuse_evidence(
            image_data=self.mock_image,
            audio_data=self.mock_audio,
            video_data=self.mock_video,
            witness_notes=self.witness_notes
        )
        brief = self.engine.generate_case_brief(fused)

        with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp_pdf:
            tmp_path = tmp_pdf.name

        try:
            report_data = {
                "case_id": "CV-TEST-FUSION",
                "case_info": {"incident_location": "Metropolitan Central", "lead_investigator": "Lead Investigator"},
                "case_brief": brief,
                "evidence_confidence_score": fused["evidence_confidence_score"],
                "master_timeline": fused["master_timeline"]
            }
            out_file = self.engine.export_forensic_pdf(report_data, tmp_path)
            self.assertTrue(os.path.exists(out_file))
            self.assertTrue(os.path.getsize(out_file) > 3000)
        finally:
            if os.path.exists(tmp_path):
                os.remove(tmp_path)

    def test_05_3d_spatial_coordinate_projection(self):
        """Validates 3D spatial markers and suspect trajectory line calculation."""
        scene = generate_3d_crime_scene_data(
            {"incident_location": "Metropolitan Sector 4"},
            [self.mock_image],
            [self.mock_audio],
            [self.mock_video]
        )
        self.assertIn("evidence_markers", scene)
        self.assertIn("suspect_path", scene)
        self.assertTrue(len(scene["evidence_markers"]) >= 3)
        self.assertTrue(len(scene["suspect_path"]) >= 4)


if __name__ == "__main__":
    unittest.main(verbosity=2)
