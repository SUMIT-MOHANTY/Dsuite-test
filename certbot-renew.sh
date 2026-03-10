#!/usr/bin/env bash
set -e

# This script would be used with real domains for Let's Encrypt
# For localhost/development, we'll use self-signed certs

DOMAIN=${DOMAIN:-localhost}
EMAIL=${CERT_EMAIL:-admin@example.com}

# Only run if we have a real domain (not localhost)
if [[ "$DOMAIN" != "localhost" ]] && [[ "$DOMAIN" != "127.0.0.1" ]]; then
    certbot certonly \
        --webroot \
        --webroot-path=/var/www/certbot \
        -d "$DOMAIN" \
        --email "$EMAIL" \
        --agree-tos \
        --non-interactive
    
    # Reload nginx
    nginx -s reload
else
    echo "Skipping certbot for localhost - using self-signed certificate"
fi
