import pygame
import sys
import random
import math
from pygame.locals import *
from sounds import SoundManager

# Initialize Pygame
pygame.init()

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (RGB)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 40
        self.speed = 5
        self.health = 100
        self.max_health = 100
        self.shoot_cooldown = 0
        self.shoot_delay = 10  # frames between shots
        
    def update(self, keys):
        # Movement
        if keys[K_LEFT] or keys[K_a]:
            self.x -= self.speed
        if keys[K_RIGHT] or keys[K_d]:
            self.x += self.speed
        if keys[K_UP] or keys[K_w]:
            self.y -= self.speed
        if keys[K_DOWN] or keys[K_s]:
            self.y += self.speed
            
        # Keep player on screen
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.width))
        self.y = max(0, min(self.y, SCREEN_HEIGHT - self.height))
        
        # Update shoot cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
            
    def shoot(self):
        if self.shoot_cooldown <= 0:
            self.shoot_cooldown = self.shoot_delay
            return Bullet(self.x + self.width // 2, self.y, 0, -8, GREEN, "player")
        return None
        
    def draw(self, screen):
        # Draw player ship (simple triangle)
        points = [
            (self.x + self.width // 2, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height)
        ]
        pygame.draw.polygon(screen, BLUE, points)
        
        # Draw health bar
        bar_width = 60
        bar_height = 8
        bar_x = self.x + (self.width - bar_width) // 2
        bar_y = self.y - 15
        
        # Background (red)
        pygame.draw.rect(screen, RED, (bar_x, bar_y, bar_width, bar_height))
        # Health (green)
        health_width = int((self.health / self.max_health) * bar_width)
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, health_width, bar_height))

