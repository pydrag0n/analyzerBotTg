
import asyncio
import json
from message_printer import MessagePrinter
from pyrogram import Client, filters
import time
import random
from config import API_ID, API_HASH, PHONE_NUMBER, PHONE_CODE

    
mp = MessagePrinter()
app = Client("my_account", api_id=API_ID,
             api_hash=API_HASH,
             phone_code=PHONE_CODE, phone_number=PHONE_NUMBER)

@app.on_message(filters.command("start"))
async def start_handler(client, message):
    try:
        await app.send_message(message.from_user.id,f"Получен /start от пользователя {message.from_user.id}")
        data = {}
        chat = await app.get_chat("naebnet")
        chat_id = chat.id
        mp.info_message("START")
        data_list=[]
        async for posts in app.get_chat_history(chat_id, limit=1000):
            data["views"] = posts.views
            data["date"] = str(posts.date)
            
            data_list.append(data)
            data = {}
        time.sleep(random.randint(2, 6))
        with open('datas.json','w', encoding='utf-8') as f:
            json.dump(data_list, f, ensure_ascii=False, indent=4)
        
        mp.info_message("END")
        
        
    except Exception as e:
        mp.error_message(e)

app.run()