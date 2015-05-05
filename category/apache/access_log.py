from base.command import Command
from base.actions import Actions

keywords = {'apache': 10, 'access': 5, 'log': 5}
description = 'Apache access log file'
def run_func(words):
	print 'access_log'
	print words

def info_func(words):
	print 'info access_log'
	print words

access_log = Command(keywords, description, run_func, info_func)