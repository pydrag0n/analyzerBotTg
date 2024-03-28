import asyncio
import json
from message_printer import MessagePrinter
from pyrogram import Client
import time
from config import API_ID, API_HASH, PHONE_NUMBER, PHONE_CODE

class TelegramDataProcessor:
    def __init__(self, username="pydrag0n"):
        self.data_list = []
        self.LIMIT = 100
        self.username = username
        self.data = {}
        self.mp = MessagePrinter()
        self.app = Client("my_account", 
                          api_id=API_ID,
                          api_hash=API_HASH,
                          phone_code=PHONE_CODE,
                          phone_number=PHONE_NUMBER)

    async def write_file(self, filename: str = "datas"):
        with open(f'{filename}.json', 'w', encoding='utf-8') as f:
            json.dump(self.data_list, f, ensure_ascii=False, indent=4)

    async def process_data(self):
        async with self.app:
            try:
                await self.app.send_message(self.username, f"Получен /start от пользователя pydragon")

                chat = await self.app.get_chat("naebnet")  # Не очень понятно, что это за чат
                chat_id = chat.id

                self.mp.info_message("START")
                col = 1

                async for post in self.app.get_chat_history(chat_id, limit=self.LIMIT):
                    col += 1
                    self.data["views"] = post.views
                    self.data["date"] = str(post.date)
                    
                    self.data_list.append(self.data.copy())
                    if col % 100 == 0:
                        await asyncio.sleep(1)
                await self.write_file()

                self.mp.info_message("END")

            except Exception as e:
                self.mp.error_message(e)

def main():
    processor = TelegramDataProcessor()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(processor.process_data())

if __name__ == "__main__":
    main()