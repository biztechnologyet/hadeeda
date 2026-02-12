# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
import unittest
from hadeeda.hadeeda.controllers.sop_engine import SOPEngine

class TestSOPEngine(unittest.TestCase):
	def test_version_creation(self):
		# Create dummy SOP
		sop = frappe.get_doc({
			"doctype": "HDA SOP Document",
			"title": "Test SOP",
			"sop_id": "SOP-TEST-001",
			"version": "1.0",
			"status": "Draft",
			"category": "HR" # Assuming HR category exists or needs to be created
		})
		# Need category first
		if not frappe.db.exists("HDA SOP Category", "HR"):
			frappe.get_doc({"doctype": "HDA SOP Category", "category_name": "HR"}).insert()
			
		if not frappe.db.exists("HDA SOP Document", "Test SOP"):
			sop.insert()
			
		engine = SOPEngine()
		new_version = engine.create_new_version("Test SOP")
		self.assertEqual(new_version, "1.1")
