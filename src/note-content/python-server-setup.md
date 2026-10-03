---
date: January 8, 2026
description: Tools and configuration settings for deploying a Python app on a Hetzner cloud server.
tags: python, terminal, quart, caddy
---

## Server Setup for a Python Quart App

Deploying a web application to a cloud server offers great flexibility but can be a daunting task. The tools and configuration settings discussed below were used to deploy a Python Quart app to a Hetzner cloud server. This information is also applicable to other cloud server providers and web apps developed in other programming languages.

### Hetzner firewall settings

In the Hetzner dashboard, setup a firewall for the server to restrict inbound traffic to HTTP (TCP port 80) and HTTPS (TCP port 443). Also restrict inbound SSH connections to your computer's IP address and change the SSH port to something other than the default TCP port 22.

### Cloud-init configuration

Cloud-init is available on many cloud services to initialize a server with networking, SSH keys, packages, and other system settings. This reduces manual setup after the server is created and can be used to create multiple servers with the same configuration.

Below is a cloud-init configuration that creates a non-root sudo user and disables root login. SSH access is only given to the non-root user while other SSH settings such as a different port number are also defined. All of this can be copy-and-pasted into the Hetzner dashboard when creating a new server; but don't forget to replace the `USERNAME`, `PUBLIC_SSH_KEY`, and `SSH_PORT` with your own values. Installation for Fail2Ban, Caddy, and uv is also defined along with some sane vim settings.

```yaml
#cloud-config

# Create a non-root sudo user
users:
  - name: USERNAME
    groups: sudo
    shell: /bin/bash
    sudo: "ALL=(ALL) NOPASSWD:ALL"
    ssh_authorized_keys:
      - PUBLIC_SSH_KEY

# Disable root login and SSH password auth
disable_root: true
ssh_pwauth: false

# Update and upgrade packages
package_update: true
package_upgrade: true

# Install packages
packages:
  - fail2ban
  - debian-keyring
  - debian-archive-keyring
  - apt-transport-https
  - curl

# Create configuration files for SSH, fail2ban, and vim
write_files:
  - path: /etc/ssh/sshd_config.d/custom.conf
    content: |
      AllowAgentForwarding no
      AllowTcpForwarding no
      AllowUsers USERNAME
      PasswordAuthentication no
      PermitEmptyPasswords no
      PermitRootLogin no
      PubkeyAuthentication yes
      Port SSH_PORT
      MaxAuthTries 3
      X11Forwarding no

  - owner: USERNAME:USERNAME
    path: /home/USERNAME/.vimrc
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

runcmd:
  # Install Caddy
  - curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/gpg.key' | gpg --dearmor -o /usr/share/keyrings/caddy-stable-archive-keyring.gpg
  - curl -1sLf 'https://dl.cloudsmith.io/public/caddy/stable/debian.deb.txt' | tee /etc/apt/sources.list.d/caddy-stable.list
  - chmod o+r /usr/share/keyrings/caddy-stable-archive-keyring.gpg
  - chmod o+r /etc/apt/sources.list.d/caddy-stable.list
  - apt install -y caddy

  # Install uv for the sudo user
  - sudo -u USERNAME -i bash -c "curl -LsSf https://astral.sh/uv/install.sh | sh"
```

### Fail2Ban settings

Fail2Ban bans IP addresses that conduct too many failed login attempts. Put configuration settings for Fail2Ban in the `/etc/fail2ban/jail.local` file (see below). Replace `SSH_PORT` with the port number used above. Reload the client to enable the settings.

```ini
[DEFAULT]
bantime = 1h
maxretry = 3

[sshd]
enabled = true
port = SSH_PORT
```

```bash
sudo fail2ban-client reload
```

### Namecheap subdomain

Since I have a domain name for my personal website via Namecheap, I can setup a subdomain for the Quart app instead of purchasing a new domain. The first step to setup a subdomain is to get the IP address of the Hetzner server from the Hetzner Cloud Console. Next, log into Namecheap and select the domain from the Domain List then click Manage. In the Advanced DNS tab, add an A Record where the Host is `myapp` and the Value is the IP address of the Hetzner server. If the domain is `example.com` then the Quart app will be accessible from `myapp.example.com`. Verify the subdomain using the `nslookup myapp.example.com` command. In summary, for a subdomain such as `myapp.example.com`, create a new DNS record as follows:

- Type: A Record
- Host: myapp
- Value: HETZNER_SERVER_IP_ADDRESS
- TTL: Automatic

### Caddy proxy server

Use Caddy on the Hetzner server to point traffic to the Quart app by editing the `/etc/caddy/Caddyfile` as shown below. Caddy will automatically obtain and renew TLS certificates therefore the app will be served over HTTPS.

```yaml
myapp.example.com {
encode
reverse_proxy 127.0.0.1:8000
}
```

Next, reload Caddy to enable the configuration changes:

```bash
sudo caddy reload --config /etc/caddy/Caddyfile
```

### Rsync files to the server

Use rsync to upload code to the Hetzner server. Git could be used to pull down the files from a remote repository, but it would include all the Git history which isn't needed for a production server.

Dry-run deploy to the Hetzner server from current directory:

```bash
rsync -avzn --delete \
  --exclude='.git/' \
  --exclude='.venv/' \
  --exclude='.DS_Store' \
  --exclude='__pycache__/' \
  --exclude='*.pyc' \
  --exclude='.pytest_cache/' \
  --exclude='.ruff_cache/' \
  -e "ssh -p SSH_PORT" \
  ./ \
  USERNAME@HETZNER_SERVER_IP_ADDRESS:/home/USERNAME/myapp/
```

Production deploy to the Hetzner server from current directory:

```bash
rsync -avz --delete \
  --exclude='.git/' \
  --exclude='.venv/' \
  --exclude='.DS_Store' \
  --exclude='__pycache__/' \
  --exclude='*.pyc' \
  --exclude='.pytest_cache/' \
  --exclude='.ruff_cache/' \
  -e "ssh -p SSH_PORT" \
  ./ \
  USERNAME@HETZNER_SERVER_IP_ADDRESS:/home/USERNAME/myapp/
```

### System service

Serving the web app as a system service will automatically restart it whenever the machine reboots. Create a service at `/etc/systemd/system/myapp.service` with the following contents:

```ini
[Unit]
Description=Microblog web application
After=network.target

[Service]
User=ubuntu
WorkingDirectory=/home/ubuntu/myapp
ExecStart=/home/ubuntu/myapp/.venv/bin/hypercorn myapp.main --workers 2
Restart=always

[Install]
WantedBy=multi-user.target
```

After adding the service to the system, reload and run it with the following:

```bash
# Reload the system daemon then start the `myapp` service
sudo systemctl daemon-reload
sudo systemctl start myapp

# Check the status of the `myapp` service
sudo systemctl status myapp

# After uploading new code with rsync, restart service to apply changes
sudo systemctl restart myapp
```

The web app should now be available at the subdomain. Finally!

### Docker

Let's complicate things even more by putting everything in a Docker container and forward the container ports for external access. Just kidding, there's no need for Docker. Everything mentioned above works just fine.

### Further reading

See the links below for more information about the tools discussed above.

- Cloud-init <https://cloudinit.readthedocs.io>
- Caddy <https://caddyserver.com>
- Fail2Ban <https://github.com/fail2ban/fail2ban>
- Hetzner <https://www.hetzner.com>
- Namecheap <https://www.namecheap.com>
