import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()

# Получаем данные из окружения
username = os.getenv("GITHUB_USERNAME")
token = os.getenv("GITHUB_TOKEN")
repo_name = os.getenv("REPO_NAME")
org_name = os.getenv("ORG_NAME")

headers = {
    "Authorization": f"Bearer {token}",
    "Accept": "application/vnd.github.v3+json"
}

def print_pretty(data):
    # Используем json.dumps() для отформатированного вывода
    print(json.dumps(data, indent=4))


# Функция для получения репозиториев организации
def get_org_repos():
    url = f"https://api.github.com/orgs/{org_name}/repos"
    response = requests.get(url, headers=headers)
    print_pretty(response.json()) 

# Функция для получения репозиториев пользователя
def get_user_repos():
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url, headers=headers)
    print_pretty(response.json()) 

# Функция для создания репозитория
def create_repo():
    url = "https://api.github.com/user/repos"
    data = {"name": repo_name, "private": False}
    response = requests.post(url, json=data, headers=headers)
    print_pretty(response.json()) 

# Функция для удаления репозитория
def delete_repo():
    url = f"https://api.github.com/repos/{username}/{repo_name}"
    response = requests.delete(url, headers=headers)
    print(response.status_code)

if __name__ == "__main__":
    action = input("Choose action (get_org_repos, get_user_repos, create_repo, delete_repo): ")
    if action == "get_org_repos":
        get_org_repos()
    elif action == "get_user_repos":
        get_user_repos()
    elif action == "create_repo":
        create_repo()
    elif action == "delete_repo":
        delete_repo()
    else:
        print("Unknown action")
