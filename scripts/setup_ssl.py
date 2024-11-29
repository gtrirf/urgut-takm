import os

def install_certbot():
    os.system("sudo apt install certbot python3-certbot-nginx -y")
    print("Certbot o'rnatildi.")

def obtain_ssl_certificate(domain):
    os.system(f"sudo certbot --nginx -d {domain} --non-interactive --agree-tos -m your_email@example.com")  # o'zgartiring
    print(f"{domain} uchun SSL sertifikati muvaffaqiyatli olindi.")

if __name__ == "__main__":
    domain = "yourdomain.com"  # o'zgartiring
    install_certbot()
    obtain_ssl_certificate(domain)
