from __future__ import annotations

import re
from enum import Enum


class AtomType(str, Enum):
    TECHNIQUE = "TECHNIQUE"
    METRIC = "METRIC"
    CONSTRAINT = "CONSTRAINT"
    TOOL = "TOOL"
    COMBINATION = "COMBINATION"
    FAILURE_MODE = "FAILURE_MODE"
    ANTI_PATTERN = "ANTI_PATTERN"
    TRADEOFF = "TRADEOFF"
    RECIPE = "RECIPE"


class EvidenceStrength(str, Enum):
    STRONG = "STRONG"
    MODERATE = "MODERATE"
    WEAK = "WEAK"


class Domain(str, Enum):
    D1 = "D1"
    D2 = "D2"
    D3 = "D3"
    D4 = "D4"
    D5 = "D5"
    D6 = "D6"
    D7 = "D7"
    D8 = "D8"
    D9 = "D9"
    D10 = "D10"
    D11 = "D11"
    D12 = "D12"


DOMAIN_NAMES: dict[str, str] = {
    "D1": "Agent Architecture & Orchestration",
    "D2": "Task Management & Decomposition",
    "D3": "Context & Prompt Engineering",
    "D4": "Memory & Knowledge Systems",
    "D5": "Code Intelligence & Representations",
    "D6": "Testing & Validation",
    "D7": "Security & Guardrails",
    "D8": "Model Management & Routing",
    "D9": "CI/CD & DevOps",
    "D10": "Workspace & Infrastructure Management",
    "D11": "Human Interaction",
    "D12": "Self-Improvement & Optimization",
}


class SDLCPhase(str, Enum):
    P1 = "P1"
    P2 = "P2"
    P3 = "P3"
    P4 = "P4"
    P5 = "P5"
    P6 = "P6"
    P7 = "P7"
    P8 = "P8"


PHASE_NAMES: dict[str, str] = {
    "P1": "Discovery & Onboarding",
    "P2": "Planning & Design",
    "P3": "Implementation",
    "P4": "Testing & Verification",
    "P5": "Code Review",
    "P6": "Debugging & Error Recovery",
    "P7": "Deployment & Release",
    "P8": "Maintenance & Monitoring",
}


class ProductCategory(str, Enum):
    PC1 = "PC1"
    PC2 = "PC2"
    PC3 = "PC3"
    PC4 = "PC4"
    PC5 = "PC5"
    PC6 = "PC6"
    PC7 = "PC7"
    PC8 = "PC8"
    PC9 = "PC9"
    PC10 = "PC10"


PRODUCT_NAMES: dict[str, str] = {
    "PC1": "Modes",
    "PC2": "Skills",
    "PC3": "Workflows",
    "PC4": "Prompts",
    "PC5": "MCP Configurations",
    "PC6": "Rules",
    "PC7": "Context Management Strategies",
    "PC8": "Task Decomposition Patterns",
    "PC9": "Workspace Management",
    "PC10": "Techniques & Strategies",
}


# ---------------------------------------------------------------------------
# Domain keyword vocabularies (D1-D12)
# An atom is tagged with a domain when >=2 keywords match.
# ---------------------------------------------------------------------------

DOMAIN_KEYWORDS: dict[str, list[str]] = {
    "D1": [
        "agent", "orchestrat", "hierarchical", "swarm", "debate",
        "mixture of agents", "MoA", "delegation", "handoff", "consensus",
        "trust scor", "performance scor", "deadlock", "livelock",
        "state machine", "lifecycle", "multi-agent", "coordinator",
        "supervisor", "specialist", "mode switch",
    ],
    "D2": [
        "task decompos", "subtask", "dependency", "paralleliz",
        "commit", "branch", "conflict resolution", "work tree",
        "initiative", "atomic action", "sequenc", "priorit",
        "task graph", "topological", "kanban", "backlog",
    ],
    "D3": [
        "context window", "prompt engineer", "token budget", "compression",
        "attention", "placement", "context partition", "system prompt",
        "few-shot", "chain-of-thought", "CoT", "instruction",
        "context rotat", "context refresh", "token limit",
        "prompt template", "prompt structure", "LLMLingua",
        "Selective Context", "context poison",
    ],
    "D4": [
        "memory", "knowledge graph", "vector db", "vector database",
        "embedding", "retrieval", "RAG", "persistent",
        "short-term", "long-term", "cross-session", "episodic",
        "semantic search", "knowledge base", "auto-learn",
    ],
    "D5": [
        "AST", "CFG", "DFG", "CPG", "SSA", "Tree-sitter",
        "Sourcegraph", "CodeQL", "Semgrep", "Joern", "LSIF",
        "symbol index", "code graph", "parse", "taint",
        "semantic diff", "code representation", "call graph",
        "interprocedural", "intraprocedural", "type inference",
    ],
    "D6": [
        "test generat", "unit test", "integration test", "e2e test",
        "mutation test", "quality gate", "validation pipeline",
        "property-based", "behavioral test", "coverage",
        "happy path", "sad path", "test framework", "assertion",
    ],
    "D7": [
        "prompt injection", "hallucination", "slopsquat",
        "sandbox", "isolation", "privilege", "secret",
        "adversarial", "guardrail", "safety", "vulnerability",
        "package verif", "bidirectional", "unicode", "fabricat",
        "malicious", "attack", "defense", "security",
    ],
    "D8": [
        "model select", "model rout", "confidence-based",
        "cost-aware", "temperature", "fallback", "multi-model",
        "capability matrix", "hallucination profil", "token cost",
        "latency", "throughput", "model switch", "ensemble",
    ],
    "D9": [
        "CI/CD", "pipeline", "canary", "blue-green", "deploy",
        "self-healing", "container", "orchestration",
        "observability", "rollback", "build", "release",
        "continuous integration", "continuous delivery",
    ],
    "D10": [
        "workspace", "branch strateg", "work tree", "file organiz",
        "state persist", "artifact", "cleanup", "environment",
        "provisioning", "git worktree", "merge conflict",
    ],
    "D11": [
        "human", "escalat", "approval", "handoff",
        "confidence threshold", "notification", "explainab",
        "visualization", "user feedback", "human-in-the-loop",
        "HITL", "interactive",
    ],
    "D12": [
        "self-improv", "optimization loop", "A/B test",
        "regression detect", "prompt optim", "cost optim",
        "feedback loop", "auto-tun", "performance regression",
        "skill enable", "skill disable", "token efficien",
    ],
}


