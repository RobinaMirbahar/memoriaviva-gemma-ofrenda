# 👻🕯️ MemoriaViva: Cute Ghost in the Machine: Open-Weights Gemma 4 & Google ADK Family Oral-History & Heirloom Recipe Weaver

[![Hacktoberfest 2026](https://img.shields.io/badge/Hacktoberfest%202026-Ghost%20in%20the%20Machine-f59e0b?style=for-the-badge&logo=github)](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)
[![Google Gemma 4](https://img.shields.io/badge/Open--Weights-Gemma%204%20(27B)-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma)
[![Google ADK](https://img.shields.io/badge/Orchestration-Google%20ADK-34A853?style=for-the-badge&logo=googlecloud&logoColor=white)](https://google.github.io/adk-docs/)
[![Sentry Agent Tracing](https://img.shields.io/badge/Observability-Sentry%20Agent%20Tracing-362D59?style=for-the-badge&logo=sentry&logoColor=white)](https://sentry.io)
[![Privacy](https://img.shields.io/badge/Privacy-100%25%20Air--Gapped%20Local-10b981?style=for-the-badge)](https://github.com/RobinaMirbahar/memoriaviva-gemma-ofrenda)

![MemoriaViva Cover](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/cover_google_ghost_style.jpg)

> **Author & Architect:** [Robina Mirbahar](https://github.com/RobinaMirbahar): Google Developer Expert (GDE) in Cloud & AI · Google Cloud Champion Innovator · Author of [*AI Engineering*](https://amazon.com/dp/B0GWCZWCF4)  
> **Challenge Track:** Hacktoberfest Open-Source AI Challenge Week 4: *Ghost in the Machine* (`#hf26challenge`, `#gemma`, `#googleai`)

---

## 🎯 Why I Built MemoriaViva

Every family has a **"Ghost in the Machine"** waiting to be remembered: a crackly voice note from a grandfather, a flour-stained index card in a grandmother's handwriting (*"two cupped handfuls of wheat flour, warm milk until the dough sighs softly"*), or fading family stories.

**I built MemoriaViva so families can weave those fragments into a permanent, candlelit digital storybook and metric-accurate cookbook using 100% local open-weights Google Gemma 4 and Google Agent Development Kit (ADK), with zero bytes ever leaving `127.0.0.1`.**

![MemoriaViva Cute Ghost in the Machine](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/arch_google_ghost_style.jpg)

---

## 🏗️ System Architecture

![MemoriaViva Scrapbook Architecture](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/arch_google_ghost_style.jpg)

```mermaid
flowchart TD
    subgraph Input ["1. Local Family Heritage Inputs (Air-Gapped 127.0.0.1)"]
        I_Voice["Elders' Voice Notes & Transcripts (EN / UR / ES)"]
        I_Recipe["Poetic Handwritten Measurements ('A Handful / Teacup / Pinch')"]
        I_Guard["verify_air_gapped_endpoint() Socket Guard (0 Cloud Bytes)"]
    end

    subgraph ADK ["2. Google ADK 3-Stage SequentialAgent + Open-Weights Gemma 4"]
        A_Stage1["Stage 1: OralHistoryWhisperAgent (Verbatim Quote & Cultural Context)"]
        A_Stage2["Stage 2: HeirloomRecipeAlchemistAgent (Poetic Phrase -> Metric g/mL)"]
        A_Stage3["Stage 3: CandlelitOfrendaCuratorAgent (50-Year HTML5 Card Builder)"]
    end

    subgraph Audit ["3. Deterministic Guardrails & Sentry Agent Tracing"]
        G_Hydration["compute_and_validate_hydration() (45%-95% Culinary Ratio Audit)"]
        G_Schema["Pydantic v2 Schema Validation (WovenHeirloomStoryCard)"]
        G_Sentry["LocalSentryTracer (18 gen_ai.agent & gen_ai.tool Spans)"]
    end

    subgraph Vault ["4. Permanent Family Archive & FastAPI Dashboard"]
        V_UI["FastAPI Candlelit Digital Ofrenda UI (GET / & POST /api/weave)"]
        V_HTML["Zero-Dependency 50-Year Static HTML5 + JSON Export"]
    end

    I_Voice --> I_Guard --> A_Stage1 --> A_Stage2 --> G_Hydration --> A_Stage3 --> G_Schema --> V_UI
    A_Stage2 --> G_Sentry
    V_UI --> V_HTML
```

---

## 🚀 Quickstart (One-Command Demo & Benchmark)

```bash
pip install -r requirements.txt
python scripts/run_memoriaviva_demo.py
```

### Launch the Interactive Candlelit Ofrenda Web App

```bash
uvicorn memoriaviva.dashboard:app --host 127.0.0.1 --port 8090
```

![MemoriaViva Candlelit UI](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/memoriaviva_ui_white.jpg)

---

## 👩‍💻 About the Author

**Robina Mirbahar**: AI Researcher, Cloud Solutions Architect & Author of [*AI Engineering*](https://amazon.com/dp/B0GWCZWCF4)

[![GitHub](https://img.shields.io/badge/GitHub-RobinaMirbahar-181717?style=flat-square&logo=github)](https://github.com/RobinaMirbahar)
[![Portfolio](https://img.shields.io/badge/Portfolio-robinamirbahar.github.io-38bdf8?style=flat-square&logo=googlechrome&logoColor=white)](https://robinamirbahar.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Robina%20Mirbahar-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/robinamirbahar)
[![GDE](https://img.shields.io/badge/Google%20Developer%20Expert-Cloud%20%26%20AI-4285F4?style=flat-square&logo=google)](https://developers.google.com/profile/u/106918534005910641104)
[![DEV.to](https://img.shields.io/badge/DEV.to-@robinamirbahar-0A0A0A?style=flat-square&logo=devdotto)](https://dev.to/robinamirbahar)
[![Medium](https://img.shields.io/badge/Medium-@robinamirbahar-12100E?style=flat-square&logo=medium)](https://medium.com/@robinamirbahar)
[![YouTube](https://img.shields.io/badge/YouTube-@robinacodesai-FF0000?style=flat-square&logo=youtube)](https://www.youtube.com/@robinacodesai)
[![Amazon Book](https://img.shields.io/badge/Amazon%20Book-AI%20Engineering-FF9900?style=flat-square&logo=amazon)](https://amazon.com/dp/B0GWCZWCF4)
