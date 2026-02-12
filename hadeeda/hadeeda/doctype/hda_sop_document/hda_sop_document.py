# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HDASOPDocument(Document):
	def autoname(self):
		from frappe.model.naming import set_name_by_naming_series
		# Ensure SOP Numbering e.g. SOP-.category.-.####
		if not self.sop_number:
			self.sop_number = set_name_by_naming_series(self, "naming_series", 
				f"SOP-{self.category}-", "0001")
		self.name = self.sop_number

	def before_insert(self):
		if not self.version:
			self.version = "1.0"
		if not self.status:
			self.status = "Draft"

	def on_update(self):
		# Sync logic if needed
		pass
