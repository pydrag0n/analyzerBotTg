import asyncio
import json
from message_printer import MessagePrinter
from pyrogram import Client, filters
import time
import random
from config import API_ID, API_HASH, PHONE_NUMBER, PHONE_CODE


async def write_file(data_list: list, filename: str="datas"):
    with open('{filename}.json','w', encoding='utf-8') as f:
        json.dump(data_list, f, ensure_ascii=False, indent=4)


mp = MessagePrinter()
app = Client("my_account", 
             api_id=API_ID,
             api_hash=API_HASH,
             phone_code=PHONE_CODE,
             phone_number=PHONE_NUMBER)


# @app.on_message(filters.command("start"))
async def main():
    data = {}
    data_list=[]
    LIMIT = 100
    async with app:
        try:
            await app.send_message('pydrag0n',
                                f"Получен /start от пользователя 'pydrag0n")

            chat = await app.get_chat("naebnet")
            chat_id = chat.id
            
            mp.info_message("START")

            async for posts in app.get_chat_history(chat_id, limit=LIMIT):
                
                data["views"] = posts.views
                data["date"] = str(posts.date)
                
                data_list.append(data)
                data = {}
                
            time.sleep(random.randint(2, 5))
            await write_file(data_list)
            
            mp.info_message("END")
            
            
        except Exception as e:
            mp.error_message(e)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())