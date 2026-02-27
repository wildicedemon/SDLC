const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// Knowledge Atom Types
const ATOM_TYPES = [
    "TECHNIQUE", "METRIC", "CONSTRAINT", "TOOL", 
    "COMBINATION", "FAILURE MODE", "ANTI-PATTERN", 
    "TRADEOFF", "RECIPE"
];

// Evidence Strength Levels
const EVIDENCE_STRENGTH = ["STRONG", "MODERATE", "WEAK"];

// Technical Domains
const DOMAINS = [
    "D1: Meta Architecture", "D2: Agent Orchestration", "D3: Context & Memory Intelligence",
    "D4: Code Intelligence", "D5: SDLC Automation", "D6: Data Infrastructure",
    "D7: Human Interaction", "D8: Model Management", "D9: Research Discipline",
    "D10: Scaling Enterprise", "D11: Advanced Runtime", "D12: Self-Improvement"
];

// SDLC Phases
const SDLC_PHASES = [
    "P1: Requirements", "P2: Design", "P3: Implementation", "P4: Testing",
    "P5: Deployment", "P6: Operation", "P7: Maintenance", "P8: Retirement"
];

// Product Categories
const PRODUCT_CATEGORIES = [
    "PC1: AI Coding Assistants", "PC2: Agent Orchestration Frameworks",
    "PC3: Code Analysis Tools", "PC4: Testing Automation",
    "PC5: CI/CD Systems", "PC6: Context Management",
    "PC7: Knowledge Bases", "PC8: DevOps Platforms",
    "PC9: Security Tools", "PC10: Observability Platforms"
];

function main() {
    console.log("Starting knowledge atom extraction...");
    
    const allAtoms = [];
    let atomCounter = 1;
    
    // Process main research files
    const filesToProcess = [
        "docs/research/02_agent_orchestration/agent_system_design/patterns.md",
        "docs/research/03_context_memory_intelligence/context_management/patterns.md",
        "docs/research/05_sdlc_automation/testing_architecture/patterns.md"
    ];
    
    filesToProcess.forEach(filePath => {
        if (fs.existsSync(filePath)) {
            console.log(`Processing file: ${filePath}`);
            try {
                const content = fs.readFileSync(filePath, 'utf8');
                const sections = extractSections(content);
                
                sections.forEach(section => {
                    if (shouldKeep(section)) {
                        const atom = createAtom(atomCounter, section, filePath);
                        allAtoms.push(atom);
                        atomCounter++;
                    }
                });
                
            } catch (error) {
                console.error(`Error reading file ${filePath}:`, error);
            }
        }
    });
    
    console.log(`Extracted ${allAtoms.length} atoms`);
    
    // Save to JSON
    fs.writeFileSync('knowledge_atom_registry.json', JSON.stringify(allAtoms, null, 2));
    console.log('Registry saved to knowledge_atom_registry.json');
}

function extractSections(content) {
    const sections = [];
    const pattern = /### Pattern: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)/g;
    let match;
    
    while ((match = pattern.exec(content)) !== null) {
        sections.push(match[0].trim());
    }
    
    return sections;
}

function shouldKeep(content) {
    const discardPatterns = [
        /Definition: .*/i, /Definition of .*/i,
        /Introduction to .*/i, /Overview of .*/i,
        /This paper.*/i, /This study.*/i,
        /Background.*/i, /Related work.*/i,
        /Future work.*/i, /Conclusion.*/i,
        /Abstract.*/i, /Summary.*/i,
        /References.*/i, /Citations.*/i,
        /Literature review.*/i, /Survey of .*/i
    ];
    
    return !discardPatterns.some(pattern => pattern.test(content));
}

function createAtom(atomId, content, filePath) {
    let atomType = "TECHNIQUE";
    if (content.includes("Tradeoff")) {
        atomType = "TRADEOFF";
    } else if (content.includes("Anti-pattern")) {
        atomType = "ANTI-PATTERN";
    }
    
    let domains = ["D9: Research Discipline"];
    if (filePath.includes("agent")) {
        domains = ["D2: Agent Orchestration"];
    } else if (filePath.includes("context")) {
        domains = ["D3: Context & Memory Intelligence"];
    } else if (filePath.includes("testing")) {
        domains = ["D5: SDLC Automation"];
    }
    
    return {
        "ID": `KA-${String(atomId).padStart(3, '0')}`,
        "TYPE": atomType,
        "CONTENT": content,
        "EVIDENCE_STRENGTH": "STRONG",
        "SOURCE": [filePath],
        "DOMAINS": domains,
        "SDLC_PHASES": ["P1: Requirements", "P2: Design", "P3: Implementation"],
        "PRODUCTS": ["PC1: AI Coding Assistants", "PC2: Agent Orchestration Frameworks"]
    };
}

main();const path = require('path');
const { execSync } = require('child_process');

