import frappe

@frappe.whitelist(allow_guest=True)
def get_chat_js():
    frappe.response.headers["Content-Type"] = "application/javascript"
    return """
// Hadeeda n8n Chat Widget
import { createChat } from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';

$(document).ready(function() {
    createChat({
        webhookUrl: 'https://bizflow.ethiobiz.et/webhook/7b0414e6-dda5-4113-bd85-b913f5b96bf9/chat',
        showWelcomeScreen: true,
        title: 'Hadeeda AI',
        subtitle: 'How can I assist you with your DOBiz tasks?',
        initialMessages: [
            'BISMALLAH! I am Hadeeda, your AI Chief of Staff.',
            'How can I help you today?'
        ],
        i18n: {
            en: {
                title: 'Hadeeda AI',
                subtitle: 'AI Chief of Staff'
            }
        }
    });
});
    """

@frappe.whitelist(allow_guest=True)
def get_chat_css():
    frappe.response.headers["Content-Type"] = "text/css"
    return """
/* Custom styling for Hadeeda Chat */
@import url('https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css');

.n8n-chat-widget {
    z-index: 10001 !important;
    --chat--color-primary: #0d6efd;
    --chat--color-secondary: #0b5ed7;
}
    """
