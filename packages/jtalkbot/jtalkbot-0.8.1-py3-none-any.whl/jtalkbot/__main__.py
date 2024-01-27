"""main entry point """

# standard modules
import asyncio
import logging
import logging.handlers
import os
from ctypes.util import find_library
from io import BytesIO
from typing import Any

# discord.py
from discord import (
    # clients
    Client,
    # voice related
    VoiceClient, PCMAudio,
    # Discord models
    Message, Member, VoiceState, VoiceChannel,
    # data classes
    Intents,
)
import discord.opus
import discord.utils

# other third-party libraries
import dotenv

# jtalkbot local libraries
from jtalkbot import __version__
from jtalkbot.openjtalk import FREQ_48000HZ, OpenJTalkAgent


# load .env file and environment variables
dotenv.load_dotenv()
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
OPEN_JTALK_FLAGS = os.environ.get('OPEN_JTALK_FLAGS', '')


# configure logging
LOG_FORMAT = '{asctime} {levelname} {name} {message}'
LOG_DATEFMT = '%Y-%m-%dT%H:%M:%S%z'
LOG_STYLE = '{'
logging.basicConfig(format=LOG_FORMAT, datefmt=LOG_DATEFMT, style=LOG_STYLE)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(
    'jtalkbot.log', maxBytes=1*1024*1024, backupCount=5, encoding='utf-8')
formatter = logging.Formatter(LOG_FORMAT, LOG_DATEFMT, LOG_STYLE)
handler.setFormatter(formatter)
logger.addHandler(handler)
discord.utils.setup_logging(handler=handler, formatter=formatter,
                            level=logging.INFO, root=False)


# create instances
intents = Intents.default()
intents.message_content = True
client = Client(intents=intents)

open_jtalk_agent = OpenJTalkAgent.from_flags(OPEN_JTALK_FLAGS)
open_jtalk_agent.sampling = FREQ_48000HZ


# utility functions
def debug(msg: Any, *args: Any, **kwds: Any) -> None:
    logger.debug(msg, *args, **kwds)


def info(msg: Any, *args: Any, **kwds: Any) -> None:
    logger.info(msg, *args, **kwds)


def warning(msg: Any, *args: Any, **kwds: Any) -> None:
    logger.warning(msg, *args, **kwds)


def error(msg: Any, *args: Any, **kwds: Any) -> None:
    logger.error(msg, *args, **kwds)


def critical(msg: Any, *args: Any, **kwds: Any) -> None:
    logger.critical(msg, *args, **kwds)


def find_voice_client(channel: VoiceChannel, /) -> VoiceClient | None:
    voice_client = discord.utils.find(lambda vcl: vcl.channel == channel,
                                      client.voice_clients)
    return voice_client if isinstance(voice_client, VoiceClient) else None



# event handlers
@client.event
async def on_message(message: Message) -> None:
    """Called when a Message is created and sent. """

    if (isinstance(message.channel, VoiceChannel)
        and (voice_client := find_voice_client(message.channel))):

        info(f'Reading out message ({len(message.content)} chars).')
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
        # client itself

        if (before.channel is None
            and isinstance(channel := after.channel, VoiceChannel)):
            # attended the voice channel
            info('Attended the voice channel.')

            if channel.members == [client.user]:
                info('Client is only member in voice channell.')
                if voice_client := find_voice_client(channel):
                    await voice_client.disconnect()

        elif (after.channel is None
              and isinstance(channel := before.channel, VoiceChannel)):
            # left the voice channel
            pass

    else:
        # other memeber

        if (before.channel is None
            and isinstance(channel := after.channel, VoiceChannel)):
            # attended the voice channel
            info('Detect someone attended voice channel.')

            if not (voice_client := find_voice_client(channel)):
                voice_client = await channel.connect()

            await asyncio.sleep(3.0)
            text = f'{member.display_name}さんこんにちは。'
            data = await open_jtalk_agent.async_talk(text)
            stream = BytesIO(data)
            voice_client.play(PCMAudio(stream), after=lambda e: stream.close())

        elif (after.channel is None
              and isinstance(channel := before.channel, VoiceChannel)):
            # left the voice channel
            info('Detect someone left voice channel.')

            if channel.members == [client.user]:
                info('Client is only member in the voice channell.')
                if voice_client := find_voice_client(channel):
                    await voice_client.disconnect()


@client.event
async def on_resumed() -> None:
    """Called when the client has resumed a session. """

    # re-connect the voice channels that have connected members
    info('Re-connect active voice channels...')
    for guild in client.guilds:
        for channel in guild.voice_channels:
            if channel.members:
                await channel.connect()


# main
def main() -> None:
    """main entry point. """

    info(f'jtalkbot {__version__}')

    # load Opus library for voice to work
    if filename := find_library('opus'):
        discord.opus.load_opus(filename)
        if discord.opus.is_loaded():
            info(f'Successfully loaded opus library: {filename}')
        else:
            error(f'Failed to load opus library: {filename}')
    else:
        error('Not found Opus library.')

    client.run(DISCORD_TOKEN, log_handler=None)


if __name__ == '__main__':
    main()
