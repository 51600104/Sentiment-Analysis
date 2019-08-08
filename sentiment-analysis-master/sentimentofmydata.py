from textblob import TextBlob
import nltk
from textblob.sentiments import NaiveBayesAnalyzer
from textblob.classifiers import NaiveBayesClassifier  
from nltk.tokenize import word_tokenize ,sent_tokenize

train_data = [  
    ('I love this sandwich.', 'pos'),
    ('I like it','pos'),
    ('I like the pizza','pos'),
    ('this is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('this is my best work.', 'pos'),
    ("what an awesome view", 'pos'),
    ('I do not like this restaurant', 'neg'),
    ("But I don't like it","neg"),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('Nice docking station for home or work', 'pos'),
    ('The move was fantastic I like it', 'pos'),
    ('You should watch it, it is brilliant', 'pos'),
    ('Exceptionally good', 'pos'),
    ("Wonderfully directed and executed. I like it", 'pos'),
    ('It was very boring', 'neg'),
    ('I did not like the movie', 'neg'),
    ("The movie was horrible", 'neg'),
    ('I will not recommend', 'neg'),
    ('The acting is pathetic', 'neg'),
    ('he is my sworn enemy!', 'neg'),
    ('my boss is horrible.', 'neg'),
    ('beautiful','pos'),
    ('I have had problems wit hit dropping signal and more','neg')
]
all_words = set(word.lower() for passage in train_data for word in word_tokenize(passage[0]))
t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1]) for x in train_data]
classifier = nltk.NaiveBayesClassifier.train(t)
#test_sentence = "I like the blue shirt. But the price is expensive. I want you to give me a discount. so I will buy it"
#test_sent_features = {word: (word in word_tokenize(test_sentence.lower())) for word in all_words}
#test_sent_features
#print(classifier.classify(test_sent_features))
##
classifier = NaiveBayesClassifier(train_data)  
#prob_dist = classifier.prob_classify("I like the blue shirt. But the price is expensive. I want you to give me a discount. so I will buy it")
#print(prob_dist.max())
#print(round(prob_dist.prob("pos"), 2))


##
blob = TextBlob("I like the blue shirt. But the price is expensive. I want you to give me a discount. so I will buy it")
print(blob.sentiment)
#print(sent_tokenize("I like the blue shirt. But the price is expensive. I want you to give me a discount. so I will buy it"))
neu = sent_tokenize("I like the blue shirt. But the price is expensive. I want you to give me a discount. so I will buy it")

for x in neu :
    print(x)
    
    s =TextBlob(x)
    
    
    print(s.sentiment)
    prob_dist = classifier.prob_classify(x)
    print(prob_dist.max())
    print(round(prob_dist.prob("pos"), 2))
    test_sent_features = {word: (word in word_tokenize(x.lower())) for word in all_words}
    test_sent_features
    print(classifier.classify(test_sent_features))
    #print(s.tags)
    #print(s.noun_phrases)
    #print(s.words)

#print(blob.sentiment)
#print(blob.tags)
#print(blob.noun_phrases)
#print(blob.words)