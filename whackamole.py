import pygame
import random


def main():
    try:
        screen = pygame.display.set_mode((640, 512))
        mole_image = pygame.image.load("mole.png")
        clock = pygame.time.Clock()
        pygame.init()
        columns = 20
        rows = 16
        mole_x = 0
        mole_y = 0
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.fill("light green")

            for row in range(rows + 1):
                pygame.draw.line(surface=screen, color="black", start_pos=(0, row * 32), end_pos=(640, row * 32))
            for col in range(columns + 1):
                pygame.draw.line(surface=screen, color="black", start_pos=(col * 32, 0), end_pos=(col * 32, 512))
            mole_rect = mole_image.get_rect(topleft=(mole_x, mole_y))
            screen.blit(mole_image, mole_rect)
          
            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_pressed()[0] == 1:
                if mole_rect.collidepoint(pos):
                    spawn_row = random.randrange(0, rows)
                    spawn_col = random.randrange(0, columns)
                    mole_x = spawn_col * 32
                    mole_y = spawn_row * 32
                    screen.blit(mole_image, (mole_x - 32, mole_y - 32))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
