# Git Command Cheat Sheet

A quick reference guide to commonly used Git commands.

## 1. Configuration

| Command | Description |
|---|---|
| `git config --global user.name "Name"` | Set Git username |
| `git config --global user.email "email"` | Set Git email |
| `git config --list` | View Git configuration |

## 2. Repository Management

| Command | Description |
|---|---|
| `git init` | Initialize a repository |
| `git clone URL` | Clone a remote repository |
| `git status` | Check repository status |
| `git remote -v` | View remote repositories |

## 3. Basic Git Operations

| Command | Description |
|---|---|
| `git add .` | Stage all changes |
| `git add filename` | Stage a specific file |
| `git commit -m "message"` | Save changes in a commit |
| `git log --oneline` | View commit history |
| `git diff` | View unstaged changes |

## 4. GitHub Operations

| Command | Description |
|---|---|
| `git push origin main` | Push commits to GitHub |
| `git pull origin main` | Download and integrate remote changes |
| `git fetch` | Retrieve remote updates |
| `git branch` | List local branches |
| `git switch branch-name` | Switch branches |
| `git switch -c branch-name` | Create and switch to a new branch |

## 5. Undo Operations

| Command | Description |
|---|---|
| `git restore filename` | Discard unstaged changes in a file |
| `git restore --staged filename` | Unstage a file |
| `git reset --soft HEAD~1` | Undo the last commit while keeping changes staged |

## 6. Typical Git Workflow

```bash
git status
git add .
git commit -m "Describe your changes"
git push origin main
```

## Conclusion

Git helps developers track changes, manage source code, collaborate with others, and maintain project history. GitHub provides a platform for hosting and sharing Git repositories.