import pygame
import sys
import random
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Aim Tester")

font = pygame.font.Font(None, 36)

def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_obj, text_rect)

def main_menu():
    while True:
        screen.fill(WHITE)
        draw_text("Aim Tester", font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)

        play_button = pygame.Rect(300, 300, 200, 50)
        pygame.draw.rect(screen, BLACK, play_button)
        draw_text("Play", font, WHITE, screen, play_button.centerx, play_button.centery)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    return

        pygame.display.update()

def game_over(level):
    while True:
        screen.fill(WHITE)
        draw_text("Game Over", font, RED, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 3)
        draw_text(f"Reached Level: {level}", font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        draw_text("Click anywhere to return to main menu", font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT * 2 // 3)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                return

        pygame.display.update()

def generate_circles(level):
    circles = []
    for _ in range(5):
        radius = (50 - level * 5) // 2
        x = random.randint(radius, SCREEN_WIDTH - radius)
        y = random.randint(radius, SCREEN_HEIGHT - radius)
        circles.append((x, y, radius))
    return circles

def draw_circles(circles):
    for circle in circles:
        pygame.draw.circle(screen, RED, (circle[0], circle[1]), circle[2])

def main_game():
    level = 1
    while True:
        circles = generate_circles(level)
        start_time = time.time()
        while time.time() - start_time < 3:
            screen.fill(WHITE)
            draw_text(f"Level {level}", font, BLACK, screen, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        start_time = time.time()
        while time.time() - start_time < 5:
            screen.fill(WHITE)
            draw_circles(circles)
            time_left = int(5 - (time.time() - start_time))
            draw_text(f"Level: {level}", font, BLACK, screen, 70, 20)
            draw_text(f"Time Left: {time_left}", font, BLACK, screen, SCREEN_WIDTH - 100, 20)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for circle in circles:
                        if pygame.Rect(circle[0] - circle[2], circle[1] - circle[2], circle[2] * 2, circle[2] * 2).collidepoint(mouse_pos):
                            circles.remove(circle)
                            break
            if not circles:
                level += 1
                break
        else:
            game_over(level)
            return

def main():
    while True:
        main_menu()
        main_game()

if __name__ == "__main__":
    main()
