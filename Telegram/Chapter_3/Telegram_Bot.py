from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import logging
import time

updater = Updater(token='YOUR_TOKEN', use_context=False)

# 印出log的方法
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

# 有Debug 以及 Info 模式，因為我不需要印太多資訊只需要Info就好
# logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)


def getUrl(bot, update):

    reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton('Mark 粉絲專頁', url = 'https://github.com/mzshieh/pa19spring'),
        InlineKeyboardButton('Mark 部落格教學文章', url = 'https://python-telegram-bot.readthedocs.io/en/stable/index.html'),
        InlineKeyboardButton('Google 首頁', url = 'https://www.google.com.tw/')]])

    bot.send_message(update.message.chat.id, '網站連結', reply_to_message_id = update.message.message_id,
                     reply_markup = reply_markup)
    logging.info('[getUrl][chat id]: %s' % update.message.chat.id)
    logging.info('[getUrl][reply_to_message_id]: %s' % update.message.message_id)
    logging.info('[getUrl][reply_markup]: %s' % reply_markup)


def clickButton(bot, update):
    reply_markup = InlineKeyboardMarkup([[
        InlineKeyboardButton('吃飽了', callback_data='eat'),
        InlineKeyboardButton('還沒吃飽', callback_data='notEat'),
        InlineKeyboardButton('還在想要吃什麼？', callback_data='think')]])

    bot.send_message(update.message.chat.id, '你吃飽了嗎？', reply_to_message_id = update.message.message_id,
                     reply_markup = reply_markup)
    logging.info('[clickButton][reply_markup]: %s' % reply_markup)
    logging.info('[clickButton][chat id]: %s' % update.message.chat.id)
    logging.info('[clickButton][reply_to_message_id]: %s' % update.message.message_id)


def getClickButtonData(bot, update):
    if update.callback_query.data == 'eat':
        update.callback_query.edit_message_text('真好我都還沒吃')
    if update.callback_query.data == 'notEat':
        update.callback_query.edit_message_text('還不去吃？')
    if update.callback_query.data == 'think':
        update.callback_query.edit_message_text('你慢慢想吧！我先去吃嚕！')
    logging.info('[getClickButtonData][callback_query data]: %s' % update.callback_query.data)


# 套用 testReply()，當你對你的機器人說'/url'，就會執行這串
updater.dispatcher.add_handler(CommandHandler('url', getUrl))
updater.dispatcher.add_handler(CommandHandler('today', clickButton))
updater.dispatcher.add_handler(CallbackQueryHandler(getClickButtonData))

# 這串是執行機器人算是一個運行server?很類似 我是這樣覺得
updater.start_polling()
updater.idle()
