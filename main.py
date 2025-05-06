import pygame
import random
import sys

# Инициализация Pygame
pygame.init()

# Настройки окна
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Тир")

# Цвета
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Шрифт для текста
font = pygame.font.SysFont(None, 36)

# Мишень
target_radius = 30
target_x = random.randint(target_radius, WIDTH - target_radius)
target_y = random.randint(target_radius, HEIGHT - target_radius)

# Счёт
score = 0
misses = 0

# Функция отрисовки мишени
def draw_target(x, y):
    pygame.draw.circle(screen, RED, (x, y), target_radius)
    pygame.draw.circle(screen, WHITE, (x, y), target_radius - 10)
    pygame.draw.circle(screen, RED, (x, y), target_radius - 20)
    pygame.draw.circle(screen, WHITE, (x, y), target_radius - 30)

# Основной цикл игры
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)

    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            distance = ((mouse_x - target_x) ** 2 + (mouse_y - target_y) ** 2) ** 0.5

            if distance <= target_radius:
                score += 1
                # Перемещение мишени
                target_x = random.randint(target_radius, WIDTH - target_radius)
                target_y = random.randint(target_radius, HEIGHT - target_radius)
            else:
                misses += 1

    # Отрисовка мишени
    draw_target(target_x, target_y)

    # Отрисовка счёта
    score_text = font.render(f"Попаданий: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    miss_text = font.render(f"Промахов: {misses}", True, BLACK)
    screen.blit(miss_text, (10, 50))

    # Обновление экрана
    pygame.display.flip()
    clock.tick(60)

# Завершение работы
pygame.quit()
sys.exit()