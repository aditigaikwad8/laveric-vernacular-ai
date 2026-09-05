# Upstream Sync Guide

## Remotes
- origin   = our private Laveric repo (fetch + push)
- upstream = original Dograh repo, read-only (fetch only, push blocked)

## How to fetch latest upstream changes
1. git fetch upstream
2. git log HEAD..upstream/main --oneline    # preview what's new before touching anything

## How to rebase our work onto upstream
1. Create a scratch branch first, never rebase main directly:
   git checkout -b rebase-test
2. git rebase upstream/main
3. Resolve any conflicts manually - check the divergence log (DIVERGENCE.md)
   to know which files we intentionally changed and why, before deciding
   how to resolve a conflict.
4. After rebase completes: run the app (docker compose up) and confirm
   it still starts and a full call works end-to-end.
5. Only after confirming it works, fast-forward the real branch.

## Who approves
- Any rebase onto main requires senior sign-off before merging (per
  Section 0 review gates).

## Never
- Never force-push a shared branch.
- Never resolve a conflict by deleting upstream's side just because our
  version "already works" - we lose their fix. Understand it first.
