class bot_history:

    def __init__(self, numMessagesToKeep=20):
        self.numMessagesToKeep = numMessagesToKeep

        self.emotions = {'anger'    : [],
                         'disgust'  : [],
                         'fear'     : [],
                         'joy'      : [],
                         'sadness'  : []}
        self.sentiments = []

    def addResponse(self, emotion):
        if (len(self.emotions['anger']) >= self.numMessagesToKeep):
            for s in self.emotions:
                s.pop(0)
            # self.sentiments.pop(0)

        print emotion
        self.emotions['anger'].append(emotion['anger'])
        self.emotions['disgust'].append(emotion['disgust'])
        self.emotions['fear'].append(emotion['fear'])
        self.emotions['joy'].append(emotion['joy'])
        self.emotions['sadness'].append(emotion['sadness'])
        # self.sentiments.append(sentiment)

    # prints the current averages of each emotion
    def getAllMeasures(self):
        average = {}
        for e in self.emotions:
            eSum = 0
            for i in self.emotions[e]:
                eSum += float(i)
            # eSum = sum(float(self.emotions[e]))
            average[e] = eSum*1.0 / len(self.emotions[e])*1.0
        # print average
        return average

    # prints the user's highest emotion
    def getHighEmotion(self):
        highScore = 0
        highEmotion = ''
        emotes = self.getAllMeasures()
        for e in emotes:
            if emotes[e] > highScore:
                highScore = emotes[e]
                highEmotion = e
        if e == '':
            print 'No entries for user yet'
        return highEmotion
