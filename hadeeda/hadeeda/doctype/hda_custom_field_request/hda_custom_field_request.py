# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import scrub

class HDACustomFieldRequest(Document):
	def validate(self):
		if self.label and not self.fieldname:
			self.fieldname = scrub(self.label)
