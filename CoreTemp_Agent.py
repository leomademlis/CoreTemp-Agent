import random
import time
import requests
import csv
from datetime import datetime
import os

# --- THE APPSHEET / ERP BRIDGE (CSV EXPORT) ---
def log_decision_to_csv(temp, speed, ai_response):
    filename = "TraceAudit_Log.csv"
    file_exists = os.path.isfile(filename)
    machine_command = "MANUAL CHECK REQUIRED"
    if "COMMAND:" in ai_response:
        machine_command = ai_response.split("COMMAND:")[-1].strip()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "Sensor_Temp", "Line_Speed", "AI_Command"])
        writer.writerow([timestamp, temp, speed, machine_command])
    print(f"   [SYSTEM] 💾 Audit record saved to {filename} for AppSheet sync.")

# --- THE AI AGENT ---
def call_nvidia_agent(speed, temp):
    print("   [AGENT] Contacting Nebius AI...")
    api_url = "https://api.studio.nebius.ai/v1/chat/completions"
    api_key = "PUT_YOUR_REAL_API_KEY_HERE"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    prompt_message = (
        f"I am a Factory Manager. Tunnel temp is {temp}C, line speed is {speed} kg/h. "
        "Energy is 0.17 EUR/kWh, labor is 56 EUR/h, raw dough cost is 1.20 EUR/kg. "
        "PHYSICS CONSTRAINT: You cannot increase tunnel residence time without proportionally dropping line speed. "
        "Option 1: Drop line speed to 650 kg/h (Tunnel stays 40 mins). WARNING: This mismatch causes 1.5% dough scrap due to deformation! "
        "Option 2 (Synchronized): Increase tunnel time to 45 mins AND drop line speed to 640 kg/h (0% scrap). "
        "Calculate the total extra cost per kg for both options (labor/energy + dough scrap cost). Which is cheaper? "
        "IMPORTANT: End your response with a clear 'COMMAND:' stating exactly what speed and time parameters to change."
    )
    data = {
        "model": "nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B", 
        "messages": [
            {"role": "system", "content": "You are a precise industrial AI agent. Always provide the math and end with a clear COMMAND."},
            {"role": "user", "content": prompt_message}
        ],
        "temperature": 0.1 
    }
    try:
        response = requests.post(api_url, headers=headers, json=data)
        if response.status_code != 200:
            return f"ERROR: {response.status_code} - {response.text}"
        return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        return f"ERROR: {e}"

# --- MAIN FACTORY OPERATION ---
def simulate_factory():
    print("FACTORY OPERATION STARTED...")
    current_speed = 720  # kg/h
    current_temp = -35.5
    print(f"[SENSOR] Speed: {current_speed} kg/h | Tunnel Temp: {current_temp} °C")
    print("   -> ⚠️ WARNING: Cooling capacity dropping!")
    ai_answer = call_nvidia_agent(current_speed, current_temp)
    print(f"   -> 🤖 AI DECISION:\n{ai_answer}")
    log_decision_to_csv(current_temp, current_speed, ai_answer)

if __name__ == '__main__':
    simulate_factory()
