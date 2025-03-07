import random
import time

# Game settings
GRID_SIZE = 10
DIRECTIONS = {'w': 'up', 's': 'down', 'a': 'left', 'd': 'right'}

def generate_food(snake):
    """Generate food at a position not occupied by the snake."""
    while True:
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - 1)
        if [row, col] not in snake:
            return [row, col]

def print_grid(snake, food):
    """Print the game grid."""
    grid = [[' ' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    # Draw snake
    for segment in snake:
        grid[segment[0]][segment[1]] = 'O'
    # Draw head
    head = snake[0]
    grid[head[0]][head[1]] = '@'
    # Draw food
    grid[food[0]][food[1]] = '*'
    
    print("\n" + "-" * (GRID_SIZE * 2 + 1))
    for row in grid:
        print("|" + " ".join(row) + "|")
    print("-" * (GRID_SIZE * 2 + 1))

def game_loop():
    """Main game loop."""
    snake = [[5, 5]]  # Initial position
    direction = 'right'
    food = generate_food(snake)
    game_over = False

    while not game_over:
        # Clear terminal (works in most environments)
        print("\033c", end="")
        print_grid(snake, food)
        
        # Get keyboard input
        try:
            key = input("Direction (W/A/S/D): ").lower()
            new_dir = DIRECTIONS.get(key, direction)
            # Prevent 180-degree turns
            if (direction == 'up' and new_dir != 'down') or \
               (direction == 'down' and new_dir != 'up') or \
               (direction == 'left' and new_dir != 'right') or \
               (direction == 'right' and new_dir != 'left'):
                direction = new_dir
        except:
            pass

        # Calculate new head position
        head = [snake[0][0], snake[0][1]]
        if direction == 'up': head[0] -= 1
        elif direction == 'down': head[0] += 1
        elif direction == 'left': head[1] -= 1
        elif direction == 'right': head[1] += 1

        # Collision checks
        if (head[0] < 0 or head[0] >= GRID_SIZE or
            head[1] < 0 or head[1] >= GRID_SIZE or
            head in snake):
            game_over = True
            print(f"Game Over! Score: {len(snake)-1}")
            break

        # Update snake
        snake.insert(0, head)
        if head == food:
            food = generate_food(snake)
        else:
            snake.pop()

        time.sleep(0.2)

if __name__ == "__main__":
    game_loop()