// Knowledge Atom Types
const ATOM_TYPES = [
    "TECHNIQUE", "METRIC", "CONSTRAINT", "TOOL", 
    "COMBINATION", "FAILURE MODE", "ANTI-PATTERN", 
    "TRADEOFF", "RECIPE"
];

// Evidence Strength Levels
const EVIDENCE_STRENGTH = ["STRONG", "MODERATE", "WEAK"];

// Technical Domains
const DOMAINS = [
    "D1: Meta Architecture", "D2: Agent Orchestration", "D3: Context & Memory Intelligence",
    "D4: Code Intelligence", "D5: SDLC Automation", "D6: Data Infrastructure",
    "D7: Human Interaction", "D8: Model Management", "D9: Research Discipline",
    "D10: Scaling Enterprise", "D11: Advanced Runtime", "D12: Self-Improvement"
];

// SDLC Phases
const SDLC_PHASES = [
    "P1: Requirements", "P2: Design", "P3: Implementation", "P4: Testing",
    "P5: Deployment", "P6: Operation", "P7: Maintenance", "P8: Retirement"
];

// Product Categories
const PRODUCT_CATEGORIES = [
    "PC1: AI Coding Assistants", "PC2: Agent Orchestration Frameworks",
    "PC3: Code Analysis Tools", "PC4: Testing Automation",
    "PC5: CI/CD Systems", "PC6: Context Management",
    "PC7: Knowledge Bases", "PC8: DevOps Platforms",
    "PC9: Security Tools", "PC10: Observability Platforms"
];

function main() {
    console.log("Starting knowledge atom extraction...");
    
    const allAtoms = [];
    let atomCounter = 1;
    
    // Process main research files
    const filesToProcess = [
        "docs/research/02_agent_orchestration/agent_system_design/patterns.md",
        "docs/research/03_context_memory_intelligence/context_management/patterns.md",
        "docs/research/05_sdlc_automation/testing_architecture/patterns.md"
    ];
    
    filesToProcess.forEach(filePath => {
        if (fs.existsSync(filePath)) {
            console.log(`Processing file: ${filePath}`);
            try {
                const content = fs.readFileSync(filePath, 'utf8');
                const sections = extractSections(content);
                
                sections.forEach(section => {
                    if (shouldKeep(section)) {
                        const atom = createAtom(atomCounter, section, filePath);
                        allAtoms.push(atom);
                        atomCounter++;
                    }
                });
                
            } catch (error) {
                console.error(`Error reading file ${filePath}:`, error);
            }
        }
    });
    
    console.log(`Extracted ${allAtoms.length} atoms`);
    
    // Save to JSON
    fs.writeFileSync('knowledge_atom_registry.json', JSON.stringify(allAtoms, null, 2));
    console.log('Registry saved to knowledge_atom_registry.json');
}

function extractSections(content) {
    const sections = [];
    const pattern = /### Pattern: [^\n]+(?:\n|$)([\s\S]*?)(?=\n### |$)/g;
    let match;
    
    while ((match = pattern.exec(content)) !== null) {
        sections.push(match[0].trim());
    }
    
    return sections;
}

function shouldKeep(content) {
    const discardPatterns = [
        /Definition: .*/i, /Definition of .*/i,
        /Introduction to .*/i, /Overview of .*/i,
        /This paper.*/i, /This study.*/i,
        /Background.*/i, /Related work.*/i,
        /Future work.*/i, /Conclusion.*/i,
        /Abstract.*/i, /Summary.*/i,
        /References.*/i, /Citations.*/i,
        /Literature review.*/i, /Survey of .*/i
    ];
    
    return !discardPatterns.some(pattern => pattern.test(content));
}

function createAtom(atomId, content, filePath) {
    let atomType = "TECHNIQUE";
    if (content.includes("Tradeoff")) {
        atomType = "TRADEOFF";
    } else if (content.includes("Anti-pattern")) {
        atomType = "ANTI-PATTERN";
    }
    
    let domains = ["D9: Research Discipline"];
    if (filePath.includes("agent")) {
        domains = ["D2: Agent Orchestration"];
    } else if (filePath.includes("context")) {
        domains = ["D3: Context & Memory Intelligence"];
    } else if (filePath.includes("testing")) {
        domains = ["D5: SDLC Automation"];
    }
    
    return {
        "ID": `KA-${String(atomId).padStart(3, '0')}`,
        "TYPE": atomType,
        "CONTENT": content,
        "EVIDENCE_STRENGTH": "STRONG",
        "SOURCE": [filePath],
        "DOMAINS": domains,
        "SDLC_PHASES": ["P1: Requirements", "P2: Design", "P3: Implementation"],
        "PRODUCTS": ["PC1: AI Coding Assistants", "PC2: Agent Orchestration Frameworks"]
    };
}

main();
