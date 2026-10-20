// Ace Education service worker. Safe on GitHub Pages sub-paths (everything is relative to this file).
// - App shell: network first with a 4-second fallback to the cache, so a deploy reaches students on their next load.
// - Syllabus files (*-syllabus.html, 1-2 MB each): cached the first time a country is opened, then served
//   instantly and refreshed in the background. Students can study that country offline afterwards.
// - Supabase and edge-function calls are never cached or intercepted (auth, answers and AI must be live).
// - Bump VERSION only to force a full cache reset.
const VERSION = 'v16';
const SHELL = 'ace-shell-' + VERSION;
const DATA = 'ace-syllabus-' + VERSION;
const PRECACHE = ['./', 'index.html', 'manifest.webmanifest', 'icon.svg', 'today.js', 'learn.js', 'class.js', 'learner.js', 'ui.js', 'ui.css', 'campus.js', 'campus.css', 'chat.js', 'files.js', 'friends.js'];

self.addEventListener('install', e => {
  e.waitUntil(caches.open(SHELL).then(c => c.addAll(PRECACHE)).then(() => self.skipWaiting()));
});
self.addEventListener('activate', e => {
  e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== SHELL && k !== DATA).map(k => caches.delete(k)))).then(() => self.clients.claim()));
});

async function swr(cacheName, req, notify) {
  const cache = await caches.open(cacheName);
  const cached = await cache.match(req);
  const fresh = fetch(req).then(async res => {
    if (res.ok && res.type !== 'opaque') {
      if (cached && notify) {
        const [a, b] = await Promise.all([cached.clone().text(), res.clone().text()]);
        if (a !== b) (await self.clients.matchAll()).forEach(c => c.postMessage({ type: 'NEW_VERSION_READY' }));
      }
      cache.put(req, res.clone());
    }
    return res;
  }).catch(() => cached);
  return cached || fresh;
}

// App shell: network first (so a new deploy shows up on the very next load), cached copy if offline or the
// network takes longer than 4 seconds.
async function netFirst(cacheName, req) {
  const cache = await caches.open(cacheName);
  try {
    const res = await Promise.race([fetch(req, { cache: 'no-cache' }), new Promise((_, no) => setTimeout(() => no(new Error('slow')), 4000))]);
    if (res && res.ok && res.type !== 'opaque') cache.put(req, res.clone());
    return res;
  } catch (_) {
    return (await cache.match(req)) || fetch(req);
  }
}

self.addEventListener('fetch', e => {
  const req = e.request, url = new URL(req.url);
  if (req.method !== 'GET') return;
  if (url.hostname.endsWith('.supabase.co') || url.pathname.includes('/functions/v1/')) return;   // never touch live data
  if (url.origin !== location.origin) return;                                                      // fonts etc. stay with the browser
  if (/-syllabus\.html$/.test(url.pathname)) { e.respondWith(swr(DATA, req, false)); return; }
  e.respondWith(netFirst(SHELL, req));
});

self.addEventListener('message', e => { if (e.data === 'SKIP_WAITING') self.skipWaiting(); });

// Web Push (needs VAPID keys and a sender; see DEPLOY.md). Works with the tab closed.
self.addEventListener('push', e => {
  let d = {}; try { d = e.data ? e.data.json() : {}; } catch (_) { d = { body: e.data ? e.data.text() : '' }; }
  e.waitUntil(self.registration.showNotification(d.title || 'Ace Education', {
    body: d.body || '', icon: 'icon.svg', badge: 'icon.svg', tag: d.tag || 'ace', data: { url: d.url || './index.html' }, vibrate: [80, 40, 80]
  }));
});
self.addEventListener('notificationclick', e => {
  e.notification.close();
  const target = (e.notification.data && e.notification.data.url) || './index.html';
  e.waitUntil(clients.matchAll({ type: 'window', includeUncontrolled: true }).then(list => {
    for (const c of list) if ('focus' in c) return c.focus();
    return clients.openWindow ? clients.openWindow(target) : null;
  }));
});
