from language_tool_python import LanguageTool
from gensim.corpora import Dictionary
from gensim.models import LdaModel
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
import pandas as py
import nltk
import ssl


def read_excel(fileLocation: str, sheetName: str):
    responseData = py.ExcelFile(fileLocation)
    sheetData = py.read_excel(responseData, sheetName)
    return sheetData

# reads the paragraph and returns the number of words


def word_count(inputText: str):
    return len(inputText.split())

# finds the number of words in the inputed text


def analyse_word_count(wordBaseCount: int, inputText: str):
    wordCount = word_count(inputText)
    if wordCount >= wordBaseCount:
        return True
    else:
        return False

# find the number of repeative words and generate a dictonary


def analyse_conjunctions(inputParagraph: str, conjunctions):
    ssl._create_default_https_context = ssl._create_unverified_context
    nltk.download('stopwords')
    nltk.download('vader_lexicon')
    nltk.download('punkt')
    # Tokenize the paragraph into words
    words = word_tokenize(inputParagraph)
    filtered_words = [word for word in words if word.lower()]
    result = Counter(i for i in filtered_words if i in conjunctions)
    return dict(result)


# finds and gives the keyword for the given input paragraph by comparing the absolute relevancy and theme
def analyse_keywords(inputParagraph: str, coreIdea: str):
    # Define the machine learning-relevant terms to search for
    ml_terms = ["machine learning", "artificial intelligence", "algorithm", "prediction",
                "decision", "image recognition", "natural language processing", "predictive analytics"]

    # Tokenize the paragraph into words
    words = word_tokenize(inputParagraph)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.lower() not in stop_words]

    # Count the number of machine learning terms used
    ml_term_count = 0
    for word in words:
        if word.lower() in ml_terms:
            ml_term_count += 1

    print("Number of machine learning terms used:", ml_term_count)


def analyse_keywords_usage_percentage(inputParagraph: str, keywords):
    totalParagraphWord = word_count(inputParagraph)
    totalkeywords = len(keywords)
    effectiveUsageofKeyWords = (totalkeywords/totalParagraphWord) * 100
    return effectiveUsageofKeyWords


def find_the_frequency_of_words_used(inputParagraph: str):
    # Create a WordCloud object
    wordcloud = WordCloud().generate(inputParagraph)
    # Extract the word frequencies
    word_frequencies = dict(wordcloud.words_)
    # return the word frequencies
    return word_frequencies


def predict_the_topic_of_the_paragraph(text: str):
    # Convert the text to a bag-of-words representation
    dictionary = Dictionary([text.split()])
    corpus = [dictionary.doc2bow(text.split())]

    # Train the LDA model
    lda = LdaModel(corpus, num_topics=1)

    # Print the topics
    print(lda.print_topics())


def analyse_positive_negative_neutral_words(paragraph: str):
    stop_words = set(stopwords.words('english'))
    sia = SentimentIntensityAnalyzer()
    positive_words = []
    negative_words = []
    neutral_words = []

    # remove stop words
    filtered_words = [word for word in word_tokenize(
        paragraph) if word.lower() not in stop_words]

    # classify words as positive, negative, or neutral
    for word in filtered_words:
        score = sia.polarity_scores(word)
        if score['compound'] >= 0.5:
            positive_words.append(word)
        elif score['compound'] > -0.5 and score['compound'] < 0.5:
            neutral_words.append(word)
        else:
            negative_words.append(word)

    print("Positive words:", positive_words)
    print("Neutral words:", neutral_words)
    print("Negative words:", negative_words)


def analyse_grammar_errors(paragraph: str):
    # Create a LanguageTool object
    tool = LanguageTool('en-US')
    # Check the text for grammar mistakes
    matches = tool.check(paragraph)
    # Print the grammar mistakes
    for match in matches:
        print(match)
