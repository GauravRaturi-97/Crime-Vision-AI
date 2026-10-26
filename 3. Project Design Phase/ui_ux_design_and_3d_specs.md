# UI/UX Design & 3D Visualization Specifications

**Project:** CrimeVision AI — Intelligent Multimodal Forensic Analysis Platform  
**Author:** Gaurav Raturi | SmartBridge EL Capstone Project  
**Date:** October 2026  

---

## 1. UI/UX Aesthetic Principles

CrimeVision AI implements a **Law Enforcement Forensic Aesthetic**:
- **Background Palette:** Deep dark slate (`#070b14` and `#0f172a`), minimizing eye fatigue during prolonged investigative review.
- **Accents & Visual Hierarchy:**
  - Electric Blue (`#38bdf8`) for primary actions, timelines, and verified markers.
  - Alert Crimson (`#ef4444`) for weapons, critical severity warnings, and ballistic origins.
  - Emerald Green (`#10b981`) for corroborated evidence and integrity verification.
  - Monospace Fonts (`JetBrains Mono` / `Courier`) for SHA-256 hashes and timestamp offsets.

---

## 2. Interactive Three.js 3D Scene Specifications

### Lighting Configuration
- **Ambient Light:** Color `0x38bdf8`, intensity `0.35` (subtle cyan ambient glow).
- **Directional Light:** Position `[20, 30, 15]`, intensity `0.85`, shadow map resolution `2048x2048` with PCFSoft shadows.

### Interactive Raycasting
- Mouse clicks on the 3D canvas trigger `THREE.Raycaster`.
- When an evidence marker pin is clicked, its metadata is projected into the `#selected-marker-info` DOM container.

### Camera Presets
| Preset Name | Camera Position [X, Y, Z] | Target [X, Y, Z] | Intended Forensic View |
|---|---|---|---|
| **Overview** | `[16, 14, 18]` | `[0, 0, 0]` | Isometric full facility perspective |
| **Top-Down** | `[0, 26, 0.1]` | `[0, 0, 0]` | 2D architectural footprint overview |
| **Stairwell Egress (EV-01)** | `[-6, 4, 8]` | `[-6, 1, 4]` | Close-up of subject egress point |
| **Loading Bay (EV-03)** | `[7, 4, 2]` | `[7, 1, -3]` | Staging point and vehicle departure vector |
