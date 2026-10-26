# Mock Case Study: Case CV-2026-0891

**Case Name:** State v. John Doe (In Re: Metropolitan Transit Terminal Armed Robbery)  
**Lead Investigator:** Det. Sarah Jenkins (Badge #4412)  
**Incident Location:** Metropolitan Transit Terminal, Sector 4  
**Incident Timestamp:** October 18, 2026 at 21:40:00 UTC  
**Primary Offense:** Armed Commercial Robbery & Criminal Conspiracy (Penal Code § 211)  
**Author:** Gaurav Raturi | SmartBridge EL Capstone Project  

---

## 1. Incident Scenario

At 21:38 UTC, a dark 4-door sedan arrived at the commercial loading bay of the Metropolitan Transit Terminal, idling with parking lights on. At 21:40 UTC, an individual wearing a dark hooded jacket and sweatpants exited hurriedly through the secondary North stairwell carrying a silver metallic briefcase.

A dispatch transmission logged an acoustic concussive sound and verbal reports of suspect egress. A witness (Terminal Security Guard) interviewed immediately after the incident gave contradictory testimony regarding suspect footwear.

---

## 2. Evidence Register

| Artifact ID | Modality | File Name | Observations & Findings |
|---|---|---|---|
| **EV-01** | Imagery (CCTV Still) | `cctv_exterior_gate4.jpg` | RT-DETR localized Subject 01 and silver briefcase. BLIP generated scene hypothesis. Clarity confirmed high (Laplacian: 168.4). |
| **EV-02** | Audio Recording | `dispatch_recording_ch03.wav` | Whisper transcribed caller alert. Acoustic transient detected at 00:14 (Ballistics/Impact). Distress index: 0.80/1.0. |
| **EV-03** | Video Footage | `cctv_surveillance_cam04.mp4` | OpenCV frame difference logged motion surge at 00:15. Egress vector towards waiting dark sedan in bay. |
| **EV-04** | Witness Testimony | `witness_statement_guard.txt` | Claimed yellow sneakers; CCTV analysis established dark gray athletic shoes (**Contradiction flagged**). |

---

## 3. Forensic Discrepancy Matrix

```
+-----------------------------------------------------------------------------------------+
| Assertion                      | Hard Media Verification           | Finding            |
|--------------------------------|-----------------------------------|--------------------|
| Egress via North Stairwell     | CCTV-04 motion surge at 21:40:02  | CORROBORATED       |
| Metallic Briefcase in Hand     | RT-DETR visual detection bounding | CORROBORATED       |
| Yellow Sneaker Footwear        | CCTV-02 video frame inspection    | CONTRADICTION      |
| Firearm Inside Briefcase       | Exterior optics obstructed        | UNVERIFIED         |
+-----------------------------------------------------------------------------------------+
```
