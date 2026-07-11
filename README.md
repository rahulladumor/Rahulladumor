<div align="center">
  <img src="./assets/hero.svg" alt="Rahul Ladumor - Production AWS and AI Platform Architect" width="100%"/>
</div>

<h1 align="center">Production AWS &amp; AI Platform Architect</h1>

<p align="center">
  I take AWS, RAG and AI-agent systems from <b>"it works"</b> to <b>"we can trust it in production."</b>
</p>

<div align="center">

[Production Review](https://www.rahulladumor.com/contact?intent=production-review) · [Case Studies](https://www.rahulladumor.com/work) · [Services](https://www.rahulladumor.com/services) · [Architecture Notes](https://www.rahulladumor.com/writing) · [LinkedIn](https://www.linkedin.com/in/rahulladumor/)

</div>

<br/>

<div align="center">

| 9+ years in production | 3× AWS Professional | 4× AWS Community Builder | IIT Roorkee |
|:--:|:--:|:--:|:--:|
| AWS, platform and backend systems | Architecture, DevOps and GenAI | Serverless community | Agentic AI, GenAI and ML |

</div>

---

## The production gap I work on

The model is rarely the whole problem.

A serious production AI or AWS platform also needs evidence, IAM boundaries, observability, failure isolation, cost ceilings, safe releases, rollback, and an owner who knows what happens next.

I work with CTOs, founders and platform teams when:

<table>
<tr>
<td width="50%" valign="top">

### The AI system cannot be trusted

- RAG retrieves plausible but incorrect evidence
- AI agents lose context or fail during tool execution
- quality is discussed but not continuously evaluated
- prompts, traces and sensitive data have no clear governance

</td>
<td width="50%" valign="top">

### The AWS platform cannot be controlled

- cloud spend increases without technical ownership
- deployments feel risky and rollback is unclear
- serverless or container workloads fail under real traffic
- dashboards exist, but incidents still take hours to explain

</td>
</tr>
</table>

<div align="center">
  <img src="./assets/architecture-map.svg" alt="The demo-to-production gap across evidence, security, cost, delivery, operations and ownership" width="100%"/>
</div>

> **My operating principle:** boring but reliable beats clever but fragile. Every important design decision should explain cost, failure behaviour, blast radius, operational ownership, validation, and rollback.

---

## What you can bring me

<table>
<tr>
<td width="50%" valign="top">

### 01 / Production Review

A fixed-scope architecture review for an AWS or AI system that is live or approaching launch.

**Best for:** rising AWS cost, reliability risk, latency, weak observability, unsafe deployment, migration planning, or unclear rollback.

**You leave with:** prioritised findings, evidence, architecture decisions, risk levels, recommended sequence, and practical next actions.

[Review the engagement](https://www.rahulladumor.com/services)

</td>
<td width="50%" valign="top">

### 02 / GenAI and RAG Readiness Review

A production-readiness review for RAG, AI agents and Amazon Bedrock workloads.

**Best for:** retrieval quality, hallucination exposure, tool reliability, evaluation coverage, guardrails, trace governance, and cost-per-request ceilings.

**You leave with:** failure-mode analysis, evaluation plan, production controls, observability requirements, and launch blockers.

[Review the engagement](https://www.rahulladumor.com/services)

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 03 / Implementation Sprint

A scoped engineering sprint to close one important production gap.

**Typical work:** RAG hardening, AWS cost controls, deployment safety, observability, IaC repair, migration steps, IAM boundaries, or rollback automation.

**The rule:** measurable acceptance criteria and a known rollback path before implementation begins.

[Discuss a sprint](https://www.rahulladumor.com/contact)

</td>
<td width="50%" valign="top">

### 04 / Fractional Platform Architect

Ongoing architecture ownership without hiring a full-time Principal Architect.

**Typical work:** design reviews, architecture standards, production decisions, cost governance, reliability direction, team mentoring, and risk escalation.

**The role:** senior technical judgment where architecture, product delivery, and operations meet.

[Discuss fractional ownership](https://www.rahulladumor.com/contact)

</td>
</tr>
</table>

---

## Production evidence ledger

### KFC Thailand / national-scale ordering

| Signal | Evidence |
|---|---|
| **Operating scale** | More than 5M orders per month |
| **Performance** | Sub-200ms response time under production traffic |
| **Reliability** | 99.99% availability with frequent releases |
| **Engineering surface** | Event-driven services, Node.js, Go, Kafka, Kubernetes, Terraform, blue-green delivery |
| **Why it matters** | Delivery speed and availability were treated as one system rather than competing goals |

### Enterprise GenAI and RAG / knowledge retrieval

| Signal | Evidence |
|---|---|
| **Corpus** | More than 2M documents |
| **Architecture** | Amazon Bedrock, S3 and Lambda ingestion, OpenSearch vector retrieval, semantic caching |
| **Production concern** | Retrieval quality, latency, LLM cost and observable failure behaviour |
| **Result** | Sub-second retrieval with lower model spend through semantic caching |
| **Why it matters** | RAG quality was treated as a measurable production property, not a prompt-writing exercise |

### AI-assisted infrastructure validation / Turing

| Signal | Evidence |
|---|---|
| **Evaluated work** | 1,745 infrastructure tasks across a 12-repository ecosystem |
| **Frameworks** | Terraform, CDK, CDKTF, Pulumi and CloudFormation |
| **Control surface** | Automated curation, repository validation, CI/CD repair and repeatable quality gates |
| **Result** | 96.3% validated task quality across the evaluated task set |
| **Why it matters** | AI-generated infrastructure needs deterministic validation before it becomes trusted delivery output |

<details>
<summary><b>Operator note: when "Redis is at 100% CPU" was not the real root cause</b></summary>

<br/>

A shared Redis deployment reached 100% CPU with 1,620 open connections and began degrading an indexing pipeline.

The capacity graph was only the first signal. The failure chain included an unbounded key scan in a Lambda path, weak connection handling, shared workload contention, and credentials that needed remediation.

The response combined application fixes with a cost-neutral migration to a dedicated Valkey 7.2 cluster, explicit rollback, safer credentials, and operational validation.

This is the work I prefer: find the complete failure chain, control immediate risk, and leave the system easier for the next engineer to own.

</details>

---

## Systems I am building

<table>
<tr>
<td width="33%" valign="top">

### [IdleLens](https://idlelens.com)

**AWS waste evidence engine**

A read-only AWS cost-optimisation product that converts resource evidence into prioritised findings with confidence, estimated monthly impact, and a suggested operator action.

`AWS · Next.js · TypeScript · Fargate`

</td>
<td width="33%" valign="top">

### [InfraTales](https://infratales.com)

**Architecture field notes**

A publication and open-source organisation focused on real AWS and AI failure modes: what broke, what it cost, what changed, and how the system became safer.

[Explore InfraTales on GitHub](https://github.com/InfraTales)

</td>
<td width="33%" valign="top">

### AI Agent Telemetry

**Private control-plane prototype**

Session evidence, tool calls, cost, memory, approval gates, redaction, retention and review paths across local and cloud coding-agent execution.

`Claude Code · OpenTelemetry · TypeScript · Python`

</td>
</tr>
</table>

---

## Open-source proof

| Repository | Production question it answers |
|---|---|
| [AWS cost-optimisation case study](https://github.com/InfraTales/infratales-aws-cost-optimization-50l-case-study) | How do you remove cloud waste without introducing operational risk? |
| [Enterprise secure web application](https://github.com/InfraTales/enterprise-secure-webapp-3tier) | How should networking, IAM, deployment and operations fit together? |
| [Zero-trust network architecture](https://github.com/InfraTales/zero-trust-network-architecture) | How do identity-aware boundaries reduce blast radius? |
| [InfraTales repositories](https://github.com/orgs/InfraTales/repositories) | How do these patterns translate into reusable infrastructure? |

---

## Technical operating surface

<div align="center">
  <img src="https://skillicons.dev/icons?i=aws,terraform,kubernetes,docker,typescript,nodejs,python,go" alt="AWS, Terraform, Kubernetes, Docker, TypeScript, Node.js, Python and Go" />
</div>

<br/>

| Domain | Production focus |
|---|---|
| **AWS architecture** | Lambda, API Gateway, DynamoDB, EventBridge, Step Functions, SQS, ECS, EKS, RDS, S3, CloudFront, IAM, VPC, OpenSearch |
| **Production GenAI** | Amazon Bedrock, RAG, AI agents, tool execution, evaluations, guardrails, prompt and trace governance, semantic caching |
| **Platform engineering** | Terraform, CDK, CloudFormation, GitHub Actions, Kubernetes, Docker, CI/CD, multi-account foundations |
| **Reliability** | Observability, SLOs, incident analysis, failure isolation, canary and blue-green delivery, rollback engineering |
| **Cost and FinOps** | Evidence-led right-sizing, lifecycle policies, idle-resource analysis, unit economics, budgets and spend guardrails |
| **Languages** | TypeScript, Node.js, Python and Go |

---

## Professional proof

<div align="center">
<table>
<tr>
<td align="center" width="33%">
<img src="https://images.credly.com/size/340x340/images/2d84e428-9078-49b6-a804-13c15383d0de/image.png" width="112" alt="AWS Certified Solutions Architect Professional"/><br/>
<b>Solutions Architect</b><br/><sub>AWS Professional</sub>
</td>
<td align="center" width="33%">
<img src="https://images.credly.com/size/340x340/images/52c6e5ac-9516-4944-a4df-e31b23c9bbf2/blob" width="112" alt="AWS Certified Generative AI Developer Professional"/><br/>
<b>Generative AI Developer</b><br/><sub>AWS Professional</sub>
</td>
<td align="center" width="33%">
<img src="https://images.credly.com/size/340x340/images/bd31ef42-d460-493e-8503-39592aaf0458/image.png" width="112" alt="AWS Certified DevOps Engineer Professional"/><br/>
<b>DevOps Engineer</b><br/><sub>AWS Professional</sub>
</td>
</tr>
</table>
</div>

<div align="center">

**3× AWS Professional Certified** · **4× AWS Community Builder - Serverless** · **HashiCorp Terraform Associate**

**PG Certificate in Agentic AI, Generative AI and Machine Learning - IIT Roorkee**

Upwork Top Rated · AWS community organiser · Technical speaker · Based in Surat, India · Working worldwide

</div>

---

## Engineering activity

<!-- STATS:START (auto-updated weekly by .github/workflows/update-stats.yml) -->
<p align="center">
  <img alt="Contributions in the last year" src="https://img.shields.io/badge/Contributions_·_last_year-975-2ea043?style=flat-square&logo=github&logoColor=white"/>
  <img alt="Commits in the last year" src="https://img.shields.io/badge/Commits_·_last_year-941-667eea?style=flat-square&logo=git&logoColor=white"/>
  <img alt="Public repositories" src="https://img.shields.io/badge/Public_Repos-49-764ba2?style=flat-square&logo=github&logoColor=white"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white"/>
  <img src="https://img.shields.io/badge/Shell-89E051?style=flat-square&logo=gnubash&logoColor=black"/>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Terraform_%2F_HCL-7B42BC?style=flat-square&logo=terraform&logoColor=white"/>
  <img src="https://img.shields.io/badge/HTML-E34F26?style=flat-square&logo=html5&logoColor=white"/>
</p>
<!-- STATS:END -->

---

## Common production questions

<details>
<summary><b>Can you take an AI agent or RAG system from prototype to production?</b></summary>

<br/>

Yes. I work across retrieval architecture, chunking and embeddings, reranking, evaluation, hallucination controls, tool execution, guardrails, observability, IAM, deployment, cost-per-request, and operational handover.

</details>

<details>
<summary><b>Do you provide AWS architecture reviews and platform consulting?</b></summary>

<br/>

Yes. Reviews can cover serverless architecture, multi-account and multi-region design, IAM and security boundaries, Kubernetes and container platforms, Terraform and CDK, CI/CD, incident risk, reliability, and AWS cost optimisation.

</details>

<details>
<summary><b>Can AWS cost be reduced without increasing production risk?</b></summary>

<br/>

Yes, but the recommendation must include evidence, confidence, operational impact, validation and rollback. A cheaper resource configuration is not a saving if it creates latency, incident load, data risk, or future rework.

</details>

---

## Bring me the system that has to survive

A good first conversation starts with evidence: the architecture, the current failure or cost signal, the operating constraints, and what the business cannot afford to get wrong.

<div align="center">

### [Book a Production Review](https://www.rahulladumor.com/contact?intent=production-review)

[rahulladumor.com](https://www.rahulladumor.com) · [hello@rahulladumor.com](mailto:hello@rahulladumor.com) · [LinkedIn](https://www.linkedin.com/in/rahulladumor/) · [InfraTales](https://infratales.com)

</div>
