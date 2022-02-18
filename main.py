import csv
import emoji as emoji_lib
import matplotlib.pyplot as plt
import numpy as np

def extract_emojis(s):
  return [c for c in s if c in emoji_lib.UNICODE_EMOJI['en']]

def get_stats():
	with open('chat.csv', 'r', encoding='utf-8') as file:
		chars = 'abcdefghijklmnopqr'
		lines = [line for line in csv.reader(file) if line != []]
		stats = {}
		for line in lines:
			author, date, message = line[0], line[1], line[2]
			emojis = extract_emojis(message)
			emoji_set = set(emojis)
			if not date in stats:
				stats[date] = {}
			for emoji in emojis:
				if emoji in stats[date]:
					stats[date][emoji] += 1
				else:
					stats[date][emoji] = 1
		return stats

def get_counts(emoji, stats, labels):
	result = []
	for label in labels:
		if emoji in stats[label]:
			count = stats[label][emoji]
			result.append(count)
		else:
			result.append(0)
	return result

def make_emoji_chart(stats, emojis):


	fig, ax = plt.subplots()
	labels = [date for date in stats.keys()]
	x = np.arange(len(labels))
	for emoji in emojis:
		ax.set_label(emoji)	
		counts = get_counts(emoji, stats, labels)
		ax.plot(labels, counts, label=emoji_lib.demojize(emoji))

		
	ax.set_ylabel('Number')
	ax.set_xticks(x, labels)
	ax.legend()
	fig.tight_layout()
	ax.set_title('Total number of emojis send in whatsapp chat')
	plt.show()

emojis = ['💩', '🔪', '🤣', '👍', '🥰', '🙌', '😂']
stats = get_stats()
make_emoji_chart(stats, emojis)