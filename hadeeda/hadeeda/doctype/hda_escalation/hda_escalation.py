# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HDAEscalation(Document):
	def validate(self):
		if self.status == "Resolved" and not self.resolution_date:
			self.resolution_date = frappe.utils.now_datetime()
