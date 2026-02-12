# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import scrub

class HDASkill(Document):
	def validate(self):
		if not self.skill_id:
			self.skill_id = scrub(self.skill_name)
