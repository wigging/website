---
date: December 7, 2025
description: Some helpful commands for using Git in the terminal
tags: git
---

## Git Commands

Here are some useful commands for configuring and using Git in the terminal.

### Email configuration

Commands for configuring the email address globally or for a single repository.

```bash
# Set the global email address for commits
git config --global user.email "user@example.com"

# Set the email address for commits in the current repository
git config user.email "user@example.com"
```

### Rewrite history

Use the [git-filter-repo](https://github.com/newren/git-filter-repo) tool to rewrite the history of a Git repository. This can be used to change the email address associated with commits. The command shown below uses uvx to run git-filter-repo and change the old email to a new email address. The body of the callback represents the body of a Python function. Note the function must return a bytestring instead of a string.

```bash
uvx git-filter-repo --force --email-callback '
  return email.replace(b"old@email.com", b"new@email.com")
'
```

### Tags

Commands for working with tags and pushing tags to a remote repository.

```bash
# List all the tags in a repository's history
git tag

# Create a lightweight tag for the current commit
git tag v25.12

# Push the tag to the remote origin repository
git push origin v25.12

# Push all tags to the remote origin repository
git push origin --tags
```
