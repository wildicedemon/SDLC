# Step-by-Step Git Commit Guide

**For:** SDLC Repository RECP Changes  
**Date:** 2026-03-02  
**Total Changes:** 118 files deleted, 13 modified, 14 created

---

## Where to Run These Commands

**Location:** You need to run these commands in a terminal/command prompt on your local machine where you have the SDLC repository folder.

**Prerequisites:**
- Git installed on your computer
- The SDLC-main folder downloaded/extracted to your computer

---

## Step 1: Open Terminal

### Windows:
1. Press `Win + R`
2. Type `cmd` and press Enter
3. OR use Git Bash if installed

### Mac:
1. Press `Cmd + Space`
2. Type `Terminal` and press Enter

### Linux:
1. Press `Ctrl + Alt + T`
OR
2. Open Terminal from applications menu

---

## Step 2: Navigate to the Repository

Type this command (replace the path with where you saved the folder):

```bash
cd /path/to/SDLC-main
```

**Examples:**
```bash
# Windows (Git Bash)
cd C:/Users/YourName/Downloads/SDLC-main

# Mac/Linux
cd ~/Downloads/SDLC-main
```

**Verify you're in the right place:**
```bash
pwd
```
This should show the path ending in "SDLC-main"

---

## Step 3: Initialize Git (One-time setup)

```bash
git init --initial-branch=main
```

**Expected output:**
```
Initialized empty Git repository in /path/to/SDLC-main/.git/
```

---

## Step 4: Configure Your Identity (One-time setup)

```bash
git config user.email "your-email@example.com"
git config user.name "Your Name"
```

**Replace with your actual email and name.**

---

## Step 5: Create the Refactor Branch

```bash
git checkout -b refactor/restructure-20260302
```

**Expected output:**
```
Switched to a new branch 'refactor/restructure-20260302'
```

---

## Step 6: Stage All Changes

This adds all the changes (deletions, modifications, new files):

```bash
git add -A
```

---

## Step 7: Check What Will Be Committed

```bash
git status
```

**You should see:**
- A list of deleted files (cache, logs, etc.)
- Modified files (JSON repairs, docs)
- New files (RECP artifacts)
- Around 127+ files total

---

## Step 8: Commit Everything

You can do this as ONE commit (simpler):

```bash
git commit -m "refactor(recp): Complete repository restructuring

- Repair 3 malformed JSON files (remove null bytes)
- Sanitize security vulnerabilities (remove hardcoded secrets)
- Remove 74 Python cache files
- Remove 43 log files
- Remove 3 empty placeholder files
- Delete duplicate registry (master_knowledge_atoms.json)
- Update 10 documentation files with correct references
- Create RECP artifact documentation (12 files, 1339 lines)

All 12 entropy issues resolved:
- 5 CRITICAL (JSON repair, security)
- 5 HIGH (cache, logs, cleanup)
- 2 MEDIUM (consolidation, analysis)

100% knowledge retention verified."
```

**OR** as multiple commits (more detailed):

### Option B: Multiple Commits (More Granular)

```bash
# Commit 1: JSON repairs and security
git add knowledge_atom_extractor/schemas/knowledge_atom_schema.json registry_simple.json master_knowledge_atoms.json .kilocode/mcp.json .gitignore
git commit -m "refactor(recp): Cycle 1 - Repair CRITICAL infrastructure issues

- Fix malformed JSON files (3 files with null bytes)
- Sanitize security vulnerabilities (remove hardcoded JWT/PAT)
- Replace secrets with environment variable placeholders
- Add .env to .gitignore

Cycle-1"

# Commit 2: Cache and log cleanup
git add -A
git commit -m "refactor(recp): Cycle 2 - Clean HIGH severity issues

- Remove Python cache files (74 .pyc files)
- Remove __pycache__ directories (20+)
- Remove log files from logs/ (43 files)
- Remove empty placeholder files (3 files)
- Update .gitignore with logs/ pattern

Cycle-2"

# Commit 3: Final consolidation
git add -A
git commit -m "refactor(recp): Cycle 3 - Complete MEDIUM consolidation

- Delete duplicate registry (master_knowledge_atoms.json)
- Update all documentation references (10 files)
- Create RECP artifact documentation (12 files, 1339 lines)
- Verify no broken references to deleted files

Cycle-3"
```

---

## Step 9: Verify the Commit

```bash
git log --oneline -5
```

**You should see your commit(s) listed.**

Example output:
```
abc1234 refactor(recp): Complete repository restructuring
```

OR for multiple commits:
```
abc1234 refactor(recp): Cycle 3 - Complete MEDIUM consolidation
def5678 refactor(recp): Cycle 2 - Clean HIGH severity issues
ghi9012 refactor(recp): Cycle 1 - Repair CRITICAL infrastructure issues
```

---

## Step 10: Check Nothing is Left Uncommitted

```bash
git status
```

**Expected output:**
```
On branch refactor/restructure-20260302
nothing to commit, working tree clean
```

---

## What You've Accomplished

✅ All changes are now committed to git  
✅ Changes are on a separate branch (safe)  
✅ Full history preserved with descriptive messages  
✅ Ready to push to GitHub/GitLab if needed  

---

## Optional: Push to Remote Repository

If you have a GitHub/GitLab repository:

```bash
# Add remote (replace with your repo URL)
git remote add origin https://github.com/yourusername/SDLC.git

# Push the branch
git push -u origin refactor/restructure-20260302
```

---

## Troubleshooting

### "Not a git repository" error
**Solution:** Run `git init` first (Step 3)

### "Please tell me who you are" error
**Solution:** Run Step 4 to configure email and name

### "Changes not staged" after git add
**Solution:** Some files might be in .gitignore. Check with `git status`

### Want to see what changed?
```bash
git diff --stat
```

### Want to undo the commit?
```bash
git reset --soft HEAD~1
```
(This keeps your changes but undoes the commit)

---

## Quick Reference

| Command | Purpose |
|---------|---------|
| `cd /path/to/SDLC-main` | Navigate to folder |
| `git init --initial-branch=main` | Initialize git |
| `git checkout -b branch-name` | Create and switch to branch |
| `git add -A` | Stage all changes |
| `git commit -m "message"` | Commit changes |
| `git status` | Check status |
| `git log --oneline` | View commit history |

---

**Need Help?** All the detailed commit messages are in `COMMIT_LOG.md` if you want to copy-paste them.
