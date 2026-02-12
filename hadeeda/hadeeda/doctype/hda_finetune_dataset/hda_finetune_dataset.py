# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
import json

class HDAFineTuneDataset(Document):
	def validate(self):
		if self.records:
			try:
				records_data = json.loads(self.records) if isinstance(self.records, str) else self.records
				self.record_count = len(records_data)
			except Exception:
				pass
