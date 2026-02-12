# -*- coding: utf-8 -*-
# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
import sys

def import_sops(path):
	"""
	Imports SOPs from a directory.
	"""
	# TODO: Implement SOP import logic
	print(f"Importing SOPs from {path}...")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python import_sops.py [path_to_sops]")
	else:
		frappe.init(site="frontend")
		try:
			frappe.connect()
			import_sops(sys.argv[1])
		finally:
			frappe.destroy()
