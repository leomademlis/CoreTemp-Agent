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
