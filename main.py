import csv
import emoji as emoji_lib
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.font_manager as fm
import os


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

def make_bar_chart(emoji, stats):
	labels = [date for date in stats.keys()]

	x = np.arange(len(labels))  # the label locations

	fig, ax = plt.subplots()
	ax.set_label(emoji)	
	for label in labels:
		if emoji in stats[label]:
			count = stats[label][emoji]
			rect = ax.bar(label, count)
		else:
			count = 0
			rect = ax.bar(label, count)
		ax.bar_label(rect, padding=3)
		
	ax.set_ylabel('Number')
	ax.set_title(emoji)
	ax.set_xticks(x, labels)
	fig.tight_layout()

	plt.show()

def make_charts(stats):
	emojis = ['💩', '🔪', '🤣', '👍', '🥰', '🙌', '😂']
	for emoji in emojis:
		make_bar_chart(emoji, stats)

stats = get_stats()
# print(stats['2/17/22']['💩'])
make_charts(stats)