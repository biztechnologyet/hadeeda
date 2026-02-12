# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import uuid

class HDAAgentConversation(Document):
	def before_insert(self):
		if not self.conversation_id:
			self.conversation_id = str(uuid.uuid4())
