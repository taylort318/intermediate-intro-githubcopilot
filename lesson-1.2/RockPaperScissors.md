# Rock Paper Scissors with GitHub Copilot - Student Demo Guide

## Overview
This demonstration shows students how to use **comments** to communicate with GitHub Copilot and generate code through auto-completion. Students will learn that Copilot reads their comments as instructions and can generate entire functions based on well-written descriptions.

## Learning Objectives
- Understand how GitHub Copilot interprets comments as instructions
- Practice writing clear, descriptive comments
- Experience the power of AI-assisted coding
- Build a complete Rock Paper Scissors game using Copilot suggestions

## Prerequisites
- GitHub Copilot extension installed in VS Code
- Basic understanding of Python syntax (covered in previous lessons)
- Students should be working on Windows machines or GitHub Codespaces

## Instructions: Building Rock Paper Scissors with GitHub Copilot

### Step 1: Open the Python File
1. In VS Code, open the existing `app.py` file
2. Remember: You'll use comments to "talk" to Copilot
3. Good comments lead to better code suggestions

### Step 2: Start with a Clear Comment Plan
Type the following comment at the top of the file:

```python
# Rock Paper Scissors Game
# This program plays rock paper scissors with the user
# The computer makes a random choice and compares it with the user's choice
```

Copilot reads these comments to understand what you want to build.

### Step 3: Import Statements Through Comments
Type this comment and then press Tab to see Copilot's suggestion:

```python
# Import random module for computer's choice
```

**Expected Result**: Copilot should suggest `import random`

**Windows Tip**: Use **Tab** to accept suggestions, **Escape** to dismiss them.

### Step 4: Define Game Options with Comments
Type this comment:

```python
# Define the possible choices for the game
```

**Expected Result**: Copilot might suggest something like:
```python
choices = ["rock", "paper", "scissors"]
```

### Step 5: Welcome Message
Type this comment:

```python
# Print welcome message to the player
```

**Expected Result**: Copilot should suggest a print statement welcoming the player.

### Step 6: Get User Input
Type this comment:

```python
# Ask the user to choose rock, paper, or scissors
```

**Expected Result**: Copilot should suggest using `input()` to get the user's choice.

### Step 7: Get Computer Choice
Type this comment:

```python
# Computer makes a random choice from the options
```

**Expected Result**: Copilot should suggest using `random.choice()` to select from the choices list.

### Step 8: Show the Choices
Type this comment:

```python
# Display what the user and computer chose
```

**Expected Result**: Copilot should suggest print statements to show both choices.

### Step 9: Determine the Winner
Type this comment:

```python
# Check who wins - rock beats scissors, scissors beats paper, paper beats rock
```

**Expected Result**: Copilot should suggest if/elif statements to determine the winner.

### Step 10: Display the Result
Type this comment:

```python
# Tell the player who won the game
```

## Student Practice Instructions

### Building Your Rock Paper Scissors Game

1. **Open VS Code** on your Windows machine or in GitHub Codespaces
2. **Open the existing `app.py` file** in your workspace
3. **Follow these steps**, typing each comment and pressing **Tab** to accept Copilot suggestions:

#### Step-by-Step Comments to Type:

1. Start with the header:
```python
# Rock Paper Scissors Game - Interactive Python Game
```

2. Add import statement:
```python
# Import random module for computer choices
```
*Press Tab to accept the suggestion*

3. Define choices:
```python
# List of valid game choices
```
*Press Tab and see what Copilot suggests*

4. Welcome the player:
```python
# Print welcome message
```
*Press Tab after the comment*

5. Get user input:
```python
# Ask user to enter their choice
```

6. Get computer choice:
```python
# Computer picks randomly from choices
```

7. Show both choices:
```python
# Print what user and computer chose
```

8. Determine winner with simple logic:
```python
# Check if it's a tie
# Check if user wins
# Otherwise computer wins
```

9. Display the result:
```python
# Print who won the game
```

## Tips for Success

- **Be descriptive** in your comments - the more detail, the better Copilot understands
- **Press Tab** to accept suggestions on Windows
- **Press Escape** to dismiss suggestions you don't want
- **Don't worry if suggestions aren't perfect** - you can always edit them
- **Try different comment styles** to see how Copilot responds
- **Be patient** - sometimes Copilot takes a moment to generate suggestions
- **Try Ctrl+Enter** on Windows to see more suggestion options
- **Experiment** - try your own comment variations
- **Focus on clear comments** - good comments lead to better code

## Common Issues and Solutions

### If Copilot Isn't Suggesting Code:
1. Check that GitHub Copilot is enabled (look for Copilot icon in status bar)
2. Make sure comments are descriptive enough
3. Try pressing **Ctrl+Enter** (Windows) to manually trigger suggestions
4. Ensure you're in a `.py` file so Copilot knows it's Python

### If Suggestions Are Wrong:
1. Press **Escape** to dismiss
2. Try rewriting the comment with more specific details
3. Accept partial suggestions and modify them
4. Remember: Copilot is a tool to help, not replace thinking!

## Extension Activities

Once you complete the basic game, try adding these features using comments:

1. **Ask to Play Again**:
```python
# Ask if the player wants to play another round
```

2. **Input Validation**:
```python
# Check if user entered a valid choice (rock, paper, or scissors)
```

3. **Score Tracking**:
```python
# Keep track of wins and losses
```

4. **Enhanced Display**:
```python
# Add fun messages for different outcomes
```

## Assessment Questions

After completing the game, reflect on these questions:
1. How do comments help GitHub Copilot understand what we want?
2. What makes a good comment for AI assistance?
3. When might you need to edit Copilot's suggestions?
4. How can this tool help you learn programming?

## Next Steps

This exercise introduces you to AI-assisted programming. In future lessons, you can:
- Learn to write more complex programs with Copilot
- Understand when to use AI assistance vs. writing code independently
- Explore other Copilot features like inline suggestions and chat

---

*Remember: GitHub Copilot is a powerful learning tool, but understanding the underlying programming concepts is still essential for becoming a skilled developer.*