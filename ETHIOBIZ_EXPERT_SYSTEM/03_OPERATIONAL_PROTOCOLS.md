# 03. OPERATIONAL PROTOCOLS & DEPLOYMENT

## 1. The Deployment Protocol ("The Golden Path")
We do not patch the server manually. We use the **Script**.

### The Script: `execute_ui_fix.py`
This script automates:
1.  Copying your local changes (`public/css`, `public/js`) to the container.
2.  Reinstalling the app (`bench --site ethiobiz.et install-app ...`).
3.  Building assets (`bench build`).
4.  Clearing cache (`bench clear-cache`).

### Usage
```powershell
python execute_ui_fix.py
```
*   **When to run**: After *every* significant batch of CSS/JS changes.
*   **Note**: It takes a few minutes. Be patient.

## 2. The Development Lifecycle
For every feature request or bug report:

### Phase 1: Planning
1.  **Analyze**: Read the request. inspect the current code (`ethiobiz_theme.css`).
2.  **Task**: Create or update `task.md`.
3.  **Plan**: Create `implementation_plan.md`. Get user confirmation (implied or explicit).

### Phase 2: Execution
1.  **Code**: Edit the local files (e.g., `ethiobiz_theme.css`).
2.  **Review**: Check your syntax.
3.  **Deploy**: Run `execute_ui_fix.py`.

### Phase 3: Verification
1.  **Visual Check**: Use the **Browser Subagent** to take a screenshot.
    *   *Do not trust your code blindly. Trust the pixels.*
    *   *If you are logged out of EthioBiz.et, if saved password is visible, click login and proceed with the saved credentials and if saved password is not visible, request the user to login or provide the credentials to login and proceed the Browser subagent operation InSha'Allah.*
2.  **Technical Check**: If it's a backend change, check logs.

## 3. Troubleshooting & Diagnostics

### "I see no changes!"
1.  **Cache**: Did `bench clear-cache` run? Run it manually via `docker exec`.
2.  **Browser Cache**: The browser subagent might need a hard refresh protocol.
3.  **Build Error**: Did `bench build` fail? Check the script output.

### "500 Internal Server Error"
1.  **Check Logs**:
    ```powershell
    docker logs bismallah_ethiobiz_inshaallah-backend-1
    ```
2.  **Syntax Error**: Did you break `hooks.py` or a Python file?
3.  **Database**: Is the Postgres container running?

## 4. Emergency Procedures
If you break the site (White Screen of Death):
1.  **Don't Panic.**
2.  **Revert**: Undo your last code change locally.
3.  **Deploy**: Run `execute_ui_fix.py` immediately to push the reversion.
4.  **Analyze**: Why did it break?

BISMALLAH. Work systematically.
