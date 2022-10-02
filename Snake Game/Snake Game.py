import pygame  # Import pygame (install pygame with pip install pygame)
import sys  # Import sys to exit the game
import random  # Import random to generate random numbers
# Import Vector2 from pygame.math to use vectors for the snake and food position
from pygame.math import Vector2


class SNAKE:  # Snake class
    def __init__(self):  # Initialize the snake
        # Snake body is left of the head
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        # Snake direction control (up, down, left, right)
        self.direction = Vector2(0, 0)
        # Snake new block control (add a new block to the snake  when the snake eats the food)
        self.new_block = False

        # Graphics for the snake (can be found in the Graphics folder)
        self.head_up = pygame.image.load(
            'Snake Game/Graphics/head_up.png').convert_alpha()
        self.head_down = pygame.image.load(
            'Snake Game/Graphics/head_down.png').convert_alpha()
        self.head_right = pygame.image.load(
            'Snake Game/Graphics/head_right.png').convert_alpha()
        self.head_left = pygame.image.load(
            'Snake Game/Graphics/head_left.png').convert_alpha()

        self.tail_up = pygame.image.load(
            'Snake Game/Graphics/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load(
            'Snake Game/Graphics/tail_down.png').convert_alpha()
        self.tail_right = pygame.image.load(
            'Snake Game/Graphics/tail_right.png').convert_alpha()
        self.tail_left = pygame.image.load(
            'Snake Game/Graphics/tail_left.png').convert_alpha()

        self.body_vertical = pygame.image.load(
            'Snake Game/Graphics/body_vertical.png').convert_alpha()
        self.body_horizontal = pygame.image.load(
            'Snake Game/Graphics/body_horizontal.png').convert_alpha()

        self.body_tr = pygame.image.load(
            'Snake Game/Graphics/body_tr.png').convert_alpha()
        self.body_tl = pygame.image.load(
            'Snake Game/Graphics/body_tl.png').convert_alpha()
        self.body_br = pygame.image.load(
            'Snake Game/Graphics/body_br.png').convert_alpha()
        self.body_bl = pygame.image.load(
            'Snake Game/Graphics/body_bl.png').convert_alpha()

        # Sound for the snake (can be found in the Sound folder)
        self.crunch_sound = pygame.mixer.Sound('Snake Game/Sounds/Eat.wav')
        self.game_over_sound = pygame.mixer.Sound(
            'Snake Game/Sounds/Game Over.wav')
        self.background_sound = pygame.mixer.Sound(
            'Snake Game/Sounds/Background Music1.wav')  # Can use "Background Music1.wav" or "Background Music2.wav"

    def draw_snake(self):  # Draw the snake
        self.update_head_graphics()  # Uses the appropriate graphics for the snake head
        self.update_tail_graphics()  # Uses the appropriate graphics for the snake tail

        for index, block in enumerate(self.body):
            # Get the x position of the snake
            x_pos = int(block.x * cell_size)
            # Get the y position of the snake
            y_pos = int(block.y * cell_size)
            # Create a rectangle for the positioning of the snake
            block_rect = pygame.Rect(x_pos, y_pos, cell_size, cell_size)

            if index == 0:
                # Implement the snake head graphics
                screen.blit(self.head, block_rect)

            elif index == len(self.body) - 1:  # Last item in the snake list
                # Implement the snake tail graphics
                screen.blit(self.tail, block_rect)

                # Graphics for the body of the snake
            else:
                # Get the previous snake block
                previous_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - \
                    block  # Get the next snake block
                if previous_block.x == next_block.x:  # Vertical snake graphics
                    # Check if the snake is moving vertically if the x coordinates of the previous and next block are the same
                    screen.blit(self.body_vertical, block_rect)
                elif previous_block.y == next_block.y:  # Horizontal snake graphics
                    # Check if the snake is moving horizontal if the y coordinates of the previous and next block are the same
                    screen.blit(self.body_horizontal, block_rect)

                else:  # Graphics for the corners of the snake
                    if previous_block.x == -1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl, block_rect)

                    if previous_block.x == -1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl, block_rect)

                    if previous_block.x == 1 and next_block.y == -1 or previous_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr, block_rect)

                    if previous_block.x == 1 and next_block.y == 1 or previous_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br, block_rect)

    # Graphics for the snake

    def update_head_graphics(self):  # Create method for the head of the snake
        # Subtract both vectors to get a new vector that represents the direction of the snake head
        head_relation = self.body[1] - self.body[0]

        # Use the correct head graphics for the snake
        if head_relation == Vector2(1, 0):
            self.head = self.head_left

        elif head_relation == Vector2(-1, 0):
            self.head = self.head_right

        elif head_relation == Vector2(0, 1):
            self.head = self.head_up

        elif head_relation == Vector2(0, -1):
            self.head = self.head_down

    def update_tail_graphics(self):  # Create method for the tail of the snake
        # Same concept as the head graphics
        tail_relation = self.body[-2] - self.body[-1]

        # Use the correct tail graphics for the snake
        if tail_relation == Vector2(1, 0):
            self.tail = self.tail_left

        if tail_relation == Vector2(-1, 0):
            self.tail = self.tail_right

        if tail_relation == Vector2(0, 1):
            self.tail = self.tail_up

        if tail_relation == Vector2(0, -1):
            self.tail = self.tail_down

    def move_snake(self):  # Move the snake
        if self.new_block == True:  # If the snake eats the food add a new block to the snake
            body_copy = self.body[:]  # Extends the snake
            # Insert the movement vector to the body copy list at index 0 (the head) and add the movement vector to it to move the snake head in the direction of the movement vector (up, down, left, right)
            body_copy.insert(0, body_copy[0] + self.direction)
            # Return the list to the original snake and store it in the body variable
            self.body = body_copy[:]
            # Only adds one new block to the snake when the snake eats the food
            self.new_block = False
        else:  # If the snake doesn't eat the food then don't add a new block to the snake
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]

    def add_block(self):
        # Set the new_block variable to True to add a new block to the snake when the snake eats the food
        self.new_block = True

    def play_crunch_sound(self):  # Play the sound when the snake eats the food
        self.crunch_sound.set_volume(0.05)
        self.crunch_sound.play()

    def play_game_over_sound(self):  # Play the sound when the snake dies
        self.game_over_sound.set_volume(0.05)
        self.game_over_sound.play()

    def play_background_music(self):  # Play the background music
        self.background_sound.set_volume(0.1)
        self.background_sound.play(-1)

    def reset(self):
        self.body = [Vector2(5, 10), Vector2(4, 10), Vector2(3, 10)]
        self.direction = Vector2(0, 0)


