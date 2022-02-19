import csv

def get_clean_messages():
	'''
	@return List of every single message

	Removes newlines from message blocks.
	When using a newline in whatsapp, it adds a newline in the txt.
	Each newline should be interpreted as a single messsage.
	'''
	with open('WhatsAppChat.txt', 'r', encoding='utf-8') as f:
		data = f.readlines()

	cleaned_data = []
	prev = []

	for line in data:
		try:
			is_date = False
			int(line[0])
			if line[1] == '/' or line[2] == '/':
				is_date = True
			if not is_date:
				raise Exception
			
			if prev != []:
				cleaned_data.append(' '.join(prev))
				prev = []
				prev.append(line)
			else:
				prev.append(line)

		except Exception as e:
			prev.append(line)
		
	cleaned_data.append(' '.join(prev))
	return cleaned_data

def extract_message_content(message):
	'''
	@param message str: mm/tt/yy, hh:mm - author: message

	@return author str: message author
	@return message_date str: mm/tt/yy
	@return message_time str: hh:mm
	@return clean_message str: message with removed "\\n" and removed ","

	Extracts metadata from message.
	'''
	message_date = message.split(', ')[0]

	# extract author
	start = message.find('- ') + len('- ')
	end = message.find(': ')
	author = message[start:end]

	# extract time
	start = message.find(', ') + len(', ')
	end = message.find(' - ')
	message_time = message[start:end]

	clean_message = ' '.join(message.split(': ')[1:]).replace('\n', ' ').replace(',', ' ')
	return author, message_date, message_time, clean_message


def write_csv(messages):
	'''
	@param messages list: List of messages: mm/tt/yy, hh:mm - author: message

	Calls extract_message_content for each message.
	Writes a new entry, for each message, into a csv table.
	'''

	bad_sentences = ['Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more.', '<Media omitted>']
	with open('WhatsAppChat.csv', 'w', encoding='utf-8') as chat_f:
		writer = csv.writer(chat_f)
		# writer.writerow(['author', 'date', 'message'])
		for message in messages:
			
			is_bad = False
			for bad_sentence in bad_sentences:
				if bad_sentence in message:
					is_bad = True
			if is_bad:
				continue

			author, date, time, clean_message = extract_message_content(message)
			writer.writerow([author, date, time , clean_message])


if __name__ == '__main__':
	messages = get_clean_messages()
	write_csv(messages)