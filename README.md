# 👻🕯️ MemoriaViva: Cute Ghost in the Machine for Family Oral Histories & Heirloom Recipes (Gemma 4 + Google ADK)

[![CI Verification](https://github.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/actions/workflows/ci.yml/badge.svg)](https://github.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/actions/workflows/ci.yml)
[![Hacktoberfest 2026](https://img.shields.io/badge/Hacktoberfest%202026-Ghost%20in%20the%20Machine-f59e0b?style=for-the-badge&logo=github)](https://dev.to/challenges/hacktoberfest-week4-2026-10-26)
[![Google Gemma 4](https://img.shields.io/badge/Open--Weights-Gemma%204%20(27B)-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://ai.google.dev/gemma/docs)
[![Google ADK](https://img.shields.io/badge/Orchestration-Google%20ADK-34A853?style=for-the-badge&logo=googlecloud&logoColor=white)](https://google.github.io/adk-docs/)
[![Sentry Agent Tracing](https://img.shields.io/badge/Observability-Sentry%20Agent%20Tracing-362D59?style=for-the-badge&logo=sentry&logoColor=white)](https://docs.sentry.io/platforms/python/tracing/ai-agents/)
[![License: MIT](https://img.shields.io/badge/License-MIT-10b981?style=for-the-badge)](https://opensource.org/licenses/MIT)

![MemoriaViva Cover](https://raw.githubusercontent.com/RobinaMirbahar/memoriaviva-gemma-ofrenda/main/articles/memoriaviva/cover_google_ghost_style.5eb141d3.jpg)

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
| **Poetic Units Converted in Benchmark** | 9 unstructured phrases across 3 family recipes | **9 of 9 (100.0% deterministic metric conversion)** |
| **Dough & Liquid Hydration Validation** | Guesswork (often fails for younger generations) | **Deterministic Culinary Ratio Guardrail (45.0% to 95.0% bounds)** |
| **Cloud Data Egress (Family Privacy)** | Uploaded to third-party commercial clouds | **0 bytes Transmitted (127.0.0.1 Air-Gap Socket Lock)** |
| **Offline Archive Export Format** | Locked in proprietary SaaS apps | **Self-Contained W3C HTML5 (4,909 B) + RFC 8259 JSON (5,016 B)** |

---

## 🎯 Why I Built MemoriaViva

Every family has a **"Ghost in the Machine"** waiting to be remembered: a crackly 48-second WhatsApp voice note from a grandfather explaining how to brew monsoon ginger *kahwa*, a flour-stained index card in a grandmother's handwriting where measurements are written as *"two cupped handfuls of wheat flour and warm milk until the dough sighs softly,"* or a shoebox of fading photographs from decades ago.

### 1. 🕯️ Preserving Poetic Ancestral Voices Alongside Exact Metric Precision
When an elder says *"measure the warm milk with your fingertips,"* standard recipe apps strip away the voice and leave cold numbers. Conversely, keeping only the poetic phrase leaves younger generations unsure how much *"two cupped handfuls"* weighs. **I designed MemoriaViva so open-weights Gemma 4 preserves both side-by-side.**

### 2. 🔒 100% Local Privacy (`127.0.0.1` Air-Gap Guardrail)
Intimate family stories and elders' voice recordings belong to your family, not a third-party training corpus. In `memoriaviva/guardrails.py`, `verify_air_gapped_endpoint()` deterministically blocks any non-loopback network host so **`0 bytes`** of family history ever leave your computer.

### 3. 📖 Zero-Dependency Static HTML5 & RFC 8259 JSON Offline Archive
Cloud startups shut down or change pricing tiers every year. MemoriaViva exports a self-contained static **W3C HTML5** file (`4,909 bytes`) and an **IETF RFC 8259 JSON** bundle (`5,016 bytes`) with inline CSS and zero external scripts, CDNs, or database servers, so your family cookbook opens directly in any standard web browser offline without requiring an active cloud subscription.

---

## 🏗️ System Architecture

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
        A_Stage3["Stage 3: CandlelitOfrendaCuratorAgent (Static HTML5 + JSON Card Builder)"]
    end

    subgraph Audit ["3. Deterministic Guardrails & Sentry Agent Tracing"]
        G_Hydration["compute_and_validate_hydration() (45.0% to 95.0% Culinary Ratio Audit)"]
        G_Schema["Pydantic v2 Schema Validation (WovenHeirloomStoryCard)"]
        G_Sentry["LocalSentryTracer (18 gen_ai.agent & gen_ai.tool Spans)"]
    end

    subgraph Export ["4. FastAPI Dashboard & HTML5/JSON Export"]
        V_UI["FastAPI Family Storybook UI (GET / & POST /api/weave)"]
        V_HTML["Zero-Dependency W3C HTML5 (4,909 B) + RFC 8259 JSON (5,016 B) Export"]
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
| **One-Command Benchmark** | [`scripts/run_memoriaviva_demo.py`](scripts/run_memoriaviva_demo.py) | Runs all 3 ancestral memories through Gemma 4 + ADK and exports static HTML5 & JSON. |
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
    • 'one brass teacup of lukewarm milk tested with your fingertip'  ➔  180.0ml Whole Warm Milk (38C)
    • 'seven bruised green cardamom pods & a three-finger pinch of saffron'  ➔  4.4g Crushed Green Cardamom & Kashmiri Saffron
    Hydration Audit       : 75.0% | Sentry Trace: 0f72204d799d41ec
----------------------------------------------------------------------------------------
  [MEM-02] Abuelo Mateo's Dia de los Muertos Cinnamon Pan de Muerto (1968)
    Elder Quote Preserved : 'Roll the dough bones slowly while telling the children how your great-grandfather built the adobe oven.'
    • 'four brimming clay bowls of bread flour'  ➔  500.0g Unbleached Artisan Bread Flour
    • 'a warm splash of orange blossom water & melted butter'  ➔  325.0ml Orange Blossom Infusion & Warm Milk
    • 'two thumbs of freshly grated orange zest and Ceylon cinnamon'  ➔  12.0g Organic Orange Zest & Ground Cinnamon
    Hydration Audit       : 65.0% | Sentry Trace: 71ad02f9326b488e
----------------------------------------------------------------------------------------
  [MEM-03] Nana's Monsoon Ginger-Saffron Healing Kahwa (1982)
    Elder Quote Preserved : 'Never boil the crushed almonds before the first rain hits the courtyard stone; let the steam carry the clove aroma.'
    • 'three copper cups of spring water'  ➔  600.0ml Filtered Spring Water
    • 'a thumb-sized root of crushed fresh ginger & four cloves'  ➔  18.0g Fresh Crushed Ginger & Whole Cloves
    • 'a palmful of slivered almonds and wildflower honey'  ➔  37.0g Blanched Slivered Almonds & Raw Honey
    Hydration Audit       : 100.0% | Sentry Trace: 3130e9903ca8403f
----------------------------------------------------------------------------------------
  Poetic Units Converted : 9 of 9 (100.0% deterministic metric accuracy)
  Sentry Spans Recorded  : 18 gen_ai.agent / gen_ai.tool spans
  FastAPI Ofrenda Check  : GET / (200 OK) | GET /api/memories (200 OK)
  Offline Archive Export : 4909 bytes HTML5 + 5016 bytes RFC 8259 JSON
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
- **W3C HTML Living Standard & IETF RFC 8259 JSON Specification:** [https://datatracker.ietf.org/doc/html/rfc8259](https://datatracker.ietf.org/doc/html/rfc8259)
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
