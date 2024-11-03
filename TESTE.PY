Parece que houve um problema com a exibição do código. Vou dividir a resposta em partes menores para que você consiga ver tudo.

### Parte 1: Configurações Básicas

```python
import sys
import random
import pgzrun
import random
from random import choice, randint
from pgzero.actor import Actor

# Definindo dimensões e título da tela
WIDTH = 650
HEIGHT = 500
TITLE = 'Space Invasion'
FPS = 60

# Ator do fundo e do jogador
bg = Actor("galaxia")
player = Actor('player_blue', (WIDTH // 2, HEIGHT - 50))
enemies = []
lasers = []
score = 0
lives = 3

# Cores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Iniciar a música de fundo
music.play("background_music")
music.set_volume(0.5)  # Define o volume da música
```

### Parte 2: Funções de Desenho e Atualização

```python
def draw():
    screen.clear()  # Limpa a tela antes de desenhar
    bg.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for laser in lasers:
        laser.draw()
    screen.draw.text(f"Score: {score}", (10, 10), color=WHITE, fontsize=24)
    screen.draw.text(f"Lives: {lives}", (WIDTH - 100, 10), color=WHITE, fontsize=24)

def update(dt):
    global score, lives, lasers

    # Movimento do jogador
    if keyboard.left and player.left > 0:
        player.x -= 5
    if keyboard.right and player.right < WIDTH:
        player.x += 5
```

### Parte 3: Movimento e Colisão dos Inimigos e Lasers

```python
    # Movimento dos inimigos
    for enemy in enemies:
        enemy.y += enemy.speed
        if enemy.bottom > HEIGHT:
            enemies.remove(enemy)
            lives -= 1
            if lives == 0:
                game_over()

    # Movimento dos lasers
    for laser in lasers:
        laser.y -= 10
        if laser.top < 0:
            lasers.remove(laser)

    # Colisões
    for laser in lasers.copy():
        for enemy in enemies.copy():
            if laser.colliderect(enemy):
                lasers.remove(laser)
                enemies.remove(enemy)
                score += 10

    # Criação de novos inimigos
    if random.randint(0, 100) < 2:
        new_enemy()
```

### Parte 4: Criação dos Inimigos e Som do Disparo

```python
def new_enemy():
    enemy_type = choice(['enemy_red', 'enemy_orange'])
    x = randint(50, WIDTH - 50)
    enemy = Actor(enemy_type, pos=(x, -50))
    enemy.speed = randint(3, 5)
    enemies.append(enemy)

def on_key_down(key):
    if key == keys.SPACE:
        laser = Actor('lasergreen03', pos=player.midtop)
        lasers.append(laser)
        sounds.laser_sound.play()  # Reproduz o som do disparo
```

### Parte 5: Função de Game Over

```python
def game_over():
    music.stop()  # Para a música de fundo
    screen.fill((0, 0, 0))
    screen.draw.text("Game Over!", center=(WIDTH // 2, HEIGHT // 2), fontsize=64, color=RED)
    screen.draw.text(f"Sua pontuação final: {score}", center=(WIDTH // 2, HEIGHT // 2 + 50), fontsize=32, color=WHITE)

pgzrun.go()
```

Essas são todas as partes do código. Veja se agora está visível corretamente!