import pygame
import os

class SoundManager:
    def __init__(self):
        """Initialize sound manager - handles all game sounds"""
        pygame.mixer.init(frequency=22050, size=-16, channels=2, buffer=512)
        
        # Sound effects (we'll create simple tones since we don't have actual sound files)
        self.sounds = {}
        self.music_playing = False
        
        # Create simple sound effects using pygame's sound generation
        self.create_sounds()
        
    def create_sounds(self):
        """Create simple sound effects programmatically"""
        # Player shoot sound - short beep
        shoot_sound = pygame.sndarray.make_sound(self.generate_tone(800, 0.1))
        self.sounds['shoot'] = shoot_sound
        
        # Alien shoot sound - lower pitch
        alien_shoot_sound = pygame.sndarray.make_sound(self.generate_tone(400, 0.15))
        self.sounds['alien_shoot'] = alien_shoot_sound
        
        # Explosion sound - noise burst
        explosion_sound = pygame.sndarray.make_sound(self.generate_noise(0.3))
        self.sounds['explosion'] = explosion_sound
        
        # Player hit sound - harsh tone
        hit_sound = pygame.sndarray.make_sound(self.generate_tone(200, 0.2))
        self.sounds['hit'] = hit_sound
        
        # Power up sound - ascending tone
        powerup_sound = pygame.sndarray.make_sound(self.generate_ascending_tone(0.5))
        self.sounds['powerup'] = powerup_sound
        
    def generate_tone(self, frequency, duration):
        """Generate a simple tone"""
        sample_rate = 22050
        frames = int(duration * sample_rate)
        arr = []
        
        for i in range(frames):
            time = float(i) / sample_rate
            wave = 4096 * pygame.math.sin(frequency * 2 * pygame.math.pi * time)
            arr.append([int(wave), int(wave)])
            
        return pygame.sndarray.array(arr)
        
    def generate_noise(self, duration):
        """Generate white noise for explosion sound"""
        sample_rate = 22050
        frames = int(duration * sample_rate)
        arr = []
        
        for i in range(frames):
            noise = int(pygame.math.random() * 8192 - 4096)
            arr.append([noise, noise])
            
        return pygame.sndarray.array(arr)
        
    def generate_ascending_tone(self, duration):
        """Generate ascending tone for powerup"""
        sample_rate = 22050
        frames = int(duration * sample_rate)
        arr = []
        
        for i in range(frames):
            time = float(i) / sample_rate
            frequency = 200 + (time / duration) * 600  # Ascend from 200Hz to 800Hz
            wave = 4096 * pygame.math.sin(frequency * 2 * pygame.math.pi * time)
            arr.append([int(wave), int(wave)])
            
        return pygame.sndarray.array(arr)
        
    def play_sound(self, sound_name):
        """Play a sound effect"""
        if sound_name in self.sounds:
            try:
                self.sounds[sound_name].play()
            except:
                pass  # Silently fail if sound can't play
                
    def play_background_music(self):
        """Play background music (simple looping tone)"""
        if not self.music_playing:
            # Create a simple ambient background tone
            bg_music = pygame.sndarray.make_sound(self.generate_background_music())
            bg_music.play(-1)  # Loop indefinitely
            self.music_playing = True
            
    def generate_background_music(self):
        """Generate ambient background music"""
        sample_rate = 22050
        duration = 4.0  # 4 second loop
        frames = int(duration * sample_rate)
        arr = []
        
        for i in range(frames):
            time = float(i) / sample_rate
            # Create a slow, ambient chord progression
            wave1 = 1000 * pygame.math.sin(110 * 2 * pygame.math.pi * time)  # A2
            wave2 = 800 * pygame.math.sin(146.83 * 2 * pygame.math.pi * time)  # D3
            wave3 = 600 * pygame.math.sin(220 * 2 * pygame.math.pi * time)  # A3
            wave4 = 400 * pygame.math.sin(293.66 * 2 * pygame.math.pi * time)  # D4
            
            # Add some variation
            variation = 200 * pygame.math.sin(0.5 * 2 * pygame.math.pi * time)
            
            combined = (wave1 + wave2 + wave3 + wave4 + variation) / 5
            arr.append([int(combined), int(combined)])
            
        return pygame.sndarray.array(arr)
        
    def stop_music(self):
        """Stop background music"""
        pygame.mixer.music.stop()
        self.music_playing = False
