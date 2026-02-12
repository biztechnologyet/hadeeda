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

        # Step 1: Remove existing hadeeda completely (files and DB)
        print("\n=== STEP 1: Clean old installation ===")
        db_clean_py = """
import frappe
if frappe.db.exists('Module Def', 'Hadeeda'):
    frappe.delete_doc('Module Def', 'Hadeeda', force=True)
    print('Deleted Module Def')
dt = frappe.get_all('DocType', filters={'module': 'Hadeeda'}, pluck='name')
for d in dt:
    frappe.delete_doc('DocType', d, force=True)
    print(f'Deleted DocType: {d}')
if frappe.db.exists('Workspace', 'Hadeeda'):
    frappe.delete_doc('Workspace', 'Hadeeda', force=True)
    print('Deleted Workspace')
frappe.db.commit()
"""
        with client.open_sftp() as sftp:
            with sftp.file('/home/ethiobiz/clean_db.py', 'w') as f:
                f.write(db_clean_py)
        
        run_cmd(client, f"echo 'Admin@123' | sudo -S docker cp /home/ethiobiz/clean_db.py {BACKEND}:/tmp/clean_db.py")
        run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec -i {BACKEND} bash -c 'bench --site frontend console < /tmp/clean_db.py'")
        run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'cd /home/frappe/frappe-bench && bench --site frontend remove-app hadeeda --force || true; rm -rf apps/hadeeda; echo CLEANED'")

        # Step 2: Remove app via bench and delete folder
        print("\n=== STEP 2: Remove app from bench ===")
        run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'cd /home/frappe/frappe-bench && bench --site frontend remove-app hadeeda --force || true; rm -rf apps/hadeeda'")

        # Step 3: bench get-app
        print("\n=== STEP 3: bench get-app ===")
        run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'cd /home/frappe/frappe-bench && bench get-app https://github.com/biztechnologyet/hadeeda.git --branch main'", timeout=300)

        # Step 4: install-app
        print("\n=== STEP 4: bench install-app ===")
        run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'cd /home/frappe/frappe-bench && bench --site frontend install-app hadeeda'", timeout=120)

        # Step 5: migrate
        print("\n=== STEP 5: bench migrate ===")
        run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'cd /home/frappe/frappe-bench && bench --site frontend migrate'", timeout=300)

        # Step 6: Verify installation
        print("\n=== STEP 6: Verify installation ===")
        out, _, _ = run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c 'cd /home/frappe/frappe-bench && bench --site frontend list-apps'")
        print(f"\nInstalled apps: {out}")
        
        count_py = "import frappe; print('COUNT:', len(frappe.get_all('DocType', filters={'module': 'Hadeeda'})))"
        out_count, _, _ = run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec -i {BACKEND} bash -c 'bench --site frontend console <<< \"{count_py}\"'")
        print(f"\nDoctype Count: {out_count}")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 3 and sys.argv[1] == "--upload":
        local_path = sys.argv[2]
        remote_path = sys.argv[3]
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(HOST, 22, USER, PASSWORD)
            print(f"Uploading {local_path} to {remote_path}...")
            with client.open_sftp() as sftp:
                sftp.put(local_path, remote_path)
            print("Upload complete.")
        finally:
            client.close()
    elif len(sys.argv) > 2 and sys.argv[1] == "--execute":
        cmd = sys.argv[2]
        is_host = "--host" in sys.argv
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            client.connect(HOST, 22, USER, PASSWORD)
            if is_host:
                print(f"Executing on HOST: {cmd}")
                run_cmd(client, f"echo 'Admin@123' | sudo -S {cmd}")
            else:
                print(f"Executing in {BACKEND}: {cmd}")
                run_cmd(client, f"echo 'Admin@123' | sudo -S docker exec {BACKEND} bash -c '{cmd}'")
        finally:
            client.close()
    else:
        main()
