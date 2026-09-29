# CoreTemp Agent (Panthωron TraceAuditReady)

## System Architecture

```mermaid
graph LR
    Sensors[ESP32 / PLC Sensors] -->|Temp & Speed Data| Agent(CoreTemp Agent : Python)
    Agent -->|Prompt & Physics Constraints| AI{Nebius AI : Nemotron-3-Nano}
    AI -->|Cost Math & Decision| Agent
    Agent -->|Machine COMMAND| PLC[Factory PLC]
    Agent -->|Audit Log| CSV[(TraceAudit_Log.csv)]
    CSV -->|Auto-Sync| AppSheet[AppSheet ERP : ISO 22000 Reports]
    style AI fill:#76b900,stroke:#333,stroke-width:2px,color:#fff
    style Agent fill:#0055ff,stroke:#333,stroke-width:2px,color:#fff
    style AppSheet fill:#ff9900,stroke:#333,stroke-width:2px,color:#fff



## Overview
CoreTemp Agent is an autonomous "Physical AI" industrial agent designed for frozen dough manufacturing. Acting as an edge-level Factory Manager, it mitigates product degradation (clumping for HO.RE.CA markets) and prevents unnecessary thermal load transfers to storage warehouses by dynamically adjusting tunnel cooling time and line speed. 

## How we used NVIDIA Nemotron & Nebius Token Factory
We specifically integrated the `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B` model via the API. 
* **Why Nemotron-3-Nano:** In a physical IoT manufacturing environment, ultra-low latency is critical. We didn't need conversational bloat; we needed a fast, highly logical model capable of calculating complex industrial physics constraints and dough scrap costs. Nano delivered deterministic mathematical reasoning and outputted strict, PLC-ready `COMMAND` strings instantly.
* **Token Factory Acceleration:** Nebius Token Factory significantly accelerated our development workflow. The OpenAI-compatible endpoint allowed us to seamlessly plug the model into our Python script, while the Playground UI helped us perfectly refine our industrial prompt engineering before deploying the code.

## Setup Instructions
1. Open `CoreTemp_Agent.py`.
2. Insert your Nebius API Key.
3. Run the script to simulate a factory conveyor belt anomaly.
4. Check for the auto-generated `TraceAudit_Log.csv` (AppSheet/ISO 22000 compliance).
