# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
import requests
import json

class AIIntegration:
	def __init__(self):
		self.openai_config = frappe.db.get_value("HDA Integration Config", {"integration_type": "OpenAI"}, "config_value")
		self.claude_config = frappe.db.get_value("HDA Integration Config", {"integration_type": "Claude"}, "config_value")

	def call_openai(self, prompt, model="gpt-4"):
		"""
		Calls OpenAI API with the given prompt.
		"""
		if not self.openai_config:
			frappe.throw("OpenAI API key not configured.")
		
		# Placeholder for actual API call
		# response = requests.post(...)
		return "AI response placeholder for: " + prompt[:50] + "..."

	def call_claude(self, prompt, model="claude-3-opus"):
		"""
		Calls Anthropic API with the given prompt.
		"""
		if not self.claude_config:
			frappe.throw("Claude API key not configured.")
			
		return "Claude response placeholder."

	def select_skill_for_task(self, task_description, available_skills):
		"""
		Uses LLM to select the best skill for a task.
		"""
		# TODO: Implement embedding/LLM based selection
		return available_skills[0] if available_skills else None

	def generate_sop_draft(self, process_description):
		"""
		Generates a SOP draft from a description.
		"""
		return f"Title: SOP for {process_description[:20]}\n\n1. Step 1..."

	def analyze_skill_gap(self, required_skills, employee_skills):
		"""
		Analyzes gaps between required and actual skills.
		"""
		return []
