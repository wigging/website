---
title: Initialize a Server with Cloud-init
date: October 24, 2025
tags: terminal
---

Most cloud platforms like DigitalOcean and Hetzner support a cloud-init YAML configuration file to initialize a server with networking, packages, and other system settings. The example below is for creating an Ubuntu server that disables root login, creates a non-root user named `homer`, turns off SSH password authentication, changes the SSH port to 2222, creates a basic `.vimrc` file, and installs uv for Python development.

```yaml
#cloud-config

# Create a non-root sudo user
users:
  - name: homer
    groups: sudo
    shell: /bin/bash
    sudo: "ALL=(ALL) NOPASSWD:ALL"
    ssh_authorized_keys:
      - <public-ssh-key>

# Disable root login and SSH password auth
disable_root: true
ssh_pwauth: false

# Update and upgrade packages
package_update: true
package_upgrade: true

# Create configuration files for SSH and vim
write_files:
  - path: /etc/ssh/sshd_config.d/custom.conf
    content: |
      PasswordAuthentication no
      PermitRootLogin no
      Port 2222
      MaxAuthTries 3
      AllowTcpForwarding no
      X11Forwarding no
      AllowAgentForwarding no
      AllowUsers homer
  - owner: homer:homer
    path: /home/homer/.vimrc
    defer: true
    content: |
      set nocompatible
      filetype plugin indent on
      syntax on
      set backspace=indent,eol,start
      set clipboard=unnamed
      set hidden
      set hlsearch
      set mouse=a
      set number
      set noswapfile
      set laststatus=2
      imap jj <Esc>

# Install uv for user and reboot system
runcmd:
  - sudo -u homer -i bash -c "curl -LsSf https://astral.sh/uv/install.sh | sh"
  - reboot
```

Connect to this server over SSH port 2222 using the command given below. This must be done from the machine that contains the public SSH key that was used in the cloud-init config file.

```bash
ssh -p 2222 homer@<ip-address-of-server>
```

You can also use the cloud-init configuration for firewall settings. But cloud platforms usually provide their own firewall that can be configured in their online dashboard. Either way it is a good idea to only open ports that are needed and restrict SSH to the IP address of the computer that is associated with the SSH key.

More information about Cloud-init is available at <https://cloudinit.readthedocs.io>.
