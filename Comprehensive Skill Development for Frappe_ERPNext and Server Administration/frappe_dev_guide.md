# Frappe/ERPNext Development Guide (v15)

## 1. Core Architecture
Frappe is a full-stack web framework based on Python (Server) and Javascript (Client).
- **DocType**: The core building block. Defines schema, UI, and behavior.
- **Bench**: The CLI tool for managing Frappe environments.
- **Hooks**: The mechanism for extending core functionality without modifying core code.

## 2. Custom App Development
1. **Create App**: `bench new-app <app_name>`
2. **Install App**: `bench --site <site_name> install-app <app_name>`
3. **DocTypes**: Create via Desk or JSON. Use `hooks.py` to link logic.
4. **Websites**: Use Web Pages or custom templates in `www/`.

## 3. Best Practices
- **Never modify core**: Use custom apps and hooks.
- **Version Control**: Always use Git. Commit frequently with descriptive messages.
- **Testing**: Write Unit Tests in `tests/` directory. Run with `bench run-tests`.
- **UI/UX**: Follow Frappe Design System. Use `frappe.ui.form` and `frappe.msgprint`.

## 4. Version 15 Specifics
- **UI/UX**: Familiar desktop UI and navigation. Focus on Workspace and List View customizations.
- **Performance**: Optimize database queries and client-side rendering.
- **Security**: Implement robust role-based access control (RBAC) and data validation.
