import os
from base.command import Command
from base.actions import Actions

keywords = {'git': 10, 'undo': 5, 'commit': 5}
description = 'Git undo commit'
def run_func(words):
	os.system("git reset --soft HEAD~1")
	print 'undo_commit'
	print words

def info_func(words):
	print 'info undo_commit'
	print words

undo_commit = Command(keywords, description, run_func, info_func)