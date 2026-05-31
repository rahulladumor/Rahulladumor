# GitHub Profile README Upgrade — Design Spec

**Date:** 2026-05-31
**Repo:** `Rahulladumor` (GitHub profile README)
**Source of truth:** `Rahul_Ladumor_Portfolio (1).pdf` (Portfolio · 2026) + live site `rahulladumor.com`
**Approach:** Hybrid — keep GitHub-native visuals, replace substance with portfolio-accurate content in the portfolio's senior ownership voice.

## Goal

Bring the profile README in line with the 2026 portfolio: shift identity from "Senior AWS Solution Architect / open-to-hire" to **Principal Cloud & AI Platform Architect, consulting + fractional, Founder InfraTales**. Correct stale facts (certs, experience, contact), add missing sections (Products, real work history), and replace the generic 66-repo project list with real, defensible projects.

## Locked decisions

| Decision | Choice | Rationale |
|---|---|---|
| Stance | **Consulting / fractional** | Matches 2026 portfolio; drops "Hiring/full-time roles" framing |
| Rewrite scope | **Hybrid (C)** | GitHub visuals where they help, portfolio substance/voice where it counts |
| Savings metric | **₹50L+/yr** (drop ₹50Cr) | Portfolio-aligned and defensible; ₹50Cr is unverifiable and invites scrutiny |
| 66-project list | **Replace with real projects** | Generic template-style names hurt credibility next to real war stories |
| Public email | **rahuldladumor@gmail.com** | From 2026 portfolio |
| Primary website | **rahulladumor.com** | Live consulting site; old `rahulladumor.in` has expired TLS (broken) |
| Pro-cert badges | shields.io text badges | No Credly image URLs available for the Professional certs |

## Authoritative facts (from 2026 portfolio)

**Identity**
- Title: **Principal Cloud & AI Platform Architect**
- Tagline: *Production GenAI on AWS · Bedrock, RAG, Agents, Terraform · Cloud Cost & Reliability*
- 9+ years (since 2016); Founder, InfraTales
- Base: Surat, Gujarat, India · Remote-first · IST + US time zones
- Email: `rahuldladumor@gmail.com` · Phone: +91 75676 11653
- Web: `rahulladumor.com` (primary) · `infratales.com` · `linktr.ee/rahulladumor` · `linkedin.com/in/rahulladumor`

**Headline metrics (defensible)**
- 5M+ orders/month, sub-200ms latency, 99.99% uptime at peak (KFC Thailand)
- 1,745 IaC tasks validated @ 96.3% across 5 frameworks (Turing)
- ₹50L+/yr client AWS waste removed (FinOps)

**Certifications**
- AWS Certified Solutions Architect – Professional (Feb 2026)
- AWS Certified Generative AI Developer – Professional (Jan 2026)
- AWS Certified DevOps Engineer – Professional
- AWS Certified Developer – Associate
- HashiCorp Terraform Associate
- 4x AWS Community Builder (Serverless)

**Education**
- PG Certificate, Agentic AI / GenAI / ML — IIT Roorkee (2025–2026)
- M.Sc. Information Technology — VNSGU Surat (2018–2020)
- B.Sc. Information Technology — VNSGU Surat (2016–2018)
- Distinguished Alumni Recognition, 60th Anniversary

**Full work history (timeline)**
| Period | Role · Company | Note |
|---|---|---|
| Mar 2023–Present | Independent Cloud & AI Consultant | Serverless 30–40% cost cuts; ₹50L+ audits; Bedrock RAG |
| Nov 2024–Present | Cloud & AI Career Coach · Topmate.io | 1:1 mentoring |
| Sep 2025–Present | Senior AWS Solutions Architect · ASTM (via Euphoric Thought) | Valkey 7.2 migration, EKS, multi-account |
| Jul 2025–Feb 2026 | AI Infra Platform Engineer · Turing | Amazon IAC RLHF; 12-repo IaC; 1,745 @96.3% |
| 2025–Apr 2026 | AI Platform / Backend Lead · MAIA (Munn & Affiliates / Tektonik, Canada) | RAG on Pinecone, n8n, LiveKit voice agent |
| Jan 2025–Mar 2025 | Senior Software Engineer · NTT (Tokyo) | Short AWS platform contract |
| Jul 2023–Mar 2025 | Lead Platform Engineer · ProdigyBuild (via Virgo, SF Bay) | Serverless platform, ML pipeline; 40% cost cut |
| May 2022–Aug 2024 | SDE-II · ProtectOnce (via Codewits, SF Bay) | Dev-first security; eBPF monitoring |
| Apr 2022–Jun 2022 | Blockchain Developer · PrimeLab (US) | Go microservices |
| Feb 2022–Dec 2023 | Senior Software Engineer · Imaginato (via DIV Tech, China) | KFC Thailand 5M orders/mo; Qraved Indonesia |
| Aug 2021–May 2022 | Senior Software Developer · NDS Global (India) | Conversational AI on Lex / Azure Bot |
| Jan 2020–Jul 2021 | Cloud Developer · AppGambit (Surat) | 1M+ req/min on ECS/EKS/Fargate |
| Apr 2016–Jul 2019 | Bynebits → Creative Infotech (Indore/Surat) | First roles; Node.js + Lambda, PHP e-commerce |

