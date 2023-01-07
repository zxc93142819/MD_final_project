import copy
from playsound import playsound
from transitions.extensions import GraphMachine

import os
import sys
import pdfplumber
import socket
import struct
import chinese_tts as ct
import taiwanese_tts as tt

from pydub import AudioSegment
from pydub.playback import play
from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import *

from utils import send_text_message

load_dotenv()

channel_secret = os.environ.get("LINE_CHANNEL_SECRET")
channel_access_token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pyimgur
import message_template
from urllib.parse import quote

download_web = {}
search_article_title = {}
search_article_num = {}
choose_article_index = {}
search_category_num = 3
search_category_name = ["內科" , "外科" , "其他"]
search_category_web = ["http://hedu.mmh.org.tw/km/1471" , "http://hedu.mmh.org.tw/km/1472" , "http://hedu.mmh.org.tw/km/1473"]
each_category_num = [12 , 10 , 4]
choose_category_index = {}
record_article_title = {}
record_article_item = {}
record_article_num = {}
type = ""
HOST, PORT = "192.168.1.112", 8000

def get_category_article(user_id):
    choose_category_id = choose_category_index[user_id]
    response = requests.get(search_category_web[choose_category_id])
    soup = BeautifulSoup(response.content , "html.parser")
    card_num = each_category_num[choose_category_id]
    cards = soup.find_all('li' , {"class": "xtree-node type-media clearfix"} , limit=card_num)
    spe_article_title = []
    spe_download_web = []
    count = 0
    for card in cards :
        title = card.find('div' , {"class" : "node-title"}).getText()
        if title.find("英文版") != -1:
            continue
        file_web = "http://hedu.mmh.org.tw" + card.find('a' , {"class" : "xtree-node-label"}).get("href") 
        another_response = requests.get(file_web)
        another_soup = BeautifulSoup(another_response.content , "html.parser")
        another_card = another_soup.find('div' , {"class": "fs-p text-center"})
        another_download_web = "http://hedu.mmh.org.tw" + another_card.find('a' , {"class": "btn btn-default"}).get("href")
        spe_download_web.append(another_download_web)
        spe_article_title.append(title)
        count += 1
    search_article_num.update( {user_id : count} )
    search_article_title.update( {user_id : spe_article_title} )
    download_web.update( {user_id : spe_download_web} )
    return


