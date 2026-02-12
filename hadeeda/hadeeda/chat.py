import frappe

@frappe.whitelist(allow_guest=True)
def get_chat_js():
    """Serve the Hadeeda n8n Chat Widget JavaScript"""
    js_content = """
// Hadeeda n8n Chat Widget - Dynamic Asset
(function() {
    // Load n8n chat CSS
    var link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/style.css';
    document.head.appendChild(link);

    // Load n8n chat JS and initialize
    var script = document.createElement('script');
    script.type = 'module';
    script.textContent = `
        import { createChat } from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';
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
    `;
    document.head.appendChild(script);
})();
"""
    frappe.response['type'] = 'text'
    frappe.response['text'] = js_content
    frappe.response['headers'] = {
        'Content-Type': 'application/javascript'
    }

@frappe.whitelist(allow_guest=True)
def get_chat_css():
    """Serve the Hadeeda Chat Widget CSS"""
    css_content = """
/* Hadeeda Chat Widget Styles */
.n8n-chat-widget {
    z-index: 10001 !important;
    --chat--color-primary: #0d6efd;
    --chat--color-secondary: #0b5ed7;
}
"""
    frappe.response['type'] = 'text'
    frappe.response['text'] = css_content
    frappe.response['headers'] = {
        'Content-Type': 'text/css'
    }

