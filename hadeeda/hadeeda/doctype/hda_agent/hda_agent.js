// Copyright (c) 2024, Biz Technology Solutions and contributors
// For license information, please see license.txt

frappe.ui.form.on('HDA Agent', {
	refresh: function (frm) {
		if (!frm.is_new()) {
			frm.add_custom_button(__('Chat with Agent'), function () {
				frappe.new_doc('HDA Agent Conversation', {
					agent: frm.doc.name,
					user: frappe.session.user
				});
			});

			frm.add_custom_button(__('Assign Task'), function () {
				frappe.new_doc('HDA Task Assignment', {
					assigned_agent: frm.doc.name
				});
			});
		}
	}
});
