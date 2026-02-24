# Security Hardening Guide

Comprehensive security hardening for autonomous AI coding systems.

## Security Principles

### Zero Trust Architecture
1. **Never trust, always verify**
2. **Assume breach**
3. **Least privilege access**
4. **Continuous monitoring**

### Defense in Depth
Multiple security layers:
1. Network security
2. Application security
3. Data security
4. Access security
5. Audit security

## Hardening Checklist

### 1. Sandboxing (Critical)

#### gVisor Setup
```bash
# Install gVisor
(
  set -e
  ARCH=$(uname -m)
  URL=https://storage.googleapis.com/gvisor/releases/release/latest
  wget ${URL}/${ARCH}/runsc ${URL}/${ARCH}/runsc.sha512
  sha512sum -c runsc.sha512
  rm -f runsc.sha512
  sudo mv runsc /usr/local/bin/
  sudo chmod +x /usr/local/bin/runsc
)

# Configure Docker
sudo /usr/local/bin/runsc install
sudo systemctl reload docker

# Run container with gVisor
docker run --runtime=runsc -it myapp
```

#### Kata Containers Setup
```bash
# Install Kata
sudo snap install kata-containers

# Configure containerd
sudo mkdir -p /etc/containerd/
containerd config default | sudo tee /etc/containerd/config.toml

# Update runtime
sudo sed -i 's/runtime_type = "io.containerd.runc.v2"/runtime_type = "io.containerd.kata.v2"/' /etc/containerd/config.toml

# Restart containerd
sudo systemctl restart containerd
```

### 2. Network Security

#### Network Policies
```yaml
# Deny all egress
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: ai-agent-deny-egress
spec:
  podSelector:
    matchLabels:
      app: ai-agent
  policyTypes:
  - Egress
  egress: []  # No egress allowed
```

#### Allow Specific Egress
```yaml
# Allow only required endpoints
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: ai-agent-allow-egress
spec:
  podSelector:
    matchLabels:
      app: ai-agent
  policyTypes:
  - Egress
  egress:
  - to:
    - namespaceSelector:
        matchLabels:
          name: kube-system
    ports:
    - protocol: UDP
      port: 53
  - to:
    - ipBlock:
        cidr: 13.107.42.0/24  # Azure OpenAI
    ports:
    - protocol: TCP
      port: 443
```

### 3. File System Security

#### Read-Only Root Filesystem
```yaml
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
      - name: ai-agent
        securityContext:
          readOnlyRootFilesystem: true
        volumeMounts:
        - name: tmp
          mountPath: /tmp
        - name: workspace
          mountPath: /workspace
      volumes:
      - name: tmp
        emptyDir: {}
      - name: workspace
        persistentVolumeClaim:
          claimName: workspace-pvc
```

#### Workspace Restrictions
```yaml
securityContext:
  runAsNonRoot: true
  runAsUser: 1000
  allowPrivilegeEscalation: false
  capabilities:
    drop:
    - ALL
  seccompProfile:
    type: RuntimeDefault
```

### 4. Secret Management

#### Vault Integration
```python
import hvac

# Initialize Vault client
client = hvac.Client(url='https://vault.example.com')
client.auth.kubernetes.login(
    role='ai-agent',
    jwt=open('/var/run/secrets/kubernetes.io/serviceaccount/token').read()
)

# Retrieve secret
secret = client.secrets.kv.v2.read_secret_version(
    path='ai-agent/api-keys'
)
api_key = secret['data']['data']['openai_key']
```

#### Environment Variables
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: ai-agent-secrets
type: Opaque
stringData:
  OPENAI_API_KEY: <encrypted-key>
  ANTHROPIC_API_KEY: <encrypted-key>
---
apiVersion: apps/v1
kind: Deployment
spec:
  template:
    spec:
      containers:
      - name: ai-agent
        envFrom:
        - secretRef:
            name: ai-agent-secrets
```

### 5. Input Validation

#### Prompt Injection Detection
```python
import re

PROMPT_INJECTION_PATTERNS = [
    r'ignore\s+(?:all\s+)?(?:previous|above|prior)',
    r'disregard\s+(?:all\s+)?instructions',
    r'system\s*:\s*',
    r'you\s+are\s+now',
    r'new\s+persona\s*:',
]

def detect_injection(prompt):
    for pattern in PROMPT_INJECTION_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            return True
    return False

# Usage
if detect_injection(user_input):
    raise SecurityError("Potential prompt injection detected")
```

#### Output Sanitization
```python
import bleach

def sanitize_output(output):
    # Remove potentially dangerous content
    allowed_tags = ['p', 'br', 'strong', 'em', 'code']
    allowed_attributes = {}

    return bleach.clean(
        output,
        tags=allowed_tags,
        attributes=allowed_attributes,
        strip=True
    )
```

### 6. Access Control

#### RBAC Configuration
```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: ai-agent-role
rules:
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["get", "list"]
- apiGroups: [""]
  resources: ["secrets"]
  verbs: []  # No access to secrets
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: ai-agent-binding
subjects:
- kind: ServiceAccount
  name: ai-agent
roleRef:
  kind: Role
  name: ai-agent-role
```

#### Tool-Level Permissions
```python
TOOL_PERMISSIONS = {
    'file_read': ['workspace/*'],
    'file_write': ['workspace/*'],
    'shell': [],  # Disabled
    'network': [],  # Disabled
}

