# GitHub Setup Guide (Aligned to Z2/Z3/Z4 Architecture)

## 1) Repository model

Use this repo as a **control plane repo**:

- `infra/terraform`: Proxmox/network/app infra declarations.
- `infra/ansible`: host/app deployment playbooks.
- `policies/`: PaC (classification, export, document gates).
- `apps/odoo/`: custom modules (`x_data_class`, shipment gate, bindings).
- `integration/bridge/`: NC WebDAV ↔ Odoo API sync/checksum linker.
- `nextcloud/occ/`: Nextcloud tags/FAC/retention automation.

## 2) GitHub branch protections

For `main`:

- Require pull request before merging.
- Require approval from Code Owners.
- Require status checks:
  - `policy-export-gate`
  - `policy-file-safety`
  - `deploy-plan` (if you split plan/apply)
- Require signed commits.
- Restrict force pushes and deletion.

## 3) CODEOWNERS

Compliance must review:

- `policies/**`
- `.github/workflows/**`
- `nextcloud/occ/**` (contains controls)

Platform owns infra/deploy logic.

## 4) Secrets and identity

Prefer OIDC federation from GitHub Actions to Vault:

- Configure Vault JWT auth for this repo.
- Map GitHub `sub` claim to role(s):
  - staging deploy role
  - prod deploy role
- Workflows request ID token and exchange for short-lived credentials.

No static long-lived secrets in repo.

## 5) Logging and traceability

Each deployment step should emit:

- git SHA
- actor
- target env
- changed components
- result

Ship deployment logs to immutable collector endpoint from workflows or runner sidecar.

## 6) Data handling policy in GitHub

Allowed:

- code
- policy definitions
- infra configs
- synthetic test data

Disallowed:

- Red/Amber business documents (COA/Phyto/customer records)
- production dumps
- credentials/secrets

## 7) Environment strategy

- `staging`: auto-deploy from `main` after checks.
- `production`: manual approval gate + Compliance signoff.

## 8) Suggested follow-ups

- Add Open Policy Agent checks for PR metadata and file paths.
- Add SBOM + dependency/license scans.
- Add artifact signing and provenance attestation (SLSA).
