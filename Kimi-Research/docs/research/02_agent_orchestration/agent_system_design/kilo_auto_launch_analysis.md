# Kilo Auto Launch Documentation Analysis

## Executive Summary

Kilo Auto Launch is a workspace-level configuration system that enables automatic initiation of AI coding tasks when opening a project in VS Code. Originally developed as an internal testing feature, Kilo exposed this capability to users for automating repetitive development workflows, enabling model comparison testing, and standardizing team onboarding experiences.

The feature operates through a simple JSON configuration file (`.kilocode/launchConfig.json`) that specifies the initial prompt, AI provider profile, and operational mode. Upon workspace activation, Kilo Code automatically detects this configuration and executes the predefined task sequence within approximately 500ms of extension activation.

**Key Architectural Insight**: Auto Launch represents a declarative approach to agent orchestration where workspace context itself triggers agent initialization, eliminating manual intervention while maintaining flexibility through profile and mode selection.

---

## Key Concepts & Features

### 1. Declarative Task Initialization

Auto Launch implements a **configuration-driven agent activation pattern** where the workspace contains the instructions for how the AI assistant should engage with the project:

```json
{
  "prompt": "Your task description here",
  "profile": "Profile Name (optional)",
  "mode": "mode-name (optional)"
}
```

**Core Design Philosophy**: The system treats workspace configuration as executable intent, transforming static project metadata into dynamic agent behavior.

### 2. Profile-Driven Model Selection

The `profile` field enables **context-aware model routing**, allowing different workspaces to automatically use different AI providers/models:

- **Exact Match Requirement**: Profile names must match exactly (case-sensitive, including emojis)
- **Fallback Behavior**: If profile switching fails, the task continues with current settings
- **Use Case**: Enables model comparison by creating multiple workspace configurations with identical prompts but different profiles

### 3. Mode-Based Behavior Customization

The `mode` field activates **predefined behavioral personas** that shape how the AI approaches tasks:

| Mode | Purpose | Use Case |
|------|---------|----------|
| `code` | General-purpose coding tasks | Default development work |
| `architect` | Planning and technical design | System design, API planning |
| `ask` | Questions and explanations | Learning, documentation review |
| `debug` | Problem diagnosis and troubleshooting | Bug investigation |
| `test` | Testing-focused workflows | Test generation, coverage analysis |
| Custom | User-defined mode slugs | Specialized workflows |

### 4. Built-in Modes System (Extended Context)

Kilo's mode system extends beyond Auto Launch into a comprehensive **Sticky Models** architecture:

- Each mode remembers the last model used with it
- Automatic model switching when changing modes
- Custom modes can be global (cross-project) or project-specific
- File access restrictions via `fileRegex` for safety

### 5. Execution Sequence

The Auto Launch system follows a **deterministic initialization sequence**:

1. VS Code workspace opens
2. Kilo Code extension activates
3. System checks for `.kilocode/launchConfig.json` (~500ms delay)
4. If profile specified → switch provider profile
5. If mode specified → switch operational mode
6. Launch task with predefined prompt
7. Sidebar receives focus automatically

---

## CLI Agent Launching Patterns

### Pattern 1: Extension-Mediated Launch (Auto Launch)

**Architecture**: VS Code Extension → Configuration Detection → Profile/Mode Switch → Task Execution

```
Workspace Open
    ↓
Extension Activation
    ↓
Config File Detection (.kilocode/launchConfig.json)
    ↓
Profile Resolution (optional)
    ↓
Mode Selection (optional)
    ↓
Task Injection
```

**Characteristics**:
- No CLI process spawned initially
- Runs within VS Code extension context
- Uses extension's authentication and settings
- Seamless UI integration

### Pattern 2: Agent Manager with CLI Backend

**Architecture**: VS Code Webview → CLI Process Spawn → Session Management → Worktree Isolation

```
Agent Manager Open
    ↓
CLI Process Spawn (kilocode CLI)
    ↓
Session Attachment (new or existing)
    ↓
Git Worktree Creation (Parallel Mode)
    ↓
Interactive Task Execution
    ↓
Approval/Control Loop
```

