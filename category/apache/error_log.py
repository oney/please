from base.command import Command
from base.actions import Actions

keywords = {'apache': 10, 'error': 5, 'log': 5}
description = 'Apache error log file'
def run_func(words):
	print 'error_log'
	print words

def info_func(words):
	print 'info error_log'
	print words

error_log = Command(keywords, description, run_func, info_func)