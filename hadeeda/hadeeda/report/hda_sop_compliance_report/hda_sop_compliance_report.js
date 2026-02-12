// Copyright (c) 2024, Biz Technology Solutions and contributors
// For license information, please see license.txt

frappe.query_reports["HDA SOP Compliance Report"] = {
    "filters": [
        {
            "fieldname": "sop_document",
            "label": "SOP Document",
            "fieldtype": "Link",
            "options": "HDA SOP Document"
        }
    ]
};
