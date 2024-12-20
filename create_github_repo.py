import os
import requests
import json

def create_github_repository(repo_name="food-compatibility-app", description="食材相性診断＆レシピ提案アプリ"):
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        return {"error": "GitHub token not found"}

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github.v3+json"
    }

    data = {
        "name": repo_name,
        "description": description,
        "private": False,
        "auto_init": False
    }

    response = requests.post(
        "https://api.github.com/user/repos",
        headers=headers,
        data=json.dumps(data)
    )

    if response.status_code == 201:
        return response.json()
    else:
        return {"error": f"Failed to create repository: {response.text}"}

if __name__ == "__main__":
    result = create_github_repository()
    print(json.dumps(result, indent=2))
