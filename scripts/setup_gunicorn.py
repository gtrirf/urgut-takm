def create_gunicorn_service(domain):
    service_content = f"""
[Unit]
Description=gunicorn daemon for {domain}
After=network.target

[Service]
User=your_user  # o'zgartiring
Group=www-data
WorkingDirectory=/path/to/your/project  # o'zgartiring
ExecStart=/path/to/your/venv/bin/gunicorn --access-logfile - --workers 3 --bind unix:/path/to/your/project/gunicorn.sock your_project.wsgi:application  # o'zgartiring

[Install]
WantedBy=multi-user.target
"""
    return service_content


def write_gunicorn_service(domain):
    service_content = create_gunicorn_service(domain)
    service_file_path = f"/etc/systemd/system/gunicorn_{domain}.service"

    with open(service_file_path, 'w') as f:
        f.write(service_content)

    os.system(f"sudo systemctl start gunicorn_{domain}")
    os.system(f"sudo systemctl enable gunicorn_{domain}")
    print(f"Gunicorn servisi {domain} uchun yozildi va ishga tushirildi.")


if __name__ == "__main__":
    domain = "yourdomain.com"  # o'zgartiring
    write_gunicorn_service(domain)
