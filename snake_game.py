import pygame
import random

pygame.init()

clock = pygame.time.Clock()

FPS = 5

SNAKE_COLOR = (160, 32, 240)
FOOD_COLOR = (0, 255, 0)
BG = pygame.image.load(r'C:\Users\user\Downloads\954494362.png')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
CELL_SIZE = 20

eat_sound = pygame.mixer.Sound(r'C:\Users\user\Downloads\food_G1U6tlb.mp3')
end = pygame.mixer.Sound(r'C:\Users\user\Downloads\snake-dies-game-over.mp3')

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PYTHON GAME")

# Class for the snake
class Snake:
    def __init__(self):
        self.body = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (1,0)
        
    def move(self):
        head = self.body[0]
        new_head = (head[0] + self.direction[0] * CELL_SIZE, head[1] + self.direction[1] * CELL_SIZE)
        self.body.insert(0, new_head)
        self.body.pop()
    
    def grow(self):
        tail = self.body[-1]
        new_tail = (tail[0] - self.direction[0] * CELL_SIZE, tail[1] - self.direction[1] * CELL_SIZE)
        self.body.append(new_tail)

# Function to generate food randomly with weights and a timer
def generate_food_randomly(snake, food_weights, food_timer):
    total_weight = sum(food_weights.values())
    rand_num = random.randint(1, total_weight)
    cumulative_weight = 0
    
    for food_type, weight in food_weights.items():
        cumulative_weight += weight
        if rand_num <= cumulative_weight:
            while True:
                x = random.randint(0, (SCREEN_WIDTH - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
                y = random.randint(0, (SCREEN_HEIGHT - CELL_SIZE) // CELL_SIZE) * CELL_SIZE
                food_pos = (x, y)
                if food_pos not in snake.body:
                    return food_pos, food_type, food_timer

# Function to update food timer and check if food disappears
def update_food_timer(foods):
    updated_foods = []
    for food in foods:
        pos, food_type, timer = food
        timer -= 1
        if timer > 0:
            updated_foods.append((pos, food_type, timer))
    foods[:] = updated_foods

def main():
    snake = Snake()
    food_timer = 50  # Adjust timer as needed
    foods = []
    score = 0
    level = 1
    game_over = False
    paused = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused

                elif not paused:
                    if event.key == pygame.K_UP and snake.direction != (0, 1):
                        snake.direction = (0, -1)
                    elif event.key == pygame.K_DOWN and snake.direction != (0, -1):
                        snake.direction = (0, 1)
                    elif event.key == pygame.K_LEFT and snake.direction != (1, 0):
                        snake.direction = (-1, 0)
                    elif event.key == pygame.K_RIGHT and snake.direction != (-1, 0):
                        snake.direction = (1, 0)

        head = snake.body[0]
        if head[0] < 0 or head[0] >= SCREEN_WIDTH or head[1] < 0 or head[1] >= SCREEN_HEIGHT:
            game_over = True
            end.play()

        # Update food timer and remove disappeared foods
        update_food_timer(foods)

        # Check for collision with food
        for food in foods:
            if head == food[0]:
                snake.grow()
                score += 1
                eat_sound.play()
                foods.remove(food)

        # Generate new food if needed
        if len(foods) == 0:
            food_pos, food_type, food_timer = generate_food_randomly(snake, food_weights, food_timer)
            foods.append((food_pos, food_type, food_timer))

        screen.blit(BG, (0, 0))

        # Draw foods
        for food in foods:
            pygame.draw.rect(screen, FOOD_COLOR, (food[0][0], food[0][1], CELL_SIZE, CELL_SIZE))

        # Draw snake
        for segment in snake.body:
            pygame.draw.rect(screen, SNAKE_COLOR, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

        # Display score
        font = pygame.font.Font(None, 36)
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        if paused:
            # Display "Pause" text
            font = pygame.font.Font(None, 72)
            pause_text = font.render("Pause", True, (255, 0, 0))
            screen.blit(pause_text, (SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2 - 36))

        pygame.display.flip()
        clock.tick(FPS + level * 2)
        snake.move()

    # Display "Game Over" text
    font = pygame.font.Font(None, 72)
    text = font.render("Game Over", True, (255, 0, 0))
    screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 36))
    pygame.display.flip()
    pygame.time.delay(8500)  
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
