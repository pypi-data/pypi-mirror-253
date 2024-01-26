import joblib
import pandas as pd
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.util import ngrams
from transformers import RobertaTokenizer, RobertaModel
import torch
from spellchecker import SpellChecker
from gensim.models import KeyedVectors
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier

def get_user_response(user_query):
    # Load your ML model
    def load_ml_model(model_path):
        try:
            model = joblib.load(model_path)
            return model
        except Exception as e:
            print(f"Error loading the ML model: {e}")
            return None

    # Load RoBERTa tokenizer and model
    tokenizer = RobertaTokenizer.from_pretrained('roberta-base')
    model = RobertaModel.from_pretrained('roberta-base')

    # Load GloVe model
    glove_model_path = 'inquirybot/data/glove.6B.300d.txt'
    glove_model = KeyedVectors.load_word2vec_format(glove_model_path, binary=False, limit=None, no_header=True)

    # Load your DataFrame
    df = pd.read_csv('inquirybot/data/2-intent-dataset-basic-dictionary.csv')

    # Initialize stemming and lemmatization tools
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()

    class RoBERTaEmbeddingTransformer(BaseEstimator, TransformerMixin):
        def __init__(self, n_grams=1):
            self.stop_words = set(stopwords.words('english'))
            self.lemmatizer = WordNetLemmatizer()
            self.n_grams = n_grams
            self.spell_checker = SpellChecker()

        def fit(self, X, y=None):
            return self

        def transform(self, X):
            embeddings = []
            for text in X:
                # Spellchecking
                corrected_words = [self.spell_checker.correction(word) for word in text.split()]
                corrected_words = [word for word in corrected_words if word is not None]
                text = ' '.join(corrected_words)

                # Tokenization with n-grams and lemmatization
                tokenized_data = [
                    self.lemmatizer.lemmatize(word.lower()) for word in nltk.word_tokenize(text) if word.isalnum() and word.lower() not in self.stop_words
                ]

                if self.n_grams > 1:
                    n_grams_list = list(ngrams(tokenized_data, self.n_grams))
                    tokenized_data += [' '.join(gram) for gram in n_grams_list]

                preprocessed_data = ' '.join(tokenized_data)

                # The tokenizer and model lines are assumed to be defined elsewhere in your code
                inputs = tokenizer(preprocessed_data, return_tensors='pt', padding=True, truncation=True, max_length=512)
                with torch.no_grad():
                    outputs = model(**inputs)
                embeddings.append(outputs.last_hidden_state.mean(dim=1).squeeze().numpy())
            return np.array(embeddings)

    class GloveEmbeddingTransformer(BaseEstimator, TransformerMixin):
        def __init__(self, n_grams=1):
            self.stop_words = set(stopwords.words('english'))
            self.lemmatizer = WordNetLemmatizer()
            self.n_grams = n_grams
            self.spell_checker = SpellChecker()

        def fit(self, X, y=None):
            return self

        def transform(self, X):
            embeddings = []
            for text in X:
                # Spellchecking
                corrected_words = [self.spell_checker.correction(word) for word in text.split()]
                corrected_words = [word for word in corrected_words if word is not None]
                text = ' '.join(corrected_words)

                # Tokenization with n-grams and lemmatization
                tokenized_data = [
                    self.lemmatizer.lemmatize(word.lower()) for word in nltk.word_tokenize(text) if word.isalnum() and word.lower() not in self.stop_words
                ]

                if self.n_grams > 1:
                    n_grams_list = list(ngrams(tokenized_data, self.n_grams))
                    tokenized_data += [' '.join(gram) for gram in n_grams_list]

                glove_words = [word for word in tokenized_data if word in glove_model]
                if glove_words:
                    glove_embedding = np.mean([glove_model[word] for word in glove_words], axis=0)
                else:
                    glove_embedding = np.zeros(300)  # Assuming GloVe embeddings are 300-dimensional

                embeddings.append(glove_embedding)
            return np.array(embeddings)

    def classify_entity(query, entity_dict):
        query_tokens = word_tokenize(query.lower())
        matched_synonyms = []

        for synonym in entity_dict:
            synonym_tokens = word_tokenize(synonym.lower())

            # Perform stemming and lemmatization on query and synonym
            stemmed_query = [stemmer.stem(token) for token in query_tokens]
            stemmed_synonym = [stemmer.stem(token) for token in synonym_tokens]

            lemmatized_query = [lemmatizer.lemmatize(token) for token in query_tokens]
            lemmatized_synonym = [lemmatizer.lemmatize(token) for token in synonym_tokens]

            # Check if stemmed or lemmatized synonym is present in the stemmed or lemmatized query
            if set(stemmed_synonym).intersection(stemmed_query) or set(lemmatized_synonym).intersection(lemmatized_query):
                matched_synonyms.append(synonym)

        return matched_synonyms


    def classify_intent_ml(query):
        if ml_model:
            intent = ml_model.predict([query])[0]
            return intent
        else:
            return None

    def process_query(query, df):
        # Classify the intent using a placeholder function
        predicted_intent = classify_intent_ml(query)

        # Filter the DataFrame for the predicted intent
        entities_df = df[df['Intent'] == predicted_intent]

        # Identify entities based on string matching with dictionaries
        identified_entities = []
        max_match_count = 0
        selected_entity = None

        for _, row in entities_df.iterrows():
            entity_dict = row['Dictionary']
            matched_synonyms = classify_entity(query, entity_dict)
            match_count = len(matched_synonyms)

            if match_count > max_match_count:
                max_match_count = match_count
                selected_entity = row['Entity']
                selected_synonyms = matched_synonyms

        # If no entities are identified, return a default response
        if selected_entity is None:
            return "No entities identified for the given query"

        # Get the response corresponding to the identified entity
        final_response = entities_df[entities_df['Entity'] == selected_entity].iloc[0]['Response']
        return final_response

    def generate_response(input_sentence, ml_model, df):
        # Placeholder for intent classification
        predicted_intent = classify_intent_ml(input_sentence)

        # Filter the DataFrame for the predicted intent
        entities_df = df[df['Intent'] == predicted_intent]

        # Use RoBERTa embedding transformer
        roberta_embedding_transformer = RoBERTaEmbeddingTransformer()
        roberta_embedding = roberta_embedding_transformer.transform([input_sentence])

        # Use GloVe embedding transformer
        glove_embedding_transformer = GloveEmbeddingTransformer()
        glove_embedding = glove_embedding_transformer.transform([input_sentence])

        # Combine embeddings
        combined_embedding = np.concatenate([roberta_embedding, glove_embedding], axis=1)

        # Convert combined_embedding to a single string
        combined_embedding_str = ' '.join(map(str, combined_embedding.flatten()))

        # Make predictions using the ML model
        ml_prediction = ml_model.predict([combined_embedding_str])[0]

        # Process the query to identify entities and get the final response
        final_response = process_query(input_sentence, df)

        return ml_prediction, final_response

    # Load ML model
    ml_model_path = "inquirybot/models/2-intent-demo-intent-classification.pkl"
    ml_model = load_ml_model(ml_model_path)

    # Generate response
    ml_prediction, result = generate_response(user_query, ml_model, df)

    return ml_prediction, result

# Ask user for input
#user_query = input("Enter your query: ")
user_query = "Is there a specific email address for reaching out to the college's alumni relations team?"

# Call the function and get the response
ml_prediction, result = get_user_response(user_query)

# Print ML prediction and final response
#print("ML Prediction:", ml_prediction)
print("Final Response:", result)