# ---------------------------------------------------------------------------
# SDLC phase keyword vocabularies (P1-P8)
# ---------------------------------------------------------------------------

PHASE_KEYWORDS: dict[str, list[str]] = {
    "P1": [
        "scan", "onboard", "discover", "map dependen",
        "architecture extraction", "entrypoint", "endpoint",
        "pattern recognition", "gap analysis", "repo grok",
        "codebase scan", "API surface", "initial",
    ],
    "P2": [
        "plan", "design", "decompos", "sequenc",
        "architecture decision", "specification", "risk assess",
        "resource estim", "branch strategy", "blueprint",
    ],
    "P3": [
        "implement", "code generat", "write code", "coding",
        "style adheren", "incremental valid", "model select",
        "anti-hallucination", "package verif", "generation",
    ],
    "P4": [
        "test", "verif", "quality gate", "mutation",
        "performance profil", "security scan", "validation",
        "coverage", "assertion", "behavioral",
    ],
    "P5": [
        "code review", "review", "semantic diff", "change impact",
        "refactor", "anti-pattern detect", "review checklist",
        "taint analysis", "pull request",
    ],
    "P6": [
        "debug", "error recovery", "root cause", "diagnos",
        "automated repair", "regression", "investigation",
        "fix", "troubleshoot", "stack trace",
    ],
    "P7": [
        "deploy", "release", "CI/CD", "canary", "blue-green",
        "rollback", "health check", "feature flag",
        "staging", "production",
    ],
    "P8": [
        "maintenance", "monitor", "incident", "performance monitor",
        "dependency update", "technical debt", "self-healing",
        "alert", "SLA", "uptime",
    ],
}


# ---------------------------------------------------------------------------
# Product category keyword vocabularies (PC1-PC10)
# ---------------------------------------------------------------------------

PRODUCT_KEYWORDS: dict[str, list[str]] = {
    "PC1": [
        "mode", "persona", "role definition", "perspective",
        "decision authority", "transition trigger", "agent role",
        "operational persona", "mode switch",
    ],
    "PC2": [
        "skill", "technique", "procedure", "step-by-step",
        "capability", "recipe", "method", "how to",
        "technique stack", "combination recipe",
    ],
    "PC3": [
        "workflow", "pipeline", "multi-step", "sequence",
        "phase", "entry criteria", "exit criteria",
        "quality gate", "end-to-end", "orchestrat",
    ],
    "PC4": [
        "prompt", "instruction", "system message",
        "prompt template", "prompt structure", "few-shot",
        "chain-of-thought", "prompt pattern", "output format",
    ],
    "PC5": [
        "MCP", "tool access", "server", "privilege",
        "capability mapping", "tool select", "MCP server",
        "tool integration", "function call",
    ],
    "PC6": [
        "rule", "constraint", "guardrail", "must not",
        "never", "always", "invariant", "enforcement",
        "severity", "non-negotiable", "hard limit",
    ],
    "PC7": [
        "context strateg", "window partition", "compression",
        "context manag", "token budget", "ordering rule",
        "refresh policy", "context select", "content select",
    ],
    "PC8": [
        "task decompos", "breakdown", "subtask",
        "granularity", "dependency rule", "paralleliz",
        "estimation heuristic", "validation checkpoint",
    ],
    "PC9": [
        "workspace", "branch strateg", "work tree",
        "file organiz", "state persist", "artifact manag",
        "cleanup protocol", "environment provision",
    ],
    "PC10": [
        "technique", "strategy", "situational", "playbook",
        "failure mode", "recovery", "fallback",
        "decision criteria", "recognition signal", "edge case",
    ],
}


