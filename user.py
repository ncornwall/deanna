class user:

	# class variables; !!! may be better as instance variables

	numMessagesToKeep = 20
	userName = ''

	emotions = {'anger'	: [],
				  'disgust'	: [],
				  'fear'	: [],
				  'joy'		: [],
				  'sadness'	: []}
	sentiments = []

	# add a new entry to user's emotion tracking
	def addResponse(self,sentiment, emotion):
		if (len(self.emotions['anger']) >= self.numMessagesToKeep):
			for s in self.emotions:
				s.pop(0)
			self.sentiments.pop(0)

		print emotion
		self.emotions['anger'].append(emotion['anger'])
		self.emotions['disgust'].append(emotion['disgust'])
		self.emotions['fear'].append(emotion['fear'])
		self.emotions['joy'].append(emotion['joy'])
		self.emotions['sadness'].append(emotion['sadness'])
		self.sentiments.append(sentiment)

	# prints the current averages of each emotion
	def getAllMeasures(self):
		average = {}
		for e in self.emotions:
			eSum = sum(self.emotions[e])
			average[e] = eSum*1.0 / len(e)*1.0
		print average
		return average

	# prints the user's highest emotion
	def getHighEmotion(self):
		highScore = 0
		highEmotion = ''
		emotes = user.getAllMeasures()
		for e in emotes:
			if emotes[e] > highScore:
				highScore = emotes[e]
				highEmotion = e
		if e == '':
			print 'No entries for user yet'
		return highEmotion