**Key Capabilities**:
- **Local Sessions**: Direct CLI execution with terminal integration
- **Session Resumption**: Reattach to existing sessions by ID
- **Parallel Mode**: Git worktree isolation for safe experimentation
- **Cloud Sync**: Cross-device session availability

### Pattern 3: Direct CLI Invocation

**Architecture**: Terminal → Kilo CLI → TUI/Interactive Mode

```bash
# Start interactive TUI
kilo

# Configuration-driven execution
kilocode config  # Set up authentication
```

**CLI Reference (Key Commands)**:
- `kilo` - Start interactive TUI
- `kilo --version` - Version check
- `kilo --help` - Command reference

### Pattern 4: Shell Integration-Driven Execution

**Architecture**: Terminal Command → Shell Integration Capture → AI Processing → Output Analysis

**Capabilities**:
- Real-time command output capture
- Exit code observation
- Working directory tracking
- Automatic error detection and fixing
- Bidirectional terminal-AI communication

**Configuration Options**:
- `Terminal Output Limit` (default: 500 lines)
- `Terminal Shell Integration Timeout` (default: 15s)

---

## IDE Integration Approaches

### VS Code Extension Integration

**Primary Integration Method**: Auto Launch is deeply embedded in the VS Code extension lifecycle:

1. **Activation Event**: Extension activates on workspace open
2. **File System Watcher**: Monitors `.kilocode/launchConfig.json`
3. **Settings Synchronization**: Profile/mode changes propagate through VS Code settings
4. **UI Integration**: Sidebar focus, webview panels, terminal integration

**Technical Implementation**:
```
VS Code Extension Host
    ├── Extension Activation
    ├── Configuration Provider
    ├── Profile Manager
    ├── Mode Switcher
    ├── Task Launcher
    └── Terminal Integration
```

### JetBrains Extension (Mentioned)

The documentation indicates JetBrains extension support, suggesting **cross-platform IDE compatibility** for core features.

### CLI as Universal Backend

**Strategic Architecture Decision**: Kilo CLI serves as the universal execution backend across all platforms:

```
┌─────────────────┐     ┌─────────────┐     ┌─────────────────┐
│   VS Code Ext   │────→│             │     │   Local Agent   │
├─────────────────┤     │   Kilo CLI  │────→│   Execution     │
│  JetBrains Ext  │────→│  (Backend)  │     │   Environment   │
├─────────────────┤     │             │     ├─────────────────┤
│   Terminal/CLI  │────→│             │     │  Git Worktrees  │
└─────────────────┘     └─────────────┘     │  Cloud Sessions │
                                            └─────────────────┘
```

### Webview-Based Agent Manager

**UI Architecture**: Agent Manager operates as a **persistent webview panel**:

- Stays active across focus changes
- Surfaces approval prompts for tool usage
- Shows branch names and worktree paths
- Provides Cancel vs Stop controls
- Displays completion/merge instructions

---

## Configuration & Usage

### File Location Convention

```
your-workspace/
└── .kilocode/
    └── launchConfig.json
```

**Design Rationale**: 
- `.kilocode/` directory serves as project-level Kilo configuration namespace
- Similar to `.vscode/` or `.idea/` IDE configuration patterns
- Enables version-controlled AI workspace setup

### Configuration Schema

```typescript
interface LaunchConfig {
  /** Required: Task message sent to AI on workspace open */
  prompt: string;
  
  /** Optional: Exact name of API Configuration Profile */
  profile?: string;
  
  /** Optional: Operational mode (code, architect, ask, debug, test, or custom) */
  mode?: string;
}
```

### Example Configurations

**Basic Task Launch**:
```json
{
  "prompt": "Review this codebase and suggest improvements for performance and maintainability"
}
```

**Profile-Specific Task**:
```json
{
  "prompt": "Create comprehensive unit tests for all components in the src/ directory",
  "profile": "GPT-4 Turbo"
}
```

**Architecture Planning**:
```json
{
  "prompt": "Design a scalable microservices architecture for this e-commerce platform with focus on security and performance",
  "profile": "🎻 Sonnet 4",
  "mode": "architect"
}
```

**Model Comparison Setup**:
```json
{
  "prompt": "Optimize this algorithm for better time complexity and explain your approach",
  "profile": "🧠 Qwen",
  "mode": "code"
}
```

