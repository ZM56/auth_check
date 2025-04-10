#!/usr/bin/python3

import requests
import sys
from requests.exceptions import RequestException
import warnings

# Подавляем предупреждения InsecureRequestWarning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore', InsecureRequestWarning)

ELK_URL = "https://mysite.example.com"
USERNAME = "admin"
PASSWORD = "password"

def check_authorization():
    """Проверка авторизации."""
    try:
        response = requests.get(
            ELK_URL,
            auth=(USERNAME, PASSWORD),
            verify=False,
            timeout=10,
            allow_redirects=True
        )
        return 1 if response.status_code == 200 else 0
    except RequestException as e:
        print(f"Ошибка при проверке авторизации: {e}", file=sys.stderr)
        return 0
    except Exception as e:
        print(f"Неожиданная ошибка: {e}", file=sys.stderr)
        return 0

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] != "auth":
        print("Usage: auth", file=sys.stderr)
    else:
        result = check_authorization()
        print(result)  # Выводим 1 или 0 в stdout
        sys.exit(0 if result == 1 else 1)
