# Live-Style Soccer Commentary Using Open-Source LLMs

Authors: Arpan Pradhan, Matthew Schaefer, Shane Kim , Date: 2025-05-19

 1. # Introduction

 Traditional sports commentary is either manually delivered by professionals or generated through rigid rule-based systems. These approaches often lack flexibility, contextual nuance, and real-time adaptability. In contrast, recent advances in large language models (LLMs) have enabled more dynamic generation of coherent, engaging narratives based on structured data inputs.

This project explores the application of open-source LLMs to generate live-style, play-by-play soccer commentary using structured match event data (passes, shots, tackles, etc.). We investigate the capabilities of LLMs like Mistral-7B, GPT-J, and LLaMA 2, combined with retrieval-based summarization and fine-tuning techniques, to mimic the tone and pacing of real-time human commentators.

2. # Project Summary

**2.1 Objective**

To generate real-time, natural-language soccer commentary from structured match event data using open-source LLMs, enhancing fan engagement and accessibility of sports data.

**2.2 Approach Overview**

Input: Structured soccer event data (e.g., player actions, match time, outcomes) from the European Soccer Database.

Processing: Event sequences are chunked into short temporal windows, enriched with player/team context.

Modeling: Three modeling strategies are explored:

Prompt Engineering with in-context examples

Fine-Tuning using LoRA on pre-trained LLMs

Retrieval-Augmented Generation (RAG) using news headlines or historical events

Output: Natural language commentary resembling broadcast-style narration.

3. # Model Architecture

3.1 Commentary Generation Pipeline
Input Feature Extraction: Time-ordered events per match (passes, goals, fouls, substitutions)

Context Construction: Include player stats, match importance, recent plays, and team form

Prompt Formulation / Finetuned Input: Format prompts like:
"45’ — Player X passes the ball to Player Y near the penalty box..."

LLM Output:
“A slick one-two between Player X and Y slices through the defense—this is high-quality football!”


3.2 Models Explored

Mistral-7B (base and LoRA-tuned)

GPT-J (6B)

LLaMA 2 (7B, 13B)

All models were tested with prompt engineering and LoRA fine-tuning for domain adaptation.


**4. Dataset**
   
4.1 Source
European Soccer Database (Kaggle):

Covers 11 countries

Seasons: 2008–2016

Includes match results, player stats, and play-by-play events

Key tables used: match, player_attributes, event_stream (custom parsed)

| Minute | Action | Player | Target | Outcome |
| ------ | ------ | ------ | ------ | ------- |
| 15     | Pass   | X      | Y      | Success |
| 16     | Shot   | Y      | Goal   | Yes     |
| ...    | ...    | ...    | ...    | ...     |



**5. Evaluation**
   
**5.1 Quantitative Metrics**

BLEU & ROUGE: Compare generated commentary against ground truth post-match reports

Perplexity: Measure fluency and grammar quality

Comment Quality Rating (CQR): Human reviewers rate clarity, emotion, and engagement (1–5 scale)

**5.2 Qualitative Feedback**

Real-time generated commentaries were reviewed by soccer fans

Scores collected for excitement, realism, and insightfulness

Most engaging commentaries came from RAG + Prompt Ensemble setup


**6. Advantages of LLM-Based Commentary**
   
Dynamic Context Awareness: Captures player trends, match tempo

Language Diversity: Mimics broadcast commentary tone (dramatic, rhythmic)

Real-Time Potential: Can be embedded into live dashboards

Personalization: Tailor commentary based on team or fan profile

 
   





                                                                        

                                                                       

