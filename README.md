# Tool to extract metadata from whatsapp chats

- extract.py # create csv table
- main.py # creates diagrams, only emoji based for now
# Getting started

## requirements
 - WhatsAppChat.txt # txt file from WhatsAppChats
	- WhatsApp -> click on chat -> 3 dots -> more -> export chat
	- Place WhatsAppChat.txt file in root folder

## create csv table from whatsapp txt file
```
python3 extract.py
```

## create diagram

### install dependencies
```
pip install -r requirements.txt
```
edit threshold parameter to change most used emojis
```
python3 main.py
```