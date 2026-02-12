# -*- coding: utf-8 -*-
# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
import sys

def export_skill(skill_name, output_path):
	"""
	Exports a skill to a specified path.
	"""
	# TODO: Integrate with SkillEngine.export_skill logic
	print(f"Exporting skill {skill_name} to {output_path}...")

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print("Usage: python export_skill.py [skill_name] [output_path]")
	else:
		frappe.init(site="frontend")
		try:
			frappe.connect()
			export_skill(sys.argv[1], sys.argv[2])
		finally:
			frappe.destroy()
