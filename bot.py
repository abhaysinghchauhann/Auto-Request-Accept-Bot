import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, User, ChatJoinRequest

pr0fess0r_99=Client(
    "𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗣𝗹𝗲𝗮𝘀𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗢𝗽𝘂𝘀𝗧𝗲𝗰𝗵𝘇",
    bot_token = os.environ["BOT_TOKEN"],
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"]
)

CHAT_ID=int(os.environ.get("CHAT_ID", None))
TEXT=os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYour Auto Approved")
APPROVED = os.environ.get("APPROVED_WELCOME", "on").lower()

@pr0fess0r_99.on_message(filters.private & filters.command(["start"]))
async def start(client: pr0fess0r_99, message: Message):
    approvedbot = await client.get_me() 
    await message.reply_text(text="𝙷𝙴𝙻𝙻𝙾...⚡\n\n𝙸𝙰𝙼 𝙰 𝚂𝙸𝙼𝙿𝙻𝙴 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙰𝚄𝚃𝙾 𝚁𝙴𝚀𝚄𝙴𝚂𝚃 𝙰𝙲𝙲𝙴𝙿𝚃 𝙱𝙾𝚃.\n𝙵𝙾𝚁 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝚃𝚂 𝙲𝚁𝙴𝙰𝚃𝙴 𝙾𝙽𝙴 𝙱𝙾𝚃... \n𝚅𝙸𝙳𝙴𝙾 𝙾𝙽 𝙼𝚈 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻", disable_web_page_preview=True)

@pr0fess0r_99.on_chat_join_request(filters.chat(CHAT_ID))
async def autoapprove(client: pr0fess0r_99, message: ChatJoinRequest):
    chat=message.chat # Chat
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    if APPROVED == "on":
        await client.send_message(chat_id=chat.id, text=TEXT.format(mention=user.mention, title=chat.title))     

from telegram.ext import Updater, CommandHandler, MessageHandler, ChatMemberHandler
from telegram import Bot, ChatMember
import logging

logging.basicConfig(level=logging.INFO)

TOKEN = '8124145168:AAEOxp7K-E5QjWPVpHisCAyMNeuhccBbYQc'
CHAT_ID = '-1002503228855'
ATTACHMENT_BOT_USERNAME = 'Auto_Accept_Trader_777bot'

bot = Bot(TOKEN)

def start(update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    bot.send_message(chat_id=chat_id, text='Welcome! Please join our channel.')
    context.bot.send_message(chat_id=user_id, text='You have joined the channel successfully!')

def new_member(update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    bot.send_message(chat_id=chat_id, text=f'Welcome @{update.effective_user.username}!')
    bot.send_message(chat_id=user_id, text='You have joined the channel successfully!')

def accept_member_requests(update, context):
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    chat_member = bot.get_chat_member(chat_id=chat_id, user_id=user_id)
    if chat_member.status == 'member':
        return
    bot.send_message(chat_id=chat_id, text=f'@{update.effective_user.username} has requested to join.')
    bot.send_message(chat_id=user_id, text='Your request to join has been accepted!')
    bot.promote_chat_member(chat_id=chat_id, user_id=user_id, can_join_invites=True)

def auto_request_attachment_bot(update, context):
    chat_id = update.effective_chat.id
    bot.send_message(chat_id=chat_id, text=f'/start @{ATTACHMENT_BOT_USERNAME}')

def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(ChatMemberHandler(new_member, ChatMemberHandler.NEW_CHAT_MEMBERS))
    dispatcher.add_handler(ChatMemberHandler(accept_member_requests, ChatMemberHandler.CHAT_MEMBER_REQUEST))
    dispatcher.add_handler(CommandHandler('request_attachment_bot', auto_request_attachment_bot))
    updater.start_polling()
    updater.idle()

if name == 'main':
    main()

print("𝗕𝗼𝘁 𝗦𝘁𝗮𝗿𝘁𝗲𝗱 𝗣𝗹𝗲𝗮𝘀𝗲 𝗦𝘂𝗯𝘀𝗰𝗿𝗶𝗯𝗲 𝗢𝗽𝘂𝘀𝗧𝗲𝗰𝗵𝘇")
pr0fess0r_99.run()
