import paramiko
import time

HOST = "localhost"
USER = "ethiobiz"
PASSWORD = "Admin@123"
BACKEND = "frappe_docker-backend-1"

def run_cmd(client, cmd, timeout=300):
    print(f"\n>>> {cmd[:120]}...")
    stdin, stdout, stderr = client.exec_command(cmd, timeout=timeout)
    exit_status = stdout.channel.recv_exit_status()
    out = stdout.read().decode('utf-8', errors='replace').strip()
    err = stderr.read().decode('utf-8', errors='replace').strip()
    if out:
        # Safe print for Windows console
        safe_out = out[-1000:].encode('ascii', errors='replace').decode('ascii')
        print(f"OUT: {safe_out}")
    if err:
        safe_err = err[-500:].encode('ascii', errors='replace').decode('ascii')
        print(f"ERR: {safe_err}")
    print(f"EXIT: {exit_status}")
    return out, err, exit_status

def main():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        print("Connecting to VM...")
        client.connect(HOST, 22, USER, PASSWORD)
        print("Connected!")

        # Step 1: Remove existing hadeeda completely
        print("\n=== STEP 1: Clean old installation ===")
        run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'cd /home/frappe/frappe-bench && bench --site frontend remove-app hadeeda --force 2>/dev/null; rm -rf apps/hadeeda; echo CLEANED'")

        # Step 2: Use bench get-app (the correct Frappe way)
        print("\n=== STEP 2: bench get-app (clone + pip install) ===")
        out, err, status = run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'cd /home/frappe/frappe-bench && bench get-app https://github.com/biztechnologyet/hadeeda.git --branch main'", timeout=300)

        # Step 3: Verify app is registered
        print("\n=== STEP 3: Verify app files ===")
        run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'ls /home/frappe/frappe-bench/apps/hadeeda/ && python -c \"import hadeeda; print(hadeeda)\"'")

        # Step 4: Install on site
        print("\n=== STEP 4: Install app on site ===")
        out, err, status = run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'cd /home/frappe/frappe-bench && bench --site frontend install-app hadeeda'", timeout=120)

        # Step 5: Migrate
        print("\n=== STEP 5: Migrate ===")
        out, err, status = run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'cd /home/frappe/frappe-bench && bench --site frontend migrate'", timeout=300)

        # Step 6: Clear cache
        print("\n=== STEP 6: Clear cache ===")
        run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'cd /home/frappe/frappe-bench && bench --site frontend clear-cache'")

        # Step 7: Verify
        print("\n=== STEP 7: Verify installation ===")
        out, err, _ = run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'cd /home/frappe/frappe-bench && bench --site frontend list-apps'")
        print(f"\nInstalled apps: {out}")

        # Step 8: Count doctypes using bench console
        print("\n=== STEP 8: Count Hadeeda doctypes ===")
        count_cmd = '''cd /home/frappe/frappe-bench && echo "docs=frappe.get_all('DocType',filters={'module':'Hadeeda'},pluck='name'); print('Hadeeda doctypes:',len(docs))" | bench --site frontend console'''
        out, err, _ = run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c '{count_cmd}'", timeout=30)
        print(f"\nDoctypes result: {out}")

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
    finally:
        client.close()
        print("\nDone.")

if __name__ == "__main__":
    main()
