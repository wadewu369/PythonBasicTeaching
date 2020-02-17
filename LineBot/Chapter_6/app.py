from flask import Flask, request, abort
import json
from datetime import datetime

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
#
# Channel Access Token
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')
# Channel Secret
handler = WebhookHandler('YOUR_CHANNEL_SECRET')
user_id = 'user_id'



# ======================================================================================================

# @app.route("/TextSendMessage/<string:push_text_str>")
# def text_send_message(push_text_str):
#     line_bot_api.push_message(user_id, TextSendMessage(text=push_text_str))
#     return 'TextSendMessage: %s' % push_text_str

# @app.route("/TextSendMessage/")
# def text_send_message():
#     send_message_str = 'hi 你好'
#     line_bot_api.push_message(user_id, TextSendMessage(text=send_message_str))
#     return 'TextSendMessage: %s' % send_message_str
# ======================================================================================================

# @app.route("/ImageSendMessage/")
# def image_send_message():
#     image_message = ImageSendMessage(
#         original_content_url='https://shareboxnow.com/wp-content/uploads/2020/02/th.jpeg',
#         preview_image_url='https://shareboxnow.com/wp-content/uploads/2020/02/th.jpeg'
#     )
#     line_bot_api.push_message(user_id, image_message)
#     return 'ImageSendMessage Done!'


# def get_image_url_path():
#     image_url = 'https://shareboxnow.com/wp-content/uploads/2020/02/th.jpeg'
#     return image_url
#
# @app.route("/ImageSendMessage/")
# def image_send_message():
#     get_image_url = get_image_url_path()
#     image_message = ImageSendMessage(
#         original_content_url=get_image_url,
#         preview_image_url=get_image_url
#     )
#     line_bot_api.push_message(user_id, image_message)
#     return 'ImageSendMessage Done!'
# ======================================================================================================
# @app.route("/VideoSendMessage/")
# def video_send_message():
#     video_message = VideoSendMessage(
#         original_content_url='https://shareboxnow.com/wp-content/uploads/2020/02/IMG_0469.mp4',
#         preview_image_url='https://shareboxnow.com/wp-content/uploads/2020/02/th.jpeg'
#     )
#     line_bot_api.push_message(user_id, video_message)
#     return 'VideoSendMessage Done!'

# def get_video_and_preview_image_url():
#     video_url = 'https://shareboxnow.com/wp-content/uploads/2020/02/IMG_0469.mp4'
#     preview_image_url = 'https://shareboxnow.com/wp-content/uploads/2020/02/th.jpeg'
#     return video_url, preview_image_url
#
#
# @app.route("/VideoSendMessage/")
# def video_send_message():
#     video_url, preview_image_url = get_video_and_preview_image_url()
#     video_message = VideoSendMessage(
#         original_content_url=video_url,
#         preview_image_url=preview_image_url
#     )
#     line_bot_api.push_message(user_id, video_message)
#     return 'VideoSendMessage Done!'
# ======================================================================================================

# @app.route("/AudioSendMessage/")
# def audio_send_message():
#     audio = AudioSendMessage(
#         original_content_url='https://shareboxnow.com/wp-content/uploads/2020/02/test.m4a',
#         duration=2400
#     )
#     line_bot_api.push_message(user_id, audio)
#     return 'AudioSendMessage Done!'

# def get_audio_url_duration():
#     get_audio = {
#         'original_content_url': 'https://shareboxnow.com/wp-content/uploads/2020/02/test.m4a',
#         'duration': 2400
#     }
#     return get_audio
#
#
# @app.route("/AudioSendMessage/")
# def audio_send_message():
#     get_audio_dict = get_audio_url_duration()
#     audio = AudioSendMessage(get_audio_dict['original_content_url'], get_audio_dict['duration'])
#     line_bot_api.push_message(user_id, audio)
#     return 'AudioSendMessage Done!'

# ======================================================================================================

# @app.route("/LocationSendMessage/")
# def location_send_message():
#     location = LocationSendMessage(
#         title = '我未來要爬的山！',
#         address = '雪山山脈',
#         latitude = 24.533723,
#         longitude = 121.396090
#     )
#     line_bot_api.push_message(user_id, location)
#     return 'LocationSendMessage Done!'

# def get_location_dict():
#     get_location = {
#         'title': '我未來要爬的山！',
#         'address': '雪山山脈',
#         'latitude': 24.533723,
#         'longitude': 121.396090
#     }
#     return get_location
#
# @app.route("/LocationSendMessage/")
# def location_send_message():
#     get_location_data = get_location_dict()
#     location = LocationSendMessage(
#         get_location_data['title'],
#         get_location_data['address'],
#         get_location_data['latitude'],
#         get_location_data['longitude']
#     )
#     line_bot_api.push_message(user_id, location)
#     return 'LocationSendMessage Done!'

# ======================================================================================================


# @app.route("/StickerSendMessage/")
# def location_send_message():
#     sticker_message = StickerSendMessage(
#         package_id = '1',
#         sticker_id = '1'
#     )
#     line_bot_api.push_message(user_id, sticker_message)
#     return 'StickerSendMessage Done!'

# def get_sticker_dict():
#     sticker_message = {
#         'package_id': '1',
#         'sticker_id': '1'
#     }
#     return sticker_message
#
#
# @app.route("/StickerSendMessage/")
# def location_send_message():
#     get_sticker_data = get_sticker_dict()
#     sticker_message = StickerSendMessage(
#         get_sticker_data['package_id'],
#         get_sticker_data['sticker_id']
#     )
#     line_bot_api.push_message(user_id, sticker_message)
#     return 'StickerSendMessage Done!'

# ======================================================================================================

@app.route("/ButtonsTemplate/")
def ButtonsTemplate_send_message():
    buttons_template_message = TemplateSendMessage(
        alt_text = '我是按鈕範本',
        template = ButtonsTemplate(
            thumbnail_image_url = 'https://shareboxnow.com/wp-content/uploads/2020/02/th.jpeg',
            title = 'M&M Share',
            text = '請選擇你要的項目：',
            actions = [
                PostbackAction(
                    label = 'postback',
                    display_text = 'postback text',
                    data = 'action=buy&itemid=1'
                ),
                MessageAction(
                    label = '現在幾點了？',
                    text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                ),
                URIAction(
                    label = '我的部落格',
                    uri = 'https://shareboxnow.com/'
                )
            ]
        )
    )
    line_bot_api.push_message(user_id, buttons_template_message)
    return 'ButtonsTemplate_send_message Done!'




import os

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host = '0.0.0.0', port = port, debug = True)
