import os
import asyncio
import httpx
import discord
from discord import app_commands
from discord.ext import commands

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
APP_ID = int(os.getenv("DISCORD_APP_ID", "0"))
ASSISTANT_API_BASE = os.getenv("ASSISTANT_API_BASE", "http://assistant-core:8088").rstrip("/")
DEV_GUILD_IDS = [int(x) for x in os.getenv("DEV_GUILD_IDS", "").split(",") if x]

intents = discord.Intents.default()
intents.message_content = False  # using slash commands only


class AssistantClient:
    def __init__(self, base: str):
        self.base = base
        self.client = httpx.AsyncClient(timeout=None)

    async def analyze(self, user_id: int, text: str) -> str:
        r = await self.client.post(
            f"{self.base}/assistant/analyze",
            json={"user_id": str(user_id), "text": text},
        )
        r.raise_for_status()
        data = r.json()
        return data.get("result", "(no result)")

    async def aclose(self):
        await self.client.aclose()


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("!"),
            intents=intents,
            application_id=APP_ID,
        )
        self.assistant = AssistantClient(ASSISTANT_API_BASE)

    async def setup_hook(self):
        # Fast dev loop: register slash commands directly in dev guilds
        if DEV_GUILD_IDS:
            for gid in DEV_GUILD_IDS:
                self.tree.copy_global_to(guild=discord.Object(id=gid))
                await self.tree.sync(guild=discord.Object(id=gid))
        # Also sync globally (may take time to appear)
        await self.tree.sync()

    async def close(self):
        await self.assistant.aclose()
        await super().close()


bot = Bot()


@bot.tree.command(name="ping", description="Health check")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong 🏓", ephemeral=True)


@bot.tree.command(name="ask", description="Ask the assistant (routes to your LangChain agent)")
@app_commands.describe(text="Your question or request")
async def ask(interaction: discord.Interaction, text: str):
    await interaction.response.defer(thinking=True)
    try:
        result = await bot.assistant.analyze(interaction.user.id, text)
        # Discord message hard limit is 2000 chars. Chunk to be safe.
        chunks = [result[i:i + 1900] for i in range(0, len(result), 1900)] or ["(empty)"]
        for i, ch in enumerate(chunks):
            prefix = f"Part {i + 1}/{len(chunks)}\n" if len(chunks) > 1 else ""
            await interaction.followup.send(prefix + ch)
    except Exception as e:
        await interaction.followup.send(f"Error: {e}")


if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("DISCORD_BOT_TOKEN missing")
    asyncio.run(bot.start(TOKEN))

