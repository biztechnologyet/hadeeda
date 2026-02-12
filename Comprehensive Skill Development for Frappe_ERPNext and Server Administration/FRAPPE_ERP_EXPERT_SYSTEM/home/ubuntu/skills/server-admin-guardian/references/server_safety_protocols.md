# Server Administration & Safety Protocols

## 1. Pre-Operation Checklist (The Flight Check)
Before any command:
1. **Identify**: `docker ps` to see all running containers.
2. **Analyze**: Identify "Protected Neighbors" (n8n, CrewAI, Postgres).
3. **Assess**: Will this command affect other containers? (e.g., `docker-compose down` vs `docker restart <container>`).

## 2. Backup Strategy
- **Database**: `bench --site <site> backup --with-files`
- **Files**: `cp <file> <file>.bak`
- **System**: Use automated backup scripts if available.

## 3. Rollback Procedures
- **Code**: `git checkout <previous_commit>` or `git revert`.
- **Database**: `bench --site <site> restore <backup_path>`.
- **Emergency**: Revert local changes and redeploy immediately.

## 4. SSH & Remote Operations
- Always verify credentials before connecting.
- Use non-destructive commands first (`ls`, `status`, `check`).
- Log all operations in a `walkthrough.md` or similar.

## 5. Best Practices
- **Principle of Least Privilege**: Only touch what is necessary.
- **Mindfulness**: Start with "BISMALLAH", end with "INSHA'ALLAH".
- **Documentation**: Record every change for future reference.
