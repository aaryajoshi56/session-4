# Dictionary mapping letters to their Scrabble scores
scrabble_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5,
    'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4,
    'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

# Get user input
word = input("Enter a word: ").strip().upper()

# Calculate score
score = sum(scrabble_scores.get(letter, 0) for letter in word)

# Print the result
print(f"The score for {word.lower()} is {score}")
# Dictionary mapping letters to their Scrabble scores
scrabble_scores = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1, 'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8, 'K': 5,
    'L': 1, 'M': 3, 'N': 1, 'O': 1, 'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1, 'U': 1, 'V': 4,
    'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

# Get words from both players
word1 = input("Player 1: ").strip().upper()
word2 = input("Player 2: ").strip().upper()

# Calculate scores
score1 = sum(scrabble_scores.get(letter, 0) for letter in word1)
score2 = sum(scrabble_scores.get(letter, 0) for letter in word2)

# Print scores
print(f"Player 1 score is: {score1}")
print(f"Player 2 score is: {score2}")

# Determine the winner
if score1 > score2:
    print("Player 1 wins!")
elif score2 > score1:
    print("Player 2 wins!")
else:
    print("It's a tie!")
