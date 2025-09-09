# Alien Invasion - Space Shooter Game

A classic space shooter game built with Python and Pygame. Defend Earth from waves of alien invaders in this retro-style arcade game!

## 🚀 Game Features

- **Smooth Controls**: WASD or Arrow keys for movement, Space bar to shoot
- **Multiple Alien Types**: Three different alien types with unique appearances and behaviors
- **Progressive Difficulty**: Each wave brings more aliens and increased challenge
- **Sound Effects**: Immersive audio with shooting, explosion, and background music
- **Particle Effects**: Visual explosions and hit effects for better gameplay experience
- **Health System**: Player health with visual health bar
- **Scoring System**: Earn points by destroying aliens
- **Pause Functionality**: Press P to pause/resume the game

## 🎮 How to Play

### Controls
- **Movement**: WASD keys or Arrow keys
- **Shoot**: Space bar (hold for continuous fire)
- **Pause**: P key
- **Restart**: R key (when game over)
- **Quit**: ESC key

### Objective
- Destroy all alien invaders before they reach Earth
- Avoid alien bullets and collisions
- Survive as many waves as possible
- Achieve the highest score!

### Scoring
- **Alien Destroyed**: 10 points each
- **Survive Waves**: Bonus points for completing levels

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation Steps

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/yourusername/alien-invasion.git
   cd alien-invasion
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the game**
   ```bash
   python alien_invasion.py
   ```

### Alternative Installation
If you don't have pip or prefer manual installation:
```bash
pip install pygame
python alien_invasion.py
```

## 🎯 Game Mechanics

### Player Ship
- Blue triangular spaceship
- Health bar displayed above the ship
- Continuous shooting capability
- Smooth movement in all directions

### Alien Types
1. **Red Rectangle Aliens**: Basic enemies with simple movement
2. **Purple Diamond Aliens**: Slightly more aggressive
3. **Orange Circle Aliens**: Fastest and most dangerous

### Power-ups & Special Features
- Particle explosion effects when enemies are destroyed
- Visual feedback for player hits
- Progressive wave difficulty
- Background starfield animation

## 🎵 Audio Features

The game includes procedurally generated sound effects:
- **Shooting Sounds**: Different tones for player and alien weapons
- **Explosion Effects**: Dynamic noise bursts for destruction
- **Background Music**: Ambient space-themed audio loop
- **Hit Feedback**: Audio cues for player damage

## 🐛 Known Issues & Limitations

- Sound generation might be resource-intensive on older systems
- Alien AI is relatively simple (could be improved with more complex patterns)
- No save/load functionality for high scores
- Limited visual variety in alien designs
- Collision detection could be more precise for smaller objects

## 🔧 Technical Details

### File Structure
```
alien-invasion/
├── alien_invasion.py    # Main game file
├── sounds.py           # Sound management system
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

### Key Classes
- **Player**: Handles player ship movement, shooting, and health
- **Alien**: Manages alien behavior, movement patterns, and shooting
- **Bullet**: Simple projectile system for both player and aliens
- **Particle**: Visual effects for explosions and hits
- **SoundManager**: Handles all audio generation and playback
- **Game**: Main game loop and state management

### Performance Notes
- Target FPS: 60 frames per second
- Screen resolution: 800x600 pixels
- Optimized for smooth gameplay on most systems

## 🚧 Future Improvements

Some ideas for enhancing the game (if you want to contribute!):
- [ ] Add power-ups (rapid fire, shields, multi-shot)
- [ ] Implement boss battles
- [ ] Add different weapon types
- [ ] Create a high score save system
- [ ] Add more visual effects and animations
- [ ] Implement different difficulty modes
- [ ] Add a main menu and settings screen
- [ ] Create more complex alien AI patterns

## 🤝 Contributing

Feel free to fork this project and submit pull requests! Some areas that could use improvement:
- Better alien AI and movement patterns
- More visual effects and animations
- Additional sound effects and music
- Code optimization and bug fixes
- New features and game mechanics

## 📝 License

This project is open source and available under the MIT License. Feel free to use, modify, and distribute as needed.

## 🎮 Credits

Created as a learning project to practice Python game development with Pygame. The game draws inspiration from classic arcade shooters like Space Invaders and Galaga.

---

**Enjoy defending Earth from the alien invasion!** 🌍👾

*Note: This game was created for educational purposes and may contain some rough edges typical of intermediate-level programming projects.*
