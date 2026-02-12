# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HDASkillApproval(Document):
	def validate(self):
		if self.status == "Approved" and not self.approval_date:
			self.approval_date = frappe.utils.now_datetime()
			self.approved_by = frappe.session.user
