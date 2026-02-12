# -*- coding: utf-8 -*-
# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
import os
import sys

def import_skills(path):
	"""
	Imports skills from a directory.
	Each subdirectory in the path is treated as a skill if it contains SKILL.md.
	"""
	if not os.path.isdir(path):
		print(f"Error: Path {path} is not a directory.")
		return

	count = 0
	for item in os.listdir(path):
		skill_path = os.path.join(path, item)
		if os.path.isdir(skill_path):
			skill_md = os.path.join(skill_path, "SKILL.md")
			if os.path.exists(skill_md):
				print(f"Importing skill: {item}...")
				# TODO: Integrate with SkillEngine.import_skill logic
				# For now, just a placeholder
				count += 1
	
	print(f"Successfully imported {count} skills.")

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: python import_skills.py [path_to_skills]")
	else:
		frappe.init(site="frontend")
		try:
			frappe.connect()
			import_skills(sys.argv[1])
		finally:
			frappe.destroy()