# ---------------------------------------------------------------------------
# Known tool names for TOOL type classification
# ---------------------------------------------------------------------------

KNOWN_TOOLS: list[str] = [
    "Tree-sitter", "Sourcegraph", "CodeQL", "Semgrep", "Joern",
    "LSIF", "LLMLingua", "Selective Context", "LSP",
    "Language Server Protocol", "Copilot", "Cursor",
    "Aider", "SWE-bench", "SWE-agent", "Devin",
    "OpenHands", "AutoCodeRover", "Agentless",
    "GPT-4", "Claude", "Gemini", "DeepSeek",
    "Perplexity", "Anthropic", "OpenAI",
    "ChromaDB", "Pinecone", "Weaviate", "Qdrant", "Milvus",
    "FAISS", "LangChain", "LlamaIndex",
    "Docker", "Kubernetes", "Terraform",
    "GitHub Actions", "GitLab CI", "Jenkins",
    "Prometheus", "Grafana", "Datadog",
    "Volatility", "Ghidra", "IDA Pro",
    "pytest", "Jest", "Vitest", "Playwright", "Cypress",
    "ESLint", "Ruff", "Black", "Prettier",
    "Redis", "PostgreSQL", "MongoDB",
    "ArgoCD", "Flux", "Helm", "Istio", "Linkerd",
    "Vault", "AWS Secrets Manager",
    "Jaeger", "Tempo", "OpenTelemetry",
]


# ---------------------------------------------------------------------------
# Extraction patterns — classification regex (spec §5.2)
# ---------------------------------------------------------------------------

METRIC_PATTERN = re.compile(
    r"\d+[\.\d]*\s*[%x×]"
    r"|\d+\s*[-–]\s*\d+\s*%"
    r"|\d+[\.\d]*\s*(?:percent|reduction|improvement|increase|decrease|compression|accuracy|precision|recall|coverage|latency|throughput)",
    re.IGNORECASE,
)

CONSTRAINT_KEYWORDS = re.compile(
    r"\b(?:must|never|always|invariant|limit|require[ds]?|shall not|cannot|forbidden|prohibited)\b",
    re.IGNORECASE,
)

FAILURE_MODE_KEYWORDS = re.compile(
    r"\b(?:fail(?:ure|s|ed)?|break(?:s|ing)?|attacks?|vulnerabilit\w*|exploits?|fabricat\w*|hallucinat\w*|degrad\w*|corrupt\w*|poison\w*)\b",
    re.IGNORECASE,
)

ANTI_PATTERN_KEYWORDS = re.compile(
    r"\b(?:don'?t|avoid|anti-pattern|wrong|doesn'?t work|mistake|pitfall|misconception)\b",
    re.IGNORECASE,
)

TRADEOFF_KEYWORDS = re.compile(
    r"\b(?:vs\.?|tradeoff|trade-off|when .+ use|compared to|alternatively|whereas|on the other hand)\b",
    re.IGNORECASE,
)

COMBINATION_KEYWORDS = re.compile(
    r"\b(?:combin|together|unif|integrat|\+|along with|coupled with|hybrid)\b",
    re.IGNORECASE,
)

TECHNIQUE_VERBS = re.compile(
    r"\b(?:parse|build|generate|verify|extract|construct|analyze|compute|detect|transform|traverse|propagate|resolve|classify|decompose|compress|partition)\b",
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# Discard patterns — sections/content to filter out (spec §5.1)
# ---------------------------------------------------------------------------

DISCARD_SECTION_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"^\s*#+\s*See\s+also", re.IGNORECASE),
    re.compile(r"^\s*#+\s*Methodology", re.IGNORECASE),
    re.compile(r"^\s*#+\s*Search\s+Quer", re.IGNORECASE),
    re.compile(r"^\s*#+\s*References?\s*$", re.IGNORECASE),
    re.compile(r"^\s*#+\s*Related\s+", re.IGNORECASE),
    re.compile(r"^\s*#+\s*Navigation", re.IGNORECASE),
    re.compile(r"^\s*#+\s*Prior\s+Research\s+Integration", re.IGNORECASE),
    re.compile(r"^\s*#+\s*Table\s+of\s+Contents", re.IGNORECASE),
    re.compile(r"Unable to access external", re.IGNORECASE),
    re.compile(r"Future work should", re.IGNORECASE),
]

DISCARD_CONTENT_PATTERNS: list[re.Pattern[str]] = [
    re.compile(r"^\s*[-*]\s*\[.*\]\(.*\)\s*$"),
    re.compile(r"^\s*See also", re.IGNORECASE),
    re.compile(r"^\s*For more information", re.IGNORECASE),
]
