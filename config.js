/* The ONE place to configure the front end. Loaded by /login/ and /app/.
   The anon key is public by design: Row Level Security protects the data. Never put a service_role key here. */
window.ACE_CONFIG = {
  supabaseUrl: 'https://xovychuglovhvdapbmvu.supabase.co',
  supabaseAnonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InhvdnljaHVnbG92aHZkYXBibXZ1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTE0NTk2NDcsImV4cCI6MjEwNzAzNTY0N30.3jIfAxynyS935NmZBw-iFGl0P3E6fkvCYKCz4oQ5-Zg',   // Project Settings -> API -> anon public key
  appUrl: '../app/',     // where signed-in users go (relative to /login/)
  staffUrl: '../staff/', // teacher / school-admin / platform dashboard
  vapidPublicKey: '',    // Web Push public key (npx web-push generate-vapid-keys); leave empty to hide the push button
  termsVersion: '2026-10'
};
