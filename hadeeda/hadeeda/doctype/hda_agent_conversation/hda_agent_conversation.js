// Copyright (c) 2024, Biz Technology Solutions and contributors
// For license information, please see license.txt

frappe.ui.form.on('HDA Agent Conversation', {
    refresh: function (frm) {
        if (!frm.is_new()) {
            // Scroll to bottom of chat
            // This would ideally interact with a custom HTML field for chat history
        }
    },

    send_message: function (frm) {
        if (!frm.doc.message) return;

        frappe.call({
            method: "hadeeda.hadeeda.controllers.agent_controller.chat_with_agent",
            args: {
                agent_name: frm.doc.agent,
                message: frm.doc.message,
                conversation_id: frm.doc.name
            },
            callback: function (r) {
                if (!r.exc) {
                    frm.set_value('message', '');
                    frm.reload_doc();
                }
            }
        });
    }
});
