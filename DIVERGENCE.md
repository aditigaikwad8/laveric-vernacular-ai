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

# Divergence Log

Every file we've intentionally changed from stock Dograh, and why.

Update this every time you edit an existing upstream file (not new files you add - those never conflict on rebase).

| File                                           | What changed                                                                                                                                                                                                                                                                    | Why                                                                                                                                                                              | Date       |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------- |
| `api/services/configuration/registry.py`       | Removed Dograh from `ServiceProviders`; removed Dograh from `BaseServiceConfiguration.provider`; removed the old `ServiceConfig`; added `EmbeddingsConfig` for OpenAI, OpenRouter, and Azure OpenAI embeddings.                                                                 | Remove Dograh as a selectable provider and replace the old generic service configuration with the BYOK-compatible configuration structure.                                       | 2026-09-17 |
| `api/services/configuration/masking.py`        | Removed the `ServiceConfig` import and changed `_mask_service` typing from `Optional[ServiceConfig]` to `Optional[Any]`.                                                                                                                                                        | `ServiceConfig` was removed from the registry, so masking must no longer depend on that obsolete type.                                                                           | 2026-09-17 |
| `api/services/configuration/check_validity.py` | Removed `ServiceConfig` dependency; changed affected configuration parameters to `Optional[Any]`; removed the Dograh API-key validator and its mapping.                                                                                                                         | Remove validation logic tied specifically to the removed Dograh provider/service configuration.                                                                                  | 2026-09-17 |
| `api/schemas/ai_model_configuration.py`        | Reworked organization AI model configuration to the BYOK V2 structure; removed Dograh-managed configuration; added `EmbeddingsConfig` support; retained pipeline/realtime BYOK modes and validation.                                                                            | Make organization model configuration BYOK-only and eliminate the removed Dograh managed-model mode.                                                                             | 2026-09-17 |
| `api/routes/organization.py`                   | Removed Dograh-specific language/voice constants and service imports; removed `_dograh_allows_custom_voice()`; removed Dograh filtering from BYOK provider schemas/default providers; removed the Dograh V2 defaults entry; removed unused `ServiceProviders` import.           | Remove Dograh-specific organization API behavior and expose only the remaining supported BYOK providers.                                                                         | 2026-09-17 |
| `api/services/organization_bootstrap.py`       | Removed automatic Dograh managed-model provisioning, `provision_dograh_managed_model_configuration()`, the default Dograh service-key name, and provisioning-only MPS imports. Reduced `_bootstrap_organization()` to the remaining managed SIP connectivity provisioning path. | Prevent new organizations from automatically receiving the removed Dograh managed model while preserving the SIP bootstrap functionality still required by the application.      | 2026-09-17 |
| `api/services/managed_model_services.py`       | Removed the old Dograh managed-model helper logic, including Dograh provider/service-key checks and managed-v2 helpers; retained the MPS correlation-ID constant/helper used by workflow billing.                                                                               | Remove obsolete Dograh managed-service behavior while preserving the remaining correlation-ID functionality that is still used elsewhere.                                        | 2026-09-17 |
| `api/services/quota_service.py`                | Removed Dograh managed-service imports and the old OSS Dograh/managed-v2 authorization path; removed obsolete Dograh managed-v2 helper functions; changed hosted workflow authorization to use the MPS billing authorization path.                                              | Eliminate the old Dograh-specific managed-service quota flow while retaining hosted workflow quota authorization.                                                                | 2026-09-17 |
| `api/app.py`                                   | Removed `https://app.dograh.com` from FastAPI's `servers` list, leaving the local development server entry.                                                                                                                                                                     | Prevent the generated OpenAPI specification and frontend API client from using the old Dograh production URL.                                                                    | 2026-09-17 |
| `ui/src/app/layout.tsx`                        | Removed the `ChatwootWidget` import and `<ChatwootWidget />` component usage.                                                                                                                                                                                                   | Remove the Chatwoot widget integration from the frontend.                                                                                                                        | 2026-09-17 |
| `ui/public/embed/dograh-widget.js`             | Changed the non-localhost API fallback from `https://api.dograh.com` to `window.location.origin`.                                                                                                                                                                               | Prevent the embedded widget from hard-coding the external Dograh API endpoint and make it use the host where the widget is running.                                              | 2026-09-17 |
| `ui/src/client/*`                              | Regenerated the OpenAPI-generated frontend client using the local API OpenAPI endpoint.                                                                                                                                                                                         | Synchronize the generated frontend API client with the cleaned backend API schema. The regenerated client was verified to contain no `Dograh`, `dograh`, or `DOGRAH` references. | 2026-09-17 |