### Timing & Behavior Specifications

| Aspect | Specification |
|--------|---------------|
| Trigger Delay | ~500ms after extension activation |
| Focus Behavior | Sidebar automatically receives focus |
| Execution Order | Profile switch → Mode switch → Task launch |
| Error Handling | Task continues with current settings if switch fails |
| Case Sensitivity | Profile/mode names are case-sensitive |

---

## Design Principles

### 1. Convention Over Configuration

Auto Launch follows **minimal configuration philosophy**:
- Single required field (`prompt`)
- Sensible defaults (current profile/mode if not specified)
- Standard file location convention
- Automatic execution without manual triggers

### 2. Graceful Degradation

**Failure Resilience**:
- Invalid profile → Continue with current profile
- Invalid mode → Continue with current mode
- Missing config → Normal startup (no error)
- JSON syntax error → Logged to Dev Console, no crash

### 3. Composability

**Layered Configuration Architecture**:
```
Base Configuration (Auto Launch)
    ↓
Profile Selection (API Provider + Model)
    ↓
Mode Selection (Behavioral Persona)
    ↓
Custom Rules (Project-specific instructions)
    ↓
Runtime Context (File mentions, @ references)
```

### 4. Workspace-Centric Design

**Project-Local Intelligence**:
- Configuration lives with project (version controllable)
- Different projects can have different AI behaviors
- Team-wide standardization through shared config
- No global state pollution

### 5. Testing-First Origin

**Historical Context**: Auto Launch originated as an internal testing feature:
- Designed for systematic model comparison
- Enables A/B testing of prompts across models
- Supports benchmarking workflows
- Facilitates regression testing of AI behaviors

### 6. Safety Through Isolation (Agent Manager)

**Parallel Mode Architecture**:
- Git worktree isolation prevents main branch contamination
- Automatic cleanup of worktrees (branches preserved)
- Local ignore rules (`.git/info/exclude`) prevent git pollution
- Clean cooperative stop vs force termination options

---

## Relationship to Agent Orchestration

### Position in Kilo's Automation Ecosystem

```
┌─────────────────────────────────────────────────────────────┐
│                    KILO AUTOMATION STACK                     │
├─────────────────────────────────────────────────────────────┤
│  ORCHESTRATION LAYER                                         │
│  ├── Agent Manager (Interactive CLI process control)        │
│  ├── Auto Launch (Workspace-triggered initialization)       │
│  └── MCP (External tool integration)                        │
├─────────────────────────────────────────────────────────────┤
│  EXECUTION LAYER                                             │
│  ├── Kilo CLI (Universal backend)                           │
│  ├── Shell Integration (Terminal bidirectional comm)        │
│  └── Cloud Agent (Remote execution)                         │
├─────────────────────────────────────────────────────────────┤
│  CONFIGURATION LAYER                                         │
│  ├── Profiles (Model/Provider selection)                    │
│  ├── Modes (Behavioral personas)                            │
│  ├── Custom Rules (Project instructions)                    │
│  └── launchConfig.json (Auto Launch config)               │
├─────────────────────────────────────────────────────────────┤
│  INTEGRATION LAYER                                           │
│  ├── VS Code Extension                                      │
│  ├── JetBrains Extension                                    │
│  └── GitHub/Code Review Integrations                        │
└─────────────────────────────────────────────────────────────┘
```

### Auto Launch's Orchestration Role

**Function**: **Initiation Orchestrator**

Auto Launch serves as the **entry point orchestrator** in Kilo's agent system:

1. **Trigger Detection**: Monitors workspace state changes
2. **Configuration Resolution**: Gathers intent from `launchConfig.json`
3. **Context Preparation**: Switches profiles/modes as needed
4. **Agent Activation**: Injects initial prompt into AI system
5. **Handoff**: Transfers control to main AI interaction loop

### Comparison with Other Orchestration Patterns

| Pattern | Trigger | Control | Use Case |
|---------|---------|---------|----------|
| **Auto Launch** | Workspace open | Declarative config | Standardized project setup |
| **Agent Manager** | User action | Interactive UI | Long-running agent tasks |
| **MCP** | Tool call | Protocol-based | External tool integration |
| **Code Reviews** | GitHub webhook | Automated | CI/CD integration |

