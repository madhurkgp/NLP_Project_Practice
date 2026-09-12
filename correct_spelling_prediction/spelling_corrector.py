#!/usr/bin/env python3
"""
Spelling Correction Application
A standalone spelling corrector that suggests corrections for misspelled words.
"""

import re
import pickle
import os
from collections import Counter
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import pandas as pd


class SpellingCorrector:
    def __init__(self, data_path='dataset/papers.csv'):
        """Initialize the spelling corrector with dataset and models."""
        self.data_path = data_path
        self.vocab = None
        self.probs = None
        self.stop_words = None
        self.lemmatizer = None
        
        # Download required NLTK data
        self._download_nltk_data()
        
        # Initialize stopwords and lemmatizer
        self._initialize_text_processing()
        
        # Load or train the model
        self._load_or_train_model()
    
    def _download_nltk_data(self):
        """Download required NLTK data if not already present."""
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt')
        
        try:
            nltk.data.find('corpora/stopwords')
        except LookupError:
            nltk.download('stopwords')
        
        try:
            nltk.data.find('corpora/wordnet')
        except LookupError:
            nltk.download('wordnet')
    
    def _initialize_text_processing(self):
        """Initialize stopwords and lemmatizer."""
        self.stop_words = set(stopwords.words('english'))
        
        # Custom stopwords for academic papers
        new_words = ["fig", "figure", "image", "sample", "using", 
                     "show", "result", "large", 
                     "also", "one", "two", "three", 
                     "four", "five", "seven", "eight", "nine"]
        self.stop_words = list(self.stop_words.union(new_words))
        
        self.lemmatizer = WordNetLemmatizer()
    
    def _pre_process(self, text):
        """Preprocess text data."""
        # lowercase
        text = text.lower()
        
        # remove tags
        text = re.sub("</?.*?>", " <> ", text)
        
        # remove special characters and digits
        text = re.sub("(\\d|\\W)+", " ", text)
        
        # Convert to list from string
        text = text.split()
        
        # remove stopwords
        text = [word for word in text if word not in self.stop_words]

        # remove words less than three letters
        text = [word for word in text if len(word) >= 3]

        # lemmatize
        text = [self.lemmatizer.lemmatize(word) for word in text]
        
        return ' '.join(text)
    
    def _process_tweet(self, tweet):
        """Process tweet-like text (remove URLs, mentions, etc.)."""
        tweet = re.sub(r'\$\w*', '', tweet)
        tweet = re.sub(r'^RT[\s]+', '', tweet)
        tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
        tweet = re.sub(r'#', '', tweet)
        return tweet
    
    def _misc(self, file_name):
        """Extract words from text."""
        words = []
        file_name = self._process_tweet(file_name)
        words = re.findall(r'\w+', file_name)
        return words
    
    def _get_count(self, word_l):
        """Get word count dictionary."""
        word_count_dict = Counter(word_l)
        return word_count_dict
    
    def _get_probs(self, word_count_dict):
        """Get word probability dictionary."""
        probs = {}
        m = sum(word_count_dict.values())
        for key in word_count_dict.keys():
            probs[key] = word_count_dict.get(key, 0) / m
        return probs
    
    def _delete_letter(self, word, verbose=False):
        """Generate all possible words by deleting one letter."""
        delete_l = []
        split_l = [(word[:i], word[i:]) for i in range(len(word))]
        delete_l = [L + R[1:] for L, R in split_l if R]
        
        if verbose:
            print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")
        
        return delete_l
    
    def _switch_letter(self, word, verbose=False):
        """Generate all possible words by switching adjacent letters."""
        def swap(c, i, j):
            c = list(c)
            c[i], c[j] = c[j], c[i]
            return ''.join(c)

        switch_l = []
        split_l = [(word[:i], word[i:]) for i in range(len(word))]
        switch_l = [a + b[1] + b[0] + b[2:] for a, b in split_l if len(b) >= 2]

        if verbose:
            print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}")

        return switch_l
    
    def _replace_letter(self, word, verbose=False):
        """Generate all possible words by replacing one letter."""
        letters = 'abcdefghijklmnopqrstuvwxyz'
        replace_l = []
        split_l = [(word[:i], word[i:]) for i in range(len(word))]
        replace_l = [a + l + (b[1:] if len(b) > 1 else '') for a, b in split_l if b for l in letters]
        replace_set = set(replace_l)
        replace_set.discard(word)  # Remove the original word
        replace_l = sorted(list(replace_set))

        if verbose:
            print(f"Input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")

        return replace_l
    
    def _insert_letter(self, word, verbose=False):
        """Generate all possible words by inserting one letter."""
        letters = 'abcdefghijklmnopqrstuvwxyz'
        insert_l = []
        split_l = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        insert_l = [a + l + b for a, b in split_l for l in letters]

        if verbose:
            print(f"Input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")

        return insert_l
    
    def _edit_one_letter(self, word, allow_switches=True):
        """Generate all possible words by editing one letter."""
        edit_one_set = set()
        edit_one_set.update(self._delete_letter(word))
        if allow_switches:
            edit_one_set.update(self._switch_letter(word))
        edit_one_set.update(self._replace_letter(word))
        edit_one_set.update(self._insert_letter(word))
        return edit_one_set
    
    def _edit_two_letters(self, word, allow_switches=True):
        """Generate all possible words by editing two letters."""
        edit_two_set = set()
        edit_one = self._edit_one_letter(word, allow_switches=allow_switches)
        for w in edit_one:
            if w:
                edit_two = self._edit_one_letter(w, allow_switches=allow_switches)
                edit_two_set.update(edit_two)
        return edit_two_set
    
    def _load_or_train_model(self):
        """Load existing model or train new one."""
        model_files = ['word-probability-spellings.pkl', 'vocab-spellings.pkl']
        
        # Check if model files exist
        if all(os.path.exists(f) for f in model_files):
            print("Loading existing model...")
            try:
                with open('word-probability-spellings.pkl', 'rb') as f:
                    self.probs = pickle.load(f)
                with open('vocab-spellings.pkl', 'rb') as f:
                    self.vocab = pickle.load(f)
                print("Model loaded successfully!")
                return
            except Exception as e:
                print(f"Error loading model: {e}")
        
        # Train new model if loading fails or files don't exist
        print("Training new model...")
        self._train_model()
    
    def _train_model(self):
        """Train the spelling correction model."""
        if not os.path.exists(self.data_path):
            print(f"Warning: Dataset file {self.data_path} not found.")
            print("Creating a small demo vocabulary...")
            self._create_demo_vocabulary()
            return
        
        try:
            # Load dataset
            df = pd.read_csv(self.data_path)
            
            # Process first 3000 documents (as in original)
            docs = df['paper_text'].iloc[:3000].apply(lambda x: self._pre_process(x))
            sentences = docs.tolist()
            text_data = ' '.join(sentences)
            
            # Extract words
            words = self._misc(text_data)
            self.vocab = set(words)
            
            # Calculate probabilities
            word_count_dict = self._get_count(words)
            self.probs = self._get_probs(word_count_dict)
            
            # Save the model
            with open('word-probability-spellings.pkl', 'wb') as f:
                pickle.dump(self.probs, f)
            with open('vocab-spellings.pkl', 'wb') as f:
                pickle.dump(self.vocab, f)
            
            print(f"Model trained successfully! Vocabulary size: {len(self.vocab)}")
            
        except Exception as e:
            print(f"Error training model: {e}")
            self._create_demo_vocabulary()
    
    def _create_demo_vocabulary(self):
        """Create a small demo vocabulary for testing."""
        demo_words = [
            'hello', 'world', 'python', 'programming', 'computer', 'science',
            'artificial', 'intelligence', 'machine', 'learning', 'data',
            'analysis', 'algorithm', 'development', 'software', 'engineering',
            'technology', 'research', 'university', 'student', 'education'
        ]
        
        self.vocab = set(demo_words)
        word_count_dict = Counter(demo_words)
        self.probs = self._get_probs(word_count_dict)
        
        print("Demo vocabulary created for testing purposes.")
    
    def get_corrections(self, word, n=5, verbose=False):
        """
        Get spelling suggestions for a given word.
        
        Args:
            word (str): The word to correct
            n (int): Number of suggestions to return
            verbose (bool): Whether to print verbose output
            
        Returns:
            list: List of tuples with (suggested_word, probability)
        """
        if self.vocab is None or self.probs is None:
            print("Model not loaded. Please initialize the corrector first.")
            return []
        
        suggestions = []
        n_best = []
        
        # If word is already correct, return it
        if word in self.vocab:
            return [[word, self.probs.get(word, 0)]]
        
        # Get suggestions from one-letter edits
        one_edit_suggestions = self._edit_one_letter(word).intersection(self.vocab)
        
        # Get suggestions from two-letter edits if no one-edit suggestions
        if not one_edit_suggestions:
            suggestions = list(self._edit_two_letters(word).intersection(self.vocab))
        else:
            suggestions = list(one_edit_suggestions)
        
        # Calculate probabilities and sort
        n_best = [[s, self.probs.get(s, -1)] for s in suggestions]
        n_best.sort(key=lambda x: x[1], reverse=True)
        
        if verbose:
            print(f"suggestions = {suggestions}")
        
        return n_best[:n]
    
    def correct_text(self, text, n=3):
        """
        Correct spelling in a given text.
        
        Args:
            text (str): The text to correct
            n (int): Number of suggestions per word
            
        Returns:
            dict: Dictionary with original words as keys and suggestions as values
        """
        words = re.findall(r'\b\w+\b', text.lower())
        corrections = {}
        
        for word in words:
            if len(word) >= 3:  # Only check words with 3+ characters
                suggestions = self.get_corrections(word, n=n)
                if suggestions and suggestions[0][0] != word:
                    corrections[word] = suggestions
        
        return corrections


