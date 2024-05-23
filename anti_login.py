from telethon import TelegramClient , events
import config

client = TelegramClient(session='TG_anti_login',api_id=config.API_ID,api_hash=config.API_HASH)

import logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
LOGGER = logging.getLogger(__name__)



@client.on(events.NewMessage(chats=777000))
async def handlers(event):

    await client.forward_messages('me',event.message)


client.start()
client.run_until_disconnected()