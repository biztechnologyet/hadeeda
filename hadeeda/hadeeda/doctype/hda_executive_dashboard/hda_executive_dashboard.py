# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HDAExecutiveDashboard(Document):
	def before_save(self):
		self.last_modified = frappe.utils.now_datetime()