class FRUIT:  # Fruit class
    def __init__(self):
        self.randomize()

    def draw_fruit(self):  # Method for the fruit
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size), int(
            self.pos.y * cell_size), cell_size, cell_size)  # Create a rectangle for the fruit (x,y,width,height) (int casting because the position is a float) (cell_size is the size of the cell) Makes a grid

        screen.blit(banana, fruit_rect)  # Draw the fruit surface on the screen

    def randomize(self):  # Create a randomize method for the fruit position
        # Random x coordinate for the fruit (cell_number - 1 because the grid starts at 0)
        self.x = random.randint(0, cell_number - 1)
        # Random y coordinate for the fruit (cell_number - 1 because the grid starts at 0)
        self.y = random.randint(0, cell_number - 1)
        self.pos = Vector2(self.x, self.y)


class MAIN:  # Main class to combine the snake and fruit classes to organize the game
    def __init__(self):  # Initialize the main class
        self.snake = SNAKE()  # Create a snake object from the snake class
        self.fruit = FRUIT()  # Create a fruit object from the fruit class
        self.snake.play_background_music()  # Play the background music

    def update(self):  # Update method to maintain the game loop
        self.snake.move_snake()  # Move the snake
        self.check_collision()  # Check if the snake collides with the fruit
        self.check_fail()  # Check if the snake is outside of the screen or if it hits itself

    def draw_elements(self):  # Draw method
        self.draw_grass()  # Draw the grass
        self.fruit.draw_fruit()  # Draw the fruit
        self.snake.draw_snake()  # Draw the snake
        self.draw_score()  # Draw the score

    def check_collision(self):  # Check if the snake collides with the fruit
        # If the fruit position is equal to the snake head position
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()  # Randomize the fruit position after the snake eats the fruit
            self.snake.add_block()  # Add a block to the snake body after the snake eats the fruit
            # Play the crunch sound when the snake eats the fruit
            self.snake.play_crunch_sound()
        # Ensures the fruit is not on the snake
        for block in self.snake.body[1:]:
            if block == self.fruit.pos:
                self.fruit.randomize()

    def check_fail(self):  # Check if the snake is outside of the screen or if it hits itself
        # If the snake head is outside of the screen
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()  # The game ends
            self.snake.play_game_over_sound()  # Play the game over sound

        # If the snake head touches the snake body
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()  # The game ends

    def game_over(self):  # Ends the game
        self.snake.reset()  # Resets the game

    def draw_grass(self):  # Create the grass
        grass_color = (25, 25, 25)  # Set the grass color
        for row in range(cell_number):
            if row % 2 == 0:
                for col in range(cell_number):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size)  # Create a rectangle for the grass (x,y,width,height)
                        # Draw the grass rectangle on the screen
                        pygame.draw.rect(screen, grass_color, grass_rect)
            else:
                for col in range(cell_number):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(
                            col * cell_size, row * cell_size, cell_size, cell_size)
                        pygame.draw.rect(screen, grass_color, grass_rect)

    def draw_score(self):  # Draw the score
        # Set the score text to the length of the snake body minus 3 (the initial snake body)
        score_text = str(len(self.snake.body) - 3)
        # Create a score surface (text,anti-aliasing,color)
        score_surface = game_font.render(score_text, True, (255, 255, 255))
        # Set the x coordinate for the score
        score_x = int(cell_size * cell_number - 30)
        # Set the y coordinate for the score
        score_y = int(cell_size * cell_number - 40)
        score_rect = score_surface.get_rect(  # Create a rectangle for the score
            center=(score_x, score_y))  # Set the center of the rectangle to the score coordinates
        # Create a rectangle for the banana to the left of the score rectangle
        banana_rect = banana.get_rect(
            midright=(score_rect.left, score_rect.centery))
        # Create a rectangle for the background of the score and the banana rectangles (x,y,width,height)
        bg_rect = pygame.Rect(banana_rect.left, banana_rect.top,
                              banana_rect.width + score_rect.width + 5, banana_rect.height + 2)

        # Draw the background rectangle on the screen
        pygame.draw.rect(screen, (65, 65, 65), bg_rect)
        # Draw the score surface on the screen
        screen.blit(score_surface, (score_rect))
        # Draw the banana surface on the screen
        screen.blit(banana, banana_rect)
        # Draw a border around the score and banana rectangles
        pygame.draw.rect(screen, (255, 255, 255), bg_rect, 2)


