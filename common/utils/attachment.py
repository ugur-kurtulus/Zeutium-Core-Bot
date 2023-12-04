import aiohttp
import io
from PIL import Image
import os
import interactions


class Attachment:
    
    async def save(self, attachment: interactions.Attachment):
        async with aiohttp.ClientSession() as session:
            async with session.get(attachment.url) as response:
                image_data = Image.open(io.BytesIO(await response.read()))
                image_data.save(f"./attachments/{attachment.filename}")
                
    async def get(self, attachment_name: str):
        return interactions.File(f"./attachments/{attachment_name}")
                
    async def delete(self, attachment: interactions.File):
        os.remove(f"./attachments/{attachment.file_name}")