"""main entry point """

import asyncio
import logging
import logging.handlers
import os
from ctypes.util import find_library
from io import BytesIO

import discord.opus
import discord.utils
import dotenv
from discord import (Client, VoiceClient, PCMAudio,
                     Message, Member, VoiceState, Intents)

from jtalkbot import __version__
from jtalkbot.openjtalk import FREQ_48000HZ, OpenJTalkAgent


# configure logging
logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(
    'jtalkbot.log', maxBytes=1*1024*1024, backupCount=5, encoding='utf-8')
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}',
                              '%Y-%m-%d %H:%M:%S', style='{')
handler.setFormatter(formatter)
logger.addHandler(handler)
discord.utils.setup_logging(handler=handler, formatter=formatter,
                            level=logging.INFO, root=False)

# load .env file and environment variables
dotenv.load_dotenv()
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
OPEN_JTALK_FLAGS = os.environ.get('OPEN_JTALK_FLAGS', '')


# create instances
intents = Intents.default()
intents.message_content = True

client = Client(intents=intents)

open_jtalk_agent = OpenJTalkAgent.from_flags(OPEN_JTALK_FLAGS)
open_jtalk_agent.sampling = FREQ_48000HZ

voice_clients: dict[int, VoiceClient] = {}


@client.event
async def on_message(message: Message) -> None:
    """Called when a Message is created and sent. """

    if voice_client := voice_clients.get(message.channel.id):
        text = f'{message.author.display_name}「{message.content}」'
        data = open_jtalk_agent.talk(text)
        stream = BytesIO(data)
        voice_client.play(PCMAudio(stream), after=lambda e: stream.close())


@client.event
async def on_voice_state_update(member: Member,
                                before: VoiceState,
                                after: VoiceState) -> None:
    """Called when a Member changes their VoiceState. """

    if member == client.user:
        return

    if (not before.channel) and (channel := after.channel):
        # someone attended the voice channel
        if not (voice_client := voice_clients.get(channel.id)):
            voice_client = voice_clients[channel.id] = await channel.connect()
            await asyncio.sleep(3.0)
            text = f'{member.display_name}さんこんにちは。'
            data = await open_jtalk_agent.async_talk(text)
            stream = BytesIO(data)
            voice_client.play(PCMAudio(stream), after=lambda e: stream.close())


    if (not after.channel) and (channel := before.channel):
        # someone left the voice channel
        if channel.members == [client.user]:
            if voice_client := voice_clients.get(channel.id):
                await voice_client.disconnect()
                del voice_clients[channel.id]


def main():
    logger.info(f'jtalkbot {__version__}')

    # load Opus library for voice to work
    if filename := find_library('opus'):
        discord.opus.load_opus(filename)
        if discord.opus.is_loaded():
            logger.info(f'successfully loaded opus library: {filename}')
        else:
            logger.error(f'failed to load opus library: {filename}')
    else:
        logger.error('not found opus library')

    client.run(DISCORD_TOKEN, log_handler=None)


if __name__ == '__main__':
    main()
