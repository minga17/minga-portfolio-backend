/**
 * api.js — shared helper for all API calls
 * Auto-detects dev vs production URL.
 */

const API_URL = window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
  ? 'http://localhost:5000'
  : '';   // same origin on Render — no prefix needed

// ── FETCH HELPERS ─────────────────────────────────────────────────────────────

async function apiGet(path) {
  try {
    const res = await fetch(API_URL + path);
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn('API GET failed:', path, err);
    return null;
  }
}

async function apiPost(path, body) {
  try {
    const res = await fetch(API_URL + path, {
      method:  'POST',
      headers: { 'Content-Type': 'application/json' },
      body:    JSON.stringify(body),
    });
    if (!res.ok) throw new Error(`HTTP ${res.status}`);
    return await res.json();
  } catch (err) {
    console.warn('API POST failed:', path, err);
    return null;
  }
}

// ── PUBLIC API ────────────────────────────────────────────────────────────────

const API = {

  /** Fetch all projects, optionally filtered by status or category */
  getProjects(filters = {}) {
    const params = new URLSearchParams(filters).toString();
    return apiGet('/api/projects' + (params ? '?' + params : ''));
  },

  /** Fetch live stats (views, visitors, project counts) */
  getStats() {
    return apiGet('/api/stats');
  },

  /** Log a page view — call once per page load */
  logPageView(page) {
    return apiPost('/api/pageview', { page });
  },

  /** Save a contact form submission */
  submitContact(name, email, message) {
    return apiPost('/api/contact', { name, email, message });
  },
};
