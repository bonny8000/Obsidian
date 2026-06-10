---
type: playbook
status: active
created: 2026-06-01
updated: 2026-06-01
tags: [playbook, prompt, persona, synthetic-data]
---

# Playbook: Sovereign AI Persona Generation

## Purpose
This playbook is used to generate highly realistic, statistically grounded synthetic user personas for specific regions (USA, Japan, Korea) to avoid the "average user" bias (model collapse) typical of generic LLM outputs. It uses the NVIDIA Nemotron-Personas methodology.

## Target Audience / Role
- **UX Researchers:** For generating diverse, edge-case user testing scripts or synthetic interview transcripts.
- **Product Managers:** For validating product roadmaps against the *actual* demographic shape of a target market.

## The Prompt / Template
```markdown
You are an expert synthetic data generator following the "Grounded Synthetic Personas" methodology. 

Your task is to generate {NUMBER} realistic personas for the {COUNTRY} market. 

CRITICAL CONSTRAINTS:
1. **DO NOT** generate a "typical" or "average" user (e.g., do not default to a 30-year-old tech worker in a capital city). 
2. Ground your generation in the actual demographic realities of {COUNTRY}:
   - For Japan/Korea: Over-index on older age brackets (50-80s) to reflect the aging population. Include rural/agricultural occupations. Reflect the rise in single-person households.
   - For USA: Reflect diverse educational attainment by geography and ethnic diversity.
3. Each persona must be multidimensional and not a caricature.

OUTPUT FORMAT:
For each persona, provide:
- **Name:** (Culturally accurate, including generational naming trends)
- **Demographics:** Age, Sex, Marital Status, Education, Occupation, Geographic Region
- **Professional Persona:** (Their approach to work, skills, and career goals)
- **Cultural/Family Background:** (Values instilled by their upbringing)
- **Hobbies & Interests:** (Specific, localized activities, e.g., "visiting local Onsen" or "attending Hanwha Eagles games")
- **Culinary Persona:** (Specific dietary habits and cooking preferences)
- **Psychological Nuance:** (A brief note on their internal anxieties, stress factors, or hidden competitive streaks)
```

## How to Use
1. Copy the prompt block.
2. Replace `{NUMBER}` with the desired number of personas (e.g., 5).
3. Replace `{COUNTRY}` with the target market (e.g., South Korea).
4. Run the prompt in your LLM of choice.
5. Use the output to populate your Figma designs or as "synthetic interviewees" for your UXR questions.

## Linked Theory
- Grounds in: [[concepts/ux-research/grounded-synthetic-personas|Grounded Synthetic Personas]]
- Grounds in: [[concepts/infrastructure-dev/sovereign-ai|Sovereign AI]]
- Supported by: [[sources/nvidia-nemotron-personas|NVIDIA Nemotron-Personas Datasets]]
