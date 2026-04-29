import sys
import pygame # pyright: ignore[reportMissingImports]
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid # pyright: ignore[reportMissingImports]
from asteroidfield import AsteroidField # pyright: ignore[reportMissingImports]
from shot import Shot # pyright: ignore[reportMissingImports]


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    shots = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, "black")
        updatable.update(dt)
        for ast in asteroids:
            if player.collides_with(ast):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
                return
            for shot in shots:
                if shot.collides_with(ast):
                    log_event("asteroid_shot")
                    ast.split()
                    shot.kill()
        
        for thing in drawable:
            thing.draw(screen)
        
        pygame.display.flip()
        dt = clock.tick(60)
        dt = dt / 1000



if __name__ == "__main__":
    main()
