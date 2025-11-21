# 🎮 Guessing Game

## 📖 Description
A simple number guessing game built with Python. The computer picks a random number between 1 and 100, and you have to guess it! Get feedback on whether your guess is too high or too low until you find the correct number.

## 🎯 How to Play

1. Run the game: `python guessing_game.py`
2. The computer picks a random number between 1 and 100
3. Enter your first guess when prompted
4. The game will tell you if your guess is:
   - **Too low** - Your number is smaller than the target
   - **Too high** - Your number is larger than the target
   - **Correct** - You found it! 🎉
5. Keep guessing until you get it right!

## 💻 How It Works

- Uses Python's `random` module to generate a random number
- Implements a `while` loop to keep the game running until the correct number is guessed
- Takes user input after each guess
- Provides instant feedback to guide your next guess

## 🚀 Future Enhancements

- Deploy with a web interface (Streamlit or Flask)
- Add difficulty levels (different number ranges)
- Track number of guesses and display a leaderboard
- Create a fun, interactive UI for better user experience
- Add timer or score system

## 📋 Requirements

- Python 3.x

## 🎲 Example Gameplay

```
Guess a number between 1 and 100: 50
Your guess is low, try again!
Guess your next number: 75
Your guess is high, try again!
Guess your next number: 62
You are right! You must have superpowers!
```

## 👤 Author
Yeabsira Belete Mamo
