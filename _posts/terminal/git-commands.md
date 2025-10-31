---
title: Git Commands
date: September 7, 2025
tags: git
---

Here are some useful commands for configuring and using Git in the terminal.

Set the global email address used for Git commits.

```bash
git config --global user.email "your_new_email@example.com"
```

Set the email address for the current repo, overrides the global setting for the project.

```bash
git config user.email "your_new_email@example.com"
```

Use the [git-filter-repo](https://github.com/newren/git-filter-repo) tool to rewrite the history of a Git repository. This can be used to change the email address associated with commits. The command shown below uses uvx to run git-filter-repo and change the old email to a new email address. The body of the callback represents the body of a Python function. Note the function must return a bytestring instead of a string.

```bash
uvx git-filter-repo --force --email-callback '
  return email.replace(b"old@email.com", b"new@email.com")
'
```