def main():
    """Main function to run the spelling corrector."""
    print("=== Spelling Correction Application ===")
    print("Loading models...")
    
    # Initialize the corrector
    corrector = SpellingCorrector()
    
    print("\nModels loaded successfully!")
    print("Enter 'quit' to exit the application.\n")
    
    while True:
        # Get user input
        user_input = input("Enter a word or text to check: ").strip()
        
        if user_input.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if not user_input:
            continue
        
        # Check if it's a single word or text
        words = user_input.split()
        
        if len(words) == 1:
            # Single word correction
            suggestions = corrector.get_corrections(user_input, n=5, verbose=False)
            
            if suggestions:
                if suggestions[0][0] == user_input:
                    print(f"'{user_input}' is spelled correctly!")
                else:
                    print(f"Suggestions for '{user_input}':")
                    for i, (word, prob) in enumerate(suggestions, 1):
                        print(f"  {i}. {word} (probability: {prob:.6f})")
            else:
                print(f"No suggestions found for '{user_input}'")
        else:
            # Text correction
            corrections = corrector.correct_text(user_input, n=3)
            
            if corrections:
                print("Spelling suggestions:")
                for word, suggestions in corrections.items():
                    print(f"  '{word}': {[s[0] for s in suggestions]}")
            else:
                print("No spelling errors found!")
        
        print()


if __name__ == "__main__":
    main()
