# OneDrive to GitHub Photo Uploader

A Python script that automates downloading photos from OneDrive and uploading them to a GitHub repository. This tool uses the Microsoft Graph API to access your OneDrive account, downloads photos from a specified folder, and then uploads them to a new GitHub repository using the GitHub API.

This project serves as an exploration into automation and API usage for cloud-to-cloud transfers. It’s designed to help users easily back up photos, while showcasing how to use both OneDrive and GitHub APIs together in Python. 

## Features
- **OneDrive Photo Download**: Downloads all photos from a specified folder in OneDrive.
- **Automatic GitHub Repository Creation**: Creates a new repository on GitHub.
- **Photo Upload to GitHub**: Uploads all downloaded photos to the created GitHub repository.
- **File Size Management**: Automatically handles individual photo files, ensuring each file is within the GitHub free file size limit of 100 MB.

> **Note:** GitHub allows a maximum file size of 100 MB for free repositories. Since the average size of photos is between 8-10 MB, this tool is ideal for uploading photos without hitting the limit.

## Prerequisites
Before using this script, ensure you have the following:
1. **Python 3.x** installed on your system.
2. **Pip** package manager to install the required libraries.
3. A **Microsoft OneDrive account** with photos to download.
4. A **GitHub account** and a **GitHub personal access token** for creating repositories.

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone https://github.com/your-username/onedrive-to-github-photo-uploader.git
