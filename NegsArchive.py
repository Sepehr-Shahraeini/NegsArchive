
from telethon import TelegramClient, events
api_id = 14498488
api_hash = '7273c3ef3d48b1a2aa47a1ecaf39eb4b'
client = TelegramClient('sepehr', api_id, api_hash)
client.start()
print("client started")
@client.on(events.NewMessage(chats='MyGreenSilence'))

async def my_event_handler(event):
    await client.forward_messages('https://t.me/+bGV4ikMTLjswZTc8', event.message)

with client:
    client.run_until_disconnected()