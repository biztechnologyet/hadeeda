# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class HDAAgent(Document):
	def validate(self):
		self.validate_model_config()

	def validate_model_config(self):
		if self.ai_model == "Custom" and not self.system_prompt:
			frappe.msgprint("System Prompt is recommended for Custom models.", alert=True)

	def before_save(self):
		pass
