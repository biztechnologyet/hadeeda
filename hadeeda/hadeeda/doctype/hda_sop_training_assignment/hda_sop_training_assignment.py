# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HDASOPTrainingAssignment(Document):
	def validate(self):
		if self.status == "Completed" and not self.completion_date:
			self.completion_date = frappe.utils.nowdate()