### Orchestration Best Practices (Documented)

**Development Workflows**:
- Include launch configs in project templates
- Trigger code reviews on PR branch open
- Launch documentation generation for new projects

**Testing & Comparison**:
- Create multiple configs for model A/B testing
- Benchmark AI performance systematically
- Compare approaches across profiles

**Team Collaboration**:
- Standardize AI configuration across team
- Automate onboarding with optimal settings
- Enforce coding standards via mode selection

---

## References (with Quality Scores)

### Primary Sources

| Source | URL | Quality Score | Notes |
|--------|-----|---------------|-------|
| Auto Launch Documentation | https://kilo.ai/docs/automate/extending/auto-launch | ⭐⭐⭐⭐⭐ (5/5) | Complete feature documentation with examples, troubleshooting |
| Agent Manager Documentation | https://kilo.ai/docs/automate/agent-manager | ⭐⭐⭐⭐⭐ (5/5) | Comprehensive CLI process management, parallel mode details |
| Shell Integration Documentation | https://kilo.ai/docs/automate/extending/shell-integration | ⭐⭐⭐⭐☆ (4/5) | Good technical detail on terminal integration |
| Kilo CLI Documentation | https://kilo.ai/docs/code-with-ai/platforms/cli | ⭐⭐⭐⭐☆ (4/5) | Installation, basic commands, configuration |
| Custom Modes Documentation | https://kilo.ai/docs/customize/custom-modes | ⭐⭐⭐⭐⭐ (5/5) | Detailed mode configuration, YAML/JSON formats |
| Automate Overview | https://kilo.ai/docs/automate | ⭐⭐⭐⭐☆ (4/5) | High-level ecosystem overview |

### Secondary Sources

| Source | URL | Quality Score | Notes |
|--------|-----|---------------|-------|
| Kilo CLI Blog Post | https://blog.kilo.ai/p/kilo-cli | ⭐⭐⭐☆☆ (3/5) | Announcement context, replatforming information |
| Kilo GitHub Repository | https://github.com/Kilo-Org/kilocode | ⭐⭐⭐⭐☆ (4/5) | Source code, issue tracking |

### Quality Assessment Criteria

- **⭐⭐⭐⭐⭐ (5/5)**: Comprehensive documentation with examples, troubleshooting, clear structure
- **⭐⭐⭐⭐☆ (4/5)**: Good coverage, some gaps in advanced scenarios
- **⭐⭐⭐☆☆ (3/5)**: Basic information, limited depth

---

## Key Findings Summary

### Architectural Insights

1. **Declarative Agent Orchestration**: Auto Launch demonstrates how workspace configuration can drive agent behavior without explicit user commands

2. **Layered Configuration Model**: The system separates concerns across profiles (who), modes (how), prompts (what), and rules (constraints)

3. **CLI as Backend Strategy**: Kilo's architecture positions CLI as the universal execution engine, with IDE extensions as frontends

4. **Testing-First Design**: Origin as internal testing tool explains emphasis on model comparison, reproducibility, and benchmarking

### Integration Patterns

1. **Extension Lifecycle Integration**: Auto Launch hooks into VS Code's extension activation for seamless workspace-triggered execution

2. **Git-Native Isolation**: Parallel Mode's worktree approach leverages Git's native isolation mechanisms

3. **Bidirectional Terminal Communication**: Shell integration enables true two-way communication between AI and terminal environment

### Best Practices Documented

1. **Project Template Integration**: Include launch configs in templates for consistent AI assistance
2. **Model Comparison Workflows**: Use multiple configs with identical prompts, different profiles
3. **Team Standardization**: Share configs to ensure consistent AI behavior across team
4. **Safety Through Isolation**: Use Parallel Mode for experimental changes

### Limitations & Constraints

1. **VS Code Dependency**: Auto Launch currently tied to VS Code extension lifecycle
2. **Single Config Per Workspace**: One `launchConfig.json` per project
3. **No Conditional Logic**: Simple JSON schema without branching/conditional execution
4. **Exact Match Requirements**: Profile/mode names must match exactly (case-sensitive)

---

*Analysis completed: Documentation review of Kilo Auto Launch and related agent orchestration systems*
