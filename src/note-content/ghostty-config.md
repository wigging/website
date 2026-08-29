---
date: January 21, 2026
description: My configuration settings for the awesome Ghostty terminal
tags: terminal
---

## Ghostty Configuration

Ghostty is a modern terminal emulator for macOS and Linux with a native UI and GPU acceleration. My configuration settings for Ghostty on macOS are given below. The settings reside in `~/.config/ghostty/config` which is a plain text file. More information about Ghostty is available at <https://ghostty.org>.

```bash
# Configuration file for Ghostty
# https://ghostty.org

adjust-cursor-thickness = 2
adjust-cell-height = 3

font-family = Menlo
font-size = 13
font-style = Regular
font-style-bold = Regular
font-style-italic = Regular
font-style-bold-italic = Regular
font-thicken
font-thicken-strength = 100

macos-titlebar-style = native

shell-integration-features = ssh-terminfo

split-divider-color = 45475A

theme = Xcode Dark hc

window-colorspace = display-p3
window-height = 46
window-width = 140
window-theme = system

keybind = global:cmd+backquote=toggle_quick_terminal
```
