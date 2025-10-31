---
title: Tmux Commands
date: October 30, 2025
tags: terminal
---

The tmux command line tool allows you to run and manage multiple processes within a single terminal session. Below are some useful commands for working with tmux.

```bash
# Create a new session named blah
tmux new -s blah

# Attach to a session named blah
tmux attach -t blah
tmux a -t blah

# List all active terminal sessions
tmux ls
```

```text
# Detach from the current session
Ctrl+b then d

# Rename the current window
Ctrl+b then ,
```

