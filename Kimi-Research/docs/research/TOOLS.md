# Tools Directory

Curated list of tools for autonomous AI coding systems.

---

## Table of Contents

1. [AI Coding Assistants](#ai-coding-assistants)
2. [Agent Frameworks](#agent-frameworks)
3. [Vector Databases](#vector-databases)
4. [Observability Tools](#observability-tools)
5. [Security Tools](#security-tools)
6. [MCP Servers](#mcp-servers)
7. [Testing Tools](#testing-tools)
8. [Infrastructure Tools](#infrastructure-tools)

---

## AI Coding Assistants

### IDE Integrations

| Tool | IDE | Price | Best For | Link |
|------|-----|-------|----------|------|
| **GitHub Copilot** | VS Code, JetBrains, Vim | $10/mo | General coding | [github.com/copilot](https://github.com/copilot) |
| **Claude Code** | CLI, VS Code | API cost | Complex tasks | [anthropic.com](https://anthropic.com) |
| **Cursor** | VS Code fork | $20/mo | AI-native IDE | [cursor.sh](https://cursor.sh) |
| **Cody** | VS Code, JetBrains | $9/mo | Code intelligence | [sourcegraph.com/cody](https://sourcegraph.com/cody) |
| **Tabnine** | Multiple | $12/mo | Privacy-focused | [tabnine.com](https://tabnine.com) |
| **Codeium** | Multiple | Free tier | Free alternative | [codeium.com](https://codeium.com) |

### CLI Tools

| Tool | Price | Best For | Link |
|------|-------|----------|------|
| **Aider** | Free | Pair programming | [aider.chat](https://aider.chat) |
| **Claude Code** | API cost | Autonomous coding | [docs.anthropic.com](https://docs.anthropic.com) |
| **Continue** | Free | Open-source assistant | [continue.dev](https://continue.dev) |
| **Supermaven** | $10/mo | Fast completions | [supermaven.com](https://supermaven.com) |

---

## Agent Frameworks

### Python Frameworks

| Framework | Maturity | Best For | GitHub Stars | Link |
|-----------|----------|----------|--------------|------|
| **LangChain** | Production | General purpose | 95k+ | [langchain.com](https://langchain.com) |
| **LangGraph** | Production | Complex workflows | Part of LangChain | [langgraph.ai](https://langgraph.ai) |
| **CrewAI** | Production | Role-based agents | 38k+ | [crewai.com](https://crewai.com) |
| **AutoGen** | Production | Multi-agent chat | 30k+ | [microsoft.github.io/autogen](https://microsoft.github.io/autogen) |
| **LlamaIndex** | Production | RAG applications | 38k+ | [llamaindex.ai](https://llamaindex.ai) |
| **DSPy** | Production | Optimized prompting | 15k+ | [dspy-docs.vercel.app](https://dspy-docs.vercel.app) |
| **Pydantic AI** | Growing | Type-safe agents | 5k+ | [ai.pydantic.dev](https://ai.pydantic.dev) |
| **Smolagents** | New | Lightweight | 3k+ | [huggingface.co/docs/smolagents](https://huggingface.co/docs/smolagents) |

### TypeScript/JavaScript Frameworks

| Framework | Maturity | Best For | Link |
|-----------|----------|----------|------|
| **LangChain.js** | Production | Node.js agents | [js.langchain.com](https://js.langchain.com) |
| **Vercel AI SDK** | Production | Streaming UI | [sdk.vercel.ai](https://sdk.vercel.ai) |
| **Genkit** | Growing | Firebase apps | [firebase.google.com/docs/genkit](https://firebase.google.com/docs/genkit) |
| **Mastra** | New | TypeScript-first | [mastra.ai](https://mastra.ai) |

---

## Vector Databases

### Managed Services

| Database | Free Tier | Best For | Link |
|----------|-----------|----------|------|
| **Pinecone** | 2GB | Production | [pinecone.io](https://pinecone.io) |
| **Weaviate** | 5GB | Hybrid search | [weaviate.io](https://weaviate.io) |
| **Qdrant Cloud** | 1GB | Performance | [qdrant.tech](https://qdrant.tech) |
| **Chroma Cloud** | 500MB | Prototyping | [trychroma.com](https://trychroma.com) |

### Self-Hosted

| Database | License | Best For | Link |
|----------|---------|----------|------|
| **Qdrant** | Apache 2.0 | Self-hosted | [qdrant.tech](https://qdrant.tech) |
| **Weaviate** | BSD | Self-hosted | [weaviate.io](https://weaviate.io) |
| **Chroma** | Apache 2.0 | Local dev | [trychroma.com](https://trychroma.com) |
| **pgvector** | PostgreSQL | Existing PG | [github.com/pgvector/pgvector](https://github.com/pgvector/pgvector) |
| **Milvus** | Apache 2.0 | Scale | [milvus.io](https://milvus.io) |

---

## Observability Tools

### LLM Observability

| Tool | Free Tier | Best For | Link |
|------|-----------|----------|------|
| **Langfuse** | 10K traces | Open source | [langfuse.com](https://langfuse.com) |
| **LangSmith** | 5K traces | LangChain | [smith.langchain.com](https://smith.langchain.com) |
| **Helicone** | 10K requests | Cost tracking | [helicone.ai](https://helicone.ai) |
| **Weights & Biases** | 100GB | ML teams | [wandb.ai](https://wandb.ai) |
| **PromptLayer** | 1K requests | Prompt mgmt | [promptlayer.com](https://promptlayer.com) |
| **Traceloop** | 3K spans | OpenTelemetry | [traceloop.com](https://traceloop.com) |

### General Observability

| Tool | Type | Best For | Link |
|------|------|----------|------|
| **Prometheus** | Metrics | Monitoring | [prometheus.io](https://prometheus.io) |
| **Grafana** | Dashboards | Visualization | [grafana.com](https://grafana.com) |
| **Jaeger** | Tracing | Distributed tracing | [jaegertracing.io](https://jaegertracing.io) |
| **OpenTelemetry** | Standard | Vendor-neutral | [opentelemetry.io](https://opentelemetry.io) |

---

## Security Tools

### Input Validation

| Tool | Purpose | Link |
|------|---------|------|
| **Rebuff** | Prompt injection detection | [rebuff.ai](https://rebuff.ai) |
| **Prompt Armor** | Prompt security | [promptarmor.com](https://promptarmor.com) |
| **LLM Guard** | Input/output filtering | [llm-guard.com](https://llm-guard.com) |
| **Protect AI** | AI security platform | [protectai.com](https://protectai.com) |

### Output Scanning

| Tool | Purpose | Link |
|------|---------|------|
| **Nightfall** | Data loss prevention | [nightfall.ai](https://nightfall.ai) |
| **Glaive** | Code security scanning | [glaive.ai](https://glaive.ai) |
| **Snyk** | Vulnerability scanning | [snyk.io](https://snyk.io) |
| **Semgrep** | Static analysis | [semgrep.dev](https://semgrep.dev) |

### Sandboxing

| Tool | Type | Link |
|------|------|------|
| **gVisor** | Container sandbox | [gvisor.dev](https://gvisor.dev) |
| **Kata Containers** | VM sandbox | [katacontainers.io](https://katacontainers.io) |
| **Firecracker** | MicroVM | [firecracker-microvm.github.io](https://firecracker-microvm.github.io) |
| **WASM** | WebAssembly | [wasmtime.dev](https://wasmtime.dev) |

---

## MCP Servers

### Official Servers

| Server | Purpose | Install |
|--------|---------|---------|
| **filesystem** | File operations | `npx -y @modelcontextprotocol/server-filesystem` |
| **git** | Git operations | `uvx mcp-server-git` |
| **github** | GitHub API | `npx -y @modelcontextprotocol/server-github` |
| **postgresql** | Database queries | `npx -y @modelcontextprotocol/server-postgres` |
| **sqlite** | SQLite queries | `npx -y @modelcontextprotocol/server-sqlite` |
| **puppeteer** | Browser automation | `npx -y @modelcontextprotocol/server-puppeteer` |
| **fetch** | HTTP requests | Built-in |

### Community Servers

| Server | Purpose | Link |
|--------|---------|------|
| **brave-search** | Web search | [github.com/modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) |
| **slack** | Slack integration | Community |
| **notion** | Notion API | Community |
| **linear** | Linear API | Community |

---

## Testing Tools

### AI-Powered Testing

| Tool | Purpose | Link |
|------|---------|------|
| **CodiumAI** | Test generation | [codium.ai](https://codium.ai) |
| **CoverAgent** | Coverage improvement | [github.com/Codium-ai/cover-agent](https://github.com/Codium-ai/cover-agent) |
| **Chromatic** | UI testing | [chromatic.com](https://chromatic.com) |
| **Applitools** | Visual testing | [applitools.com](https://applitools.com) |
| **QA Wolf** | E2E testing | [qawolf.com](https://qawolf.com) |

### Traditional Testing

| Tool | Purpose | Link |
|------|---------|------|
| **Jest** | JavaScript testing | [jestjs.io](https://jestjs.io) |
| **Pytest** | Python testing | [pytest.org](https://pytest.org) |
| **Playwright** | E2E testing | [playwright.dev](https://playwright.dev) |
| **Cypress** | E2E testing | [cypress.io](https://cypress.io) |

---

## Infrastructure Tools

### Model Serving

| Tool | Purpose | Link |
|------|---------|------|
| **vLLM** | LLM inference | [vllm.ai](https://vllm.ai) |
| **TGI** | HuggingFace inference | [huggingface.co/docs/text-generation-inference](https://huggingface.co/docs/text-generation-inference) |
| **Ollama** | Local LLMs | [ollama.ai](https://ollama.ai) |
| **LM Studio** | Desktop LLMs | [lmstudio.ai](https://lmstudio.ai) |

### Orchestration

| Tool | Purpose | Link |
|------|---------|------|
| **Kubernetes** | Container orchestration | [kubernetes.io](https://kubernetes.io) |
| **Docker Compose** | Local orchestration | [docs.docker.com/compose](https://docs.docker.com/compose) |
| **Nomad** | HashiCorp orchestration | [nomadproject.io](https://nomadproject.io) |

### CI/CD

| Tool | Purpose | Link |
|------|---------|------|
| **GitHub Actions** | CI/CD | [github.com/features/actions](https://github.com/features/actions) |
| **GitLab CI** | CI/CD | [docs.gitlab.com/ee/ci](https://docs.gitlab.com/ee/ci) |
| **CircleCI** | CI/CD | [circleci.com](https://circleci.com) |
| **ArgoCD** | GitOps | [argoproj.github.io/cd](https://argoproj.github.io/cd) |

---

## Tool Selection Guide

### By Use Case

| Use Case | Recommended Tools |
|----------|-------------------|
| **Quick Start** | GitHub Copilot + Cursor |
| **Privacy-First** | Ollama + Continue |
| **Enterprise** | Claude Code + Langfuse |
| **Open Source** | Aider + LangChain |
| **Complex Workflows** | CrewAI + LangGraph |
| **RAG Applications** | LlamaIndex + Pinecone |

### By Budget

| Budget | Stack |
|--------|-------|
| **Free** | Codeium + Chroma + Langfuse (free tier) |
| **$50/mo** | Copilot + Pinecone + Helicone |
| **$200/mo** | Claude Code + Pinecone + LangSmith |
| **Enterprise** | Custom + Weaviate + Langfuse Enterprise |

### By Team Size

| Team Size | Recommended Setup |
|-----------|-------------------|
| **Solo** | Cursor + Ollama |
| **Small (2-10)** | Copilot + LangChain + Chroma |
| **Medium (10-50)** | Claude Code + CrewAI + Pinecone |
| **Large (50+)** | Custom + LangGraph + Weaviate |

---

## Tool Integration Matrix

| Tool | LangChain | CrewAI | AutoGen | LlamaIndex |
|------|-----------|--------|---------|------------|
| Pinecone | ✅ | ✅ | ✅ | ✅ |
| Weaviate | ✅ | ✅ | ✅ | ✅ |
| Langfuse | ✅ | ✅ | ⚠️ | ✅ |
| LangSmith | ✅ | ⚠️ | ⚠️ | ⚠️ |
| MCP | ✅ | ⚠️ | ⚠️ | ✅ |

---

## Emerging Tools

### Watch List

| Tool | Category | Status | Why Watch |
|------|----------|--------|-----------|
| **Devin** | Autonomous coding | Beta | First AI software engineer |
| **OpenAI Codex** | Code generation | Coming | Next-gen coding model |
| **Gemini Code Assist** | IDE integration | Growing | Google's entry |
| **Amazon Q** | Enterprise AI | Growing | AWS integration |

---

## Contributing

To add a tool to this directory:

1. Ensure tool is actively maintained
2. Provide accurate pricing information
3. Include objective assessment
4. Submit PR with description

---

*Tools directory updated monthly. Last updated: 2025-01-21*

*Suggest additions: tools@company.com*

---

## Related Resources

- [Comparison Matrices](./COMPARISON_MATRICES.md) - Detailed comparisons
- [Decision Matrix](./DECISION_MATRIX.md) - Selection guidance
- [Benchmarks](./BENCHMARKS.md) - Performance data
- [Templates](./TEMPLATES.md) - Configuration examples
