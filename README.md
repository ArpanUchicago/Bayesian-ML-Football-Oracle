# Live-Style Soccer Commentary Using Open-Source LLMs

![Match Stadium](https://github.com/ArpanUchicago/Bayesian-ML-Football-Oracle/blob/7e8bb8475be1ea2f545601a9f8de083ba8adfb1f/Stadium.webp?raw=true)
Image : Medium blog

**University of Chicago – MS in Applied Data Science**

**Course:** Bayesian Machine Learning with Generative AI Applications
**Date:** 05/23/2025

### Contributors:

* Arpan Pradhan
* Matthew Schaefer
*  Shane Kim

---

## 1. Introduction


![Match LLM](https://github.com/ArpanUchicago/Bayesian-ML-Football-Oracle/blob/d9cd93fbc863690588acdaec87016a43dc69c23b/ChatGPT.png?raw=true)
Image: ChatGPT generated 

Traditional sports commentary is either manually delivered by professionals or generated through rigid rule-based systems. These approaches often lack flexibility, contextual nuance, and real-time adaptability. In contrast, recent advances in large language models (LLMs) have enabled more dynamic generation of coherent, engaging narratives based on structured data inputs.

This project explores the application of open-source LLMs to generate **live-style, play-by-play soccer commentary** using structured match event data (passes, shots, tackles, etc.). We investigate the capabilities of LLMs like **Mistral-7B**, **GPT-J**, **Phi-4** and **LLaMA 2**, combined with retrieval-based summarization and fine-tuning techniques, to mimic the tone and pacing of real-time human commentators.

---

## 2. Project Overview

Live-Style Soccer Commentary LLM generates near-real-time, human-like match commentary based on structured event feeds (passes, shots, fouls, goals, etc.).

**Goals**:

* Demonstrate how parameter-efficient fine-tuning (LoRA/QLoRA) can produce engaging commentary on commodity hardware.
* Provide a template for small clubs or fan-driven applications to deploy AI commentators.

**Features**:

* Parses raw event data from CSV/JSON feeds
* Applies custom prompt templates to steer LLM output
* Supports LoRa fine-tuning

**Prerequisites**:

* Python 3.9+
* Git
* A GPU with ≥16 GB VRAM (for models ≥1 B parameters) or CPU-only for smaller models



### 2.2 Approach Overview

* **Input:** Structured soccer event data (e.g., player actions, match time, outcomes) from the European Soccer Database.
* **Processing:** Event sequences are chunked into short temporal windows, enriched with player/team context.
* **Modeling:** Two modeling strategies are explored:

  * **Prompt Engineering** with in-context examples
  * **Fine-Tuning** using LoRA on pre-trained LLMs

* **Output:** Natural language commentary resembling broadcast-style narration.

---

## 3. Dataset

### 3.1 Source

Statsbomb Open Data (https://github.com/statsbomb/open-data)

* Covers 11 countries
* Seasons: 2008–2016
* Includes match results, player stats, and play-by-play events
* Key tables used: `match`, `player_attributes`, `event_stream` (custom parsed)

### 3.2 Processed Data Format

* Source: Extracted directly from the match event JSON file provided by StatsBomb.

**Each record contains**:

* **Minute**: When the event occurred

* **Event Type**: Action taken (e.g., pass, shot)

* **Player & Team**: Who performed the action

* **Details**: Contextual metadata parsed from sub-objects (pass, shot, foul_committed, etc.)

This format feeds into the LLM prompt generator and enables highly contextual, realistic commentary output.

| Minute | Event Type | Player         | Team          | Details                                                                         |
| ------ | ---------- | -------------- | ------------- | ------------------------------------------------------------------------------- |
| 5      | Pass       | Joshua Kimmich | Bayern Munich | Picked out Thomas Müller’s run with a lofted ball behind defense.               |
| 17     | Shot       | Kai Havertz    | Chelsea       | Unleashed a curling effort from 20 yards that rifled just past the near post.   |
| 46     | Tackle     | N’Golo Kanté   | Chelsea       | Made a vital sliding interception to halt Bayern’s early second-half surge.     |
| 78     | Cross      | Leroy Sané     | Bayern Munich | Whipped in an inviting cross from the right flank, met by Lewandowski’s header. |

---

## 4. Model Architecture

### 4.1 Commentary Generation Pipeline

1. **Input Feature Extraction:** Time-ordered events per match (passes, goals, fouls, substitutions)
2. **Context Construction:** Include player stats, match importance, recent plays, and team form
3. **Prompt Formulation / Finetuned Input:** Format prompts like:
   *"45’ — Player X passes the ball to Player Y near the penalty box..."*
4. **LLM Output:**
   *“A slick one-two between Player X and Y slices through the defense—this is high-quality football!”*

**Weighing Event Importance**
* Events are weighted based on their significance to match flow and commentary value:

![Event weights](https://github.com/ArpanUchicago/Bayesian-ML-Football-Oracle/blob/main/Event%20weights.png)

**Dynamic Context Adjustments**
* Our commentary adapts based on match time and situational context:

![Time & context based modifiers](https://github.com/ArpanUchicago/Bayesian-ML-Football-Oracle/blob/main/Time%20%26%20context%20based%20modifiers.png)

**Goal Classification System**
* Goals are further categorized by position and type to generate more specific and accurate commentary:

![Goal subtype](./Goal%20subtype.png)

### 4.2 Models Explored

* **Mistral-7B (base and LoRA-tuned)**
* **GPT-J (6B)**
* **Phi-4**
* **LLaMA 2 (7B, 13B)**

All models were tested with prompt engineering and LoRA fine-tuning for domain adaptation.

---

## Live Demo

Experience the live commentary simulator in action:

[![Streamlit Status](https://share.streamlit.io/ArpanUchicago/Bayesian-ML-Football-Oracle/main/badge.svg)](https://bayesian-ml-football-oracle-commentarysimulator.streamlit.app/)

👉 **Try it now:**  
https://bayesian-ml-football-oracle-commentarysimulator.streamlit.app/




## Live Demo (LoRA Version)

Experience the LoRA-fine-tuned commentary simulator in action:

[![Streamlit Status – LoRA](https://share.streamlit.io/ArpanUchicago/Bayesian-ML-Football-Oracle/main/badge-lora.svg)](https://bayesian-ml-football-oracle-lora.streamlit.app/)

👉 **Try the LoRA version now:**  
https://bayesian-ml-football-oracle-lora.streamlit.app/

---

## 5. Evaluation

The generated commentary was evaluated using both qualitative and manual human judgment techniques.

#### 🔍 Evaluation Criteria:
- **Relevance**: Commentary correctly reflects the player and event described
- **Realism**: Output sounds like professional sports broadcasting
- **Emotion**: Goal commentary is vivid, crowd-driven, and appropriately high-energy
- **Brevity**: 2–3 sentence limit maintained without sacrificing information

#### 🧠 Methods Used:
- **Manual review process**: We conducted systematic human evaluation across 50+ diverse events (pass, goal, foul, interception), with multiple reviewers assessing each output against our criteria
- **Comparative analysis**: Outputs were compared against real broadcast commentary to identify gaps in authenticity, energy, and professional broadcasting style

#### 📊 Observations:
- The model produced highly realistic commentary for **goals and shots**
- **Pass and foul events** were often well-executed when player focus was emphasized
- **Bias toward Messi** was observed when not explicitly overridden in the prompt
- Commentary length was mostly within range, though longer completions sometimes occurred
- Crowd reactions improved noticeably when explicitly instructed

#### 🔧 Limitations:
- Lacks full tactical awareness (e.g., game flow, substitutions)
- Not robust to low-detail events (e.g., simple ball recoveries)
- Not yet benchmarked with BLEU/ROUGE due to lack of labeled reference commentary


---

## 6. Advantages of LLM-Based Commentary

* **Dynamic Context Awareness:** Captures player trends, match tempo
* **Language Diversity:** Mimics broadcast commentary tone (dramatic, rhythmic)
* **Real-Time Potential:** Can be embedded into live dashboards
* **Personalization:** Tailor commentary based on team or fan profile

---

## 7. Related Use Cases

### In Sports

* Basketball and cricket commentary generation
* Tactical insight summaries for coaches
* Match narration for accessibility tools (e.g., for visually impaired fans)

### Beyond Sports

* **Financial News Narratives:** Real-time market summaries from structured trading data
* **Healthcare Monitoring:** Patient report generation from clinical event streams
* **E-commerce:** Product update summaries from inventory events

---

## 8. Limitations & Challenges

* **Hallucinations:** Models sometimes generate incorrect or implausible actions
* **Latency:** Real-time generation needs fast inference (under 2s window)
* **Data Noise:** Match event data lacks rich descriptions (e.g., ball movement direction)

---

## 9. Conclusions & Future Work

* Fine-tuned open LLMs can effectively simulate broadcast-style soccer commentary
* Prompt engineering is competitive with fine-tuning in smaller setups
* Human-AI hybrid workflows (AI draft + human edit) show promise

**Next Steps:**

* Integrate **speaker-style transfer** using **Retrieval-Augmented Generation (RAG)** (e.g. mimic Peter Drury)
* Use multi-modal input (text + images/heatmaps)
* Evaluate in live setting with simulated match feeds
* Deploy in a web app dashboard with real-time updates
