# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HDAAICostTracking(Document):
	def before_save(self):
		if self.input_tokens and self.output_tokens and self.cost_per_token:
			self.total_cost = (self.input_tokens + self.output_tokens) * self.cost_per_token
