import os
from dotenv import load_dotenv
load_dotenv()

def create_nginx_config(domain):
    config = f"""
server {{
    listen 80;
    server_name {domain};

    location = /favicon.ico {{ access_log off; log_not_found off; }}
    location /static/ {{
        root /path/to/your/project;  
    }}

    location / {{
        include proxy_params;
        proxy_pass unix:/path/to/your/project/gunicorn.sock;  
    }}

    error_log /var/log/nginx/{domain}_error.log;
    access_log /var/log/nginx/{domain}_access.log;
}}

server {{
    listen 443 ssl;
    server_name {domain};

    ssl_certificate /etc/letsencrypt/live/{domain}/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/{domain}/privkey.pem;

    location = /favicon.ico {{ access_log off; log_not_found off; }}
    location /static/ {{
        root /path/to/your/project;  
    }}

    location / {{
        include proxy_params;
        proxy_pass unix:/path/to/your/project/gunicorn.sock;
    }}

    error_log /var/log/nginx/{domain}_error.log;
    access_log /var/log/nginx/{domain}_access.log;
}}
"""
    return config


def write_nginx_config(domain):
    nginx_config = create_nginx_config(domain)
    config_file_path = f"/etc/nginx/sites-available/{domain}"

    with open(config_file_path, 'w') as f:
        f.write(nginx_config)

    os.symlink(config_file_path, f"/etc/nginx/sites-enabled/{domain}")
    print(f"Nginx konfiguratsiyasi {domain} uchun yozildi.")


if __name__ == "__main__":
    domain = os.getenv('DOMAIN')
    write_nginx_config(domain)

    os.system("sudo systemctl restart nginx")
