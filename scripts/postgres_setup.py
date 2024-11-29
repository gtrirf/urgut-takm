import subprocess
import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def install_postgresql():
    try:
        print("PostgreSQL o'rnatilmoqda...")
        subprocess.run(["sudo", "apt", "update"], check=True)
        subprocess.run(["sudo", "apt", "install", "postgresql", "postgresql-contrib", "-y"], check=True)
        print("PostgreSQL muvaffaqiyatli o'rnatildi.")
    except subprocess.CalledProcessError as e:
        print(f"O'rnatishda xato: {e}")


def create_user_and_grant_privileges(db_name, username, password):
    try:
        connection = psycopg2.connect(dbname='postgres', user='postgres')
        connection.autocommit = True
        cursor = connection.cursor()

        cursor.execute(f"CREATE USER {username} WITH PASSWORD '{password}';")
        print(f"Foydalanuvchi '{username}' muvaffaqiyatli yaratildi.")

        cursor.execute(f"CREATE DATABASE {db_name};")
        print(f"Ma'lumotlar bazasi '{db_name}' muvaffaqiyatli yaratildi.")

        cursor.execute(f"GRANT ALL PRIVILEGES ON DATABASE {db_name} TO {username};")
        print(f"Foydalanuvchiga '{db_name}' ma'lumotlar bazasida barcha ruxsatlar berildi.")

    except Exception as e:
        print(f"Xato: {e}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


if __name__ == "__main__":
    install_postgresql()

    db_name = os.getenv('DB_NAME')
    username = os.getenv('USERNAME')
    password = os.getenv('PASSW0RD')

    create_user_and_grant_privileges(db_name, username, password)
