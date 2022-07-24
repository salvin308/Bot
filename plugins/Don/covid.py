import os
import requests
from requests.utils import requote_uri
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API = "https://api.sumanjay.cf/covid/?country="

BUTTONS = InlineKeyboardMarkup([[InlineKeyboardButton("CLOSE", callback_data='close_data')]])

@Client.on_message(filters.command("covid"))
async def reply_info(client, message):
    query = message.text.split(None, 1)[1]
    await message.reply_photo(
        photo="https://telegra.ph/file/96857d5ddf6643647a3d1.jpg https://telegra.ph/file/c501b49a11a89df538dd3.jpg https://telegra.ph/file/6a308c718c3e3dd3d4120.jpg https://telegra.ph/file/6780f1e2706d1f9b78e5b.jpg https://telegra.ph/file/1e796ee8b7d4269ae1fbc.jpg https://telegra.ph/file/4b1bba9fa8c9ef2c5247a.jpg https://telegra.ph/file/8731ae4f058aafa01f6af.jpg https://telegra.ph/file/f3362123e598d0589b9a5.jpg https://telegra.ph/file/cb4a5ba0db89608e59c8e.jpg",
        caption=covid_info(query),
        quote=True
    )


def covid_info(country_name):
    try:
        r = requests.get(API + requote_uri(country_name.lower()))
        info = r.json()
        country = info['country'].capitalize()
        active = info['active']
        confirmed = info['confirmed']
        deaths = info['deaths']
        info_id = info['id']
        last_update = info['last_update']
        latitude = info['latitude']
        longitude = info['longitude']
        recovered = info['recovered']
        covid_info = f"""--**𝙲𝙾𝚅𝙸𝙳 𝟷𝟿 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽**--
᚛› Country : `{country}`
᚛› Actived : `{active}`
᚛› Confirmed : `{confirmed}`
᚛› Deaths : `{deaths}`
᚛› ID : `{info_id}`
᚛› Last Update : `{last_update}`
᚛› Latitude : `{latitude}`
᚛› Longitude : `{longitude}`
᚛› Recovered : `{recovered}`"""
        return covid_info
    except Exception as error:
        return error
