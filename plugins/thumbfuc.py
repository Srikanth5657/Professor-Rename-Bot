from pyrogram import Client, filters
from helper.database import db

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumb(client, message):    
    thumb = await db.get_thumbnail(message.from_user.id)
    if thumb:
       await client.send_photo(
	   chat_id=message.chat.id, 
	   photo=thumb)
    else:
        await message.reply_text("😔**Sorry ! No thumbnail found...**😔") 
		
@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client, message):
    await db.set_thumbnail(message.from_user.id, file_id=None)
    await message.reply_text("❌️ __**Tʜᴜᴍʙɴᴀɪʟ Dᴇʟᴇᴛᴇᴅ**__")
	
@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    SnowDev = await message.reply_text("Please Wait ...")
    await db.set_thumbnail(message.from_user.id, file_id=message.photo.file_id)                
    await SnowDev.edit("✅️ __**Tʜᴜᴍʙɴᴀɪʟ Sᴀᴠᴇᴅ**__")
	
