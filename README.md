# Tool to extract metadata from whatsapp chats
Creates csv table from WhatsAppChat.txt file.

# Getting started

## requirements
 - WhatsAppChat.txt # txt file from WhatsAppChats
	- WhatsApp -> click on chat -> 3 dots -> more -> export chat
	- Place WhatsAppChat.txt file in root folder

## install dependencies
```
pip install -r requirements.txt
```

## create csv table from whatsapp txt file
```
python3 extract.py
```

## create diagram
edit threshold parameter to change most used emojis
```
python3 main.py
```