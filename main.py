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


def make_bar_chart(emoji, stats, length):
	pass

def make_charts(stats):

	emojis = ['💩', '🔪', '🤣', '👍', '🥰', '🙌', '😂', '❤️']
	fig, axis = plt.subplots(len(emojis)//2, 2, sharex=True)
	axs = np.concatenate(axis)

	for index, emoji in enumerate(emojis):

		labels = [date for date in stats.keys()]

		x = np.arange(len(labels))  # the label locations


		axs[index].set_label(emoji)	
		counts = get_counts(emoji, stats, labels)
		rects = axs[index].bar(labels, counts)
		axs[index].bar_label(rects, padding=3)
			
		axs[index].set_ylabel('Number')
		axs[index].set_title(emoji_lib.demojize(emoji))
		axs[index].set_xticks(x, labels)
		fig.tight_layout()

	plt.show()

	#for emoji in emojis:
	#	make_bar_chart(emoji, stats, len(emojis))

stats = get_stats()
# print(stats['2/17/22']['💩'])
make_charts(stats)