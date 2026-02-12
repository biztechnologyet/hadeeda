# 05. DATABASE ACCESS & N8N INTEGRATION

## 1. Overview
 This document serves as the **Single Source of Truth** for accessing the EthioBiz database (MariaDB) and integrating it with the automation engine (n8n).
 Both systems run in a production Docker ecosystem on `128.140.82.215`.

## 2. Network Topology (Crucial for n8n)
*   **External Network**: `ethiobiz_hadeeda_bridge`
*   **Significance**: This network connects `backend` (Frappe), `db` (MariaDB), and `n8n`.
*   **Internal Hostname**: Within this network, the database container is accessible simply as `db`. **Do not use localhost or the public IP.**

## 3. MariaDB Connection Credentials

### A. Site-Specific Connection (Recommended for n8n)
Use these credentials for all n8n workflows and day-to-day operations. It accesses the specific database for `ethiobiz.et`.

| Parameter | Value |
| :--- | :--- |
| **Host** | `db` (Internal Docker Network) |
| **Port** | `3306` |
| **Database Name** | `_fe9b2d5bf372f5c7` |
| **User** | `_fe9b2d5bf372f5c7` |
| **Password** | `GFPafYamxu9YKh4t` |

### B. Root Access (Admin Only)
Use ONLY for server maintenance or creating new sites.
| Parameter | Value |
| :--- | :--- |
| **User** | `root` |
| **Password** | `admin` |
| **Host** | `db` |

## 4. How to Connect n8n (Step-by-Step)
1.  Open your n8n workflow editor.
2.  Add a **MySQL** node.
3.  Create a new Credential:
    *   **User**: `_fe9b2d5bf372f5c7`
    *   **Password**: `GFPafYamxu9YKh4t`
    *   **Database**: `_fe9b2d5bf372f5c7`
    *   **Host**: `db`
    *   **Port**: `3306`
4.  **Test Connection**: It should return "Connection Successful".

## 5. Deployment Reference
*   **Docker Compose File**: `pwd-cloud-existing.yml` (in `BISMALLAH_ETHIOBIZ_INSHA'ALLAH`)
*   **Frappe Version**: `v15.92.4`
*   **MariaDB Version**: `10.6`

BISMALLAH. Use these credentials wisely and keep them secure.
