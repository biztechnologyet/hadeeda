// Hadeeda n8n Chat Widget
import { createChat } from 'https://cdn.jsdelivr.net/npm/@n8n/chat/dist/chat.bundle.es.js';

$(document).on('ready', function () {
    // 1. Initialize the Chat Widget but keep it hidden initially
    const chat = createChat({
        webhookUrl: 'https://bizflow.ethiobiz.et/webhook/7b0414e6-dda5-4113-bd85-b913f5b96bf9/chat',
        showWelcomeScreen: true,
        title: 'Hadeeda AI',
        subtitle: 'How can I assist you with your DOBiz tasks?',
        initialMessages: [
            'BISMALLAH! I am Hadeeda, your AI Chief of Staff.',
            'How can I help you today?'
        ]
    });

    // 2. Inject Button into Navbar
    function injectNavbarButton() {
        if ($('#hadeeda-nav-item').length) return;

        const navbarNav = $('.navbar .navbar-nav');
        if (!navbarNav.length) return;

        const chatButtonHtml = `
            <li class="nav-item dropdown" id="hadeeda-nav-item">
                <button class="btn-reset nav-link" id="hadeeda-chat-toggle" title="Chat with Hadeeda AI">
                    <span class="hadeeda-icon">🤖</span>
                </button>
            </li>
        `;

        // Insert after the account menu (dropdown-navbar-user)
        const userMenu = navbarNav.find('.dropdown-navbar-user');
        if (userMenu.length) {
            $(chatButtonHtml).insertAfter(userMenu);
        } else {
            navbarNav.append(chatButtonHtml);
        }

        // Toggle chat on click
        $('#hadeeda-chat-toggle').on('click', function (e) {
            e.preventDefault();
            const widget = document.querySelector('.n8n-chat-widget');
            if (widget) {
                widget.classList.toggle('hadeeda-chat-visible');
            }
        });
    }

    // Try injecting immediately and also on a timer in case of SPA navigation
    injectNavbarButton();
    setInterval(injectNavbarButton, 2000);
});
