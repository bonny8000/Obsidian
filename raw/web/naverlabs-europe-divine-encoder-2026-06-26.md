---
source_url: (Naver Labs Europe — original URL not provided)
captured: 2026-06-26
title: "DIVINE: A Universal AI Encoder for General-Purpose Robots"
authors: [Naver Labs Europe]
published: unknown
publisher: Naver Labs Europe
---

# DIVINE: A Universal AI Encoder for General-Purpose Robots

**Capture status:** AI-written summary (not verbatim), captured 2026-06-26. Obtained from user-supplied text (a Chinese translation pasted by Bonny); the original Naver Labs Europe URL was not provided. All efficiency metrics are vendor-reported and unverified.

## Summary
Naver Labs Europe released DIVINE, a "general-purpose AI encoder" that compresses multiple specialized perception encoders into a single, smaller one so a robot's many downstream AI tasks can share one data input instead of each re-processing the same raw sensor stream. The encoder is built via multi-teacher distillation, integrating teacher models such as DUSt3R (3D spatial understanding) and multi-HMR (human pose/motion), and is designed as a general, extensible framework into which more foundation models — including language and audio — can be added as teachers. Vendor-reported results claim ~90% memory reduction and up to 12x faster processing at the encoding stage, and 62% total system memory reduction with up to 4x overall speedup. Naver Labs Europe positions this as a key enabler for onboard (vehicle/edge) robot AI and points to non-robotics domains (AR/VR, medical imaging, manufacturing, agriculture, environmental monitoring).

## Key Points
- DIVINE is framed as a turning point toward general-purpose AI integrated into robots; an "encoder" converts raw sensor input (e.g., camera) into a form AI models can process.
- Problem addressed: modern robots run many separate encoders that each re-process the same raw input (position estimation, depth/distance, human and obstacle recognition, scene understanding), inflating compute and memory.
- Core idea: compress MULTIPLE encoders into ONE smaller, lighter encoder so multiple downstream AIs share a SINGLE data input simultaneously, eliminating duplicate processing.
- Method: **multi-teacher distillation** — DIVINE learns from each specialized "teacher" model and compresses that knowledge into one encoder.
- Teacher models integrated include **DUSt3R** (3D spatial understanding) and **multi-HMR** (human pose and motion recognition).
- Not merely model reduction: it integrates the strengths of different model TYPES into one encoder, and during distillation each absorbed task can gain knowledge an individual model lacked — so DIVINE can OUTPERFORM the original standalone models on some tasks.
- Designed as a GENERAL framework: extensible to add Naver Labs Europe's own models and external models, and extensible beyond vision to multimodal (language, audio) foundation models as teachers.
- Encoding-stage efficiency (vendor-reported): memory use down ~90%, processing speed up to 12x faster vs before.
- Whole-system efficiency (vendor-reported): total memory reduced 62%, overall processing speed up to 4x faster.
- Claimed first: Naver Labs Europe says it is the first to integrate completely different tasks — semantic segmentation, 3D spatial reconstruction, human recognition — into a single encoder.
- Publication venues cited: CVPR 2025 and ECCV 2024 (top computer-vision venues).
- Application plan: roll out across various current and future Naver robots; Naver's multiple robot platforms are organically linked to AI research, an advantageous validation environment.
- Stated cross-domain applicability: AR/VR, medical imaging, manufacturing, agriculture, environmental monitoring — anywhere many AI tasks must run at once.

## Follow-up
- Locate and capture the original Naver Labs Europe English source URL to verify wording, claimed metrics, and benchmark conditions.
- Verify the CVPR 2025 / ECCV 2024 papers to confirm which tasks outperform standalone teachers and under what evaluation protocol.
- Clarify the "outperform standalone" claim: which specific tasks/metrics, and against which baseline model versions.
