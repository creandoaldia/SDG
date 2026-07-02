/**
 * SDG Localidades — Auth Frontend Module
 * Handles: auth status check, login redirect, session keepalive
 */
const AUTH = (() => {
    'use strict';

    let _checkInProgress = false;

    /**
     * Check auth status. If not authenticated, redirect to login.
     * Returns {authenticated, csrf_token} or redirects.
     */
    async function checkAuth() {
        if (_checkInProgress) return { authenticated: false };
        _checkInProgress = true;

        try {
            const res = await fetch('/api/auth/status');
            const data = await res.json();

            if (!data.authenticated) {
                const currentPath = window.location.pathname + window.location.search;
                // Don't redirect if already on login page
                if (!window.location.pathname.includes('/login')) {
                    window.location.href = `/login?next=${encodeURIComponent(currentPath)}`;
                    return { authenticated: false };
                }
            }

            _checkInProgress = false;
            return data;
        } catch (err) {
            _checkInProgress = false;
            console.warn('[Auth] Status check failed:', err);
            return { authenticated: false };
        }
    }

    /**
     * Get CSRF token for POST requests.
     */
    async function getCsrfToken() {
        try {
            const res = await fetch('/api/auth/status');
            const data = await res.json();
            return data.csrf_token || '';
        } catch {
            return '';
        }
    }

    /**
     * Logout: POST to /api/logout, redirect to /login.
     */
    async function logout() {
        try {
            await fetch('/api/logout', { method: 'POST' });
        } catch (_) { /* ignore */ }
        window.location.href = '/login';
    }

    /**
     * Add auth header (CSRF token) to fetch options for POST/PUT/DELETE.
     */
    async function withCsrf(options = {}) {
        const token = await getCsrfToken();
        if (!token) return options;

        const headers = options.headers || {};
        const body = options.body ? JSON.parse(options.body) : {};
        body.csrf_token = token;
        options.body = JSON.stringify(body);
        options.headers = { ...headers, 'Content-Type': 'application/json' };
        return options;
    }

    return {
        checkAuth,
        getCsrfToken,
        logout,
        withCsrf,
    };
})();

// Auto-check auth on page load (for non-login pages)
document.addEventListener('DOMContentLoaded', () => {
    if (!window.location.pathname.includes('/login')) {
        AUTH.checkAuth();
    }
});