def tts(str , type) :
    adjust = str
    if type == "中文" :
        ct.send_data(adjust)
    else :
        tt.send_data(adjust)

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)

    def is_going_to_menu(self, event):
        text = event.message.text
        return text == "主選單"

    def is_going_to_show_fsm_pic(self, event):
        text = event.message.text
        return text == "fsm"

    def is_going_to_introduction(self, event):
        text = event.message.text
        return text == "功能介紹與使用說明"

    # back----------------------------------------------------
    def is_going_to_back_menu(self , event):
        text = event.message.text
        return text == "返回主選單重新選擇功能"

    def is_going_to_back_category_menu(self , event):
        text = event.message.text
        return text == "返回重新選擇衛教類別"

    def is_going_to_back_search_category(self , event):
        text = event.message.text
        return text == "返回重新選擇我要的文章"

    def is_going_to_back_choose_word_or_speak(self , event):
        text = event.message.text
        return text == "返回重新選擇我要的文章表現方式"
    # ---------------------------------------------------------
    # ---------------------------------------------------------
    def is_going_to_category_menu(self , event):
        text = event.message.text
        return text == "選擇衛教文章類別"

    def is_going_to_search_category(self , event):
        text = event.message.text
        has_that_category = False
        for i in range(search_category_num) :
            if search_category_name[i] == text:
                choose_category_index.update( {event.source.user_id : i} )
                has_that_category = True
                break
        return has_that_category

    def is_going_to_choose_word_or_speak(self , event):
        text = event.message.text
        has_that_article = False
        for i in range(search_article_num[event.source.user_id]) :
            if search_article_title[event.source.user_id][i] == text:
                choose_article_index.update( {event.source.user_id : i} )
                has_that_article = True
                break
        return has_that_article

    def is_going_to_show_to_user(self , event):
        text = event.message.text
        return text == "文章檔案"

    def is_going_to_choose_chi_or_tai(self , event):
        text = event.message.text
        return text == "語音合成講給我聽"
    
    def is_going_to_read_to_user(self , event):
        text = event.message.text
        global type
        type = text
        return text == "台語" or text == "中文"


    def on_enter_category_menu(self , event):
        reply_token = event.reply_token
        message = message_template.category_menu
        message_to_reply = FlexSendMessage("choose category", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_search_category(self , event):
        reply_token = event.reply_token
        get_category_article(event.source.user_id)  #衛教爬蟲
        message = copy.deepcopy(message_template.article_list)
        num = search_article_num[event.source.user_id]
        for i in range (num):
            make_message = copy.deepcopy(message_template.article_template)
            make_message["action"]["label"] = search_article_title[event.source.user_id][i]
            make_message["action"]["text"] = search_article_title[event.source.user_id][i]
            message["body"]["contents"].append(make_message)
        message["body"]["contents"].append(message_template.separator)
        message_to_reply = FlexSendMessage("查詢結果", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_choose_word_or_speak(self , event):
        reply_token = event.reply_token
        message = message_template.word_or_speak
        message_to_reply = FlexSendMessage("文字或語音", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_show_to_user(self , event):
        # 給檔案
        reply_token = event.reply_token
        make_message = copy.deepcopy(message_template.word_demo)
        choose_article_id = choose_article_index[event.source.user_id]
        make_message["body"]["contents"][1]["action"]["label"] = search_article_title[event.source.user_id][choose_article_id]
        make_message["body"]["contents"][1]["action"]["uri"] = download_web[event.source.user_id][choose_article_id]
        make_message["footer"]["contents"][2]["action"]["data"] = "加入," + search_article_title[event.source.user_id][choose_article_id] + "," + download_web[event.source.user_id][choose_article_id]
        message_to_reply = FlexSendMessage("文字", make_message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)
    
    def on_enter_choose_chi_or_tai(self , event):
        reply_token = event.reply_token
        message = message_template.choose_chinese_or_taiwanese
        message_to_reply = FlexSendMessage("選擇語言", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_read_to_user(self , event):
        reply_token = event.reply_token
        user_id = event.source.user_id
        choose_article_id = choose_article_index[user_id]

        article_web = download_web[user_id][choose_article_id]
        article = requests.get(article_web)
        with open("temp.pdf" , 'wb') as f:
            f.write(article.content)
        this_pdf = pdfplumber.open("temp.pdf")
        page = this_pdf.pages[0]
        text = page.extract_text()
        this_pdf.close
        # split content
        begin = text.find("審閱")
        another_begin = text.find("修訂")
        if begin == -1:
            begin = another_begin
        begin = begin + 2
        end = text.find("若有問題請隨時提出")
        # 例外處理
        another_end = text.find("有任何問題")
        if end == -1:
            end = another_end
        # 直到中文為止
        while '\u4e00' >= text[begin] or text[begin] >= '\u9fa5':
            begin += 1
        # 直到。為止
        while text[end] != '\u3002':
            end -= 1
        text = text[begin : end + 1]
        # tts(text , type)
        language = type
        category = search_category_name[choose_category_index[user_id]]
        title = search_article_title[user_id][choose_article_id]
        print(language)
        print(category)
        print(title)
        mainUrl = "https://md-linebot.onrender.com/output/" + language + "/" + category + "/" + title
        message = AudioSendMessage(original_content_url = mainUrl , duration = 330 * len(text))
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message)
        # self.go_back()
        return 'OK'
            

    # 加入紀錄-----------------------------------------------------------------------
    def is_going_to_add_record(self , event):
        text = event.postback.data
        add_or_delete = text.split(',')[0]
        return add_or_delete == '加入'

    def on_enter_add_record(self, event):
        reply_token = event.reply_token
        user_id = event.source.user_id
        # 檔案的title
        title = event.postback.data.split(',')[1]
        # 檔案的adress
        address = event.postback.data.split(',')[2]
        has_data = False
        num = 0
        article_title = []
        article_item = []
        msg = ""
        if record_article_title.__contains__(user_id):
            article_title = record_article_title[user_id]
            article_item = record_article_item[user_id]
            num = record_article_num[user_id]

        for temp_title in article_title :
            if temp_title == title :
                msg = '已在我的紀錄!'
                has_data = True
                break
        if has_data == False :
            if num < 10:
                article_title.append(title)
                article_item.append(address)
                num += 1
                msg = '成功加入我的紀錄'
            else:
                msg = '我的紀錄已滿(最多10個)'
        record_article_title.update( {user_id : article_title} )
        record_article_item.update( {user_id : article_item} )
        record_article_num.update( {user_id : num} )
        
        message = message_template.add_reply
        message["body"]["contents"][0]["text"] = msg
        message_to_reply = FlexSendMessage("加入最愛", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)
        
    # ----------------------------------------------------------------------------------------------------
    
    # 查詢紀錄-----------------------------------------------------------------------
    def is_going_to_show_record(self , event):
        text = event.message.text
        return text == "查看我的瀏覽紀錄"

    def on_enter_show_record(self, event):
        reply_token = event.reply_token
        user_id = event.source.user_id
        num = 0
        article_title = []
        article_item = []
        if record_article_item.__contains__(user_id):
            article_title = record_article_title[user_id]
            article_item = record_article_item[user_id]
            num = record_article_num[user_id]

        if num != 0:
            message = copy.deepcopy(message_template.restaurant_list)
            print("現在有" + str(num) + "個")
            # message["contents"].clear()
            for i in range (num) :
                make_message = copy.deepcopy(message_template.show_restaurant_item)
                make_message["body"]["contents"][0]["action"]["label"] = article_title[i]
                make_message["body"]["contents"][0]["action"]["uri"] = article_item[i]
                make_message["footer"]["contents"][0]["action"]["data"] = "移除," + article_title[i] + "," + article_item[i]
                message["contents"].append(make_message)
            del message["contents"] [0]
            # message["contents"].append(message_template.separator)
            message_to_reply = FlexSendMessage("紀錄", message)
            line_bot_api = LineBotApi( channel_access_token )
            line_bot_api.reply_message(reply_token, message_to_reply)
        else:
            message_to_reply = FlexSendMessage("紀錄", message_template.no_result)
            line_bot_api = LineBotApi( channel_access_token )
            line_bot_api.reply_message(reply_token, message_to_reply)
    # ----------------------------------------------------------------------------------------------------

    # 刪除最愛-----------------------------------------------------------------------
    def is_going_to_delete_record(self , event):
        text = event.postback.data
        add_or_delete = text.split(',')[0]
        return add_or_delete == '移除'

    def on_enter_delete_record(self, event):
        reply_token = event.reply_token
        user_id = event.source.user_id
        # 檔案的title
        title = event.postback.data.split(',')[1]
        # 檔案的adress
        address = event.postback.data.split(',')[2]
        has_data = False
        num = 0
        article_title = []
        article_item = []
        msg = ""
        if record_article_title.__contains__(user_id):
            article_title = record_article_title[user_id]
            article_item = record_article_item[user_id]
            num = record_article_num[user_id]

        for temp_title in article_title :
            if temp_title == title:
                has_data = True
                break
        if has_data == False :
            msg = '紀錄中無此資料'
        else :
            article_title.remove(title)
            article_item.remove(address)
            num -= 1
            msg = '成功從我的紀錄移除'
        
        record_article_title.update( {user_id : article_title} )
        record_article_item.update( {user_id : article_item} )
        record_article_num.update( {user_id : num} )

        message = message_template.add_reply
        message["body"]["contents"][0]["text"] = msg
        message_to_reply = FlexSendMessage("加入最愛", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)
    # ----------------------------------------------------------------------------------------------------
    

    def on_enter_introduction(self, event):
        reply_token = event.reply_token
        message = message_template.introduction_message
        message_to_reply = FlexSendMessage("功能介紹與使用說明", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_menu(self, event):
        reply_token = event.reply_token
        message = message_template.main_menu
        message_to_reply = FlexSendMessage("開啟主選單", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)

    def on_enter_show_fsm_pic(self, event):
        reply_token = event.reply_token
        message = message_template.show_pic
        message_to_reply = FlexSendMessage("查看fsm結構圖", message)
        line_bot_api = LineBotApi( channel_access_token )
        line_bot_api.reply_message(reply_token, message_to_reply)
