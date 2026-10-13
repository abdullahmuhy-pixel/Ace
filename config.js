/* The ONE place to configure the front end. Loaded by /login/ and /app/.
   The anon key is public by design: Row Level Security protects the data. Never put a service_role key here. */
window.ACE_CONFIG = {
  supabaseUrl: 'https://xovychuglovhvdapbmvu.supabase.co',
  supabaseAnonKey: '',   // Project Settings -> API -> anon public key
  appUrl: '../app/',     // where signed-in users go (relative to /login/)
  staffUrl: '../staff/', // teacher / school-admin / platform dashboard
  vapidPublicKey: '',    // Web Push public key (npx web-push generate-vapid-keys); leave empty to hide the push button
  termsVersion: '2026-10'
};
