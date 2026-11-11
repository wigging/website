---
date: November 11, 2026
description: Using the Amp app and its environment variables with a local project.
tags: terminal, amp
---

## Local Projects with Amp

[Amp](https://ampcode.com) provides a great development environment for using agents to write code. The Amp app can directly create threads for local projects if the Mac is enabled as a runner in the App Settings. However, if you don't want to make your Mac a runner using the App Settings, run the amp CLI in the local project directory to make that project available to the Amp app.

```bash
cd myproject
amp --no-tui --amp-env
```

This will serve the project to Amp and inject any environment variables defined in the Amp app into the terminal environment. Now you can select the local project when creating a new thread in the Amp app.
