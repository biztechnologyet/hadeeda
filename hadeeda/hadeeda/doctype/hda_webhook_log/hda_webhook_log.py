# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HDAWebhookLog(Document):
	def before_insert(self):
		if not self.timestamp:
			self.timestamp = frappe.utils.now_datetime()
