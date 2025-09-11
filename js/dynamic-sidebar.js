/**
 * Dynamic Sidebar Generator
 * Generates sidebar navigation based on the current page
 */

class DynamicSidebar {
    constructor() {
        this.currentPath = window.location.pathname;
        this.currentPage = this.getCurrentPageType();
        this.isUserGuide = this.currentPath.includes('/user_guide/');
        this.pathPrefix = this.getPathPrefix();
    }

    /**
     * Initialize the dynamic sidebar
     */
    init() {
        // Add CSS styles first
        this.addStyles();

        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.render());
        } else {
            this.render();
        }
    }

    /**
     * Add required CSS styles for the dynamic sidebar
     */
    addStyles() {
        const styleId = 'dynamic-sidebar-styles';

        // Check if styles already exist
        if (document.getElementById(styleId)) {
            return;
        }

        const style = document.createElement('style');
        style.id = styleId;
        style.textContent = `
            /* Dynamic Sidebar Styles */
            .sidenav {
                height: 100vh;
                width: 200px;
                position: fixed;
                z-index: 1000;
                top: 0;
                left: 0;
                background: #16381f;
                overflow-x: hidden;
                overflow-y: auto;
                padding: 20px 0 30px 0;
                box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1);
                border-right: 1px solid rgba(0, 0, 0, 0.1);
                display: flex;
                flex-direction: column;
            }

            .sidenav a {
                padding: 12px 16px 12px 24px;
                text-decoration: none;
                font-size: 16px;
                font-weight: 500;
                color: rgba(255, 255, 255, 0.7);
                display: block;
                transition: all 0.3s ease;
                border-left: 3px solid transparent;
                margin: 2px 0;
                position: relative;
            }

            .sidenav a:hover {
                color: #ffffff;
                background: rgba(255, 255, 255, 0.1);
                border-left-color: #ffffff;
                transform: translateX(5px);
            }

            .sidenav a.active {
                color: #ffffff;
                background: rgba(255, 255, 255, 0.15);
                border-left-color: #ffffff;
                font-weight: 600;
            }

            .sidenav a:before {
                content: '';
                position: absolute;
                left: 0;
                top: 0;
                bottom: 0;
                width: 3px;
                background: #ffffff;
                transform: scaleY(0);
                transition: transform 0.3s ease;
            }

            .sidenav a:hover:before,
            .sidenav a.active:before {
                transform: scaleY(1);
            }

            .sidenav i {
                margin-right: 8px;
                font-size: 14px;
                opacity: 0.9;
                color: rgba(255, 255, 255, 0.9);
            }

            /* Sidebar trademark */
            .sidenav-trademark {
                padding: 20px 24px;
                border-bottom: 1px solid rgba(255, 255, 255, 0.1);
                color: white;
                font-size: 25px;
                line-height: 1.4;
                text-align: center;
                background: transparent;
            }

            .sidenav-trademark .trademark-title {
                font-weight: 600;
                color: #ffffff;
                text-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
            }

            .sidenav-trademark .trademark-text {
              font-size: 12px;
                opacity: 0.8;
            }

            /* Main content adjustment - handled in style.css */

            /* Navbar adjustment to prevent overlap */
            .gtco-nav {
                margin-left: 200px;
                background: white;
                border-bottom: 1px solid #e9ecef;
            }

            .gtco-nav .gtco-container {
                max-width: calc(1140px - 200px);
            }

            /* On smaller screens, adjust sidebar */
            @media screen and (max-height: 450px) {
                .sidenav {
                    padding: 15px 0;
                }
                .sidenav a {
                    font-size: 14px;
                    padding: 8px 16px 8px 20px;
                }
            }

            /* On mobile screens, hide the sidebar and adjust main content */
            @media screen and (max-width: 768px) {
                .sidenav {
                    display: none;
                }

                .main {
                    margin-left: 0;
                }

                .gtco-nav {
                    margin-left: 0;
                }

                .gtco-nav .gtco-container {
                    max-width: 1140px;
                }
            }

            /* Adjust TOC positioning when main sidebar is present */
            .guide-toc-container {
                left: 220px !important;
            }

            @media screen and (max-width: 768px) {
                .guide-toc-container {
                    left: 15px !important;
                }
            }
        `;

        document.head.appendChild(style);
    }

    /**
     * Get the current page type based on URL
     */
    getCurrentPageType() {
        const path = this.currentPath.toLowerCase();

        if (path.includes('index.html') || path.endsWith('/')) {
            return 'home';
        } else if (path.includes('freebirdapplication.html')) {
            return 'freebird';
        } else if (path.includes('documentation.html')) {
            return 'documentation';
        } else if (path.includes('/user_guide/')) {
            return 'userguide';
        }

        return 'default';
    }

    /**
     * Get the appropriate path prefix based on current location
     */
    getPathPrefix() {
        if (this.isUserGuide) {
            return '../';
        }
        return '';
    }

    /**
     * Generate sidebar configuration based on page type
     */
    getSidebarConfig() {
        const configs = {
            home: {
                title: 'Navigation',
                items: [
                    { text: 'About', href: '#about', icon: 'ti-info' },
                    { text: 'FreeBIRD', href: '#freebird', icon: 'ti-package' },
                    { text: 'What is BIRD', href: '#what-is-bird', icon: 'ti-help' },
                    { text: 'GitHub', href: 'https://github.com/eclipse/efbt', icon: 'ti-github', target: '_blank' }
                ]
            },
            freebird: {
                title: 'FreeBIRD App',
                items: [
                    { text: 'Home', href: `${this.pathPrefix}index.html`, icon: 'ti-home' },
                    { text: 'Overview', href: '#overview', icon: 'ti-eye' },
                    { text: 'Features', href: '#features', icon: 'ti-star' },
                    { text: 'Getting Started', href: '#getting-started', icon: 'ti-rocket' },
                    { text: 'Documentation', href: `${this.pathPrefix}documentation.html`, icon: 'ti-book' },
                    { text: 'GitHub', href: 'https://github.com/eclipse/efbt', icon: 'ti-github', target: '_blank' }
                ]
            },
            documentation: {
                title: 'Documentation',
                items: [
                    { text: 'Quick Start', href: '#quickstart', icon: 'ti-rocket' },
                    { text: 'User Guides', href: '#user-guides', icon: 'ti-bookmark' },
                    { text: 'Feedback', href: '#feedback', icon: 'ti-comment' },
                    { text: 'GitHub', href: 'https://github.com/eclipse/efbt', icon: 'ti-github', target: '_blank' }
                ]
            },
            userguide: {
                title: 'User Guide',
                items: [
                    { text: 'All Guides', href: `${this.pathPrefix}documentation.html#user-guides`, icon: 'ti-list' },
                    ...this.getGuideSpecificItems(),
                    { text: 'GitHub', href: 'https://github.com/eclipse/efbt', icon: 'ti-github', target: '_blank' }
                ]
            },
            default: {
                title: 'Navigation',
                items: [
                    { text: 'Home', href: `${this.pathPrefix}index.html`, icon: 'ti-home' },
                    { text: 'FreeBIRD App', href: `${this.pathPrefix}freebirdapplication.html`, icon: 'ti-package' },
                    { text: 'Documentation', href: `${this.pathPrefix}documentation.html`, icon: 'ti-book' },
                    { text: 'GitHub', href: 'https://github.com/eclipse/efbt', icon: 'ti-github', target: '_blank' }
                ]
            }
        };

        return configs[this.currentPage] || configs.default;
    }

    /**
     * Get guide-specific navigation items based on current guide
     */
    getGuideSpecificItems() {
        const filename = this.currentPath.split('/').pop();
        const guideItems = [];

        // Add common guide sections
        const sections = this.detectPageSections();
        sections.forEach(section => {
            guideItems.push({
                text: section.text,
                href: section.href,
                icon: 'ti-angle-right'
            });
        });

        return guideItems;
    }

    /**
     * Detect sections in the current page for navigation
     */
    detectPageSections() {
        const sections = [];

        // Try to find headings in the page
        const headings = document.querySelectorAll('h1, h2, h3');
        headings.forEach((heading, index) => {
            if (heading.id) {
                // Only include h1 and h2 in sidebar navigation
                if (heading.tagName === 'H1' || heading.tagName === 'H2') {
                    sections.push({
                        text: heading.textContent.trim(),
                        href: `#${heading.id}`
                    });
                }
            }
        });

        // If no headings found, provide default sections
        if (sections.length === 0) {
            sections.push(
                { text: 'Overview', href: '#overview' },
                { text: 'Getting Started', href: '#getting-started' },
                { text: 'Configuration', href: '#configuration' },
                { text: 'Usage', href: '#usage' }
            );
        }

        return sections;
    }

    /**
     * Render the sidebar
     */
    render() {
        const config = this.getSidebarConfig();
        const sidebarHTML = this.generateSidebarHTML(config);

        // Insert sidebar after header
        const header = document.querySelector('header');
        if (header) {
            header.insertAdjacentHTML('afterend', sidebarHTML);
        }

        // Add event listeners for smooth scrolling
        this.addSmoothScrolling();

        // Highlight active section
        this.highlightActiveSection();
    }

    /**
     * Generate the sidebar HTML
     */
    generateSidebarHTML(config) {
        const itemsHTML = config.items.map(item => {
            const target = item.target ? ` target="${item.target}"` : '';
            const icon = item.icon ? `<i class="${item.icon}"></i> ` : '';

            return `<a href="${item.href}"${target}>${icon}${item.text}</a>`;
        }).join('');

        const trademarkHTML = `
            <div class="sidenav-trademark">
                <div class="trademark-title">ECLIPSE FREE BIRD TOOLS&trade;</div>
            </div>
        `;

        return `
            <div class="sidenav" id="dynamicSidebar">
              ${trademarkHTML}
                <div class="sidenav-navigation">
                    ${itemsHTML}
                </div>

            </div>
        `;
    }

    /**
     * Add smooth scrolling to anchor links
     */
    addSmoothScrolling() {
        const sidebar = document.getElementById('dynamicSidebar');
        if (!sidebar) return;

        sidebar.addEventListener('click', (e) => {
            const link = e.target.closest('a');
            if (!link) return;

            const href = link.getAttribute('href');
            if (href && href.startsWith('#')) {
                e.preventDefault();

                const targetElement = document.querySelector(href);
                if (targetElement) {
                    const headerOffset = 100;
                    const elementPosition = targetElement.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - headerOffset;

                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });

                    // Update active state
                    this.updateActiveLink(link);
                }
            }
        });
    }

    /**
     * Highlight the active section based on scroll position
     */
    highlightActiveSection() {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.id;
                    if (id) {
                        const activeLink = document.querySelector(`.sidenav a[href="#${id}"]`);
                        if (activeLink) {
                            this.updateActiveLink(activeLink);
                        }
                    }
                }
            });
        }, {
            rootMargin: '-20% 0px -70% 0px'
        });

        // Observe all elements with IDs
        document.querySelectorAll('[id]').forEach(element => {
            observer.observe(element);
        });
    }

    /**
     * Update the active link styling
     */
    updateActiveLink(activeLink) {
        // Remove active class from all sidebar links
        document.querySelectorAll('.sidenav a').forEach(link => {
            link.classList.remove('active');
        });

        // Add active class to current link
        if (activeLink) {
            activeLink.classList.add('active');
        }
    }
}

// Initialize the dynamic sidebar
const dynamicSidebar = new DynamicSidebar();
dynamicSidebar.init();
