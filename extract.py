from asyncore import write
import csv

def get_sentences():
	with open('WhatsAppChat.txt', 'r', encoding='utf-8') as f:
		data = f.readlines()

	cleaned_data = []
	prev = []

	for line in data:
		try:
			isDate = False
			int(line[0])
			if line[1] == '/' or line[2] == '/':
				isDate = True
			if not isDate:
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

def write_csv(cleaned_data):
	bad_sentences = ['Messages and calls are end-to-end encrypted. No one outside of this chat, not even WhatsApp, can read or listen to them. Tap to learn more.', '<Media omitted>']
	with open('chat.csv', 'w', encoding='utf-8') as chat_f:
		writer = csv.writer(chat_f)
		# writer.writerow(['author', 'date', 'message'])
		for line in cleaned_data:
			
			isBad = False
			for bad_sentence in bad_sentences:
				if bad_sentence in line:
					isBad = True
			if isBad:
				continue

			m_date = line.split(', ')[0]

			start = line.find('- ') + len('- ')
			end = line.find(': ')
			author = line[start:end]

			start = line.find(', ') + len(', ')
			end = line.find(' - ')
			time = line[start:end]

			clean_line = ' '.join(line.split(': ')[1:]).replace('\n', ' ').replace(',', ' ')
			writer.writerow([author, m_date, time , clean_line])


cleaned_data = get_sentences()
write_csv(cleaned_data)