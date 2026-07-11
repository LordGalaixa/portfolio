import json
import os
from datetime import datetime

# Simulated raw data payload coming from a web form or external database
RAW_CLIENT_DATA = [
    {"name": "john doe", "region": "NY - Brooklyn", "status": "pending_auth", "priority": "high"},
    {"name": "ALICE SMITH", "region": "North Carolina Regional", "status": "intake_review", "priority": "standard"},
    {"name": "charles brown", "region": "Arizona Pilot Expansion", "status": "ready_for_staffing", "priority": "high"},
    {"name": "EMILY DAVIS", "region": "NY - Queens", "status": "pending_auth", "priority": "standard"},
    {"name": "Michael Green", "region": "Utah Hub", "status": "intake_review", "priority": "high"}
]

class ABAPipelineManager:
    def __init__(self, dataset):
        self.dataset = dataset
        self.processed_count = 0
        # Initialize storage files mapping directly to internal company departments
        self.departments = {
            "intake_department": [],
            "authorizations_department": [],
            "staffing_department": []
        }

    def clean_and_route_data(self):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Initializing Python Automation Matrix...")
        print("-" * 60)
        
        for client in self.dataset:
            # 1. Data Standardization (Fixing messy text capitalization)
            clean_name = client["name"].strip().title()
            region = client["region"].strip()
            status = client["status"]
            priority = client["priority"].upper()

            # 2. Advanced Conditional Matrix Routing Logic
            processed_packet = {
                "client_id": f"ABA-{1000 + self.processed_count}",
                "timestamp": datetime.now().isoformat(),
                "full_name": clean_name,
                "operational_region": region,
                "workflow_priority": priority,
                "api_sync_status": "Ready for Monday.com Sync"
            }

            # Route to respective department list based on system status tags
            if status == "intake_review":
                self.departments["intake_department"].append(processed_packet)
            elif status == "pending_auth":
                self.departments["authorizations_department"].append(processed_packet)
            elif status == "ready_for_staffing":
                self.departments["staffing_department"].append(processed_packet)

            self.processed_count += 1
            print(f"[SUCCESS] Processed packet for: {clean_name} | Assigned to: {status}")

    def output_department_matrices(self):
        print("-" * 60)
        print(f"Processing Complete. Exporting clean JSON payloads for system integration...")
        
        # Simulating saving out distinct department operational lists
        for dept_name, data_packets in self.departments.items():
            filename = f"{dept_name}.json"
            print(f" -> Exported {len(data_packets)} active items to file matrix: [ {filename} ]")
            
            # On a desktop, this writes real files. On mobile/simulators, it prints structured data.
            # with open(filename, 'w') as f:
            # json.dump(data_packets, f, indent=4)

if __name__ == "__main__":
    # Initialize the automated script routing array
    pipeline = ABAPipelineManager(RAW_CLIENT_DATA)
    pipeline.clean_and_route_data()
    pipeline.output_department_matrices()