class Alien:
    def __init__(self, x, y, alien_type=1):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 30
        self.speed = 2
        self.health = 20
        self.max_health = 20
        self.alien_type = alien_type
        self.shoot_cooldown = random.randint(30, 120)
        self.shoot_delay = random.randint(60, 180)
        self.direction = 1  # 1 for right, -1 for left
        self.move_timer = 0
        
    def update(self):
        # Simple zigzag movement
        self.move_timer += 1
        if self.move_timer > 60:  # Change direction every 60 frames
            self.direction *= -1
            self.move_timer = 0
            
        self.x += self.direction * self.speed
        
        # Move down occasionally
        if random.randint(1, 300) == 1:
            self.y += 20
            
        # Keep alien on screen horizontally
        if self.x <= 0 or self.x >= SCREEN_WIDTH - self.width:
            self.direction *= -1
            self.y += 20
            
        # Update shoot cooldown
        if self.shoot_cooldown > 0:
            self.shoot_cooldown -= 1
            
    def shoot(self):
        if self.shoot_cooldown <= 0 and random.randint(1, 100) < 2:  # 2% chance per frame
            self.shoot_cooldown = self.shoot_delay
            return Bullet(self.x + self.width // 2, self.y + self.height, 0, 4, RED, "alien")
        return None
        
    def draw(self, screen):
        # Draw different alien types
        if self.alien_type == 1:
            # Type 1: Simple rectangle
            pygame.draw.rect(screen, RED, (self.x, self.y, self.width, self.height))
        elif self.alien_type == 2:
            # Type 2: Diamond shape
            points = [
                (self.x + self.width // 2, self.y),
                (self.x + self.width, self.y + self.height // 2),
                (self.x + self.width // 2, self.y + self.height),
                (self.x, self.y + self.height // 2)
            ]
            pygame.draw.polygon(screen, PURPLE, points)
        else:
            # Type 3: Circle
            pygame.draw.ellipse(screen, ORANGE, (self.x, self.y, self.width, self.height))

class Bullet:
    def __init__(self, x, y, dx, dy, color, owner):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
        self.owner = owner
        self.width = 4
        self.height = 8
        
    def update(self):
        self.x += self.dx
        self.y += self.dy
        
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        
    def is_off_screen(self):
        return (self.y < 0 or self.y > SCREEN_HEIGHT or 
                self.x < 0 or self.x > SCREEN_WIDTH)

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.dx = random.uniform(-3, 3)
        self.dy = random.uniform(-3, 3)
        self.color = color
        self.life = 30
        self.max_life = 30
        
    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.life -= 1
        self.dx *= 0.98  # Slow down over time
        self.dy *= 0.98
        
    def draw(self, screen):
        if self.life > 0:
            alpha = int((self.life / self.max_life) * 255)
            size = int((self.life / self.max_life) * 5) + 1
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), size)
            
    def is_dead(self):
        return self.life <= 0

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Alien Invasion - Space Shooter")
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Initialize sound manager
        self.sound_manager = SoundManager()
        
        # Game objects
        self.player = Player(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 60)
        self.aliens = []
        self.bullets = []
        self.particles = []
        
        # Game state
        self.score = 0
        self.level = 1
        self.game_over = False
        self.paused = False
        self.wave_timer = 0
        self.aliens_per_wave = 5
        
        # Start background music
        self.sound_manager.play_background_music()
        
        # Spawn first wave
        self.spawn_wave()
        
    def spawn_wave(self):
        """Spawn a new wave of aliens"""
        for i in range(self.aliens_per_wave):
            x = random.randint(0, SCREEN_WIDTH - 40)
            y = random.randint(-200, -50)
            alien_type = random.randint(1, 3)
            self.aliens.append(Alien(x, y, alien_type))
            
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                elif event.key == K_SPACE:
                    if not self.game_over:
                        bullet = self.player.shoot()
                        if bullet:
                            self.bullets.append(bullet)
                            self.sound_manager.play_sound('shoot')
                elif event.key == K_p:
                    self.paused = not self.paused
                elif event.key == K_r and self.game_over:
                    self.restart_game()
                    
    def update(self):
        if self.paused or self.game_over:
            return
            
        keys = pygame.key.get_pressed()
        
        # Update player
        self.player.update(keys)
        
        # Auto-shoot for player (space bar also works)
        if keys[K_SPACE]:
            bullet = self.player.shoot()
            if bullet:
                self.bullets.append(bullet)
                self.sound_manager.play_sound('shoot')
        
        # Update aliens
        for alien in self.aliens[:]:
            alien.update()
            
            # Alien shooting
            bullet = alien.shoot()
            if bullet:
                self.bullets.append(bullet)
                self.sound_manager.play_sound('alien_shoot')
                
            # Remove aliens that are off screen
            if alien.y > SCREEN_HEIGHT:
                self.aliens.remove(alien)
                
        # Update bullets
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                self.bullets.remove(bullet)
                
        # Update particles
        for particle in self.particles[:]:
            particle.update()
            if particle.is_dead():
                self.particles.remove(particle)
                
        # Check collisions
        self.check_collisions()
        
        # Spawn new wave if needed
        if len(self.aliens) == 0:
            self.wave_timer += 1
            if self.wave_timer > 60:  # Wait 1 second
                self.level += 1
                self.aliens_per_wave += 2
                self.spawn_wave()
                self.wave_timer = 0
                
    def check_collisions(self):
        # Player bullets vs Aliens
        for bullet in self.bullets[:]:
            if bullet.owner == "player":
                for alien in self.aliens[:]:
                    if (bullet.x < alien.x + alien.width and
                        bullet.x + bullet.width > alien.x and
                        bullet.y < alien.y + alien.height and
                        bullet.y + bullet.height > alien.y):
                        
                        # Hit!
                        self.bullets.remove(bullet)
                        self.aliens.remove(alien)
                        self.score += 10
                        self.sound_manager.play_sound('explosion')
                        
                        # Create explosion particles
                        for _ in range(8):
                            self.particles.append(Particle(alien.x + alien.width//2, 
                                                          alien.y + alien.height//2, 
                                                          random.choice([RED, ORANGE, YELLOW])))
                        break
                        
        # Alien bullets vs Player
        for bullet in self.bullets[:]:
            if bullet.owner == "alien":
                if (bullet.x < self.player.x + self.player.width and
                    bullet.x + bullet.width > self.player.x and
                    bullet.y < self.player.y + self.player.height and
                    bullet.y + bullet.height > self.player.y):
                    
                    # Hit player!
                    self.bullets.remove(bullet)
                    self.player.health -= 20
                    self.sound_manager.play_sound('hit')
                    
                    # Create hit particles
                    for _ in range(5):
                        self.particles.append(Particle(self.player.x + self.player.width//2, 
                                                      self.player.y + self.player.height//2, 
                                                      WHITE))
                    
                    if self.player.health <= 0:
                        self.game_over = True
                        
        # Aliens vs Player (collision damage)
        for alien in self.aliens[:]:
            if (alien.x < self.player.x + self.player.width and
                alien.x + alien.width > self.player.x and
                alien.y < self.player.y + self.player.height and
                alien.y + alien.height > self.player.y):
                
                # Collision!
                self.aliens.remove(alien)
                self.player.health -= 30
                self.sound_manager.play_sound('explosion')
                
                # Create explosion particles
                for _ in range(10):
                    self.particles.append(Particle(alien.x + alien.width//2, 
                                                  alien.y + alien.height//2, 
                                                  random.choice([RED, ORANGE, YELLOW])))
                
                if self.player.health <= 0:
                    self.game_over = True
                    
    def draw(self):
        self.screen.fill(BLACK)
        
        # Draw stars background
        for i in range(50):
            x = (i * 37) % SCREEN_WIDTH
            y = (i * 23) % SCREEN_HEIGHT
            pygame.draw.circle(self.screen, WHITE, (x, y), 1)
            
        if not self.game_over:
            # Draw game objects
            self.player.draw(self.screen)
            
            for alien in self.aliens:
                alien.draw(self.screen)
                
            for bullet in self.bullets:
                bullet.draw(self.screen)
                
            for particle in self.particles:
                particle.draw(self.screen)
                
            # Draw UI
            font = pygame.font.Font(None, 36)
            score_text = font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            
            level_text = font.render(f"Level: {self.level}", True, WHITE)
            self.screen.blit(level_text, (10, 50))
            
            if self.paused:
                pause_text = font.render("PAUSED - Press P to resume", True, YELLOW)
                text_rect = pause_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
                self.screen.blit(pause_text, text_rect)
        else:
            # Game over screen
            font_large = pygame.font.Font(None, 72)
            font_medium = pygame.font.Font(None, 48)
            font_small = pygame.font.Font(None, 36)
            
            game_over_text = font_large.render("GAME OVER", True, RED)
            game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 100))
            self.screen.blit(game_over_text, game_over_rect)
            
            final_score_text = font_medium.render(f"Final Score: {self.score}", True, WHITE)
            final_score_rect = final_score_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 50))
            self.screen.blit(final_score_text, final_score_rect)
            
            restart_text = font_small.render("Press R to restart or ESC to quit", True, YELLOW)
            restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 50))
            self.screen.blit(restart_text, restart_rect)
            
        pygame.display.flip()
        
    def restart_game(self):
        """Restart the game"""
        self.player = Player(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 60)
        self.aliens = []
        self.bullets = []
        self.particles = []
        self.score = 0
        self.level = 1
        self.game_over = False
        self.paused = False
        self.wave_timer = 0
        self.aliens_per_wave = 5
        self.spawn_wave()
        
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
            
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()