# Initialize the mixer to play sounds on time
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()  # Initialize pygame
cell_size = 40  # Cell size for the snake body parts and the fruit is set to 40 pixels
cell_number = 20  # Number of cells in the game is set to 20 cells (800 pixels)
screen = pygame.display.set_mode(
    (cell_number*cell_size, cell_number*cell_size))  # Create screen object
clock = pygame.time.Clock()  # Create clock to control the framerate

# Graphics (can be found in the graphics folder in the repository)
banana = pygame.image.load(
    'Snake Game/Graphics/banana.png').convert_alpha()  # banana image
banana = pygame.transform.scale(banana, (40, 40))  # Scale the banana image

# Font
# Set the font and the font size
game_font = pygame.font.Font('Snake Game/Font/retro.ttf', 40)


SCREEN_UPDATE = pygame.USEREVENT  # Create a user event for the screen update

# Set the screen update time to every 100 milliseconds
pygame.time.set_timer(SCREEN_UPDATE, 100)


main_game = MAIN()  # Create a main game object from the main class


# Event loop
while True:
    for event in pygame.event.get():  # Get events

        if event.type == pygame.QUIT:  # If the event is quit
            pygame.quit()  # Quit pygame
            sys.exit()  # Exit the program

        if event.type == SCREEN_UPDATE:  # If the event is the screen update event
            main_game.update()  # Update the game to move the snake

        # Movement keys
        if event.type == pygame.KEYDOWN:  # If a key is pressed down

            # If the key is the up arrow key
            if event.key == pygame.K_UP:  # If the up key is pressed
                # If the snake is not moving down (prevents the snake from itself)
                if main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(
                        0, -1)  # Set the snake direction to up

            # If the key is the down arrow key
            if event.key == pygame.K_DOWN:  # If the down key is pressed
                # If the snake is not moving up (prevents the snake from itself)
                if main_game.snake.direction.y != -1:
                    # Set the snake direction to down
                    main_game.snake.direction = Vector2(0, 1)

            # If the key is the left arrow key
            if event.key == pygame.K_LEFT:  # If the left key is pressed
                # If the snake is not moving right (prevents the snake from itself)
                if main_game.snake.direction.x != 1:
                    # Set the snake direction to left
                    main_game.snake.direction = Vector2(-1, 0)

            # If the key is the right arrow key
            if event.key == pygame.K_RIGHT:  # If the right key is pressed
                # If the snake is not moving left (prevents the snake from itself)
                if main_game.snake.direction.x != -1:
                    # Set the snake direction to right
                    main_game.snake.direction = Vector2(1, 0)

    screen.fill((0, 0, 0))  # Fill the screen with a color

    main_game.draw_elements()  # Draw the game elements (snake and fruit)

    # Displays information on the screen
    pygame.display.update()

    # Set the framerate to the supported refresh rate of your monitor (In my case 180 Hz)
    clock.tick(180)
