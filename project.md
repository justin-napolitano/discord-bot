---
slug: github-discord-bot
id: github-discord-bot
title: Python Discord Bot with Docker Integration
repo: justin-napolitano/discord-bot
githubUrl: https://github.com/justin-napolitano/discord-bot
generatedAt: '2025-11-24T21:34:33.348Z'
source: github-auto
summary: >-
  A guide to building a Discord bot in Python with Docker support, featuring
  slash commands and external API integration.
tags:
  - discord.py
  - docker
  - python
  - httpx
  - api integration
  - bot development
seoPrimaryKeyword: discord bot python docker
seoSecondaryKeywords:
  - discord bot setup
  - python bot commands
  - docker compose discord
  - async http requests
  - guild-specific commands
seoOptimized: true
topicFamily: null
topicFamilyConfidence: null
kind: project
entryLayout: project
showInProjects: true
showInNotes: false
showInWriting: false
showInLogs: false
---

A Discord bot implemented in Python that integrates with an external assistant API to provide interactive slash commands. Designed for deployment with Docker and supports rapid development via guild-specific command registration.

## Features

- Slash command-based interaction (no message content reading).
- Integration with an external assistant API for text analysis.
- Health check command (`/ping`).
- Development-friendly command syncing scoped to specified guilds.
- Containerized deployment with Docker and Docker Compose.

## Tech Stack

- Python 3
- discord.py library
- httpx for asynchronous HTTP requests
- Docker & Docker Compose

## Getting Started

### Prerequisites

- Python 3.8+ (if running locally)
- Docker and Docker Compose (for containerized deployment)
- Discord Bot Token and Application ID

### Installation

1. Clone the repository:

```bash
git clone https://github.com/justin-napolitano/discord-bot.git
cd discord-bot
```

2. Create a `.env` file based on `env-example.txt` and set the following environment variables:

```
DISCORD_BOT_TOKEN=your_discord_bot_token
DISCORD_APP_ID=your_discord_application_id
DEV_GUILD_IDS=comma_separated_dev_guild_ids (optional)
ASSISTANT_API_BASE=http://assistant-core:8088
```

### Running Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the bot:

```bash
python bot.py
```

### Running with Docker Compose

Build and start the containers:

```bash
docker-compose up --build
```

This will start the `discord-bot` service and link it with the `assistant-core` service on the `assistant-net` network.

## Project Structure

```
discord-bot/
├── bot.py               # Main bot implementation
├── Dockerfile           # Docker image definition for the bot
├── docker-compose.yml   # Docker Compose configuration
├── env-example.txt      # Example environment variables file
└── requirements.txt     # Python dependencies
```

- `bot.py` contains the bot logic, including command registration and interaction with the assistant API.
- `Dockerfile` and `docker-compose.yml` enable containerized deployment.
- `env-example.txt` provides a template for required environment variables.

## Future Work / Roadmap

- Expand command set beyond `/ping` and `/ask`.
- Implement message content command support if needed.
- Add logging and error handling improvements.
- Support dynamic configuration for assistant API base URL.
- Add automated tests and CI/CD integration.
- Improve documentation and usage examples.

---

For questions or contributions, please open an issue or submit a pull request.

---

_This README is generated based on current repository state and may be updated as the project evolves._
