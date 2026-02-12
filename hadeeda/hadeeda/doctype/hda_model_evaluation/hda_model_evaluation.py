# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HDAModelEvaluation(Document):
	def before_insert(self):
		if not self.evaluation_date:
			self.evaluation_date = frappe.utils.now_datetime()
