# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HDATaskAssignment(Document):
	def validate(self):
		if self.status == "Completed" and not self.actual_completion:
			self.actual_completion = frappe.utils.now_datetime()
