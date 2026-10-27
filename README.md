# 👻🕯️ MemoriaViva: Cute Ghost in the Machine for Family Oral Histories & Heirloom Recipes (Gemma 4 + Google ADK)

[![CI Verification](https://github.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/actions/workflows/ci.yml/badge.svg)](https://github.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/actions/workflows/ci.yml)
[![Hacktoberfest 2026](https://img.shields.io/badge/Hacktoberfest%202026-Ghost%20in%20the%20Machine-f59e0b?style=for-the-badge&logo=github)](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)
[![Google Gemma 4](https://img.shields.io/badge/Open--Weights-Gemma%204%20(27B)-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma/docs)
[![Google ADK](https://img.shields.io/badge/Orchestration-Google%20ADK-34A853?style=for-the-badge&logo=googlecloud&logoColor=white)](https://google.github.io/adk-docs/)
[![Sentry Agent Tracing](https://img.shields.io/badge/Observability-Sentry%20Agent%20Tracing-362D59?style=for-the-badge&logo=sentry&logoColor=white)](https://docs.sentry.io/platforms/python/tracing/ai-agents/)
[![License: MIT](https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge)](https://opensource.org/licenses/MIT)

![MemoriaViva Cover](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/cover_google_ghost_style.jpg)

> **Author & Architect:** [Robina Mirbahar](https://github.com/RobinaMirbahar) (Google Developer Expert in Cloud & AI · Google Cloud Champion Innovator · Author of [*AI Engineering*](https://amazon.com/dp/B0GWCZWCF4))  
> **Challenge Track:** Hacktoberfest Open-Source AI Challenge Week 4: *Ghost in the Machine* (`#hf26challenge`, `#gemma`, `#googleai`)  
> **Core Stack:** Open-Weights **Google Gemma 4** (`google/gemma-4-27b-it`), **Google Agent Development Kit (ADK)**, **Google AI Studio**, **FastAPI**, **Pydantic v2**, and **Sentry Agent Tracing**.

---

## 📊 Live Architecture Telemetry & Benchmark Highlights

<p align="center">
  <img src="https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/assets/card_gemma.svg" alt="Gemma 4 Engine" width="23%" />
  <img src="https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/assets/card_adk.svg" alt="Google ADK Pipeline" width="23%" />
  <img src="https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/assets/card_privacy.svg" alt="Air-Gapped Privacy" width="23%" />
  <img src="https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/assets/card_sentry.svg" alt="Sentry Agent Tracing" width="23%" />
</p>

| Heritage Archival Metric | Raw Family Voice Notes & Index Cards | MemoriaViva (Gemma 4 + Google ADK) |
| :--- | :--- | :--- |
| **Ancestral Measurement Format** | Ambiguous (*"a handful," "a teacup," "until soft"*) | Dual-Format: Verbatim Poetic Phrase + Exact Metric (`g` / `ml`) |
| **Poetic Units Converted in Benchmark** | 9 unstructured phrases across 3 family recipes | **9/9 (100.0% deterministic metric conversion)** |
| **Dough & Liquid Hydration Validation** | Guesswork (often fails for younger generations) | **Deterministic Culinary Ratio Guardrail (`45% to 95%` validated)** |
| **Cloud Data Egress (Family Privacy)** | Uploaded to third-party commercial clouds | **0 Bytes Transmitted (`127.0.0.1` Air-Gap Socket Lock)** |
| **Archival Lifespan** | Locked in proprietary SaaS apps | **50-Year Self-Contained Static HTML5 + JSON Vault** |

---

## 🎯 Why I Built MemoriaViva

Every family has a **"Ghost in the Machine"** waiting to be remembered: a crackly 48-second WhatsApp voice note from a grandfather explaining how to brew monsoon ginger *kahwa*, a flour-stained index card in a grandmother's handwriting where measurements are written as *"two cupped handfuls of wheat flour and warm milk until the dough sighs softly,"* or a shoebox of fading photographs from decades ago.

### 1. 🕯️ Preserving Poetic Ancestral Voices Alongside Exact Metric Precision
When an elder says *"measure the warm milk with your fingertips,"* standard recipe apps strip away the voice and leave cold numbers. Conversely, keeping only the poetic phrase leaves younger generations unsure how much *"two cupped handfuls"* weighs. **I designed MemoriaViva so open-weights Gemma 4 preserves both side-by-side.**

### 2. 🔒 100% Local Privacy (`127.0.0.1` Air-Gap Guardrail)
Intimate family stories and elders' voice recordings belong to your family, not a third-party training corpus. In `memoriaviva/guardrails.py`, `verify_air_gapped_endpoint()` deterministically blocks any non-loopback network host so **0 bytes** of family history ever leave your computer.

### 3. 📖 50-Year Zero-Dependency Family Archive
Cloud startups shut down or change pricing tiers every year. MemoriaViva exports a self-contained static HTML5 and JSON family storybook that opens in any web browser 50 years from now without requiring an active cloud subscription.

---

## 🏗️ System Architecture

![MemoriaViva 3-Step Scrapbook Workflow](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/arch_google_ghost_style.jpg)

![MemoriaViva Technical Architecture on White Background](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/memoriaviva_arch_white_v2.jpg)

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
        G_Hydration["compute_and_validate_hydration() (45% to 95% Culinary Ratio Audit)"]
        G_Schema["Pydantic v2 Schema Validation (WovenHeirloomStoryCard)"]
        G_Sentry["LocalSentryTracer (18 gen_ai.agent & gen_ai.tool Spans)"]
    end

    subgraph Vault ["4. Permanent Family Archive & FastAPI Dashboard"]
        V_UI["FastAPI Family Storybook UI (GET / & POST /api/weave)"]
        V_HTML["Zero-Dependency 50-Year Static HTML5 + JSON Export"]
    end

    I_Voice --> I_Guard --> A_Stage1 --> A_Stage2 --> G_Hydration --> A_Stage3 --> G_Schema --> V_UI
    A_Stage2 --> G_Sentry
    V_UI --> V_HTML
```

### 🧩 Architectural Subsystem Index

| Subsystem | File Location | Engineering Responsibility |
| :--- | :--- | :--- |
| **Pydantic v2 Contracts** | [`memoriaviva/schemas.py`](memoriaviva/schemas.py) | Enforces strict typing for `RawFamilyMemory`, `StandardizedIngredient`, and `WovenHeirloomStoryCard`. |
| **Privacy & Culinary Guardrails** | [`memoriaviva/guardrails.py`](memoriaviva/guardrails.py) | Implements `verify_air_gapped_endpoint()` (`127.0.0.1` lock) and `compute_and_validate_hydration()`. |
| **Gemma 4 + ADK Pipeline** | [`memoriaviva/agents.py`](memoriaviva/agents.py) | Orchestrates the 3-stage `SequentialAgent` workflow and records `LocalSentryTracer` spans. |
| **Family Storybook UI** | [`memoriaviva/dashboard.py`](memoriaviva/dashboard.py) | Serves the FastAPI Storybook UI (`GET /`, `GET /api/memories`, `POST /api/weave`). |
| **One-Command Benchmark** | [`scripts/run_memoriaviva_demo.py`](scripts/run_memoriaviva_demo.py) | Runs all 3 ancestral memories through Gemma 4 + ADK and verifies FastAPI endpoints. |
| **Automated Unit Tests** | [`tests/test_memoriaviva.py`](tests/test_memoriaviva.py) | Verifies air-gap socket blocking, metric unit standardization, and hydration bounds. |

---

## 🖥️ Interactive Family Storybook UI Preview

![MemoriaViva White-Background Storybook UI](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/memoriaviva_ui_white.jpg)

---

## 🚀 Quickstart (One-Command Demo & Benchmark)

```bash
git clone https://github.com/RobinaMirbahar/memoriaviva-gemma-ofrenda.git
cd memoriaviva-gemma-ofrenda
pip install -r requirements.txt
python scripts/run_memoriaviva_demo.py
```

### Sample Benchmark Output

```text
========================================================================================
👻🕯️ MEMORIAVIVA: CUTE GHOST IN THE MACHINE (GEMMA 4 + ADK + SENTRY TRACING)
========================================================================================
  Model                  : google/gemma-4-27b-it (100% Local Ollama / vLLM)
  Air-Gapped Endpoint    : http://127.0.0.1:11434 (0 Cloud Egress Verified)
  Family Memories Loaded : 3 ancestral voice & recipe records
----------------------------------------------------------------------------------------
  [MEM-01] Dadi Jan's Partition-Era Cardamom & Saffron Sweet Bread (1947)
    Elder Quote Preserved : 'Measure the warm milk with your fingertips; when the dough sighs softly, the cardamom is awake.'
    • 'two generous cupped handfuls of stone-ground wheat flour'  ➔  240.0g Stone-Ground Whole Wheat Flour (Atta)
    • 'one brass teacup of lukewarm milk tested with your fingertip'  ➔  180.0ml Whole Warm Milk (38°C)
    • 'seven bruised green cardamom pods & a three-finger pinch of saffron'  ➔  4.4g Crushed Green Cardamom & Kashmiri Saffron
    Hydration Audit       : 75.0% | Sentry Trace: db4de60c9e774e83 | 142.9 ms
----------------------------------------------------------------------------------------
  Poetic Units Converted : 9/9 (100.0% deterministic metric accuracy)
  Sentry Spans Recorded  : 18 gen_ai.agent / gen_ai.tool spans
  FastAPI Ofrenda Check  : GET / (200 OK) | GET /api/memories (200 OK)
  Cloud Bytes Transmitted: 0 bytes (100% Local Family Privacy Preserved)
========================================================================================
```

### Launch the Interactive Storybook Web Server

```bash
uvicorn memoriaviva.dashboard:app --host 127.0.0.1 --port 8090
```

---

## 📚 Official Documentation & References

- **Google Gemma Open-Weights Models Documentation:** [https://ai.google.dev/gemma/docs](https://ai.google.dev/gemma/docs)
- **Google Agent Development Kit (ADK) Documentation (`SequentialAgent`):** [https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/](https://google.github.io/adk-docs/agents/workflow-agents/sequential-agents/)
- **Google GenAI SDK (`google-genai`) Official Docs:** [https://googleapis.github.io/python-genai/](https://googleapis.github.io/python-genai/)
- **Google AI Studio (Structured Outputs & Prompt Prototyping):** [https://ai.google.dev/gemini-api/docs/structured-output](https://ai.google.dev/gemini-api/docs/structured-output)
- **Google Cloud Run Documentation:** [https://cloud.google.com/run/docs](https://cloud.google.com/run/docs)
- **Sentry AI Agent Tracing & OpenTelemetry Semantic Conventions:** [https://docs.sentry.io/platforms/python/tracing/ai-agents/](https://docs.sentry.io/platforms/python/tracing/ai-agents/)

---

## 👩‍💻 About the Author

**Robina Mirbahar**  
AI Researcher · Cloud Solutions Architect · Author of [*AI Engineering*](https://amazon.com/dp/B0GWCZWCF4)

[![GitHub](https://img.shields.io/badge/GitHub-RobinaMirbahar-181717?style=flat-square&logo=github)](https://github.com/RobinaMirbahar)
[![Portfolio](https://img.shields.io/badge/Portfolio-robinamirbahar.github.io-38bdf8?style=flat-square&logo=googlechrome&logoColor=white)](https://robinamirbahar.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Robina%20Mirbahar-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/robinamirbahar)
[![GDE](https://img.shields.io/badge/Google%20Developer%20Expert-Cloud%20%26%20AI-4285F4?style=flat-square&logo=google)](https://developers.google.com/profile/u/106918534005910641104)
[![DEV.to](https://img.shields.io/badge/DEV.to-@robinamirbahar-0A0A0A?style=flat-square&logo=devdotto)](https://dev.to/robinamirbahar)
[![Medium](https://img.shields.io/badge/Medium-@robinamirbahar-12100E?style=flat-square&logo=medium)](https://medium.com/@robinamirbahar)
[![YouTube](https://img.shields.io/badge/YouTube-@robinacodesai-FF0000?style=flat-square&logo=youtube)](https://www.youtube.com/@robinacodesai)
[![Amazon Book](https://img.shields.io/badge/Amazon%20Book-AI%20Engineering-FF9900?style=flat-square&logo=amazon)](https://amazon.com/dp/B0GWCZWCF4)
