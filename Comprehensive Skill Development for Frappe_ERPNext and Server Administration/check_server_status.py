#!/usr/bin/env python3

import subprocess
import sys

def run_command(command):
    print(f"Executing: {command}")
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    if process.returncode != 0:
        print(f"Error: {process.stderr}")
        # Do not exit on error for status checks, just report
    return process.stdout

if __name__ == "__main__":
    print("BISMALLAH. Checking server status INSHA'ALLAH.")

    print("\n--- Running Docker Containers ---")
    run_command("docker ps")

    print("\n--- Network Port Usage ---")
    # netstat might not be installed by default in some minimal Docker images
    # Using `ss` as a more modern alternative if available, or `netstat -tulnp`
    # For sandbox, `netstat` is available.
    run_command("netstat -tulnp || ss -tulnp")

    print("\n--- Disk Usage ---")
    run_command("df -h")

    print("\n--- Memory Usage ---")
    run_command("free -h")

    print("Server status check completed INSHA'ALLAH.")
