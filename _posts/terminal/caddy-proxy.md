---
title: Reverse Proxy and Basic Auth with Caddy
date: October 26, 2025
tags: terminal
---

Below is a Caddyfile with a reverse proxy from HTTP port 80 to the local host port 5000. This will direct HTTP traffic to the service or app running on port 5000 on the server. Basic authentication is enabled where the username is `bart` and the hashed password is `12$3asDfjl45$97845ashLKdjFg`. Use tabs, not spaces, for indentation in the Caddyfile.

```json
:80 {
    basic_auth {
        bart 12$3asDfjl45$97845ashLKdjFg
    }
    reverse_proxy localhost:5000
}
```

The Caddy command show below was used to hash the password. This example creates a password hash for the password `password123`.

```bash
caddy hash-password -p password123
```

In the same directory as the Caddyfile, use the commands given below to start or stop the Caddy server:

```bash
# Start the caddy server
sudo caddy start

# Stop the caddy server
sudo caddy stop
```

More information about Caddy is available at <https://caddyserver.com>.
