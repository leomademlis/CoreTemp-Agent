# CoreTemp Agent (Panthωron TraceAuditReady)

## Overview
CoreTemp Agent is an autonomous "Physical AI" industrial agent designed for frozen dough manufacturing. Acting as an edge-level Factory Manager, it mitigates product degradation (clumping for HO.RE.CA markets) and prevents unnecessary thermal load transfers to storage warehouses by dynamically adjusting tunnel cooling time and line speed. 

## System Architecture

```mermaid
graph LR
    %% Data Collection
    Sensors[ESP32 / PLC Sensors] -->|Temp & Speed Data| Agent(CoreTemp Agent : Python)
    
    %% AI Processing
    Agent -->|Prompt & Physics Constraints| AI{Nebius AI : Nemotron-3-Nano}
    AI -->|Cost Math & Decision| Agent
    
    %% Action & Compliance
    Agent -->|Machine COMMAND| PLC[Factory PLC]
    Agent -->|Audit Log| CSV[(TraceAudit_Log.csv)]
    CSV -->|Auto-Sync| AppSheet[AppSheet ERP : ISO 22000 Reports]

    %% Styling 
    style AI fill:#76b900,stroke:#333,stroke-width:2px,color:#fff
    style Agent fill:#0055ff,stroke:#333,stroke-width:2px,color:#fff
    style AppSheet fill:#ff9900,stroke:#333,stroke-width:2px,color:#fff

How we used NVIDIA Nemotron & Nebius Token Factory

We heavily utilized the Nebius Token Factory to power our edge agent. We specifically integrated the nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B model via the API.

    Why Nemotron-3-Nano: In a physical IoT manufacturing environment, ultra-low latency is critical. We didn't need conversational bloat; we needed a fast, highly logical model capable of calculating complex industrial physics constraints and dough scrap costs. Nano delivered deterministic mathematical reasoning and outputted strict, PLC-ready COMMAND strings instantly.

    Token Factory Acceleration: Nebius Token Factory significantly accelerated our development workflow. The OpenAI-compatible endpoint allowed us to seamlessly plug the model into our Python script, while the Playground UI helped us perfectly refine our industrial prompt engineering before deploying the code.

Setup Instructions

To run and test the simulation:

    Open the provided CoreTemp_Agent.py script in Google Colab (or any local Python environment).

    Locate the line: api_key = "PUT_YOUR_REAL_API_KEY_HERE" and insert your Nebius API Key.

    Run the script. The system will simulate a factory conveyor belt.

    When a temperature drop is simulated (<-36.0°C), the Nebius AI will trigger, calculate costs, and output a COMMAND.

    Check the local file directory (left panel in Colab) for the auto-generated TraceAudit_Log.csv. This is the audit-ready file designed to sync with AppSheet for ISO 22000 compliance.

License

This project is licensed under the MIT License - see the LICENSE file for details.