## Files inspected but intentionally NOT changed

The following files were inspected during the cleanup but were **not intentionally modified** in this chat:

| File                                           | Reason                                                                                                                                                   |
| ---------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api/services/organization_context.py`         | Contains `managed_service_version` / `uses_managed_service_v2`; these were investigated but not removed without a complete usage audit.                  |
| `api/errors/failure.py`                        | Contains the broader `DograhFailure` model and provider-specific classification. It was not removed blindly because the failure model is used elsewhere. |
| `.github/workflows/build-api-image.yml`        | `app.dograh.com` was found only in a comment; `dograh-api` is used as a CI/Docker image name. No change was justified.                                   |
| `.github/workflows/api-tests.yml`              | Inspected through search only; CI audit was still in progress when this report was requested.                                                            |
| `.github/workflows/docker-image.yml`           | Searched for Dograh references; image/job/artifact names were found but were not changed.                                                                |
| `.github/workflows/pre-pr-drift-check.yml`     | Only notification text was found; no change made.                                                                                                        |
| `.github/workflows/release-deployment.yml`     | Only notification text was found; no change made.                                                                                                        |
| `.github/workflows/slack-announcements.yml`    | Existing Slack secret naming was found; no change made.                                                                                                  |
| `docker-compose.yaml`                          | Verified that the UI already uses a local `ui/Dockerfile` build rather than `dograhai/dograh-ui:latest`; no change required.                             |
| `docker-compose-local.yaml`                    | Searched as part of the Compose audit; no `dograhai/dograh-ui` reference was found.                                                                      |
| `.devcontainer/docker-compose.yml`             | Searched as part of the Compose audit; no `dograhai/dograh-ui` reference was found.                                                                      |
| `deploy/hostinger/docker-compose.yaml`         | Searched as part of the Compose audit; no `dograhai/dograh-ui` reference was found.                                                                      |
| `deploy/hostinger/docker-compose.traefik.yaml` | Searched as part of the Compose audit; no `dograhai/dograh-ui` reference was found.                                                                      |

## Verification performed

* `api/app.py` passed `python -m py_compile` **inside the Docker API container**.
* API Docker image successfully rebuilt.
* API container successfully started.
* API health endpoint returned HTTP `200`.
* OpenAPI endpoint returned HTTP `200`.
* OpenAPI `servers` was verified to contain only `http://localhost:8000`.
* Frontend OpenAPI client generation completed successfully with `@hey-api/openapi-ts v0.97.3`.
* Generated `ui/src/client` was searched and contained no Dograh references.
* `ui/src/app/layout.tsx` was searched and contained no Chatwoot references.
* `ui/public/embed/dograh-widget.js` was searched and contained no `api.dograh.com` / `https://api` fallback reference.
* All discovered Compose files were searched and contained no `dograhai/dograh-ui` image reference.

## Still pending

* Finish the GitHub Actions / CI audit.
* Audit remaining production Dograh references, especially `api/errors/failure.py` and `api/services/quota_service.py`.
* Decide whether obsolete `managed_service_version` code can be safely removed.
* Update tests that still reference the removed Dograh provider/managed configuration.
* Run the complete backend test suite.
* Run frontend/build verification after all cleanup.
* Perform the final whole-project egress/provider search.
* Perform final Docker/runtime verification.
