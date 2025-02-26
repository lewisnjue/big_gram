from collections import defaultdict, Counter
import random

class BigramModel:
    def __init__(self):
        self.bigram_counts = defaultdict(Counter)  # Stores counts of bigrams
        self.unigram_counts = Counter()  # Stores counts of unigrams

    def train(self, corpus):
        """Train the bigram model on a given corpus."""
        for sentence in corpus:
            words = sentence.split()
            for i in range(1, len(words)):
                # Update bigram counts
                self.bigram_counts[words[i-1]][words[i]] += 1
                # Update unigram counts
                self.unigram_counts[words[i-1]] += 1

    def predict_next_word(self, word):
        """Predict the next word given the current word."""
        if word not in self.bigram_counts:
            return None  # Word not seen during training
        # Get the most likely next word based on bigram counts
        next_word = self.bigram_counts[word].most_common(1)
        return next_word[0][0] if next_word else None

    def generate_text(self, start_word, num_words=10):
        """Generate text using the bigram model."""
        current_word = start_word
        text = [current_word]
        for _ in range(num_words - 1):
            next_word = self.predict_next_word(current_word)
            if not next_word:
                break
            text.append(next_word)
            current_word = next_word
        return ' '.join(text)

# Example usage
corpus = [
    "I love programming",
    "I love machine learning",
    "I love Python",
    "Python is great",
    "Machine learning is fun"
]

# Train the model
model = BigramModel()
model.train(corpus)

# Predict the next word
print("Next word after 'I':", model.predict_next_word("I"))

# Generate text
print("Generated text:", model.generate_text("I", num_words=5))
