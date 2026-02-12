# BISMALLAH - EthioBiz UI Customization Reference (InSha'Allah)

This document provides a technical record of the UI customizations implemented for the EthioBiz system as of February 2026. This is essential for future system administration, app upgrades, and troubleshooting.

## 1. Overview of Customizations
The primary goal was to create a clean, professional user interface by hiding unnecessary onboarding popups and updating service links across three main applications:
1. **EthioBiz (ERP/Desk)**: General UI cleanliness.
2. **Walta (Helpdesk/Ticketing)**: Branded link updates and popup hiding.
3. **Dagu (LMS/Learning)**: Popup hiding and button functionality restoration.

---

## 2. App-Specific Implementation Details

### A. EthioBiz (ERP Desk)
- **Location**: `bismillah_ethiobiz/public/css/ethiobiz_theme.css` and `js/ethiobiz_theme.js`.
- **Target Elements**: 
  - "Get more insights" link.
  - "Switch to Desk" and "Apps" links in the dropdown menu.
- **Method**: Standard Frappe `app_include_css` and `app_include_js` hooks.

### B. Walta (Helpdesk)
- **Location**: `bismillah_ethiobiz/public/css/walta.css` and `js/walta.js`.
- **Target Elements**: 
  - "Getting Started" onboarding popup.
  - "Support" link redirected to Telegram (`https://t.me/BizSupportOfficial`).
  - "Docs" link redirected to `https://ethiobiz.et/support`.
- **Method**: Standard Frappe hooks + `bench build`.

### C. Dagu (LMS) - "The Dagu Exception"
> [!IMPORTANT]
> **Technical Warning**: Dagu LMS is a Vue Single Page Application (SPA). It uses its own compiled CSS bundle and **does not** load standard Frappe website hooks (`web_include_css`).

- **Method**: **Direct HTML Injection**.
- **Files Modified**: 
  - `/home/frappe/frappe-bench/sites/assets/lms/frontend/index.html`
  - `/home/frappe/frappe-bench/apps/lms/lms/www/lms.html`
- **Logic**: A `<style>` tag is injected directly into the `<head>` of these templates.
- **Maintenance**: If the LMS app is upgraded or its frontend is rebuilt, **these HTML files will be overwritten**. The administrator MUST re-apply the injection using the deployment script (`deploy_v3.4.4_fix_create_button.py`).

---

## 3. CSS Selector Precision (Crucial)
During the "Dagu Fix" (v3.4.3 vs v3.4.4), it was discovered that broad selectors cause collateral damage.

- **BAD (v3.4.3)**: `.bg-surface-modal.shadow-2xl { display: none !important; }`
  - *Result*: Hid the onboarding popup BUT also hid the "Create New Course" dropdown menu.
- **GOOD (v3.4.4)**: `.fixed.right-0.w-80.bg-surface-modal.shadow-2xl { display: none !important; }`
  - *Result*: Only hides the popup because of the `.fixed.right-0.w-80` specificity (dropdowns are not fixed to the right with 80rem width).

---

## 4. Deployment Inventory
The following scripts were used to implement these changes:

| Version | Script Name | Key Change |
|:---:|:---|:---|
| **v3.4.0** | `deploy_v3.4.0_hide_popups.py` | Initial Walta popup hide and link updates. |
| **v3.4.3** | `deploy_v3.4.3_dagu_complete.py` | First successful Dagu popup hide (via HTML injection). |
| **v3.4.4** | `deploy_v3.4.4_fix_create_button.py` | **CURRENT STABLE VERSION**. Fixes Create Button conflict. |

---

## 5. Maintenance Checklist for Upgrades
When performing a `bench update` or app-specific upgrade:
1. **Verify ERP Desk**: Ensure `ethiobiz_theme.css` changes persist (they usually do).
2. **Verify Walta**: Run `bench build` to ensure custom assets are re-minified.
3. **Verify Dagu (Critical)**: Check if the "Getting Started" popup has returned. If it has, use the **HTML Injection Script** (v3.4.4) to restore the clean UI.
4. **Link Check**: Verify `https://ethiobiz.et/lms/courses` -> click "Create". Ensure the dropdown is visible.

---
**ALHAMDULILLAH - System State is CLEAN and FUNCTIONAL.**
