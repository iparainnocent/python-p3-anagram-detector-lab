# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possible_anagrams):
        # Create a sorted version of the original word
        sorted_word = sorted(self.word)
        
        # Initialize an empty list to hold matches
        matches = []
        
        # Iterate over the possible anagrams
        for candidate in possible_anagrams:
            # Check if the sorted version of the candidate matches the sorted original word
            if sorted(candidate) == sorted_word:
                matches.append(candidate)
        
        return matches