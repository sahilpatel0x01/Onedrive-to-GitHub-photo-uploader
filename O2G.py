import os
import requests
import json
import base64
from github import Github
from msal import ConfidentialClientApplication

# OneDrive API details
CLIENT_ID = 'your_client_id'
CLIENT_SECRET = 'your_client_secret'
TENANT_ID = 'your_tenant_id'
SCOPES = ['https://graph.microsoft.com/.default']
AUTHORITY = f'https://login.microsoftonline.com/{TENANT_ID}'
REDIRECT_URI = 'http://localhost'  # Adjust if needed

# GitHub API details
GITHUB_TOKEN = 'your_github_token'
GITHUB_USERNAME = 'your_github_username'
REPO_NAME = 'your_repo_name'

# OneDrive Functions
def get_onedrive_token():
    app = ConfidentialClientApplication(CLIENT_ID, authority=AUTHORITY, client_credential=CLIENT_SECRET)
    result = app.acquire_token_for_client(SCOPES)
    if 'access_token' in result:
        return result['access_token']
    else:
        raise Exception("Failed to get OneDrive token")

def download_photos_from_onedrive(folder_path):
    access_token = get_onedrive_token()
    url = f'https://graph.microsoft.com/v1.0/me/drive/root:/{folder_path}:/children'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        files = response.json()['value']
        downloaded_files = []
        for file in files:
            if file['file']['mimeType'].startswith('image/'):
                download_url = file['@microsoft.graph.downloadUrl']
                file_name = file['name']
                file_content = requests.get(download_url).content
                with open(file_name, 'wb') as f:
                    f.write(file_content)
                downloaded_files.append(file_name)
        return downloaded_files
    else:
        raise Exception(f"Error downloading files from OneDrive: {response.text}")

# GitHub Functions
def create_github_repo(repo_name):
    g = Github(GITHUB_TOKEN)
    user = g.get_user()
    repo = user.create_repo(repo_name)
    return repo

def upload_to_github(repo, file_path):
    with open(file_path, "rb") as file:
        content = file.read()
    encoded_content = base64.b64encode(content).decode("utf-8")
    repo.create_file(file_path, f"Add {file_path}", encoded_content)

# Main Workflow
def main():
    # Step 1: Download Photos from OneDrive
    folder_path = 'Photos'  # Replace with your OneDrive folder
    photos = download_photos_from_onedrive(folder_path)

    # Step 2: Create GitHub Repository
    g = Github(GITHUB_TOKEN)
    user = g.get_user()
    repo = user.create_repo(REPO_NAME)
    
    # Step 3: Upload Photos to GitHub
    for photo in photos:
        upload_to_github(repo, photo)

if __name__ == "__main__":
    main()
