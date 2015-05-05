class Command:
	def __init__(self, keywords, description, run_func, info_func):
		self.keywords = keywords
		self.description = description
		self.run_func = run_func
		self.info_func = info_func

	def rate(self, words):
		rating = 0
		for keyword in self.keywords.keys():
			if keyword in words:
				rating += self.keywords[keyword]
		return rating

	def run(self, words):
		self.run_func(words)
	def info(self, words):
		self.info_func(words)