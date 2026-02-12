#!/usr/bin/env python3

import subprocess
import sys
import datetime
import os

def run_command(command, check=True):
    print(f"Executing: {command}")
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    if process.returncode != 0 and check:
        print(f"Error: {process.stderr}")
        sys.exit(1)
    print(process.stdout)
    return process.stdout

if __name__ == "__main__":
    print("BISMALLAH. Starting full system backup INSHA'ALLAH.")

    backup_dir = "/home/ubuntu/backups"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    current_backup_path = os.path.join(backup_dir, f"full_system_backup_{timestamp}")
    os.makedirs(current_backup_path, exist_ok=True)

    # 1. Backup Frappe/ERPNext database and files
    print("\n--- Backing up Frappe/ERPNext site ---")
    site_name = "ethiobiz.et" # This should be configured or passed as argument
    frappe_backup_path = os.path.join(current_backup_path, "frappe_backup")
    os.makedirs(frappe_backup_path, exist_ok=True)
    # Assuming bench is accessible in the environment
    run_command(f"bench --site {site_name} backup --with-files --backup-path {frappe_backup_path}")

    # 2. Backup Docker Compose configuration and volumes (simplified for sandbox)
    print("\n--- Backing up Docker Compose configuration ---")
    docker_compose_path = "/home/ubuntu/bismillah_ethiobiz_new" # Assuming this is the project root
    if os.path.exists(os.path.join(docker_compose_path, "docker-compose.yml")):
        run_command(f"cp {os.path.join(docker_compose_path, 'docker-compose.yml')} {current_backup_path}/")
    else:
        print(f"Warning: docker-compose.yml not found at {docker_compose_path}. Skipping Docker Compose config backup.")

    # 3. Generic file system backup (example: important config files or custom app directories)
    print("\n--- Backing up important configuration files and custom apps ---")
    # Example: backing up the entire ethiobiz_expert_system directory
    run_command(f"cp -r /home/ubuntu/ethiobiz_expert_system {current_backup_path}/ethiobiz_expert_system_docs")
    # Example: backing up custom Frappe apps (assuming they are in a specific bench apps folder)
    # This part would need more specific knowledge of the Frappe bench structure
    # For now, we'll assume custom apps are part of the bench backup or managed via Git.

    print(f"Full system backup completed successfully to {current_backup_path} INSHA'ALLAH.")
