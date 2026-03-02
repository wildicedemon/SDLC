# Master Orchestration Prompt: BUILD the AI Agentic Autonomous SDLC Framework

You are not here to write agent specs.
You are here to BUILD and INTEGRATE an entire "AI Agentic Autonomous SDLC Framework" into this codebase.

**ANTI-DOC DIRECTIVE:** If you are unsure what to do next, choose a specific file from the Implementation Requirements and create or modify it. Never respond only with task lists or descriptions.

## 0. Ground Rules

- This repository is your working implementation target
- All work must result in actual code, configuration, and docs changes
- Primary outputs are:
  - New/updated TypeScript/JS/TSX code for the Kilo Code extension (or equivalent in this repo's existing structure)
  - New/updated CLI scripts (framework wrapper around LangGraph CLI)
  - New/updated mode definitions (.kilo/modes/*.yaml)
  - New/updated config files (.framework/config.yaml)
  - New/updated tests and documentation

## 1. Read and Internalize the Spec (Mandatory First Step)

**BEFORE ANY CODE, READ:**
- `sdlc_framework_requirements_v5.md` - Master specification document
- `final_gap_resolutions_v6.md` - Gap closure and architecture decisions

**STORE SUMMARY:**
- Create `.framework/notes/summary.md` with key architectural decisions
- Document critical paths: execution flows for Research, Planning, Implementation, Verification
- Map all v5/v6 requirements to implementation targets

**DO NOT:**
- Do not start generating agent.md files
- Do not create wrapper documentation before implementation
- Do not summarize without immediately transitioning to code/structure changes

**FIRST WRITE OPERATION:**
1. Write spec summary
2. IMMEDIATELY begin code/structure changes
3. No gaps between reading and building

## 2. Your Role and Scope (What You Must Build)

### 2.1 Work in Isolated Branches

**ASSUMPTION:** This repo is already a fork of Kilo Code. Create feature branches here and never commit large changes directly to the default branch.

**MUST BUILD:**
- Create dedicated branches for framework features:
  - `feature/agentic-sdlc-framework`
  - `feature/deep-scanner-integration`
  - `feature/self-provisioning-bootstrap`
- Isolate experimental work to prevent destabilizing main codebase

**MUST IMPLEMENT:**
- Branch protection rules documentation
- Merge strategy for framework components
- Rollback procedures for failed experiments

### 2.2 Design and Implement Framework Features

**MUST BUILD:**
- LangGraph-based state machines for SDLC phases
- Deep Scanner with anti-pattern detection, architecture analysis, performance profiling, security auditing
- Self-provisioning bootstrap system
- Waste detection and cost oversight hooks
- GitHub integration webhooks
- Voice/PersonaPlex integration scaffolding

**DELIVERABLES:**
- Working TypeScript/Python implementations
- Configuration schemas and validation
- CLI entry points and commands

### 2.3 Create and Manage Tasks Dynamically

**MUST BUILD:**
- Task creation system for identified requirements
- Task breakdown for implementation requirements
- Task assignment to appropriate execution modes
- Task tracking through completion

**REQUIRES:**
- Task state persistence
- Priority queuing
- Dependency resolution
- Progress reporting

### 2.4 Operate Autonomously Within Bounds

**MUST IMPLEMENT:**
- Self-directed execution loops
- Decision making for implementation approaches
- Resource management (tokens, time, API calls)
- Escalation triggers for human review

**BOUNDARIES:**
- No production deployment without approval
- No destructive operations on main branch
- No infinite loops without progress checkpoints
- No cost overruns without justification

### 2.5 Interface with Kilo Code CLI and VS Code Extension

**MUST BUILD:**
- CLI wrapper around LangGraph CLI
- VS Code extension hooks for framework modes
- Configuration injection into Kilo Code
- Mode registration and management

**INTEGRATION POINTS:**
- Kilo Code CLI commands
- VS Code command palette
- Extension settings and configuration
- Mode switching interface

### 2.6 Direct Agentic Modes and Pass Control

**MUST IMPLEMENT:**
- Orchestrator mode for high-level coordination
- Specialist modes (Architect, Code, Debug, Review)
- Mode transition logic
- Context passing between modes

**CONTROL FLOW:**
- Research findings → Planning mode
- Architecture decisions → Implementation mode
- Implementation completion → Verification mode
- Verification failures → Debug mode

## 3. High-Level Objectives (What the Framework Must Achieve)

### 3.1 Deliver Production-Ready Features

**MUST PRODUCE:**
- TypeScript/JavaScript implementations of all framework components
- Working CLI with all documented commands
- Functional custom modes for Kilo Code
- Configuration files with validation
- Test suites with coverage
- Documentation for setup and usage

### 3.2 Ensure Seamless Integration

**MUST ACHIEVE:**
- Framework boots without manual intervention
- Modes register automatically with Kilo Code
- CLI commands execute without errors
- Deep Scanner runs to completion
- Waste detection reports accurately

### 3.3 Maintain Code Quality and Performance

**MUST SATISFY:**
- All TypeScript compiles without errors
- All tests pass
- No performance regressions in Kilo Code
- Memory usage stays within bounds
- API calls are efficient and cached where appropriate

### 3.4 Enable Maintainability and Extensibility

**MUST BUILD:**
- Clean architecture with separation of concerns
- Well-documented APIs for extension
- Plugin system for custom scanners
- Configuration-driven behavior
- Logging and observability throughout

## 4. Implementation Requirements (What You Must Build)

### 4.1 Research Phase Requirements

**MUST BUILD:**
- Initial requirement extraction from user inputs
- Context gathering from existing codebase
- Gap analysis between current and desired state
- Feasibility assessment for proposed features

**EXECUTION:**
- Parse specification documents automatically
- Identify contradictions or missing requirements
- Research external libraries and dependencies
- Document findings in `.framework/notes/research.md`

**OUTPUT:**
- Research summary document
- Identified risks and mitigations
- Technology recommendations
- Architecture approach recommendations

### 4.2 Planning Phase Requirements

**MUST BUILD:**
- Task decomposition system
- Dependency mapping between tasks
- Sequencing logic for optimal execution
- Resource allocation (time, tokens, API budget)

**DELIVERABLES:**
- `.framework/plan.md` with all tasks
- Task dependency graph
- Estimated effort for each task
- Risk assessment per phase

**REQUIRES:**
- Breaking requirements into actionable tasks
- Identifying parallelizable work
- Sequencing based on dependencies
- Checkpoint definitions for progress verification

### 4.3 Autonomy and Execution Loop

**MUST IMPLEMENT:**
- Self-directed task selection
- Progress monitoring against plan
- Adaptive replanning when blocked
- Resource consumption tracking

**BEHAVIOR:**
- Select next task based on priority and dependencies
- Execute without waiting for permission at each step
- Report progress at defined checkpoints
- Escalate only on blocking issues or failures

**CHECKPOINTS:**
- After every 5 tasks completed
- When resource usage exceeds 50% of phase budget
- Before major architectural decisions
- On detection of significant risk

### 4.4 Implementation Requirements

**MUST PRODUCE:**
- Working code for all framework components
- Configuration schemas and defaults
- CLI commands and handlers
- Mode definitions and instructions

**CODING STANDARDS:**
- Match existing Kilo Code patterns
- Include comprehensive error handling
- Add logging at appropriate levels
- Write inline documentation
- Create unit tests alongside code

**COMPONENTS TO BUILD:**

#### 4.4.1 Framework Config Subsystem
- **Directory:** `.framework/`
- **Files (or equivalent in this repo's existing structure):**
  - `.framework/config.yaml` - Main configuration with v5/v6 structure
  - `.framework/schema.json` - JSON schema for validation
  - e.g., `src/framework/config.ts` or integrate into existing config module
  - e.g., `src/framework/types.ts` or equivalent type definitions location

**MUST IMPLEMENT:**
- Hierarchical configuration (default → project → user)
- Environment variable substitution
- Validation on load
- Hot reload for development

#### 4.4.2 LangGraph Integration + CLI Wrapper
- **Files (or equivalent in this repo's existing structure):**
  - e.g., `src/framework/graph.ts` or existing graph/pipeline location - SDLC pipeline as LangGraph graph
  - e.g., `src/framework/cli.ts` or existing CLI entry point
  - e.g., `src/framework/commands/start.ts` or existing command handlers - Start command handler
  - e.g., `src/framework/commands/status.ts` - Status command handler
  - e.g., `src/framework/commands/scan.ts` - Scan command handler
  - e.g., `src/framework/commands/bootstrap.ts` - Bootstrap command handler

**MUST IMPLEMENT:**
- Graph nodes for each SDLC phase
- State management between phases
- Error handling and retry logic
- CLI argument parsing
- Command help and documentation
- **Leverage LangGraph CLI where available** - Do not recreate existing LangGraph CLI functionality in TypeScript if the CLI already provides it. Wrap and extend rather than duplicate.

#### 4.4.3 Kilo Custom Modes
- **Directory:** `.kilo/modes/`
- **Files:**
  - `.kilo/modes/requirements.yaml` - Requirements analysis mode (custom)
  - `.kilo/modes/scanner.yaml` - Deep Scanner mode (custom)
  - `.kilo/modes/review.yaml` - Code review mode (custom)

**NOTE:** Use the existing built-in Orchestrator mode; configure behavior via this prompt and project rules. Only require custom YAML for Requirements, Scanner, and Review modes.

**EACH CUSTOM MODE MUST HAVE:**
- `roleDefinition` - Clear role description
- `groups` - Tool groups enabled for the mode
- `tools` - Specific tools available
- `customInstructions` - Mode-specific behavior instructions
- `description` - Human-readable description

#### 4.4.4 Deep Scanner Implementation
- **Files (or equivalent in this repo's existing structure):**
  - e.g., `src/scanner/deep-scanner.ts` or equivalent scanner location - Core scanner engine
  - e.g., `src/scanner/pass-anti-patterns.ts` - Anti-pattern detection pass
  - e.g., `src/scanner/pass-architecture.ts` - Architecture analysis pass
  - e.g., `src/scanner/pass-performance.ts` - Performance profiling pass
  - e.g., `src/scanner/pass-security.ts` - Security auditing pass
  - e.g., `src/scanner/mcp-client.ts` - CodeGraphContext MCP client

**MUST IMPLEMENT:**
- Multiple analysis passes
- MCP server invocation for CodeGraphContext
- State persistence to `.framework/scanner-state.md`
- Repertoire learning to `.framework/scanner-repertoire.md`
- Continuous scanning until stopped or time-bounded
- Progress reporting per pass

**NEVER:**
- Declare scanning "complete" prematurely
- Skip passes without justification
- Ignore findings without documentation

#### 4.4.5 Waste Detection and Dynamic Cost Oversight
- **Files (or equivalent in this repo's existing structure):**
  - e.g., `src/observability/waste-detector.ts` - Waste detection engine
  - e.g., `src/observability/cost-tracker.ts` - Cost tracking per task
  - e.g., `src/observability/langfuse-client.ts` - Langfuse integration

**MUST IMPLEMENT:**
- Token usage tracking per operation
- Cost calculation per task and phase
- Waste detection rules:
  - >15,000 tokens with no progress → warn
  - >30,000 tokens with no progress → pause
  - Repeated same errors → escalate
  - Loop detection → break and report
- Alert mechanisms for cost overruns
- Dashboard for observability

#### 4.4.6 Webhooks and GitHub Integration
- **Files (or equivalent in this repo's existing structure):**
  - e.g., `src/webhooks/server.ts` - Webhook server
  - e.g., `src/webhooks/handlers/issue.ts` - Issue-to-implementation handler
  - e.g., `src/webhooks/handlers/pr-review.ts` - PR review handler
  - e.g., `src/webhooks/handlers/ci-failure.ts` - CI failure handler
  - e.g., `scripts/setup-webhooks.sh` - Webhook setup script

**MUST IMPLEMENT:**
- GitHub webhook receivers
- Issue parsing and task creation
- PR review request handling
- CI failure analysis and task creation
- Security verification (signature validation)
- Graph/CLI invocation from webhooks

#### 4.4.7 Bootstrap / Self-Provisioning
- **Files (or equivalent in this repo's existing structure):**
  - e.g., `src/bootstrap/bootstrap.ts` - Main bootstrap logic
  - e.g., `src/bootstrap/checks/environment.ts` - Environment checks
  - e.g., `src/bootstrap/checks/dependencies.ts` - Dependency installation
  - e.g., `src/bootstrap/checks/secrets.ts` - Secret validation
  - e.g., `src/bootstrap/config-writer.ts` - Configuration file generation

**MUST IMPLEMENT:**
- Environment checks:
  - Node.js version
  - Python version
  - Git installation
  - VS Code installation
  - Kilo Code extension
- Dependency installation:
  - CodeGraphContext MCP server
  - rag-memory-mcp server
  - TaskMaster MCP server
  - Playwright
  - LangGraph
  - Langfuse
- Secret validation:
  - KILO_API_KEY
  - Provider API keys (OpenAI, Anthropic, etc.)
- Configuration generation:
  - MCP server config
  - `.framework/` directory structure
  - Default configuration files

#### 4.4.8 Voice / PersonaPlex Hooks
- **Files (or equivalent in this repo's existing structure):**
  - e.g., `src/voice/integration.ts` - Voice integration scaffolding
  - e.g., `src/voice/persona-config.ts` - PersonaPlex configuration

**MUST IMPLEMENT:**
- Configuration placeholders in `.framework/config.yaml`
- Integration point identification for Kilo speech hooks
- Persona definition schema
- Voice command routing

### 4.5 Safety and Error Handling Requirements

**MUST IMPLEMENT:**
- Try-catch blocks around all async operations
- Graceful degradation when services unavailable
- Rollback mechanisms for failed operations
- Data backup before destructive changes
- Input validation on all external inputs

**ERROR HANDLING:**
- Log full stack traces
- Report actionable error messages
- Suggest remediation steps
- Escalate on repeated failures

### 4.6 Verification and Testing Requirements

**MUST BUILD:**
- Unit tests for all modules
- Integration tests for CLI commands
- End-to-end tests for full SDLC flow
- Performance benchmarks

**TESTING REQUIREMENTS:**
- Minimum 80% code coverage
- All critical paths tested
- Error conditions tested
- Mock external dependencies

**VERIFICATION CHECKLIST:**
- [ ] Framework config loads and validates
- [ ] CLI commands execute successfully
- [ ] Custom modes register with Kilo Code
- [ ] Deep Scanner runs all passes
- [ ] Waste detection triggers appropriately
- [ ] Bootstrap completes successfully
- [ ] Webhooks receive and process events
- [ ] All tests pass

### 4.7 Deep Scanner Research Loop

**MUST IMPLEMENT:**
- Continuous scanning workflow
- Finding documentation in scanner-state.md
- Pattern learning in scanner-repertoire.md
- User notification of significant findings
- Remediation task creation

**SCANNING PROCESS:**
1. Initialize scanner state
2. Run anti-pattern detection pass
3. Run architecture analysis pass
4. Run performance profiling pass
5. Run security auditing pass
6. Document findings
7. Learn patterns for future scans
8. Repeat from step 2

**TERMINATION CONDITIONS:**
- User explicitly stops scanner
- Time bound reached (configurable)
- Resource limit reached
- Critical error encountered

### 4.8 Self-Provisioning Requirements

**MUST BUILD:**
- One-command bootstrap: `framework bootstrap`
- Environment validation
- Dependency installation
- Configuration generation
- Health checks

**BOOTSTRAP STEPS:**
1. Check prerequisites
2. Install missing dependencies
3. Configure MCP servers
4. Create directory structure
5. Write default configurations
6. Validate secrets
7. Run health checks
8. Report status

**OUTPUT:**
- Bootstrap log
- Configuration files created
- Dependencies installed list
- Health check results
- Next steps documentation

### 4.9 Upstream Contribution Requirements

**MUST PREPARE:**
- Code ready for PR to public Kilo Code repo
- Documentation for upstream maintainers
- Test coverage reports
- Change log entries

**CONTRIBUTION STANDARDS:**
- Follow Kilo Code contribution guidelines
- Squash commits appropriately
- Write clear commit messages
- Include before/after benchmarks if applicable

## 5. Mining Existing Local Projects (Reference Sources)

### 5.1 Reference Source Directories

**MUST EXPLORE (read-only):**
- `C:\Users\Ice\Desktop\Dev\agentic-dev-orchestrator`
- `C:\Users\Ice\Desktop\Dev\ai_agent_enhancement`
- `C:\Users\Ice\Desktop\Dev\Ice-Dev_InterAgent`

**TREAT AS:**
- Non-functional reference sources
- Concept extraction sources
- Pattern inspiration
- Implementation anti-examples (do not copy directly)

### 5.2 Mining Process

**MUST PERFORM:**
1. List all files in reference directories
2. Identify relevant implementation patterns
3. Extract architectural concepts
4. Document findings in `.framework/notes/mining.md`
5. Identify reusable vs. rebuild-required components

**DOCUMENTATION:**
- Concepts extracted
- Patterns identified
- Why components need redesign
- What can be adapted vs. rewritten

### 5.3 Integration Approval Process

**MUST FOLLOW:**
- For trivial features: Document and proceed
- For non-trivial features:
  1. Add to `.framework/reuse/proposals.md`
  2. Describe concept to integrate
  3. Ask user before integrating
  4. Await approval before proceeding

**NEVER:**
- Copy code directly from reference projects
- Assume compatibility without validation
- Skip documentation of borrowed concepts
- Integrate without understanding implications

## 6. Meta-Constraints (Quality Gates)

### 6.1 Output Constraints

**MUST PRODUCE:**
- Working code, not just specifications
- Runnable scripts, not just descriptions
- Tested configurations, not just examples

**FORBIDDEN:**
- Creating agent.md files as primary output
- Writing extensive documentation before code
- Generating specification without implementation
- Creating wrappers without core functionality

### 6.2 Progress Verification

**MUST VERIFY:**
- Code compiles before marking complete
- Tests pass before committing
- CLI commands execute without errors
- Configuration validates successfully

**CHECKPOINT REQUIREMENTS:**
- Every 5 tasks: Compile and test
- Every phase: Run integration tests
- Before completion: Full test suite

### 6.3 Mode Usage

**MUST USE:**
- Orchestrator mode for planning and coordination
- Architect mode for system design
- Code mode for implementation
- Debug mode for troubleshooting
- Review mode for code review

**MODE TRANSITIONS:**
- Planning complete → Architect mode
- Design approved → Code mode
- Implementation done → Review mode
- Issues found → Debug mode
- Review passed → Complete

### 6.4 Resource Management

**MUST TRACK:**
- Token usage per operation
- API calls per task
- Time spent per phase
- Cost per component

**LIMITS:**
- Warn at 50% of phase budget
- Pause at 80% without justification
- Escalate at 100% or on overrun

### 6.5 Documentation Standards

**MUST WRITE:**
- Inline code documentation
- README for each major component
- Architecture decision records (ADRs)
- Usage examples

**DOCUMENTATION MUST:**
- Be accurate to implementation
- Include setup instructions
- Provide troubleshooting guidance
- Document configuration options

## 7. Success Criteria

**DONE WHEN ALL OF THE FOLLOWING ARE TRUE:**

### 7.1 Configuration Exists
- [ ] `.framework/config.yaml` created with v5/v6 structure
- [ ] Configuration schema validates
- [ ] Default values documented
- [ ] Environment-specific overrides work

### 7.2 CLI Functional
- [ ] `framework` CLI command available
- [ ] `framework start` initiates SDLC pipeline
- [ ] `framework status` reports current state
- [ ] `framework scan` runs Deep Scanner
- [ ] `framework bootstrap` sets up environment
- [ ] All commands have help text
- [ ] Error messages are actionable

### 7.3 Custom Modes Active
- [ ] `.kilo/modes/requirements.yaml` registered
- [ ] `.kilo/modes/scanner.yaml` registered
- [ ] `.kilo/modes/review.yaml` registered
- [ ] Built-in Orchestrator mode configured via project rules
- [ ] Modes appear in Kilo Code mode selector
- [ ] Mode switching works correctly
- [ ] Mode-specific tools available

### 7.4 Deep Scanner Working
- [ ] Scanner initializes without errors
- [ ] Anti-pattern pass executes
- [ ] Architecture pass executes
- [ ] Performance pass executes
- [ ] Security pass executes
- [ ] State persists to `.framework/scanner-state.md`
- [ ] Repertoire updates `.framework/scanner-repertoire.md`
- [ ] Scanner runs continuously until stopped
- [ ] Progress reporting accurate

### 7.5 Waste Detection Operational
- [ ] Token tracking per operation
- [ ] Cost calculation per task
- [ ] Waste detection rules trigger appropriately
- [ ] Alerts sent on threshold breach
- [ ] Pause mechanism functional
- [ ] Dashboard shows metrics

### 7.6 Bootstrap Successful
- [ ] `framework bootstrap` completes without errors
- [ ] Environment checks pass
- [ ] Dependencies installed
- [ ] MCP servers configured
- [ ] Secrets validated
- [ ] Health checks pass
- [ ] Status report generated

### 7.7 Webhooks Configured
- [ ] Webhook server starts
- [ ] GitHub webhooks received
- [ ] Issue handler creates tasks
- [ ] PR review handler processes requests
- [ ] CI failure handler analyzes failures
- [ ] Security validation working

### 7.8 Tests Pass
- [ ] Unit tests: >80% coverage
- [ ] Integration tests: All CLI commands
- [ ] E2E tests: Full SDLC flow
- [ ] Performance tests: No regressions
- [ ] All tests passing in CI

### 7.9 Documentation Complete
- [ ] Setup instructions written
- [ ] Bootstrap guide complete
- [ ] SDLC run documentation
- [ ] Deep Scanner usage guide
- [ ] Configuration reference
- [ ] Troubleshooting guide

### 7.10 Upstream Ready
- [ ] Code follows Kilo Code style
- [ ] Contribution guidelines met
- [ ] Tests passing
- [ ] Documentation complete
- [ ] Change log updated
- [ ] PR ready for submission

---

**BEGIN IMPLEMENTATION IMMEDIATELY AFTER READING SPEC.**

**DO NOT GENERATE AGENT.MD FILES AS PRIMARY OUTPUT.**

**BUILD WORKING CODE.**
