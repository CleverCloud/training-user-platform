# Session 2 — Prerequisites

*To forward to the customer contact. To be ready **before** the session and checked the day before.*

## On the platform

| # | What |
|---|------|
| 1 | A training organisation, every trainee a member with the **Admin** or **Manager** role |
| 2 | Quota per trainee: 1 Python application (small flavor) + 1 **PostgreSQL** add-on (`dev` plan) + 1 **FS Bucket** add-on |
| 3 | The Python runtime, PostgreSQL and FS Bucket available on the installation |

## On each trainee's workstation

| # | What | Check |
|---|------|-------|
| 1 | Git, with `user.name` and `user.email` configured | `git --version` |
| 2 | Clever Tools installed and **logged in to the platform** (with the platform's endpoints if it isn't the public Clever Cloud) | `clever profile` shows the trainee's account |
| 3 | Access to the organisation | `clever applications list --org <training org>` works |
| 4 | A browser able to reach the Console and the application domain; `curl` | — |

Behind a corporate proxy or a private certificate authority, see the "corporate proxy" section of the Session 1 prerequisites, or <https://www.clever.cloud/developers/doc/manage/cli/>.
