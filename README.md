# Custom Programmable Search Engine with Python

This repository contains a Python script to automate searches using the Google Custom Search API, along with instructions on setting up the Custom Search Engine and generating API keys.

## Overview

This project aims to create a custom search engine using Google's Programmable Search Engine (PSE) service and automate searches through a Python script. The custom search engine is configured to search only within a specific pool of URLs, reducing noise and providing more relevant results.

## Setup Instructions

### 1. Create a Programmable Search Engine (PSE)

- Visit [Google Programmable Search Engine](https://programmablesearchengine.google.com/).
- Follow the instructions provided in the repository's README to create a new search engine and configure it with the desired URLs.
- Note down the Search Engine ID.

### 2. Generate an API Key

- Go to the [Google Cloud Console](https://console.cloud.google.com/).
- Enable the Custom Search API for your project.
- Create an API Key.
- Copy the generated API Key.

### 3. Set Up Python Environment

- Ensure Python is installed on your system.
- Install the required libraries using pip:
  ```bash
  pip install google-api-python-client
