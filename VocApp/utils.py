import nltk
from nltk.corpus import stopwords
from nltk.util import ngrams
from nltk import pos_tag
from collections import Counter
from voiceDB.models import VocabDB
from pattern.fr import conjugate, INFINITIVE

# nltk.download('universal_tagset')
# nltk.download('maxent_treebank_pos_tagger')
french_pos_tagger = nltk.data.load("tokenizers/punkt/french.pickle")

# nltk.download("punkt")
# nltk.download("stopwords")
voc_words = VocabDB.objects.values_list('French', flat=True)
# Function to preprocess and tokenize text
def preprocess_text(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text.lower())
    
    # Remove punctuation and stopwords
    words = [word for word in words if word.isalnum() and (word not in stopwords.words("french")) and (word not in voc_words)]
    try:
        words = [conjugate(word, tense=INFINITIVE) for word in words]
    except:
        print('unable to conjugate words')

    return words


def preprocess_text_ns(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text.lower())
    
    # Remove punctuation and stopwords
    # words = [word for word in words if word.isalnum() and word not in stopwords.words("french")]
    words = [word for word in words if word.isalnum()]
    
    return words

# Function to count most repeated words
def count_most_repeated_words(text, num_words=10):
    words = preprocess_text(text)
    
    # Count word frequencies
    word_counts = Counter(words)
    
    # Get the most common words
    most_common_words = word_counts.most_common(num_words)
    
    return most_common_words

# Function to count most repeated phrases (n-grams)
def count_most_repeated_phrases(text, n=2, num_phrases=10):
    words = preprocess_text_ns(text)
    
    # Generate n-grams
    ngram_counts = Counter(ngrams(words, n))
    
    # Get the most common n-grams
    most_common_phrases = ngram_counts.most_common(num_phrases)
    
    return most_common_phrases
