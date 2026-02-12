// Hadeeda n8n Chat Widget
import { createChat } from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';

$(document).on('ready', function () {
    createChat({
        webhookUrl: 'https://bizflow.ethiobiz.et/webhook/7b0414e6-dda5-4113-bd85-b913f5b96bf9/chat',
        mode: 'window',
        showWelcomeScreen: true,
        title: 'Hadeeda AI',
        subtitle: 'How can I help you today?',
        initialMessages: [
            'BISMALLAH! I am Hadeeda, your AI Chief of Staff.',
            'How can I assist you with your ERPNext tasks today?'
        ],
        theme: {
            button: {
                backgroundColor: '#0d6efd',
            }
        }
    });
});
