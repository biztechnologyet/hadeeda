# 02. APP ARCHITECTURE & CUSTOMIZATION

## 1. The Core Application
*   **App Name**: `bismillah_ethiobiz` (or `bismillah_ethiobiz_new`)
*   **Path**: `.../BISMALLAH_ETHIOBIZ_INSHA'ALLAH/bismillah_ethiobiz_new`
*   **Framework**: built on **Frappe Framework** (Python/JS).

## 2. The Theming Engine (The "Soul" of the UI)
The visual identity of EthioBiz is defined almost entirely by **CSS Overrides** rather than deep template modification. This is safer and easier to maintain.

### Key Files
1.  **CSS Source of Truth**:
    *   Path: `public/css/ethiobiz_theme.css`
    *   **Role**: Defines the "Perfect Glassmorphism".
    *   **Structure**:
        *   **Block 1: Structural Transparency**: Makes large containers (`.page-head`, `.layout-main`) invisible so the background shows through.
        *   **Block 2: Universal Glass**: Applies the 20% opacity white/black tint + Blur to content cards (`.frappe-card`, `.widget`).
2.  **JS Logic**:
    *   Path: `public/js/ethiobiz_theme.js`
    *   **Role**: Handles dynamic behaviors (e.g., relocating elements that CSS can't reach, injecting specific classes on route change).

## 3. Customization Logic
When you need to change a UI element:
1.  **Target the CSS First**: 90% of changes (colors, transparency, rounded corners) belong in `ethiobiz_theme.css`.
2.  **Use Specificity**: Frappe has strong default styles. Use `!important` judiciously or increase specificity (e.g., `body[data-theme="dark"] .my-class`) to override.
3.  **The "Two-Block" Strategy**:
    *   If it's a **Container** (holding other things): Make it TRANSPARENT.
    *   If it's a **Card** (holding text/data): Make it GLASS (Translucent).

## 4. Backend Hooks
*   **File**: `hooks.py`
*   **Role**: Connects the custom app to Frappe.
*   **Critical**: Ensure `app_include_css` and `app_include_js` point to your theme files.

## 5. Development Pattern
1.  **Edit**: Modify the CSS/JS file locally.
2.  **Deploy**: Run the deployment script (see `03_OPERATIONAL_PROTOCOLS.md`).
3.  **Verify**: Check the browser.

BISMALLAH. maintain the beauty.
