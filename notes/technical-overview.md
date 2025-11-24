---
slug: github-discord-bot-note-technical-overview
id: github-discord-bot-note-technical-overview
title: discord-bot
repo: justin-napolitano/discord-bot
githubUrl: https://github.com/justin-napolitano/discord-bot
generatedAt: '2025-11-24T18:35:02.365Z'
source: github-auto
summary: >-
  This repository contains a Python-based Discord bot that uses slash commands
  for interaction. It connects to an external assistant API for text analysis
  and supports quick development with guild-specific command registration.
tags: []
seoPrimaryKeyword: ''
seoSecondaryKeywords: []
seoOptimized: false
topicFamily: null
topicFamilyConfidence: null
kind: note
entryLayout: note
showInProjects: false
showInNotes: true
showInWriting: false
showInLogs: false
---

This repository contains a Python-based Discord bot that uses slash commands for interaction. It connects to an external assistant API for text analysis and supports quick development with guild-specific command registration.

## Key Components

- Built with Python 3 and the `discord.py` library.
- Uses `httpx` for async HTTP requests.
- Packaged for deployment using Docker and Docker Compose.

## Quick Start

1. Clone the repo:

   ```bash
   git clone https://github.com/justin-napolitano/discord-bot.git
   cd discord-bot
   ```

2. Create a `.env` file from `env-example.txt` and set your Discord bot token and application ID.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. To run locally, execute:

   ```bash
   python bot.py
   ```

   Or for Docker:

   ```bash
   docker-compose up --build
   ```

### Gotchas

Make sure to set the environment variables correctly. If using Docker, ensure the `assistant-core` service is running to avoid connection issues.
