"""
CrimeVision AI - Unit & Integration Tests: AudioForensicEngine
Lead Architect: Gaurav Raturi | SmartBridge EL Capstone Project
"""

import os
import sys
import unittest

DEV_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "5. Project Development Phase"))
if DEV_DIR not in sys.path:
    sys.path.insert(0, DEV_DIR)

from audio_engine import (
    AudioForensicEngine,
    get_audio_engine,
    analyze_audio,
    compute_sha256,
    generate_mock_wav_bytes
)


class TestAudioForensicEngine(unittest.TestCase):

    def setUp(self):
        self.engine = get_audio_engine()
        self.mock_wav_bytes = generate_mock_wav_bytes(duration_sec=1.0, sample_rate=16000)

    def test_01_engine_initialization(self):
        """Validates AudioForensicEngine initializes with Whisper base model."""
        self.assertIsNotNone(self.engine)
        self.assertEqual(self.engine.model_size, "base")
        self.assertIn(self.engine.device, ["cpu", "cuda"])

    def test_02_sha256_cryptographic_hash(self):
        """Validates audio stream digital fingerprinting."""
        sha = compute_sha256(self.mock_wav_bytes)
        self.assertEqual(len(sha), 64)
        self.assertEqual(sha, compute_sha256(self.mock_wav_bytes))

    def test_03_transcribe_audio(self):
        """Validates multilingual speech transcription and segment intervals."""
        res = self.engine.transcribe_audio(self.mock_wav_bytes)
        self.assertIn("full_transcript", res)
        self.assertIn("language", res)
        self.assertIn("segments", res)
        self.assertIsInstance(res["segments"], list)
        self.assertTrue(len(res["full_transcript"]) > 0)

    def test_04_extract_audio_events_keywords(self):
        """Validates extraction of high-urgency acoustic and testimony events."""
        test_segments = [
            {"id": 0, "start": 3.0, "end": 5.5, "text": "Red car speeding away from transit bay!"},
            {"id": 1, "start": 8.0, "end": 11.0, "text": "Gunshot fired! Help, suspect ran away!"}
        ]
        events = self.engine.extract_audio_events(test_segments, groq_client=None)
        self.assertIsInstance(events, list)
        self.assertTrue(len(events) >= 2)
        for ev in events:
            self.assertIn("timestamp_seconds", ev)
            self.assertIn("event_type", ev)
            self.assertIn("statement_excerpt", ev)
            self.assertIn("speaker_sentiment", ev)
            self.assertIn("credibility_tag", ev)

    def test_05_end_to_end_analyze_backwards_compatible(self):
        """Validates analyze_audio API integration and distress scoring."""
        res = analyze_audio(self.mock_wav_bytes, "test_dispatch.wav")
        self.assertEqual(res["filename"], "test_dispatch.wav")
        self.assertEqual(len(res["sha256"]), 64)
        self.assertTrue(len(res["transcript"]) > 0)
        self.assertIn("acoustic_events", res)
        self.assertTrue(len(res["acoustic_events"]) > 0)
        self.assertTrue(0.0 <= res["distress_score"] <= 1.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
