corpus = [
    'URGENT! You have won a 1 week FREE membership in our prize jackpot.',
    'Hey, what time is the meeting tomorrow?',
    'WINNER!! As a valued network customer you have been selected to receive a prize.',
    'Are you coming to the party tonight?',
    'Congratulations! You won a free flight to Bahamas.'
]

def build_vocabulary(corpus):
    """
    Builds a sorted list of unique words from all documents in the corpus.
    
    Args:
        corpus (list of str): A list of text documents.
        
    Returns:
        list of str: A sorted list of unique words.
    """
    # 1. Initialize an empty set to store unique words. A set is used to automatically handle duplicates.
    # 2. Loop through each document in the corpus.
    # 3. For each document, split it into words (use .lower() to make it case-insensitive).
    # 4. Add all words to the set.
    # 5. Convert the set to a list and sort it alphabetically.
    # 6. Return the sorted list.
    
    unique_words = set()
    for document in corpus:
        words = document.lower().split()
        cleaned_words = [word.strip('.,!?') for word in words]  # Remove punctuation
        unique_words.update(cleaned_words)

    vocabulary = sorted(unique_words)

    # 7. Print the sorted list of unique words.
    
    return vocabulary

def vectorize_text(text, vocabulary):
    """
    Converts a single text document into a numerical vector.
        
    Args:
        text (str): The text document to vectorize.
        vocabulary (list of str): The sorted list of unique words.
            
    Returns:
        list of int: A numerical vector representing the word counts.
    """
        # 1. Initialize a vector of zeros. The length of this vector should be the same as the vocabulary's length.
        # 2. Pre-process the input text (e.g., convert to lowercase) and split it into words.
        # 3. Loop through the words in the processed text.
        # 4. For each word, if it exists in the vocabulary:
            # a. Find the index (position) of that word in the vocabulary.
            # b. Increment the count at that index in your vector.
        # 5. Return the final vector.
       
    vector = [0] * len(vocabulary)
    
    cleaned_text = text.lower().split()
    cleaned_text = [word.strip('.,!?') for word in cleaned_text]  #
    
    for word in cleaned_text:
        if word in vocabulary: 
            index = vocabulary.index(word)
            vector[index] += 1
    print(f"Vector after processing text: {vector}")
    return vector

# --- Main Execution ---
if __name__ == '__main__':
    # 1. Build the vocabulary from the corpus
    vocabulary = build_vocabulary(corpus)
    print(f"Vocabulary ({len(vocabulary)} words):")
    print(vocabulary)
    print("-" * 30)

    # 2. Vectorize each document in the corpus
    print("Vectorized Corpus:")
    for doc in corpus:
        vector = vectorize_text(doc, vocabulary)
        print(f"Original: {doc}")
        print(f"Vector:   {vector}\n")
