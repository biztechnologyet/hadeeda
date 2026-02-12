# Copyright (c) 2024, Biz Technology Solutions and contributors
# For license information, please see license.txt

import frappe
from frappe.utils import now_datetime
import json

class AgentController:
	def assign_task_to_agent(self, task):
		"""
		Assigns a task to the most suitable agent based on the task description and type.
		"""
		# TODO: Implement intelligent agent selection logic (AI-based)
		agent_name = self.select_agent_for_task(task.description, task.type)
		
		if agent_name:
			assignment = frappe.get_doc({
				"doctype": "HDA Task Assignment",
				"task": task.name,
				"assigned_agent": agent_name,
				"status": "Assigned",
				"assignment_reason": "AI matched task description to agent role.",
				"confidence_score": 0.95 # Placeholder
			})
			assignment.insert()
			return assignment
		else:
			return None

	def select_agent_for_task(self, task_description, task_type):
		"""
		Selects an agent based on rules or AI.
		"""
		# Simple rule-based selection for now
		agents = frappe.get_all("HDA Agent", fields=["name", "role", "description"], filters={"is_active": 1})
		
		for agent in agents:
			if task_type and task_type.lower() in agent.role.lower():
				return agent.name
			# TODO: deeper analysis using embeddings/LLM
			
		return agents[0].name if agents else None

	def execute_agent_action(self, agent_name, action, params):
		"""
		Executes an action via the agent (calling tools/skills).
		"""
		# TODO: Integrate with SkillEngine
		pass

	def escalate_to_human(self, task, reason):
		"""
		Creates an escalation record.
		"""
		escalation = frappe.get_doc({
			"doctype": "HDA Escalation",
			"original_task": task.name,
			"reason": reason,
			"priority": "High",
			"status": "Open"
		})
		escalation.insert()
		return escalation

	def generate_insights(self):
		"""
		Periodic job to generate insights from data.
		"""
		pass
