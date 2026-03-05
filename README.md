# Trilok Ventures - GitHub Governance Repository

This repository is the **Z2 governance layer** for Trilok Ventures.

It stores **code, configurations, and policies only** (no regulated business data), and drives controlled deployments into the Z3 app zone (Odoo, Nextcloud, integration bridge) through self-hosted runners.

## Repository scope

- IaC/Deployment: `infra/`
- Policy-as-Code: `policies/`
- Odoo modules: `apps/odoo/`
- Integration bridge: `integration/bridge/`
- Nextcloud automation/policies: `nextcloud/occ/`
- CI/CD and controls: `.github/workflows/`

## Security controls implemented here

- CODEOWNERS protections for policy-sensitive paths.
- CI guardrail that blocks accidental export permission for Red/Amber records.
- Signed-commit requirement can be enforced at GitHub branch protection level.
- Deployment workflow designed for OIDC + Vault JIT secret retrieval and immutable deploy logging.

## Quick start

1. Create teams:
   - `@trilok-ventures/compliance`
   - `@trilok-ventures/platform`
2. Enable branch protection on `main`:
   - Require PRs + required checks
   - Require CODEOWNER review
   - Require signed commits
3. Register self-hosted runners in Z3:
   - labels: `self-hosted`, `z3`, `staging`, `prod`
4. Configure repository/environment secrets/variables:
   - `VAULT_ADDR`, `VAULT_ROLE`
   - `IMMUTABLE_LOG_ENDPOINT`
   - `DEPLOY_TARGET_STAGING`, `DEPLOY_TARGET_PROD`
5. Review `docs/github-setup.md` and apply org-level settings.

## Important note

Do not commit COA/Phyto/PCP/customer files or production extracts to this repository.
