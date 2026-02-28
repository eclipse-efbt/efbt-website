/**
 * Page Allowlist Management
 * Checks if current page is allowed and redirects if not
 */

(function() {
    'use strict';

    // Define allowed pages - add or remove paths as needed
    const ALLOWED_PAGES = [
        '/',
        '/index.html',
        '/documentation.html',
        '/nextgen.html',
        '/freebirdapplication.html',
        '/page-not-available.html',
        '/user-guide/cube-links-view-and-edit.html',
        '/user-guide/execute-datapoint-guide.html',
        '/user-guide/mapping-editor.html',
        '/user-guide/member-hierarchy-editor.html',
        '/user-guide/pull-request-creation-guide.html',
        '/user-guide/workflow-dashboard-guide.html',
        '/user-guide/dpm-operations-guide.html',
        '/workflow/task.html'
    ];

    // Get current page path
    const currentPath = window.location.pathname;

    // Normalize path (remove trailing slash, handle relative paths)
    const normalizedPath = currentPath.endsWith('/') && currentPath.length > 1
        ? currentPath.slice(0, -1)
        : currentPath;

    // Check if current page is in allowlist
    const isAllowed = ALLOWED_PAGES.some(allowedPath => {
        // Handle exact matches
        if (normalizedPath === allowedPath) return true;

        // Handle relative paths (for pages in subdirectories)
        if (normalizedPath.endsWith(allowedPath)) return true;

        return false;
    });

    // If page is not allowed, redirect immediately
    if (!isAllowed) {
        // Prevent any content from showing
        if (document.documentElement) {
            document.documentElement.style.display = 'none';
        }

        // Redirect to construction page or main documentation
        const redirectUrl = window.location.origin + '/page-not-available.html';

        // Try to redirect to construction page, fallback to documentation
        window.location.replace(redirectUrl);

        // Fallback if redirect fails
        setTimeout(function() {
            window.location.replace(window.location.origin + '/documentation.html');
        }, 100);
    }
})();