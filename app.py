import os
import sys
import graphviz 

from flask import Flask, jsonify, request, abort, send_file,send_from_directory
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage,PostbackEvent

from fsm import TocMachine
from utils import send_text_message

load_dotenv()

machine_dict = {}

app = Flask(__name__, static_url_path="")

channel_secret = os.environ.get("LINE_CHANNEL_SECRET")
channel_access_token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")

if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)

@app.route("/callback", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)

    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        enter = False
        enter_postback = False
        if event.source.user_id not in machine_dict:
            machine_dict[event.source.user_id] = TocMachine(
                states = [
                    "user", 
                    "menu",
                    "category_menu",
                    "show_fsm_pic",
                    "search_category",
                    "show_record",
                    "add_record",
                    "delete_record",
                    "choose_word_or_speak",
                    "show_to_user",
                    "choose_chi_or_tai",
                    "read_to_user",
                    "introduction",
                    ],
                transitions=[
                    {"trigger": "advance" , "source": "user" , "dest": "menu" , "conditions": "is_going_to_menu",},
                    {"trigger": "advance" , "source": "menu" , "dest": "menu" , "conditions": "is_going_to_menu",},
                    {"trigger": "advance" , "source": "show_record" , "dest": "menu" , "conditions": "is_going_to_menu",},
                    {"trigger": "advance" , "source": "show_to_user" , "dest": "menu" , "conditions": "is_going_to_menu",},
                    {"trigger": "advance" , "source": "read_to_user" , "dest": "menu" , "conditions": "is_going_to_menu",},
                    {"trigger": "advance" , "source": "introduction" , "dest": "menu" , "conditions": "is_going_to_menu",},
                    {"trigger": "advance" , "source": "add_record" , "dest": "menu" , "conditions": "is_going_to_menu",},
                    {"trigger": "advance" , "source": "delete_record" , "dest": "menu" , "conditions": "is_going_to_menu",},

                    {"trigger": "advance" , "source": "menu" , "dest": "show_fsm_pic" , "conditions": "is_going_to_show_fsm_pic",},
                    {"trigger": "advance" , "source": "menu" , "dest": "introduction" , "conditions": "is_going_to_introduction",},
                    {"trigger": "advance" , "source": "menu" , "dest": "show_record" , "conditions": "is_going_to_show_record",},

                    # 選擇文章類別
                    # 繼續
                    {"trigger": "advance" , "source": "menu" , "dest": "category_menu" , "conditions": "is_going_to_category_menu",},
                    # 回到上一步
                    {"trigger": "advance" , "source": "category_menu" , "dest": "menu" , "conditions": "is_going_to_back_menu",},
                    
                    # 搜尋選擇該類別的文章
                    # 繼續
                    {"trigger": "advance" , "source": "category_menu" , "dest": "search_category" , "conditions": "is_going_to_search_category",},
                    # 回到上一步
                    {"trigger": "advance" , "source": "search_category" , "dest": "category_menu" , "conditions": "is_going_to_back_category_menu",},
                    
                    # 選擇文字或語音
                    # 繼續
                    {"trigger": "advance" , "source": "search_category" , "dest": "choose_word_or_speak" , "conditions": "is_going_to_choose_word_or_speak",},
                    # 回到上一步
                    {"trigger": "advance" , "source": "choose_word_or_speak" , "dest": "search_category" , "conditions": "is_going_to_back_search_category",},
                    
                    # 文檔
                    # 繼續
                    {"trigger": "advance" , "source": "choose_word_or_speak" , "dest": "show_to_user" , "conditions": "is_going_to_show_to_user",},
                    # 回到上一步
                    {"trigger": "advance" , "source": "show_to_user" , "dest": "choose_word_or_speak" , "conditions": "is_going_to_back_choose_word_or_speak",},

                    # 選擇中文或台語
                    # 繼續
                    {"trigger": "advance" , "source": "choose_word_or_speak" , "dest": "choose_chi_or_tai" , "conditions": "is_going_to_choose_chi_or_tai",},
                    # 回到上一步
                    {"trigger": "advance" , "source": "choose_chi_or_tai" , "dest": "choose_word_or_speak" , "conditions": "is_going_to_back_choose_word_or_speak",},

                    #唸出來
                    {"trigger": "advance" , "source": "choose_chi_or_tai" , "dest": "read_to_user" , "conditions": "is_going_to_read_to_user",},
                    
                    # 新增紀錄
                    {"trigger": "advance_postback" , "source": "show_to_user" , "dest": "add_record" , "conditions": "is_going_to_add_record",},

                    # 查看最愛
                    {"trigger": "advance" , "source": ["user" , "menu"] , "dest" : "show_record" , "conditions": "is_going_to_show_record",},
                    # 刪除紀錄
                    {"trigger": "advance_postback" , "source": "show_record" , "dest": "delete_record" , "conditions": "is_going_to_delete_record",},
                    # add delete後回去
                    {"trigger": "go_back", "source": "add_record", "dest": "show_to_user"},
                    {"trigger": "go_back", "source": "delete_record", "dest": "show_record"},
                    {"trigger": "go_back", "source": "read_to_user", "dest": "menu"},
                ],
                initial="user",
                auto_transitions=False,
                show_conditions=True,
            )

        if isinstance(event, MessageEvent):
            if isinstance(event.message, TextMessage) and isinstance(event.message.text, str):
                response = machine_dict[event.source.user_id].advance(event)
                enter = response
        elif isinstance(event, PostbackEvent):
            if isinstance(event.postback.data, str):
                response = machine_dict[event.source.user_id].advance_postback(event)
                enter_postback = response
        print(f"\nFSM STATE: {machine_dict[event.source.user_id].state}")
        print(f"REQUEST BODY: \n{body}")
        if enter == False:
            if enter_postback == False:
                send_text_message(event.reply_token, "請依照指示與按鈕來操作!")

    return "OK"


import io
import pydub
# /<category>/<filename>
@app.route('/output/<language>/<category>/<title>', methods=['GET'])
def return_audio(language , category , title):
    # sound = pydub.AudioSegment.from_wav("./audios/output.wav")
    # sound.export("./audios/output.mp3", format="mp3")
    # path_to_file ="output.aac"
    # file_name = filename + ".wav"
    print(language)
    print(category)
    print(title)
    return send_file(f'{language}/{category}/{title}.wav',mimetype='audio/wav')
    # return send_file(f'audios/output.wav',mimetype='audio/wav')

if __name__ == "__main__":
    port = os.environ.get("PORT", 8000)
    app.run(host="0.0.0.0", port=port, debug=True)
