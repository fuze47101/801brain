# 801brain — Andrew's Project Monorepo

## Owner
Andrew Peterson (andrew@801inc.com) — CEO/Founder, 801 Inc.

## What This Is
**801brain** is the central monorepo for all of Andrew's active design and
working projects — the single repo to clone on a new machine to get the full
context of every project he's running. CLAUDE.md files in each project folder
are the source of truth for that project's memory.

## Multi-Machine Sync Workflow
This repo is meant to sync across multiple computers. Always:

1. **At session start:** `cd ~/Desktop/801brain && git pull`
2. **At session end (or when CLAUDE.md changes):** `git add -A && git commit -m "..." && git push`

If you ever see a "fetch first" rejection on push, your other machine has changes.
Run `git pull --rebase` first, resolve any conflicts (most often in CLAUDE.md
files), then push.

## Repo Layout

```
801brain/
├── CLAUDE.md                    ← this file (top-level memory, project index)
├── agents/                      ← shared agent prompts and rules
├── logs/                        ← session logs
├── memory/                      ← shared cross-project memory
├── projects/                    ← one folder per active project
│   ├── Atlas/                   ← (control-plane scaffolding, see note below)
│   ├── container-theft/         ← Container theft case (legal)
│   ├── Helios/                  ← Expedry Capsule + IR camera + scientific rigs
│   ├── Ledge-Marketing/         ← Ledge Outdoors marketing memory
│   ├── Peterson-Solar/          ← Off-grid solar install for Roger Peterson
│   ├── Solaris/                 ← Solaris FZ-500 fabric/material testing rig
│   └── venom-and-vinegar/       ← Personal/legal — divorce proceedings (private)
├── scripts/
└── strategy/
```

## Active Projects

Each project folder has its own `CLAUDE.md` — read it before starting any work
in that project.

| Project | Folder | Status | Notes |
|---|---|---|---|
| **Container theft** | `projects/container-theft/` | Active | CBP / customs case, attorney package |
| **Solaris FZ-500** | `projects/Solaris/` | Active | Fabric IR/heat testing rig — Portland show prep |
| **Helios (Expedry Capsule)** | `projects/Helios/` | Active | Humidity testing apparatus, deploy_v3 |
| **Peterson Solar** | `projects/Peterson-Solar/` | Active | Off-grid system for Roger Peterson |
| **Ledge Marketing** | `projects/Ledge-Marketing/` | Active | Pulse hydration, Alaska sleeping bag, Meta/TikTok ads |
| **Venom & Vinegar** | `projects/venom-and-vinegar/` | Active | Personal/legal — confidential |

**Note on Atlas folder:** `projects/Atlas/` contains older control-plane
scaffolding (architecture.md, decisions.md, orchestrator.py). The active
**FUZE Atlas** product code lives in its own deployed repo (see below). This
folder may be cleaned up or removed in the future.

## Projects That Live in Their Own Repos
These are deployed applications — they stay in separate repos to preserve their
deployment pipelines (Vercel, Railway, Pi firmware, etc.). Clone separately if
you need to work on the code:

| Project | Repo | Deploys To |
|---|---|---|
| **FUZE Atlas** (multi-portal app) | `git@github.com:fuze47101/fuzeatlas.git` | Vercel — fuzeatlas.com |
| **fuzefaq.com / FUZE Cost** | `git@github.com:fuze47101/fuzecost.git` | Railway — fuzefaq.com |
| **Helios (firmware/deploy)** | `git@github.com:fuze47101/helios_expedry.git` | Raspberry Pi (alliedV2) |
| **Ledge Outdoors marketing assets** | `git@github.com:fuze47101/ledge.git` | (no deployment — design assets) |

> **Why this split?** "Design monorepo" — 801brain holds all design/working
> content for fast cross-project context, while deployed apps stay in their own
> repos so Vercel/Railway/Pi pipelines are not disturbed. New machines clone
> 801brain first, then any of the deployed repos as needed.

## Holding Files (Pending Manual Merge)
A few CLAUDE.md holding files exist as a safety net for content that needs to
be hand-merged into the canonical CLAUDE.md, then the holding file deleted:

- `projects/Helios/CLAUDE-from-dx-laptop-2026-05-06.md` *(in helios repo, not here)*
  — TPU laminate Mesh_Frames_v1.scad design notes from a dx laptop sync
- `projects/Peterson-Solar/CLAUDE-from-Ledge_Master.md`
  — earlier 172-line draft; check if any unique content vs the 465-line CLAUDE.md
- `projects/Peterson-Solar/CLAUDE-from-Peterson-Solar-2.md`
  — CLAUDE.md from the Peterson Solar 2 working folder; compare and merge

## Migration History
- **2026-05-06** — Pre-Mac-transfer monorepo consolidation. Container, Peterson Solar 2,
  loose Solaris files moved into `projects/`. Stray sub-CLAUDEs from Ledge_Master
  relocated to their proper project folders. Top-level CLAUDE.md (this file) added.
