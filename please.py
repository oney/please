#!/usr/bin/python

import sys
from operator import itemgetter

words = sys.argv[1:]
print words

from category.apache.access_log import access_log
from category.apache.error_log import error_log
from category.git.undo_commit import undo_commit

commands = []
commands.append(access_log)
commands.append(error_log)
commands.append(undo_commit)

candidate_max = 3
candidates = []

for command in commands:
	rating = command.rate(words)
	rating_count = 0
	for candidate in candidates:
		if candidate["rating"] > rating:
			rating_count += 1
			if rating_count == candidate_max:
				break
	if rating_count < candidate_max:
		candidates.append({'rating': rating, 'command': command})

# TODO remove rating to low

if len(candidates) == 1:
	candidate[0]['command'].run(words)
else:
	candidates = sorted(candidates, key=itemgetter('rating'), reverse=True)
	for candidate in candidates:
		candidate['command'].info(words)