def check_permission(tool, target):
    allowed = TOOL_PERMISSIONS.get(tool, [])
    for pattern in allowed:
        if fnmatch(target, pattern):
            return True
    return False
```

### 7. Audit Logging

#### Comprehensive Logging
```python
import logging
import json

# Configure structured logging
logging.basicConfig(
    format='%(message)s',
    level=logging.INFO
)

logger = logging.getLogger('ai-agent')

def log_action(action, user, details):
    log_entry = {
        'timestamp': datetime.utcnow().isoformat(),
        'action': action,
        'user': user,
        'details': details,
        'source_ip': request.remote_addr,
        'trace_id': get_trace_id(),
    }
    logger.info(json.dumps(log_entry))

# Usage
log_action(
    action='code_generated',
    user='developer@example.com',
    details={'model': 'gpt-4', 'tokens': 150}
)
```

#### Audit Trail Storage
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: fluentd-config
data:
  fluent.conf: |
    <source>
      @type tail
      path /var/log/ai-agent/*.log
      pos_file /var/log/fluent/ai-agent.log.pos
      tag ai-agent
      <parse>
        @type json
      </parse>
    </source>

    <match ai-agent>
      @type elasticsearch
      host elasticsearch
      port 9200
      index_name ai-agent-audit
    </match>
```

### 8. Container Security

#### Image Scanning
```bash
# Trivy scan
trivy image my-ai-agent:latest

# Snyk scan
snyk container test my-ai-agent:latest

# Grype scan
grype my-ai-agent:latest
```

#### Distroless Images
```dockerfile
# Build stage
FROM python:3.11-slim as builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# Runtime stage
FROM gcr.io/distroless/python3-debian12
COPY --from=builder /root/.local /home/nonroot/.local
COPY --chown=nonroot:nonroot . /app
WORKDIR /app
USER nonroot
ENV PATH=/home/nonroot/.local/bin:$PATH
CMD ["python", "-m", "ai_agent"]
```

### 9. Code Security

#### Dependency Scanning
```yaml
# GitHub Actions
name: Security Scan
on: [push, pull_request]

jobs:
  scan:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Run Snyk
      uses: snyk/actions/python@master
      env:
        SNYK_TOKEN: ${{ secrets.SNYK_TOKEN }}

    - name: Run Bandit
      run: |
        pip install bandit
        bandit -r . -f json -o bandit-report.json

    - name: Run Safety
      run: |
        pip install safety
        safety check
```

#### Secret Scanning
```yaml
# Pre-commit hook
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    hooks:
      - id: detect-private-key

  - repo: https://github.com/Yelp/detect-secrets
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']
```

### 10. Runtime Security

#### Falco Rules
```yaml
# Detect unusual file access
- rule: AI Agent Sensitive File Access
  desc: Detect access to sensitive files
  condition:>
    spawned_process and
    container.name contains "ai-agent" and
    (fd.name contains "/etc/shadow" or
     fd.name contains "/etc/passwd")
  output:>
    Sensitive file accessed
    user=%user.name file=%fd.name
  priority: WARNING

# Detect network connections
- rule: AI Agent Network Connection
  desc: Detect unexpected network connections
  condition:>
    outbound and
    container.name contains "ai-agent" and
    not (fd.sip in (trusted_endpoints))
  output:>
    Unexpected network connection
    connection=%fd.name
  priority: NOTICE
```

## Security Hardening Checklist

### Pre-Deployment
- [ ] Sandboxing configured (gVisor/Kata)
- [ ] Network policies defined
- [ ] Secrets management implemented
- [ ] RBAC configured
- [ ] Container image scanned
- [ ] Dependencies audited
- [ ] Secrets scanning enabled

### Runtime
- [ ] Audit logging enabled
- [ ] Monitoring configured
- [ ] Alert rules defined
- [ ] Incident response plan
- [ ] Backup procedures
- [ ] Recovery tested

### Ongoing
- [ ] Regular security scans
- [ ] Dependency updates
- [ ] Access reviews
- [ ] Log analysis
- [ ] Penetration testing
- [ ] Security training

## Security Incident Response

### Detection
1. Monitor security alerts
2. Analyze suspicious activity
3. Correlate events
4. Determine scope

### Containment
1. Isolate affected systems
2. Block malicious traffic
3. Revoke compromised credentials
4. Preserve evidence

### Eradication
1. Remove malware
2. Patch vulnerabilities
3. Reset credentials
4. Update configurations

### Recovery
1. Restore from clean backups
2. Verify system integrity
3. Monitor for recurrence
4. Document lessons learned

## Security Tools

### Container Security
- **Trivy**: Vulnerability scanner
- **Falco**: Runtime security
- **Snyk**: Dependency scanning
- **Grype**: Container scanning

### Code Security
- **Bandit**: Python security
- **Semgrep**: Static analysis
- **CodeQL**: GitHub security
- **SonarQube**: Code quality

### Secrets Management
- **HashiCorp Vault**: Enterprise secrets
- **AWS Secrets Manager**: Cloud-native
- **GitHub Secrets**: CI/CD secrets
- **Mozilla SOPS**: Encrypted files

---

*Security is an ongoing process. Regular reviews, updates, and testing are essential.*
