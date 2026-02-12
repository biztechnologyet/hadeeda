# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HDAInsight(Document):
	def validate(self):
		if self.status == "Acknowledged" and not self.acknowledged_on:
			self.acknowledged_on = frappe.utils.now_datetime()
			self.acknowledged_by = frappe.session.user
