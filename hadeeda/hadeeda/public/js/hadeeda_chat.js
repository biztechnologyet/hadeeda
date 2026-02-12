// Hadeeda n8n Chat Widget
import { createChat } from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';

$(document).ready(function () {
    // Initialize the n8n Chat Widget (Floating Bottom-Right)
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
