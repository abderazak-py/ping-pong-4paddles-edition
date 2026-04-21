# 🏓 Ping Pong 4 Paddles Edition
A 2-player ping pong game with 4 paddles (2 vertical + 2 horizontal) built with Python Turtle.

## 🎮 Game Features
- **4 Paddles Total**
  - Left vertical paddle (Player 1)
  - Right vertical paddle (Player 2)  
  - Bottom horizontal paddle (Player 1)
  - Top horizontal paddle (Player 2)
- Real time score tracking
- Ball physics with bouncing
- Smooth movement controls

## 🎯 Controls

| Player | Action           | Key         |
|--------|------------------|-------------|
| Player 1 | Move left paddle UP    | **Z**       |
| Player 1 | Move left paddle DOWN  | **S**       |
| Player 1 | Move bottom paddle LEFT | **Q**     |
| Player 1 | Move bottom paddle RIGHT | **D**    |
| --- | --- | --- |
| Player 2 | Move right paddle UP   | **↑ Up Arrow** |
| Player 2 | Move right paddle DOWN | **↓ Down Arrow** |
| Player 2 | Move top paddle LEFT   | **← Left Arrow** |
| Player 2 | Move top paddle RIGHT  | **→ Right Arrow** |

## 🚀 How to Play
1. Make sure you have Python installed
2. Run the game:
   ```bash
   python main.py
   ```
3. Score points by getting the ball past your opponent's paddles
4. First player to reach your agreed score wins!

## ⚙️ Game Settings
You can modify these values at the top of `main.py`:
```python
BALL_SPEED = 1    # Adjust ball speed
PADDLE_SPEED = 2  # Adjust paddle movement speed
```

## 🎨 Colors
- 🟦 Player 1 paddles: Blue
- 🔴 Player 2 paddles: Red
- 🟢 Ball: Green
- 🟡 Background: Yellow

---
Created with Python Turtle Graphics