# Функция рисования квадрата
def draw_square(x, y, color):
    pygame.draw.rect(screen, color, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    pygame.draw.rect(screen, GRAY, (x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)


# Выбор случайных квадратов
def choose_random_squares(num_squares):
    squares = []
    while len(squares) < num_squares:
        new_square = (random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1))
        if new_square not in squares:
            squares.append(new_square)
    return squares


def main():
    running = True
    highlighted_squares = choose_random_squares(4)
    sequence_index = 0
    player_sequence = []
    interval = 1000  # Интервал мигания в миллисекундах

    while running:
        screen.fill(WHITE)

        # Рисуем сетку квадратов
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                draw_square(i, j, WHITE)

        # Отображение последовательности мигания
        if sequence_index < len(highlighted_squares):
            current_square = highlighted_squares[sequence_index]
            draw_square(current_square[0], current_square[1], BLUE)
            pygame.display.update()
            pygame.time.delay(interval)
            draw_square(current_square[0], current_square[1], WHITE)
            pygame.display.update()
            pygame.time.delay(interval)
            sequence_index += 1
        else:
            # Ожидание ввода пользователя
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    clicked_square = (x // SQUARE_SIZE, y // SQUARE_SIZE)
                    player_sequence.append(clicked_square)
                    draw_square(clicked_square[0], clicked_square[1], BLUE)
                    pygame.display.update()
                    pygame.time.delay(500)
                    draw_square(clicked_square[0], clicked_square[1], WHITE)
                    pygame.display.update()

                    if len(player_sequence) == len(highlighted_squares):
                        if player_sequence == highlighted_squares:
                            print("Правильно!")
                        else:
                            print("Попробуйте снова!")
                        highlighted_squares = choose_random_squares(4)
                        sequence_index = 0
                        player_sequence = []

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == "__main__":
    main()