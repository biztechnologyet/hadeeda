#!/usr/bin/env python3

import os
import subprocess
import sys

def run_command(command, check=True):
    print(f"Executing: {command}")
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    if process.returncode != 0 and check:
        print(f"Error: {process.stderr}")
        sys.exit(1)
    print(process.stdout)
    return process.stdout

if __name__ == "__main__":
    print("BISMALLAH. Starting UI fix deployment INSHA\'ALLAH.")

    site_name = "ethiobiz.et" # This should ideally be passed as an argument or configured
    app_name = "bismillah_ethiobiz_new" # This should ideally be passed as an argument or configured
    frappe_backend_container = "bismillah_ethiobiz_inshaallah-backend-1" # Assuming this is the Frappe backend container name
    
    # Define paths relative to the project root where the script is run
    local_app_path = os.path.join(os.getcwd(), app_name)
    container_app_path = f"/home/frappe/frappe-bench/apps/{app_name}"

    # 1. Copy local changes (public/css, public/js) to the container
    print(f"\n--- Copying local changes from {local_app_path} to {frappe_backend_container}:{container_app_path} ---")
    # Copy public assets (CSS/JS) and other app files
    run_command(f"docker cp {local_app_path}/public {frappe_backend_container}:{container_app_path}/")
    run_command(f"docker cp {local_app_path}/hooks.py {frappe_backend_container}:{container_app_path}/")
    # Add more `docker cp` commands for other relevant app files/directories as needed

    # 2. Reinstalling the app or migrating changes
    print(f"\n--- Migrating Frappe app changes for site {site_name} ---")
    # Use `docker exec` to run bench commands inside the container
    run_command(f"docker exec {frappe_backend_container} bench --site {site_name} migrate")

    # 3. Building assets
    print("\n--- Building Frappe assets ---")
    run_command(f"docker exec {frappe_backend_container} bench build")

    # 4. Clearing cache
    print(f"\n--- Clearing Frappe cache for site {site_name} ---")
    run_command(f"docker exec {frappe_backend_container} bench --site {site_name} clear-cache")

    print("UI fix deployment completed INSHA\'ALLAH.")
