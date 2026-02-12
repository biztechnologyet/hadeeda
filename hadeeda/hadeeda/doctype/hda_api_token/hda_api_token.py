# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import secrets

class HDAAPIToken(Document):
	def before_insert(self):
		self.token = secrets.token_urlsafe(32)
