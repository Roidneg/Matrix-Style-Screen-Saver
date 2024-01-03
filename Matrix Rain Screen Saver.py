import pygame
import random

pygame.init()

# Set the dimensions of the display window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Set the title of the display window
pygame.display.set_caption("Matrix Code Rain")

# Set the font for the characters
font_size = 18
font = pygame.font.SysFont(None, font_size)

# Set the character set to use (ASCII Characters)
chars = [chr(i) for i in range(33, 127)] + [chr(i) for i in range(65, 91)]
chars += [chr(i) for i in range(0x3040, 0x309F)] # hiragana
chars += [chr(i) for i in range(0x30A0, 0x30FF)] # katakana
chars += [chr(i) for i in range(0x4E00, 0x9FBF)] # kanji

# Set the number of characters to display
num_chars = 550

# Set the speed of the characters
speed = .33

# Set the color of the characters (Green for The Matrix of course!)
color = (28, 161, 82)

# Define the number of columns and the width of each column
num_columns = 20
column_width = window_width // num_columns

# Create a list to store the character positions and initialize them randomly
positions = [(random.randint(0, window_width), random.randint(-1000, 0)) for i in range(num_chars)]

# Create a list of columns, where each column is a list of character positions
columns = [[] for i in range(num_columns)]

# Initialize the character positions randomly in each column
for i in range(num_chars):
    column = random.randint(0, num_columns - 1)
    x = random.randint(column * column_width, (column + 1) * column_width)
    y = random.randint(-1000, 0)
    positions[i] = (x, y)
    columns[column].append(i)

def glitch_text(text, char_set):
    glitched_text = ''
    for char in text:
        if random.random() < 0.1: # 10% chance of glitching a character
            glitched_text += random.choice(char_set + [char])# replace with a random character
        else:
            glitched_text += char
    return glitched_text

# Now in the loop, update the positions of the characters in each column separately
while True:
    # Handle events (e.g. closing the window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Fill the display background as black
    window.fill((0, 0, 0))

    # Draw characters on the screen and update their positions
    for column in columns:
        for i in column:
            # Get the current position of the character
            x, y = positions[i]
            # Add a random offset to the y-position of the character
            y += random.randint(-4, 5)
            # Draw the character on the screen
            text = font.render(glitch_text(random.choice(chars), chars), True, color)
            window.blit(text, (x, y))

            # Update the character's position
            positions[i] = (x, y + speed)

            # If the character has moved off the bottom of the screen, reset its position
            if y > window_height:
                column.remove(i)
                new_column = random.randint(0, num_columns - 1)
                x = random.randint(new_column * column_width, (new_column + 1) * column_width)
                y = random.randint(-1000, 0)
                positions[i] = (x, y)
                columns[new_column].append(i)

    # Update the display
    pygame.display.update()

