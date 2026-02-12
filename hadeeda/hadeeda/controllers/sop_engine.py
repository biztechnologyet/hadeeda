# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
import json

class SOPEngine:
	def create_new_version(self, sop_name):
		"""
		Creates a new version of an SOP document.
		"""
		sop = frappe.get_doc("HDA SOP Document", sop_name)
		
		# Create snapshot in Revision History
		revision = frappe.get_doc({
			"doctype": "HDA SOP Revision History",
			"sop_document": sop.name,
			"version": int(float(sop.version)),
			"revision_date": frappe.utils.nowdate(),
			"revised_by": frappe.session.user,
			"content": sop.content,
			"status": sop.status
		})
		revision.insert()
		
		# Increment main doc version
		new_version = float(sop.version) + 0.1
		sop.version = str(round(new_version, 1))
		sop.status = "Draft"
		sop.save()
		
		return sop.version

	def check_compliance(self, sop_name):
		"""
		Runs a compliance check on an SOP.
		"""
		# Placeholder logic for compliance checking
		# In future, this could use AI to check against standards
		return {"status": "Compliant", "score": 100}
