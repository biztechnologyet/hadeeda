#!/bin/bash
# Hadeeda Automated Deployment Script
# Run this on the Ubuntu host as user 'ethiobiz'

echo "=========================================="
echo "Starting Hadeeda Deployment"
echo "=========================================="

# 1. Access backend container and execute commands
echo "[1/3] Accessing backend container..."
sudo docker compose -f /home/ethiobiz/frappe_docker/pwd.yml exec backend bash -c '
    echo "INSIDE CONTAINER: User $(whoami)"
    cd /home/frappe/frappe-bench/apps

    # 2. Deploy app
    echo "[2/3] Cloning/updating app..."
    if [ -d "hadeeda" ]; then
        echo "Removing existing hadeeda folder..."
        rm -rf hadeeda
    fi

    echo "Cloning repository..."
    git clone https://github.com/biztechnologyet/hadeeda.git

    # Handle monorepo structure if needed
    if [ -d "hadeeda/hadeeda" ]; then
        echo "Flattening directory structure..."
        mv hadeeda/hadeeda/* hadeeda/
        rmdir hadeeda/hadeeda
    fi

    cd ..

    echo "Installing app on site frontend..."
    bench --site frontend install-app hadeeda --force

    echo "Migrating database..."
    bench --site frontend migrate

    echo "Clearing cache..."
    bench --site frontend clear-cache

    echo "Restarting bench..."
    bench restart

    # 3. Verification
    echo "[3/3] Verifying installation..."
    echo "Apps Installed:"
    bench --site frontend list-apps | grep hadeeda

    echo "DocType Count:"
    bench --site frontend console <<EOF
import frappe
count = frappe.db.get_all("DocType", filters={"module": "Hadeeda"}, pluck="name")
print(f"Hadeeda doctypes: {len(count) if count else 0}")
EOF
'

echo "=========================================="
echo "Deployment Complete!"
echo "=========================================="
