from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
sentimentanalyzer=SentimentIntensityAnalyzer()
file=open('examples.txt', 'r')
for statement in file:
	analyzer=sentimentanalyzer.polarity_scores(statement)
	print 'Sentiment Analysis=>',
	for word in analyzer:
		print('{0}: {1}, '.format(word, analyzer[word])),
	print ''
file.close()