/**
 * User Guides Dynamic Loader
 * Dynamically loads and displays user guides from the index.json file
 */

class UserGuidesLoader {
    constructor() {
        this.guidesContainer = null;
        this.loadingElement = null;
        this.errorElement = null;
        this.guides = [];
    }

    /**
     * Initialize the user guides loader
     */
    init() {
        // Wait for DOM to be ready
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', () => this.loadGuides());
        } else {
            this.loadGuides();
        }
    }

    /**
     * Load guides from the index.json file
     */
    async loadGuides() {
        console.log('UserGuidesLoader: Loading guides...');

        this.guidesContainer = document.getElementById('dynamic-user-guides');

        if (!this.guidesContainer) {
            console.error('User guides container with id "dynamic-user-guides" not found');
            return;
        }

        // Show loading state
        this.showLoading();

        try {
            const response = await fetch('user_guide/index.json');

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            this.guides = data.guides || [];
            console.log(`Found ${this.guides.length} guides`);

            // Log disabled guides
            const disabledCount = this.guides.filter(g => g.disabled === true || g.status === 'coming_soon').length;
            if (disabledCount > 0) {
                console.log(`${disabledCount} guides are disabled/coming soon`);
            }

            // Clear loading state and render guides
            this.clearLoading();
            this.renderGuides();

        } catch (error) {
            console.error('Error loading user guides:', error);
            this.showError();
        }
    }

    /**
     * Show loading state
     */
    showLoading() {
        this.guidesContainer.innerHTML = `
            <div class="loading-guides text-center">
                <div class="loading-spinner">
                    <i class="icon-refresh animate-spin" style="font-size: 24px; color: #f92672;"></i>
                </div>
                <p style="margin-top: 10px; color: #666;">Loading user guides...</p>
            </div>
        `;
    }

    /**
     * Show error state
     */
    showError() {
        this.guidesContainer.innerHTML = `
            <div class="error-guides text-center">
                <div class="error-icon">
                    <i class="icon-alert-circle" style="font-size: 24px; color: #e74c3c;"></i>
                </div>
                <p style="margin-top: 10px; color: #666;">
                    Unable to load user guides. Please check back later.
                </p>
            </div>
        `;
    }

    /**
     * Clear loading state
     */
    clearLoading() {
        this.guidesContainer.innerHTML = '';
    }

    /**
     * Render the user guides
     */
    renderGuides() {
        console.log('🎨 Starting to render guides...');

        if (!this.guides || this.guides.length === 0) {
            console.log('📭 No guides to render, showing empty state');
            this.renderEmptyState();
            return;
        }


        const guidesHtml = `
            <div class="user-guides-grid">
                ${this.guides.map(guide => this.createGuideMiniature(guide)).join('')}
            </div>
        `;

        this.guidesContainer.innerHTML = guidesHtml;
    }

    /**
     * Render empty state when no guides are available
     */
    renderEmptyState() {
        this.guidesContainer.innerHTML = `
            <div class="empty-guides text-center">
                <div class="empty-icon">
                    <i class="ti-book" style="font-size: 48px; color: #ccc;"></i>
                </div>
                <p style="margin-top: 20px; color: #666;">
                    No user guides available yet. Check back soon!
                </p>
            </div>
        `;
    }

    /**
     * Create HTML for a single guide miniature card
     * @param {Object} guide - Guide metadata object
     * @returns {string} HTML string for the guide miniature
     */
    createGuideMiniature(guide) {
        const truncatedDescription = this.truncateText(guide.description, 150);
        const formattedDate = this.formatDate(guide.last_modified);
        const guideIcon = this.getGuideIcon(guide.slug);
        const isDisabled = guide.disabled === true || guide.status === 'coming_soon';

        // Different styling and behavior for disabled guides
        const linkClass = isDisabled ? 'user-guide-miniature disabled' : 'user-guide-miniature';
        const badgeText = isDisabled ? 'Coming Soon' : 'Available Now';
        const badgeClass = isDisabled ? 'miniature-badge coming-soon' : 'miniature-badge available';
        const iconClass = isDisabled ? `${guideIcon} disabled-icon` : guideIcon;
        // For disabled guides, use a div instead of a link to make them non-clickable
        const elementTag = isDisabled ? 'div' : 'a';
        const hrefAttribute = isDisabled ? '' : `href="${guide.path}"`;

        return `
            <${elementTag} ${hrefAttribute} class="${linkClass}">
                <div class="miniature-header">
                    <div class="miniature-icon ${isDisabled ? 'disabled' : ''}">
                        <i class="${iconClass}"></i>
                        ${isDisabled ? '<i class="ti-clock overlay-icon"></i>' : ''}
                    </div>
                    <div class="miniature-title-area">
                        <h4 class="miniature-title">${this.escapeHtml(guide.title)}</h4>
                        <span class="${badgeClass}">${badgeText}</span>
                    </div>
                </div>

                <p class="miniature-description ${isDisabled ? 'disabled' : ''}">
                    ${this.escapeHtml(truncatedDescription)}
                </p>

                <div class="miniature-footer ${isDisabled ? 'disabled' : ''}">
                    <div class="miniature-meta">
                        <i class="ti-calendar"></i>
                        ${isDisabled ? 'Coming Soon' : `Updated ${formattedDate}`}
                    </div>
                    <div class="miniature-arrow">
                        <i class="${isDisabled ? 'ti-clock' : 'ti-arrow-right'}"></i>
                    </div>
                </div>
            </${elementTag}>
        `;
    }

    /**
     * Get appropriate icon for guide based on its slug/type
     * @param {string} slug - Guide slug
     * @returns {string} Icon class name
     */
    getGuideIcon(slug) {
        const iconMap = {
            'getting_started': 'ti-rocket',
            'getting-started': 'ti-rocket',
            'api_reference': 'ti-code',
            'api-reference': 'ti-code',
            'data_models': 'ti-database',
            'data-models': 'ti-database',
            'dataset_transformation': 'ti-exchange-vertical',
            'dataset-transformation': 'ti-exchange-vertical',
            'workflow_dashboard': 'ti-dashboard',
            'workflow-dashboard': 'ti-dashboard',
            'pull_request_guide': 'ti-git',
            'pull-request-guide': 'ti-git',
            'execute_datapoint': 'ti-play',
            'execute-datapoint': 'ti-play',
            'dpm_operations': 'ti-layers',
            'dpm-operations': 'ti-layers',
            'transformations': 'ti-settings',
            'installation': 'ti-download',
            'configuration': 'ti-settings',
            'troubleshooting': 'ti-help',
            'examples': 'ti-lightbulb',
            'tutorial': 'ti-book',
            'advanced': 'ti-star'
        };

        return iconMap[slug] || 'ti-book';
    }

    /**
     * Truncate text to specified length
     * @param {string} text - Text to truncate
     * @param {number} maxLength - Maximum length
     * @returns {string} Truncated text
     */
    truncateText(text, maxLength) {
        if (!text || text.length <= maxLength) {
            return text || '';
        }
        return text.substr(0, maxLength).trim() + '...';
    }

    /**
     * Format date for display
     * @param {string} dateString - ISO date string
     * @returns {string} Formatted date
     */
    formatDate(dateString) {
        try {
            const date = new Date(dateString);
            const now = new Date();
            const diffTime = Math.abs(now - date);
            const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

            if (diffDays === 0) {
                return 'today';
            } else if (diffDays === 1) {
                return 'yesterday';
            } else if (diffDays < 7) {
                return `${diffDays} days ago`;
            } else if (diffDays < 30) {
                const weeks = Math.floor(diffDays / 7);
                return `${weeks} week${weeks > 1 ? 's' : ''} ago`;
            } else {
                return date.toLocaleDateString('en-US', {
                    year: 'numeric',
                    month: 'short',
                    day: 'numeric'
                });
            }
        } catch (error) {
            console.error('Error formatting date:', error);
            return 'recently';
        }
    }

    /**
     * Escape HTML to prevent XSS
     * @param {string} text - Text to escape
     * @returns {string} Escaped text
     */
    escapeHtml(text) {
        if (!text) return '';
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Initialize the user guides loader
const userGuidesLoader = new UserGuidesLoader();
userGuidesLoader.init();
