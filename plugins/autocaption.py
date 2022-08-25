import pyrogram, os, asyncio

try: custom_caption = os.environ.get("custom_caption", "`{file_name}`")
except Exception as custom_caption: print(f"⚠️ Custom Caption Invalid {custom_caption}")

@Client.on_message(pyrogram.filters.channel)
def edit_caption(bot, update: pyrogram.types.Message):
  movie, _ = get_file_details(update)
  try:
      try: update.edit(custom_caption.format(file_name=movie.file_name))
      except pyrogram.errors.FloodWait as FloodWait:
          asyncio.sleep(FloodWait.value)
          update.edit(custom_caption.format(file_name=movie.file_name))
  except pyrogram.errors.MessageNotModified: pass 
    
def get_file_details(update: pyrogram.types.Message):
  if update.media:
    for message_type in (
        "photo",
        "animation",
        "audio",
        "document",
        "video",
        "video_note",
        "voice",
        # "contact",
        # "dice",
        # "poll",
        # "location",
        # "venue",
        "sticker"
    ):
        obj = getattr(update, message_type)
        if obj:
            return obj, obj.file_id
