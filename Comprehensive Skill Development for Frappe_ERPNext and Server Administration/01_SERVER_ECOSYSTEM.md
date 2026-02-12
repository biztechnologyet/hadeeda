# 01. SERVER ECOSYSTEM & SAFETY PROTOCOLS

## 1. Topography of `ethiobiz.et`
*   **OS**: Windows (Host for Development), but the target environment simulates or connects to a **Linux/Docker** production environment managed via `bismillah_ethiobiz_new`.
*   **Core Technology**: Docker Compose Orchestration.

## 2. The Container Fleet
The server hosts multiple interconnected yet distinct systems. You must know them to respect boundaries.

### A. The EthioBiz Cluster (Your Domain)
These are the containers you manage directly or indirectly via `bench`.
1.  **frontend**: Serves the Frappe UI and Assets.
2.  **backend**: Runs the Python/Frappe Application (`bismillah_ethiobiz_new`).
3.  **redis-queue, redis-cache, redis-socketio**: Support services.
4.  **mariadb/postgresql**: The database (specifically for Frappe).

### B. The Protected Neighbors (HANDLE WITH CARE)
These run on the same server/network. **DO NOT RESTART OR MODIFY THESE WITHOUT EXPLICIT USER PERMISSION.**
1.  **n8n (Workflow Automation)**:
    *   **Status**: Critical / Production.
    *   **Risk**: Restarting Docker blindly can kill active n8n workflows.
    *   **Rule**: Never run `docker-compose down` on the root level unless you are 100% sure n8n is safe or isolated.
2.  **Global PostgreSQL**:
    *   **Status**: Shared Database Resource.
    *   **Risk**: Data loss or connection drops for other apps (like CrewAI or n8n).
3.  **CrewAI**:
    *   **Status**: AI Agent Framework.
    *   **Rule**: Ensure your resource usage (CPU/RAM) doesn't starve these agents.

## 3. Network & Connectivity
*   **Port Discipline**:
    *   EthioBiz usually binds to **80/443** (via Nginx/Traefik) or specific dev ports (e.g., **8000**).
    *   **n8n** usually binds to **5678**.
    *   **Postgres** binds to **5432**.
    *   **Check First**: Use `netstat -ano` (Windows) or `docker ps` to see used ports before assigning new ones.

## 4. Safety Checklist (The "Flight Check")
Before deploying any server-wide change:
1.  [ ] **Identify Active Services**: Run `docker ps`.
2.  [ ] **Check Volume Mounts**: Ensure you aren't overwriting a shared volume.
3.  [ ] **Backup**: If modifying DBs, run `bench --site ethiobiz.et backup`.
4.  [ ] **Confirm Scope**: Does this command affect *only* the `bismillah_ethiobiz` container?
    *   Safe: `docker restart bismillah_frontend`
    *   Dangerous: `docker system prune -a` (Could wipe n8n images).

BISMALLAH. Respect the ecosystem.
