# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HDASOPApprovalWorkflow(Document):
	def validate(self):
		if self.status in ["Approved", "Rejected"] and not self.action_date:
			self.action_date = frappe.utils.now_datetime()
