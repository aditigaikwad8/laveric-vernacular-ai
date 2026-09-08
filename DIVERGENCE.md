# Divergence Log
Every file we've intentionally changed from stock Dograh, and why.
Update this every time you edit an existing upstream file (not new files
you add - those never conflict on rebase).

| File | What changed | Why | Date |
|---|---|---|---|
| (none yet) | | | |
| api/constants.py | ENABLE_TELEMETRY default changed "true" → "false" | Fail-safe default; telemetry must not be on unless explicitly enabled | [today's date] |
| ui/src/constants/documentation.ts | DOCS_BASE hardcoded to docs.dograh.com → now reads NEXT_PUBLIC_DOCS_BASE_URL env var, falls back to "#" | Laveric docs site doesn't exist yet; avoid pointing users at Dograh's docs while ours is being written | [date] |
| ui/src/components/Footer.tsx | Privacy policy link changed from dograh.com to "#" placeholder | Laveric's own privacy policy page doesn't exist yet; avoid linking users to Dograh's | [today's date] |
| ui/src/components/Footer.tsx | Privacy policy and terms-of-service links changed from dograh.com to "#" placeholder | Laveric's own legal pages don't exist yet | [today's date] |

| ui/src/app/overview/page.tsx | GitHub issues link and docs link replaced with "#"; branding text reworded | github.com/dograh-hq is Dograh's public OSS repo — no Laveric equivalent exists (fork is private per UPSTREAM.md); needs a real support-contact link once Laveric decides how users should report issues, not necessarily GitHub | [date] |

| ui/.env.example | NEXT_PUBLIC_POSTHOG_KEY value cleared | Prevent PostHog client-side telemetry init regardless of ENABLE_TELEMETRY, since instrumentation-client.ts gates on this key independently | [date] |
| ui/src/components/layout/AppSidebar.tsx | Docs link → "#" | Laveric docs site not live yet | [date] |
| ui/src/app/overview/page.tsx | Branding text removed; docs/GitHub links → "#" | Same; GitHub link had no Laveric equivalent (private fork) | [date] |
| ui/src/app/recordings/page.tsx | Docs link → "#" | Same | [date] |
| ui/src/app/settings/page.tsx | Branding text removed; docs links → "#" | Same | [date] |
| ui/src/app/telephony-configurations/page.tsx | Docs link → "#" | Same | [date] |
| ui/src/app/tools/page.tsx | Docs link → "#" | Same | [date] |
| ui/src/components/MCPSection.tsx | Docs link → "#" | Same | [date] |
| ui/src/app/files/page.tsx | Docs link → "#" | Same | [date] |