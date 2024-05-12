# Функция рисования квадрата
def draw_square(x, y, color):
    pygame.draw.rect(screen, color, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, GRAY, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

def main():
    running = True
    target_square = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))

    while running:
        screen.fill(WHITE)

        # Рисуем сетку квадратов
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                draw_square(i, j, WHITE)

        # Подсветить целевой квадрат
        draw_square(target_square[0], target_square[1], BLUE)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                clicked_square = (x // SQUARE_SIZE, y // SQUARE_SIZE)
                if clicked_square == target_square:
                    print("Правильно!")
                    target_square = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
                else:
                    print("Попробуйте снова!")

    pygame.quit()

if __name__ == '__main__':
    main()