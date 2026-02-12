# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns = [
		{"fieldname": "sop_document", "label": "SOP Document", "fieldtype": "Link", "options": "HDA SOP Document", "width": 200},
		{"fieldname": "compliance_score", "label": "Compliance Score", "fieldtype": "Float", "width": 120},
		{"fieldname": "status", "label": "Status", "fieldtype": "Data", "width": 120},
		{"fieldname": "check_date", "label": "Check Date", "fieldtype": "Date", "width": 120}
	]
	
	data = frappe.db.get_all("HDA SOP Compliance Check", 
		fields=["sop_document", "compliance_score", "status", "check_date"],
		filters=filters
	)
	
	return columns, data