**Selected projects (real — replace 66-list)**
- KFC Thailand · Omnichannel ordering — EKS + Kafka, 5M+ orders/mo, <200ms, 99.99%, blue-green 20+ releases/wk
- Turing · IaC automation platform — 12 repos, 1,745 tasks @96.3%, 5 IaC frameworks, CI/CD auto-fixer agent
- Bedrock RAG pipeline — chunking, embedding selection, reranking, RAGAS eval; lifted relevance for B2B SaaS
- Qraved Indonesia — PHP monolith → serverless GraphQL; 3x throughput, +18% CTR, +22% DAU
- ProdigyBuild · ML platform — SageMaker Pipelines, MLflow, DVC; retraining + rollback gates
- ProtectOnce · security platform — Lambda/API GW/WAF, eBPF kernel monitoring

**Products & builds (NEW section)**
- **IdleLens** (Building, v0.6.0) — AWS cloud-waste scanner SaaS; 17 scanners, 76 tests, multi-account UI; Next.js/React 19/TS/Fargate
- **InfraTales.com** (Launched 7 Apr 2026) — Ghost v6 on Lightsail; 17 pages, 8 posts; paid tier $5/mo or $50/yr
- **AI Second-Brain Dashboard** (Building) — personal knowledge dashboard; extraction layer done, UI ~75%
- Collapsed `<details>`: Second Brain (parked), Meeting Recorder (parked), Gmail Smart Organizer (built), LinkedIn Lab (parked), Fluent (parked), finance-app-ps (archived)

## README section plan (final order)

1. **Header** — animated capsule header; new title + tagline; typing-SVG lines (GenAI on AWS / 3x AWS Professional / ₹50L+/yr / 1,745 IaC @96.3% / 9+ yrs / Founder InfraTales); social badges (LinkedIn, GitHub, dev.to, Medium, Peerlist, Twitter, infratales.com); status badge **🟢 Open to consulting & fractional**; Last-Updated → May 2026.
2. **TL;DR snapshot** — Principal C&AI Platform Architect · 9+ yrs · consulting+fractional · Founder InfraTales; impact row (5M orders/mo <200ms, 99.99%, 1,745 @96.3%, ₹50L+/yr).
3. **About** — portfolio voice: "3:47 AM — the call I get hired for" hook + Redis/Valkey war story; "Four things teams hire me for" (GenAI infra / Platform & reliability / Cost FinOps / Cloud delivery); "How I weigh a system"; Education block.
4. **Certifications** — 3x AWS Professional + Developer Associate + HashiCorp Terraform Associate + 4x Community Builder (shields badges).
5. **Tech Arsenal** — icon grids (add Bedrock/SageMaker/RAG, Pinecone, OpenSearch, Valkey, LiveKit, n8n); expertise bars add GenAI/RAG + FinOps.
6. **Selected Projects** — six real projects above (client work described, not fake-linked).
7. **Products & builds** — IdleLens, InfraTales.com, AI Second-Brain; parked/archived in `<details>`.
8. **Work history** — full 12-role timeline (clean table).
9. **InfraTales** — keep + refresh (launched 7 Apr 2026, Ghost v6, 8 posts, $5/mo, 27 repos).
10. **Content & community** — VNSGU AI Agents Workshop (Apr 2026), Topmate mentoring, ~11K LinkedIn; keep real dev.to article links; drop unverifiable "100K+ views / 50+ articles" aggregate claims.
11. **Contact / Work with me** — consulting CTA (consulting engagements + fractional architect; GenAI infra / platform & reliability / FinOps); email `rahuldladumor@gmail.com`; links to `rahulladumor.com`, LinkedIn, Topmate, InfraTales, GitHub. No "full-time roles" list.
12. **Footer** — capsule footer; update © to 2026.

## Out of scope (YAGNI)

- No new automation/workflows (blog-post-list auto-update stays as-is placeholder).
- No changes to `.github/FUNDING.yml`, `SECURITY.md`, `LICENSE`.
- No verification of GitHub repo existence for the dropped 66-list (they're being removed).

## Risks / notes

- ₹50Cr → ₹50L/yr is a deliberate downward correction for credibility; confirm no external collateral still cites ₹50Cr that would contradict.
- Pro-cert badges are text-only until Credly image URLs are provided.
- `rahulladumor.in` link removed everywhere (expired TLS); replaced with `rahulladumor.com`.
