
#     screen.blit(background_image, (0, 0))
#     draw_text("Do you want to play again?", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
#     draw_text("Yes (Y) / No (N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     player_position = 0
#                     game_over = False
#                     win = False
#                     current_bridge = "left"
#                     defective_blocks = random.sample(range(bridge_length), 3)
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

# import pygame
# import random
# import sys
# import time

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load images
# try:
#     background_image = pygame.image.load("background.jpg")  # Replace with your background image
#     player_image = pygame.image.load("player.jpg")          # Replace with your player image
#     player_image.set_colorkey((255, 255, 255))  # Remove white background from player image
# except Exception as e:
#     print(f"Error loading images: {e}")
#     sys.exit()

# # Scale images if necessary
# background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
# player_image = pygame.transform.scale(player_image, (50, 100))

# # Load music
# try:
#     pygame.mixer.music.load("start_music.mp3")  # Replace with your start screen music
# except Exception as e:
#     print(f"Error loading music: {e}")

# # Game variables
# bridge_length = 10
# block_width = 80  # Increased block width
# block_height = 40  # Increased block height
# block_spacing = 20  # Space between blocks

# # Function to draw the bridges
# def draw_bridges():
#     # Left bridge
#     for i in range(bridge_length):
#         block_rect = pygame.Rect(100 + i * (block_width + block_spacing), 400, block_width, block_height)
#         pygame.draw.rect(screen, GREY, block_rect)
    
#     # Right bridge
#     for i in range(bridge_length):
#         block_rect = pygame.Rect(SCREEN_WIDTH - 300 + i * (block_width + block_spacing), 400, block_width, block_height)
#         pygame.draw.rect(screen, GREY, block_rect)

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     pygame.mixer.music.play(-1)  # Loop start music
#     screen.blit(background_image, (0, 0))
#     draw_text("Click here to start playing", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False
#     pygame.mixer.music.stop()

# # Main game loop
# def game_loop():
#     global game_over, win, start_time

#     # Initialize game variables
#     defective_blocks = random.sample(range(bridge_length), 3)  # Defective blocks (hidden)
#     player_position = 0
#     current_bridge = "left"  # Player starts on the left bridge
#     game_over = False
#     win = False
#     start_time = time.time()  # Start the timer

#     pygame.mixer.music.load("game_music.mp3")
#     pygame.mixer.music.play(-1)  # Loop game music

#     while not game_over:
#         screen.blit(background_image, (0, 0))
#         draw_bridges()

#         # Draw player
#         if current_bridge == "left":
#             player_x = 100 + player_position * (block_width + block_spacing) + (block_width - 50) // 2
#         else:
#             player_x = SCREEN_WIDTH - 300 + player_position * (block_width + block_spacing) + (block_width - 50) // 2
#         player_y = 400 - block_height - 10
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time: {30 - elapsed_time}"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         # Check if time is up
#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 # Get mouse position
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 # Check if a block on the left bridge is clicked
#                 for i in range(bridge_length):
#                     block_rect = pygame.Rect(100 + i * (block_width + block_spacing), 400, block_width, block_height)
#                     if block_rect.collidepoint(mouse_x, mouse_y) and current_bridge == "left":
#                         player_position = i
#                         if player_position in defective_blocks:
#                             game_over = True
#                             win = False
#                         if player_position == bridge_length - 1:
#                             game_over = True
#                             win = True
#                 # Check if a block on the right bridge is clicked
#                 for i in range(bridge_length):
#                     block_rect = pygame.Rect(SCREEN_WIDTH - 300 + i * (block_width + block_spacing), 400, block_width, block_height)
#                     if block_rect.collidepoint(mouse_x, mouse_y) and current_bridge == "right":
#                         player_position = i
#                         if player_position in defective_blocks:
#                             game_over = True
#                             win = False
#                         if player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.blit(background_image, (0, 0))
#     if win:
#         draw_text("YOU WIN", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOST", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.blit(background_image, (0, 0))
#     draw_text("Do you want to play again?", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
#     draw_text("Yes (Y) / No (N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

# import pygame
# import random
# import sys
# import time

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 800
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load images
# try:
#     background_image = pygame.image.load("background.jpg")  # Replace with your background image
#     player_image = pygame.image.load("player.jpg")          # Replace with your player image
#     player_image.set_colorkey((255, 255, 255))  # Remove white background from player image
# except Exception as e:
#     print(f"Error loading images: {e}")
#     sys.exit()

# # Scale images if necessary
# background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
# player_image = pygame.transform.scale(player_image, (50, 100))

# # Load music
# try:
#     pygame.mixer.music.load("start_music.mp3")  # Replace with your start screen music
# except Exception as e:
#     print(f"Error loading music: {e}")

# # Game variables
# bridge_length = 10  # Number of blocks per bridge
# block_width = 100  # Increased block width
# block_height = 100  # Increased block height
# block_spacing = 20  # Space between blocks

# # Function to draw the bridges
# def draw_bridges():
#     # Left bridge
#     for i in range(bridge_length):
#         block_rect = pygame.Rect(50 + i * (block_width + block_spacing), 400, block_width, block_height)
#         pygame.draw.rect(screen, GREY, block_rect)
    
#     # Right bridge
#     for i in range(bridge_length):
#         block_rect = pygame.Rect(SCREEN_WIDTH - 550 + i * (block_width + block_spacing), 400, block_width, block_height)
#         pygame.draw.rect(screen, GREY, block_rect)

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     pygame.mixer.music.play(-1)  # Loop start music
#     screen.blit(background_image, (0, 0))
#     draw_text("Click here to start playing", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False
#     pygame.mixer.music.stop()

# # Main game loop
# def game_loop():
#     global game_over, win, start_time

#     # Initialize game variables
#     defective_blocks = random.sample(range(bridge_length), 3)  # Defective blocks (hidden)
#     player_position = 0
#     current_bridge = "left"  # Player starts on the left bridge
#     game_over = False
#     win = False
#     start_time = time.time()  # Start the timer

#     pygame.mixer.music.load("game_music.mp3")
#     pygame.mixer.music.play(-1)  # Loop game music

#     while not game_over:
#         screen.blit(background_image, (0, 0))
#         draw_bridges()

#         # Draw player
#         if current_bridge == "left":
#             player_x = 50 + player_position * (block_width + block_spacing) + (block_width - 50) // 2
#         else:
#             player_x = SCREEN_WIDTH - 550 + player_position * (block_width + block_spacing) + (block_width - 50) // 2
#         player_y = 400 - block_height - 10
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time: {30 - elapsed_time}"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         # Check if time is up
#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 # Get mouse position
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 # Check if a block on the left bridge is clicked
#                 for i in range(bridge_length):
#                     block_rect = pygame.Rect(50 + i * (block_width + block_spacing), 400, block_width, block_height)
#                     if block_rect.collidepoint(mouse_x, mouse_y) and current_bridge == "left":
#                         player_position = i
#                         if player_position in defective_blocks:
#                             game_over = True
#                             win = False
#                         if player_position == bridge_length - 1:
#                             game_over = True
#                             win = True
#                 # Check if a block on the right bridge is clicked
#                 for i in range(bridge_length):
#                     block_rect = pygame.Rect(SCREEN_WIDTH - 550 + i * (block_width + block_spacing), 400, block_width, block_height)
#                     if block_rect.collidepoint(mouse_x, mouse_y) and current_bridge == "right":
#                         player_position = i
#                         if player_position in defective_blocks:
#                             game_over = True
#                             win = False
#                         if player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.blit(background_image, (0, 0))
#     if win:
#         draw_text("YOU WIN", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOST", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.blit(background_image, (0, 0))
#     draw_text("Do you want to play again?", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50)
#     draw_text("Yes (Y) / No (N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

# import pygame
# import random
# import sys
# import time

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1000
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load images
# try:
#     background_image = pygame.image.load("background.jpg")
#     player_image = pygame.image.load("player.jpg")
#     player_image.set_colorkey((255, 255, 255))  # Remove white background
# except Exception as e:
#     print(f"Error loading images: {e}")
#     sys.exit()

# # Scale images
# background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
# player_image = pygame.transform.scale(player_image, (70, 120))

# # Game variables
# bridge_length = 10  # Number of blocks per bridge
# block_width = 120  # Bigger blocks
# block_height = 120
# block_spacing = 30  # Space between blocks

# left_bridge_x = 150
# right_bridge_x = 550
# bridge_y = 350

# # Generate defective blocks
# defective_blocks_left = set(random.sample(range(bridge_length), 3))
# defective_blocks_right = set(random.sample(range(bridge_length), 3))

# # Function to draw the bridges
# def draw_bridges():
#     for i in range(bridge_length):
#         left_block = pygame.Rect(left_bridge_x + i * (block_width + block_spacing), bridge_y, block_width, block_height)
#         right_block = pygame.Rect(right_bridge_x + i * (block_width + block_spacing), bridge_y, block_width, block_height)
#         pygame.draw.rect(screen, GREY, left_block)
#         pygame.draw.rect(screen, GREY, right_block)

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     screen.blit(background_image, (0, 0))
#     draw_text("Click to start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Main game loop
# def game_loop():
#     player_position = (0, "left")  # (index, bridge)
#     game_over = False
#     win = False
#     start_time = time.time()

#     while not game_over:
#         screen.blit(background_image, (0, 0))
#         draw_bridges()

#         # Draw player
#         position_index, bridge = player_position
#         if bridge == "left":
#             player_x = left_bridge_x + position_index * (block_width + block_spacing) + (block_width - 70) // 2
#         else:
#             player_x = right_bridge_x + position_index * (block_width + block_spacing) + (block_width - 70) // 2
#         player_y = bridge_y - block_height - 20
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time Left: {30 - elapsed_time}s"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()

#                 for i in range(bridge_length):
#                     left_block = pygame.Rect(left_bridge_x + i * (block_width + block_spacing), bridge_y, block_width, block_height)
#                     right_block = pygame.Rect(right_bridge_x + i * (block_width + block_spacing), bridge_y, block_width, block_height)

#                     if left_block.collidepoint(mouse_x, mouse_y):
#                         player_position = (i, "left")
#                         if i in defective_blocks_left:
#                             game_over = True
#                             win = False
#                         elif i == bridge_length - 1:
#                             game_over = True
#                             win = True

#                     if right_block.collidepoint(mouse_x, mouse_y):
#                         player_position = (i, "right")
#                         if i in defective_blocks_right:
#                             game_over = True
#                             win = False
#                         elif i == bridge_length - 1:
#                             game_over = True
#                             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.blit(background_image, (0, 0))
#     if win:
#         draw_text("YOU WIN!", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOSE!", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.blit(background_image, (0, 0))
#     draw_text("Play again? (Y/N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

# import pygame
# import random
# import sys
# import time

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1200
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load images
# background_image = pygame.image.load("background.jpg")
# # background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
# background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# # background_image.fill(BLACK)

# # Game variables
# bridge_length = 20  # Number of blocks per bridge
# block_width = 100  # Block size
# block_height = 100
# block_spacing = 20  # Space between blocks

# # Lane positions
# left_bridge_x = 300
# right_bridge_x = 600
# bridge_y = 150

# # Generate defective blocks
# defective_blocks_left = set(random.sample(range(bridge_length), 3))
# defective_blocks_right = set(random.sample(range(bridge_length), 3))

# # Function to draw the bridges
# def draw_bridges():
#     for i in range(bridge_length):
#         left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, left_block)
#         pygame.draw.rect(screen, GREY, right_block)

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     screen.blit(background_image, (0, 0))
#     draw_text("Click to start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Main game loop
# def game_loop():
#     player_position = (0, "left")  # (index, bridge)
#     game_over = False
#     win = False
#     start_time = time.time()

#     while not game_over:
#         screen.blit(background_image, (0, 0))
#         draw_bridges()

#         # Draw player
#         position_index, bridge = player_position
#         if bridge == "left":
#             player_x = left_bridge_x + (block_width - 40) // 2
#         else:
#             player_x = right_bridge_x + (block_width - 40) // 2
#         player_y = bridge_y + position_index * (block_height + block_spacing) + (block_height - 40) // 2
#         pygame.draw.circle(screen, GREEN, (player_x + 20, player_y + 20), 20)

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time Left: {30 - elapsed_time}s"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()

#                 for i in range(bridge_length):
#                     left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#                     right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)

#                     if left_block.collidepoint(mouse_x, mouse_y):
#                         player_position = (i, "left")
#                         if i in defective_blocks_left:
#                             game_over = True
#                             win = False
#                         elif i == bridge_length - 1:
#                             game_over = True
#                             win = True

#                     if right_block.collidepoint(mouse_x, mouse_y):
#                         player_position = (i, "right")
#                         if i in defective_blocks_right:
#                             game_over = True
#                             win = False
#                         elif i == bridge_length - 1:
#                             game_over = True
#                             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.blit(background_image, (0, 0))
#     if win:
#         draw_text("YOU WIN!", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOSE!", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.blit(background_image, (0, 0))
#     draw_text("Play again? (Y/N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

# import pygame
# import random
# import sys
# import time

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1200
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load images
# background_image = pygame.image.load("background.jpg")
# background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
# player_image = pygame.image.load("player.jpg")
# player_image = pygame.transform.scale(player_image, (40, 40))

# # Game variables
# bridge_length = 10  # Number of blocks per bridge
# block_width = 100  # Block size
# block_height = 100
# block_spacing = 20  # Space between blocks

# # Lane positions
# left_bridge_x = 300
# right_bridge_x = 600
# bridge_y = 150

# # Generate defective blocks
# defective_blocks_left = set(random.sample(range(bridge_length), 3))
# defective_blocks_right = set(random.sample(range(bridge_length), 3))

# # Function to draw the bridges
# def draw_bridges():
#     for i in range(bridge_length):
#         left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, left_block)
#         pygame.draw.rect(screen, GREY, right_block)

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     screen.blit(background_image, (0, 0))
#     draw_text("Click to start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Main game loop
# def game_loop():
#     player_position = (0, "left")  # (index, bridge)
#     game_over = False
#     win = False
#     start_time = time.time()

#     while not game_over:
#         screen.blit(background_image, (0, 0))
#         draw_bridges()

#         # Draw player
#         position_index, bridge = player_position
#         if bridge == "left":
#             player_x = left_bridge_x + (block_width - 40) // 2
#         else:
#             player_x = right_bridge_x + (block_width - 40) // 2
#         player_y = bridge_y + position_index * (block_height + block_spacing) + (block_height - 40) // 2
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time Left: {30 - elapsed_time}s"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 for i in range(bridge_length):
#                     left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#                     right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)

#                     if left_block.collidepoint(mouse_x, mouse_y):
#                         player_position = (i, "left")
#                         if i in defective_blocks_left:
#                             game_over = True
#                             win = False
#                         elif i == bridge_length - 1:
#                             game_over = True
#                             win = True

#                     if right_block.collidepoint(mouse_x, mouse_y):
#                         player_position = (i, "right")
#                         if i in defective_blocks_right:
#                             game_over = True
#                             win = False
#                         elif i == bridge_length - 1:
#                             game_over = True
#                             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.blit(background_image, (0, 0))
#     if win:
#         draw_text("YOU WIN!", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOSE!", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.blit(background_image, (0, 0))
#     draw_text("Play again? (Y/N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()
# import pygame
# import random
# import sys
# import time

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1200
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load images
# background_image = pygame.image.load("background.jpg")
# background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
# player_image = pygame.image.load("player.jpg")
# player_image = pygame.transform.scale(player_image, (40, 40))

# # Game variables
# bridge_length = 10  # Number of blocks per bridge
# block_width = 100  # Block size
# block_height = 100
# block_spacing = 20  # Space between blocks

# # Lane positions
# left_bridge_x = 300
# right_bridge_x = 600
# bridge_y = 150

# # Generate defective blocks
# defective_blocks_left = set(random.sample(range(bridge_length), 3))  # 3 defective blocks on the left bridge
# defective_blocks_right = set(random.sample(range(bridge_length), 3))  # 3 defective blocks on the right bridge

# # Function to draw the bridges
# def draw_bridges():
#     for i in range(bridge_length):
#         # Left bridge
#         left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, left_block)
#         # Right bridge
#         right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, right_block)

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     screen.blit(background_image, (0, 0))
#     draw_text("Click to start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Main game loop
# def game_loop():
#     player_position = 0  # Current block index
#     current_bridge = "left"  # Current bridge ("left" or "right")
#     game_over = False
#     win = False
#     start_time = time.time()

#     while not game_over:
#         screen.blit(background_image, (0, 0))
#         draw_bridges()

#         # Draw player
#         if current_bridge == "left":
#             player_x = left_bridge_x + (block_width - 40) // 2
#         else:
#             player_x = right_bridge_x + (block_width - 40) // 2
#         player_y = bridge_y + player_position * (block_height + block_spacing) + (block_height - 40) // 2
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time Left: {30 - elapsed_time}s"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         # Check if time is up
#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 # Check if the player clicked on the next block on either bridge
#                 if player_position < bridge_length - 1:
#                     # Left bridge next block
#                     left_block = pygame.Rect(left_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if left_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "left"
#                         if player_position in defective_blocks_left:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#                     # Right bridge next block
#                     right_block = pygame.Rect(right_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if right_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "right"
#                         if player_position in defective_blocks_right:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.blit(background_image, (0, 0))
#     if win:
#         draw_text("YOU WIN!", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOSE!", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.blit(background_image, (0, 0))
#     draw_text("Play again? (Y/N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

# import pygame
# import random
# import sys
# import time

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1200
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load images
# background_image = pygame.image.load("background.jpg")
# background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
# player_image = pygame.image.load("player.jpg")
# player_image = pygame.transform.scale(player_image, (40, 40))

# # Game variables
# bridge_length = 10  # Number of blocks per bridge
# block_width = 80  # Block size
# block_height = 80
# block_spacing = 20  # Space between blocks

# # Lane positions
# left_bridge_x = 300
# right_bridge_x = 600
# bridge_y = 150

# # Generate defective blocks
# defective_blocks_left = set(random.sample(range(bridge_length), 3))  # 3 defective blocks on the left bridge
# defective_blocks_right = set(random.sample(range(bridge_length), 3))  # 3 defective blocks on the right bridge

# # Function to draw the bridges
# def draw_bridges():
#     for i in range(bridge_length):
#         # Left bridge
#         left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, left_block)
#         # Right bridge
#         right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, right_block)

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     screen.blit(background_image, (0, 0))
#     draw_text("Click to start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Main game loop
# def game_loop():
#     player_position = 0  # Current block index
#     current_bridge = "left"  # Current bridge ("left" or "right")
#     game_over = False
#     win = False
#     start_time = time.time()

#     while not game_over:
#         screen.blit(background_image, (0, 0))
#         draw_bridges()

#         # Draw player
#         if current_bridge == "left":
#             player_x = left_bridge_x + (block_width - 40) // 2
#         else:
#             player_x = right_bridge_x + (block_width - 40) // 2
#         player_y = bridge_y + player_position * (block_height + block_spacing) + (block_height - 40) // 2
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time Left: {30 - elapsed_time}s"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         # Check if time is up
#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 # Check if the player clicked on the next block on either bridge
#                 if player_position < bridge_length - 1:
#                     # Left bridge next block
#                     left_block = pygame.Rect(left_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if left_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "left"
#                         if player_position in defective_blocks_left:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#                     # Right bridge next block
#                     right_block = pygame.Rect(right_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if right_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "right"
#                         if player_position in defective_blocks_right:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.blit(background_image, (0, 0))
#     if win:
#         draw_text("YOU WIN!", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOSE!", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.blit(background_image, (0, 0))
#     draw_text("Play again? (Y/N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()
# import pygame
# import random
# import sys
# import time

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1800
# SCREEN_HEIGHT = 800
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load images
# background_image = pygame.image.load("public.webp")
# background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
# player_image = pygame.image.load("player.jpg")
# player_image = pygame.transform.scale(player_image, (40, 40))

# # Game variables
# bridge_length = 6 # Number of blocks per bridge
# block_width = 80  # Block size
# block_height = 80
# block_spacing = 20  # Space between blocks

# # Lane positions
# left_bridge_x = 300
# right_bridge_x = 600
# bridge_y = 150

# # Generate defective blocks
# # defective_blocks_left = set(random.sample(range(bridge_length), 2))  # 3 defective blocks on the left bridge
# # defective_blocks_right = set(random.sample(range(bridge_length), 2))  # 3 defective blocks on the right bridge
# # Generate defective blocks ensuring no overlap
# defective_blocks_left = set(random.sample(range(bridge_length), 2))  # 3 defective blocks on the left bridge

# # Generate defective blocks for the right bridge, avoiding duplicates
# available_blocks_right = list(set(range(bridge_length)) - defective_blocks_left)  # Exclude left bridge defective blocks
# defective_blocks_right = set(random.sample(available_blocks_right, 2))  # Pick 3 unique blocks from remaining ones
# print(defective_blocks_left)
# print(defective_blocks_right)

# # Function to draw the bridges
# def draw_bridges():
#     for i in range(bridge_length):
#         # Left bridge
#         left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, left_block)
#         # Right bridge
#         right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, right_block)

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     screen.blit(background_image, (0, 0))
#     draw_text("Click to start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Main game loop
# def game_loop():
#     player_position = 0  # Current block index
#     current_bridge = "left"  # Current bridge ("left" or "right")
#     game_over = False
#     win = False
#     start_time = time.time()

#     while not game_over:
#         screen.blit(background_image, (0, 0))
#         draw_bridges()

#         # Draw player
#         if current_bridge == "left":
#             player_x = left_bridge_x + (block_width - 40) // 2
#         else:
#             player_x = right_bridge_x + (block_width - 40) // 2
#         player_y = bridge_y + player_position * (block_height + block_spacing) + (block_height - 40) // 2
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time Left: {30 - elapsed_time}s"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         # Check if time is up
#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 # Check if the player clicked on the next block on either bridge
#                 if player_position < bridge_length - 1:
#                     # Left bridge next block
#                     left_block = pygame.Rect(left_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if left_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "left"
#                         if player_position in defective_blocks_left:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#                     # Right bridge next block
#                     right_block = pygame.Rect(right_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if right_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "right"
#                         if player_position in defective_blocks_right:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#         # Check if the player has reached the last block
#         if player_position == bridge_length - 1:
#             game_over = True
#             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.blit(background_image, (0, 0))
#     if win:
#         draw_text("YOU WIN!", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOSE!", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.blit(background_image, (0, 0))
#     draw_text("Play again? (Y/N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

# import pygame
# import random
# import sys
# import time
# import cv2
# import mediapipe as mp

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1800
# SCREEN_HEIGHT = 800
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load images
# background_image = pygame.image.load("public.webp")
# background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
# player_image = pygame.image.load("player.jpg")
# player_image = pygame.transform.scale(player_image, (40, 40))

# # Game variables
# bridge_length = 6
# block_width = 80
# block_height = 80
# block_spacing = 20

# left_bridge_x = 300
# right_bridge_x = 600
# bridge_y = 150

# defective_blocks_left = set(random.sample(range(bridge_length), 2))
# available_blocks_right = list(set(range(bridge_length)) - defective_blocks_left)
# defective_blocks_right = set(random.sample(available_blocks_right, 2))

# # OpenCV setup
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)
# cap = cv2.VideoCapture(0)

# def draw_bridges():
#     for i in range(bridge_length):
#         pygame.draw.rect(screen, GREY, (left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height))
#         pygame.draw.rect(screen, GREY, (right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height))

# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# def get_hand_position():
#     ret, frame = cap.read()
#     if not ret:
#         return None
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = hands.process(rgb_frame)
#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             x = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * SCREEN_WIDTH)
#             y = int(hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * SCREEN_HEIGHT)
#             return x, y
#     return None

# def game_loop():
#     player_position = 0
#     current_bridge = "left"
#     game_over = False
#     win = False
#     start_time = time.time()

#     while not game_over:
#         screen.blit(background_image, (0, 0))
#         draw_bridges()
#         player_x = left_bridge_x if current_bridge == "left" else right_bridge_x
#         player_y = bridge_y + player_position * (block_height + block_spacing)
#         screen.blit(player_image, (player_x, player_y))
#         draw_text(f"Time Left: {30 - int(time.time() - start_time)}s", small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         if int(time.time() - start_time) >= 30:
#             game_over = True
#             win = False

#         hand_pos = get_hand_position()
#         if hand_pos:
#             x, y = hand_pos
#             if player_position < bridge_length - 1:
#                 left_block = pygame.Rect(left_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                 right_block = pygame.Rect(right_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
                
#                 if left_block.collidepoint(x, y):
#                     player_position += 1
#                     current_bridge = "left"
#                     if player_position in defective_blocks_left:
#                         game_over = True
#                         win = False
#                     elif player_position == bridge_length - 1:
#                         game_over = True
#                         win = True

#                 elif right_block.collidepoint(x, y):
#                     player_position += 1
#                     current_bridge = "right"
#                     if player_position in defective_blocks_right:
#                         game_over = True
#                         win = False
#                     elif player_position == bridge_length - 1:
#                         game_over = True
#                         win = True
        
#         pygame.display.flip()

#     screen.blit(background_image, (0, 0))
#     draw_text("YOU WIN!" if win else "YOU LOSE!", font, GREEN if win else RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     screen.blit(background_image, (0, 0))
#     draw_text("Play again? (Y/N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 cap.release()
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     cap.release()
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()
# cap.release()
# cv2.destroyAllWindows()
# import pygame
# import random
# import sys
# import time
# import numpy as np
# from PIL import Image, ImageSequence

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1800
# SCREEN_HEIGHT = 800
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load player image
# player_image = pygame.image.load("player.jpg")
# player_image = pygame.transform.scale(player_image, (40, 40))

# # Game variables
# bridge_length = 6  # Number of blocks per bridge
# block_width = 80  # Block size
# block_height = 80
# block_spacing = 20  # Space between blocks

# # Lane positions
# left_bridge_x = 300
# right_bridge_x = 600
# bridge_y = 150

# # Generate defective blocks
# defective_blocks_left = set(random.sample(range(bridge_length), 2))  # 2 defective blocks on the left bridge
# available_blocks_right = list(set(range(bridge_length)) - defective_blocks_left)  # Exclude left bridge defective blocks
# defective_blocks_right = set(random.sample(available_blocks_right, 2))  # Pick 2 unique blocks from remaining ones

# # Load .webp file using Pillow
# webp_image = Image.open("public.webp")
# frames = []
# for frame in ImageSequence.Iterator(webp_image):
#     frame = frame.convert("RGBA")  # Ensure the frame has an alpha channel
#     frame = frame.resize((SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize to screen dimensions
#     frame = np.array(frame)  # Convert to a NumPy array
#     frame = pygame.surfarray.make_surface(frame)  # Convert to a Pygame surface
#     frames.append(frame)

# # Function to draw the bridges
# def draw_bridges():
#     for i in range(bridge_length):
#         # Left bridge
#         left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, left_block)
#         # Right bridge
#         right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, right_block)

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     screen.fill(BLACK)
#     draw_text("Click to start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Main game loop
# def game_loop():
#     player_position = 0  # Current block index
#     current_bridge = "left"  # Current bridge ("left" or "right")
#     game_over = False
#     win = False
#     start_time = time.time()
#     frame_index = 0  # Index for cycling through .webp frames

#     while not game_over:
#         # Draw the current frame of the .webp animation
#         screen.blit(frames[frame_index], (0, 0))
#         frame_index = (frame_index + 1) % len(frames)  # Cycle through frames

#         # Draw the bridges
#         draw_bridges()

#         # Draw player
#         if current_bridge == "left":
#             player_x = left_bridge_x + (block_width - 40) // 2
#         else:
#             player_x = right_bridge_x + (block_width - 40) // 2
#         player_y = bridge_y + player_position * (block_height + block_spacing) + (block_height - 40) // 2
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time Left: {30 - elapsed_time}s"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         # Check if time is up
#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 # Check if the player clicked on the next block on either bridge
#                 if player_position < bridge_length - 1:
#                     # Left bridge next block
#                     left_block = pygame.Rect(left_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if left_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "left"
#                         if player_position in defective_blocks_left:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#                     # Right bridge next block
#                     right_block = pygame.Rect(right_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if right_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "right"
#                         if player_position in defective_blocks_right:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#         # Check if the player has reached the last block
#         if player_position == bridge_length - 1:
#             game_over = True
#             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.fill(BLACK)
#     if win:
#         draw_text("YOU WIN!", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOSE!", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.fill(BLACK)
#     draw_text("Play again? (Y/N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

# import pygame
# import random
# import sys
# import time
# import numpy as np
# from PIL import Image, ImageSequence

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1800
# SCREEN_HEIGHT = 800
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load player image
# player_image = pygame.image.load("player.jpg")
# player_image = pygame.transform.scale(player_image, (40, 40))

# # Game variables
# bridge_length = 6  # Number of blocks per bridge
# block_width = 80  # Block size
# block_height = 80
# block_spacing = 20  # Space between blocks

# # Lane positions
# left_bridge_x = 300
# right_bridge_x = 600
# bridge_y = 150

# # Generate defective blocks
# defective_blocks_left = set(random.sample(range(bridge_length), 2))  # 2 defective blocks on the left bridge
# available_blocks_right = list(set(range(bridge_length)) - defective_blocks_left)  # Exclude left bridge defective blocks
# defective_blocks_right = set(random.sample(available_blocks_right, 2))  # Pick 2 unique blocks from remaining ones

# # Load .webp file using Pillow
# webp_image = Image.open("public.webp")
# frames = []
# for frame in ImageSequence.Iterator(webp_image):
#     frame = frame.convert("RGBA")  # Ensure the frame has an alpha channel
#     frame = frame.resize((SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize to screen dimensions
#     frame = np.array(frame)  # Convert to a NumPy array

#     # Ensure the array is in the correct format (3D array with RGB or RGBA data)
#     if frame.ndim == 3 and frame.shape[2] in [3, 4]:  # Check if it's a valid 3D array
#         frame = pygame.surfarray.make_surface(frame)  # Convert to a Pygame surface
#         frames.append(frame)
#     else:
#         print("Invalid frame format. Skipping frame.")

# # Function to draw the bridges
# def draw_bridges():
#     for i in range(bridge_length):
#         # Left bridge
#         left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, left_block)
#         # Right bridge
#         right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, right_block)

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     screen.fill(BLACK)
#     draw_text("Click to start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Main game loop
# def game_loop():
#     player_position = 0  # Current block index
#     current_bridge = "left"  # Current bridge ("left" or "right")
#     game_over = False
#     win = False
#     start_time = time.time()
#     frame_index = 0  # Index for cycling through .webp frames

#     while not game_over:
#         # Draw the current frame of the .webp animation
#         if frames:  # Ensure frames are loaded
#             screen.blit(frames[frame_index], (0, 0))
#             frame_index = (frame_index + 1) % len(frames)  # Cycle through frames

#         # Draw the bridges
#         draw_bridges()

#         # Draw player
#         if current_bridge == "left":
#             player_x = left_bridge_x + (block_width - 40) // 2
#         else:
#             player_x = right_bridge_x + (block_width - 40) // 2
#         player_y = bridge_y + player_position * (block_height + block_spacing) + (block_height - 40) // 2
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time Left: {30 - elapsed_time}s"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         # Check if time is up
#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 # Check if the player clicked on the next block on either bridge
#                 if player_position < bridge_length - 1:
#                     # Left bridge next block
#                     left_block = pygame.Rect(left_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if left_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "left"
#                         if player_position in defective_blocks_left:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#                     # Right bridge next block
#                     right_block = pygame.Rect(right_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if right_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "right"
#                         if player_position in defective_blocks_right:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#         # Check if the player has reached the last block
#         if player_position == bridge_length - 1:
#             game_over = True
#             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.fill(BLACK)
#     if win:
#         draw_text("YOU WIN!", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOSE!", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.fill(BLACK)
#     draw_text("Play again? (Y/N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

# import pygame
# import random
# import sys
# import time
# import numpy as np
# from PIL import Image, ImageSequence

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1200
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load player image
# player_image = pygame.image.load("player.jpg")
# player_image = pygame.transform.scale(player_image, (40, 40))

# # Game variables
# bridge_length = 5  # Number of blocks per bridge
# block_width = 80  # Block size
# block_height = 80
# block_spacing = 20  # Space between blocks

# # Lane positions
# left_bridge_x = 400
# right_bridge_x = 700
# bridge_y = 100

# # Generate defective blocks
# defective_blocks_left = set(random.sample(range(bridge_length), 2))  # 2 defective blocks on the left bridge
# available_blocks_right = list(set(range(bridge_length)) - defective_blocks_left)  # Exclude left bridge defective blocks
# defective_blocks_right = set(random.sample(available_blocks_right, 3))  # Pick 2 unique blocks from remaining ones

# # Load .webp file using Pillow
# webp_image = Image.open("public.webp")
# frames = []
# for frame in ImageSequence.Iterator(webp_image):
#     frame = frame.convert("RGBA")  # Ensure the frame has an alpha channel
#     frame = frame.resize((SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize to screen dimensions
#     frame_data = frame.tobytes()  # Convert frame to bytes
#     frame_surface = pygame.image.fromstring(frame_data, frame.size, "RGBA")  # Convert to Pygame surface
#     frames.append(frame_surface)

# # Function to draw the bridges
# def draw_bridges():
#     for i in range(bridge_length):
#         # Left bridge
#         left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, left_block)
#         # Right bridge
#         right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, right_block)

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     screen.fill(BLACK)
#     draw_text("Click to start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Main game loop
# def game_loop():
#     player_position = 0  # Current block index
#     current_bridge = "left"  # Current bridge ("left" or "right")
#     game_over = False
#     win = False
#     start_time = time.time()
#     frame_index = 0  # Index for cycling through .webp frames

#     while not game_over:
#         # Draw the current frame of the .webp animation
#         if frames:  # Ensure frames are loaded
#             screen.blit(frames[frame_index], (0, 0))
#             frame_index = (frame_index + 1) % len(frames)  # Cycle through frames

#         # Draw the bridges
#         draw_bridges()

#         # Draw player
#         if current_bridge == "left":
#             player_x = left_bridge_x + (block_width - 40) // 2
#         else:
#             player_x = right_bridge_x + (block_width - 40) // 2
#         player_y = bridge_y + player_position * (block_height + block_spacing) + (block_height - 40) // 2
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time Left: {30 - elapsed_time}s"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         # Check if time is up
#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 # Check if the player clicked on the next block on either bridge
#                 if player_position < bridge_length - 1:
#                     # Left bridge next block
#                     left_block = pygame.Rect(left_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if left_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "left"
#                         if player_position in defective_blocks_left:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#                     # Right bridge next block
#                     right_block = pygame.Rect(right_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if right_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "right"
#                         if player_position in defective_blocks_right:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#         # Check if the player has reached the last block
#         if player_position == bridge_length - 1:
#             game_over = True
#             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.fill(BLACK)
#     if win:
#         draw_text("YOU WIN!", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOSE!", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.fill(BLACK)
#     draw_text("Play again? (Y/N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

# import pygame
# import random
# import sys
# import time
# import numpy as np
# from PIL import Image, ImageSequence

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1200
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# YELLOW = (255, 255, 0)  # For block borders

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load player image
# player_image = pygame.image.load("player.jpg")
# player_image = pygame.transform.scale(player_image, (40, 40))

# # Game variables
# bridge_length = 5  # Number of blocks per bridge
# block_width = 80  # Block size
# block_height = 80
# block_spacing = 20  # Space between blocks

# # Lane positions
# left_bridge_x = 400
# right_bridge_x = 700
# bridge_y = 100

# # Generate defective blocks
# defective_blocks_left = set(random.sample(range(bridge_length), 2))  # 2 defective blocks on the left bridge
# available_blocks_right = list(set(range(bridge_length)) - defective_blocks_left)  # Exclude left bridge defective blocks
# defective_blocks_right = set(random.sample(available_blocks_right, 3))  # Pick 2 unique blocks from remaining ones

# # Load .webp file using Pillow
# webp_image = Image.open("public.webp")
# frames = []
# for frame in ImageSequence.Iterator(webp_image):
#     frame = frame.convert("RGBA")  # Ensure the frame has an alpha channel
#     frame = frame.resize((SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize to screen dimensions
#     frame_data = frame.tobytes()  # Convert frame to bytes
#     frame_surface = pygame.image.fromstring(frame_data, frame.size, "RGBA")  # Convert to Pygame surface
#     frames.append(frame_surface)

# # Load music
# pygame.mixer.music.load("start_music.mp3")  # Replace with your music file
# pygame.mixer.music.play(-1)  # Loop the music

# # Function to draw the bridges
# def draw_bridges():
#     for i in range(bridge_length):
#         # Left bridge
#         left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, left_block)
#         pygame.draw.rect(screen, YELLOW, left_block, 3)  # Add border to the block

#         # Right bridge
#         right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, right_block)
#         pygame.draw.rect(screen, YELLOW, right_block, 3)  # Add border to the block

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     screen.fill(BLACK)
#     draw_text("Click to start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Main game loop
# def game_loop():
#     player_position = 0  # Current block index
#     current_bridge = "left"  # Current bridge ("left" or "right")
#     game_over = False
#     win = False
#     start_time = time.time()
#     frame_index = 0  # Index for cycling through .webp frames

#     while not game_over:
#         # Draw the current frame of the .webp animation
#         if frames:  # Ensure frames are loaded
#             screen.blit(frames[frame_index], (0, 0))
#             frame_index = (frame_index + 1) % len(frames)  # Cycle through frames

#         # Draw the bridges
#         draw_bridges()

#         # Draw player
#         if current_bridge == "left":
#             player_x = left_bridge_x + (block_width - 40) // 2
#         else:
#             player_x = right_bridge_x + (block_width - 40) // 2
#         player_y = bridge_y + player_position * (block_height + block_spacing) + (block_height - 40) // 2
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time Left: {30 - elapsed_time}s"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         # Check if time is up
#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 # Check if the player clicked on the next block on either bridge
#                 if player_position < bridge_length - 1:
#                     # Left bridge next block
#                     left_block = pygame.Rect(left_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if left_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "left"
#                         if player_position in defective_blocks_left:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#                     # Right bridge next block
#                     right_block = pygame.Rect(right_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if right_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "right"
#                         if player_position in defective_blocks_right:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#         # Check if the player has reached the last block
#         if player_position == bridge_length - 1:
#             game_over = True
#             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.fill(BLACK)
#     if win:
#         draw_text("YOU WIN!", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOSE!", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.fill(BLACK)
#     draw_text("Play again? (Y/N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

# import pygame
# import random
# import sys
# import time
# import numpy as np
# from PIL import Image, ImageSequence

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1200
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# YELLOW = (255, 255, 0)  # For block borders

# # Fonts
# font = pygame.font.Font(None, 74)
# small_font = pygame.font.Font(None, 50)

# # Load images
# start_background = pygame.image.load("start_background.jpeg")  # Background for the start screen
# end_background = pygame.image.load("end_background.jpg")  # Background for the play-again screen
# player_image = pygame.image.load("player.jpg")
# player_image = pygame.transform.scale(player_image, (40, 40))

# # Game variables
# bridge_length = 5  # Number of blocks per bridge
# block_width = 80  # Block size
# block_height = 80
# block_spacing = 20  # Space between blocks

# # Lane positions
# left_bridge_x = 400
# right_bridge_x = 700
# bridge_y = 100

# # Generate defective blocks
# defective_blocks_left = set(random.sample(range(bridge_length), 2))  # 2 defective blocks on the left bridge
# available_blocks_right = list(set(range(bridge_length)) - defective_blocks_left)  # Exclude left bridge defective blocks
# defective_blocks_right = set(random.sample(available_blocks_right, 3))  # Pick 2 unique blocks from remaining ones

# # Load .webp file using Pillow
# webp_image = Image.open("public.webp")
# frames = []
# for frame in ImageSequence.Iterator(webp_image):
#     frame = frame.convert("RGBA")  # Ensure the frame has an alpha channel
#     frame = frame.resize((SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize to screen dimensions
#     frame_data = frame.tobytes()  # Convert frame to bytes
#     frame_surface = pygame.image.fromstring(frame_data, frame.size, "RGBA")  # Convert to Pygame surface
#     frames.append(frame_surface)

# # Load music
# pygame.mixer.music.load("start_music.mp3")  # Replace with your music file
# pygame.mixer.music.play(-1)  # Loop the music

# # Function to draw the bridges
# def draw_bridges():
#     for i in range(bridge_length):
#         # Left bridge
#         left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, left_block)
#         pygame.draw.rect(screen, YELLOW, left_block, 3)  # Add border to the block

#         # Right bridge
#         right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, right_block)
#         pygame.draw.rect(screen, YELLOW, right_block, 3)  # Add border to the block

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     screen.blit(start_background, (0, 0))  # Display the start background image
#     draw_text("Click to start", font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Main game loop
# def game_loop():
#     player_position = 0  # Current block index
#     current_bridge = "left"  # Current bridge ("left" or "right")
#     game_over = False
#     win = False
#     start_time = time.time()
#     frame_index = 0  # Index for cycling through .webp frames

#     while not game_over:
#         # Draw the current frame of the .webp animation
#         if frames:  # Ensure frames are loaded
#             screen.blit(frames[frame_index], (0, 0))
#             frame_index = (frame_index + 1) % len(frames)  # Cycle through frames

#         # Draw the bridges
#         draw_bridges()

#         # Draw player
#         if current_bridge == "left":
#             player_x = left_bridge_x + (block_width - 40) // 2
#         else:
#             player_x = right_bridge_x + (block_width - 40) // 2
#         player_y = bridge_y + player_position * (block_height + block_spacing) + (block_height - 40) // 2
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time Left: {30 - elapsed_time}s"
#         draw_text(timer_text, small_font, WHITE, SCREEN_WIDTH // 2, 50)

#         # Check if time is up
#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 # Check if the player clicked on the next block on either bridge
#                 if player_position < bridge_length - 1:
#                     # Left bridge next block
#                     left_block = pygame.Rect(left_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if left_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "left"
#                         if player_position in defective_blocks_left:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#                     # Right bridge next block
#                     right_block = pygame.Rect(right_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if right_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "right"
#                         if player_position in defective_blocks_right:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#         # Check if the player has reached the last block
#         if player_position == bridge_length - 1:
#             game_over = True
#             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.blit(end_background, (0, 0))  # Display the end background image
#     if win:
#         draw_text("YOU WIN!", font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOSE!", font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.blit(end_background, (0, 0))  # Display the end background image
#     draw_text("Play again? (Y/N)", small_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

# import pygame
# import random
# import sys
# import time
# import numpy as np
# from PIL import Image, ImageSequence

# # Initialize pygame
# pygame.init()

# # Screen dimensions
# SCREEN_WIDTH = 1200
# SCREEN_HEIGHT = 600
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Squid Game: Double Bridge Challenge")

# # Colors
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREY = (128, 128, 128)
# RED = (255, 0, 0)
# GREEN = (0, 255, 0)
# YELLOW = (255, 255, 0)  # For block borders

# # Load spooky fonts
# try:
#     spooky_font = pygame.font.Font("Chiller.ttf", 100)  # Large spooky font
#     small_spooky_font = pygame.font.Font("Chiller.ttf", 80)  # Smaller spooky font
# except FileNotFoundError:
#     print("Spooky font not found. Using default font.")
#     spooky_font = pygame.font.Font(None, 100)  # Fallback to default font
#     small_spooky_font = pygame.font.Font(None, 80)

# # Load images
# # start_background = pygame.image.load("start_background.jpeg") 
#  # Background for the start screen
# start_background = pygame.image.load("start_background.jpeg")
# start_background = pygame.transform.scale(start_background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize to full screen
# end_background = pygame.image.load("end_background.jpg")  # Background for the play-again screen
# player_image = pygame.image.load("player.jpg")
# player_image = pygame.transform.scale(player_image, (40, 40))

# # Game variables
# bridge_length = 5  # Number of blocks per bridge
# block_width = 80  # Block size
# block_height = 80
# block_spacing = 20  # Space between blocks

# # Lane positions
# left_bridge_x = 400
# right_bridge_x = 700
# bridge_y = 100

# # Generate defective blocks
# defective_blocks_left = set(random.sample(range(bridge_length), 2))  # 2 defective blocks on the left bridge
# available_blocks_right = list(set(range(bridge_length)) - defective_blocks_left)  # Exclude left bridge defective blocks
# defective_blocks_right = set(random.sample(available_blocks_right, 3))  # Pick 2 unique blocks from remaining ones

# # Load .webp file using Pillow
# webp_image = Image.open("public.webp")
# frames = []
# for frame in ImageSequence.Iterator(webp_image):
#     frame = frame.convert("RGBA")  # Ensure the frame has an alpha channel
#     frame = frame.resize((SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize to screen dimensions
#     frame_data = frame.tobytes()  # Convert frame to bytes
#     frame_surface = pygame.image.fromstring(frame_data, frame.size, "RGBA")  # Convert to Pygame surface
#     frames.append(frame_surface)

# # Load music
# pygame.mixer.music.load("start_music.mp3")  # Replace with your music file
# pygame.mixer.music.play(-1)  # Loop the music

# # Function to draw the bridges
# def draw_bridges():
#     for i in range(bridge_length):
#         # Left bridge
#         left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, left_block)
#         pygame.draw.rect(screen, YELLOW, left_block, 3)  # Add border to the block

#         # Right bridge
#         right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
#         pygame.draw.rect(screen, GREY, right_block)
#         pygame.draw.rect(screen, YELLOW, right_block, 3)  # Add border to the block

# # Function to display text
# def draw_text(text, font, color, x, y):
#     text_surface = font.render(text, True, color)
#     text_rect = text_surface.get_rect(center=(x, y))
#     screen.blit(text_surface, text_rect)

# # Start screen
# def start_screen():
#     screen.blit(start_background, (0, 0))  # Display the start background image
#     draw_text("Click to start", spooky_font, YELLOW, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 waiting = False

# # Main game loop
# def game_loop():
#     player_position = 0  # Current block index
#     current_bridge = "left"  # Current bridge ("left" or "right")
#     game_over = False
#     win = False
#     start_time = time.time()
#     frame_index = 0  # Index for cycling through .webp frames

#     while not game_over:
#         # Draw the current frame of the .webp animation
#         if frames:  # Ensure frames are loaded
#             screen.blit(frames[frame_index], (0, 0))
#             frame_index = (frame_index + 1) % len(frames)  # Cycle through frames

#         # Draw the bridges
#         draw_bridges()

#         # Draw player
#         if current_bridge == "left":
#             player_x = left_bridge_x + (block_width - 40) // 2
#         else:
#             player_x = right_bridge_x + (block_width - 40) // 2
#         player_y = bridge_y + player_position * (block_height + block_spacing) + (block_height - 40) // 2
#         screen.blit(player_image, (player_x, player_y))

#         # Display timer
#         elapsed_time = int(time.time() - start_time)
#         timer_text = f"Time Left: {30 - elapsed_time}s"
#         draw_text(timer_text, small_spooky_font, WHITE, SCREEN_WIDTH // 2, 50)

#         # Check if time is up
#         if elapsed_time >= 30:
#             game_over = True
#             win = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_x, mouse_y = pygame.mouse.get_pos()
#                 # Check if the player clicked on the next block on either bridge
#                 if player_position < bridge_length - 1:
#                     # Left bridge next block
#                     left_block = pygame.Rect(left_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if left_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "left"
#                         if player_position in defective_blocks_left:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#                     # Right bridge next block
#                     right_block = pygame.Rect(right_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
#                     if right_block.collidepoint(mouse_x, mouse_y):
#                         player_position += 1
#                         current_bridge = "right"
#                         if player_position in defective_blocks_right:
#                             game_over = True
#                             win = False
#                         elif player_position == bridge_length - 1:
#                             game_over = True
#                             win = True

#         # Check if the player has reached the last block
#         if player_position == bridge_length - 1:
#             game_over = True
#             win = True

#         pygame.display.flip()

#     # Display win/lose message
#     screen.blit(end_background, (0, 0))  # Display the end background image
#     if win:
#         draw_text("YOU WIN!", spooky_font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     else:
#         draw_text("YOU LOSE!", spooky_font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()
#     pygame.time.wait(3000)

#     # Play again option
#     screen.blit(end_background, (0, 0))  # Display the end background image
#     draw_text("Play again? (Y/N)", small_spooky_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
#     pygame.display.flip()

#     waiting = True
#     while waiting:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_y:
#                     waiting = False
#                     game_loop()
#                 if event.key == pygame.K_n:
#                     pygame.quit()
#                     sys.exit()

# # Run the game
# start_screen()
# game_loop()

import pygame
import random
import sys
import time
import numpy as np
from PIL import Image, ImageSequence

def run_bridge_game():
    # Initialize pygame
    pygame.init()

    # Screen dimensions
    SCREEN_WIDTH = 1200
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Squid Game: Double Bridge Challenge")

    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    GREY = (128, 128, 128)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)  # For block borders

    # Load spooky fonts
    try:
        spooky_font = pygame.font.Font("Chiller.ttf", 100)  # Large spooky font
        small_spooky_font = pygame.font.Font("Chiller.ttf", 80)  # Smaller spooky font
    except FileNotFoundError:
        print("Spooky font not found. Using default font.")
        spooky_font = pygame.font.Font(None, 100)  # Fallback to default font
        small_spooky_font = pygame.font.Font(None, 80)

    # Load images
    start_background = pygame.image.load("start_background.jpeg")
    start_background = pygame.transform.scale(start_background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize to full screen
    end_background = pygame.image.load("end_background.jpg")  # Background for the play-again screen
    player_image = pygame.image.load("player.jpg")
    player_image = pygame.transform.scale(player_image, (40, 40))

    # Game variables
    bridge_length = 5  # Number of blocks per bridge
    block_width = 80  # Block size
    block_height = 80
    block_spacing = 20  # Space between blocks

    # Lane positions
    left_bridge_x = 400
    right_bridge_x = 700
    bridge_y = 100

    # Generate defective blocks
    defective_blocks_left = set(random.sample(range(bridge_length), 2))  # 2 defective blocks on the left bridge
    available_blocks_right = list(set(range(bridge_length)) - defective_blocks_left)  # Exclude left bridge defective blocks
    defective_blocks_right = set(random.sample(available_blocks_right, 3))  # Pick 2 unique blocks from remaining ones

    # Load .webp file using Pillow
    webp_image = Image.open("public.webp")
    frames = []
    for frame in ImageSequence.Iterator(webp_image):
        frame = frame.convert("RGBA")  # Ensure the frame has an alpha channel
        frame = frame.resize((SCREEN_WIDTH, SCREEN_HEIGHT))  # Resize to screen dimensions
        frame_data = frame.tobytes()  # Convert frame to bytes
        frame_surface = pygame.image.fromstring(frame_data, frame.size, "RGBA")  # Convert to Pygame surface
        frames.append(frame_surface)

    # Load music
    pygame.mixer.music.load("start_music.mp3")  # Replace with your music file
    pygame.mixer.music.play(-1)  # Loop the music

    # Function to draw the bridges
    def draw_bridges():
        for i in range(bridge_length):
            # Left bridge
            left_block = pygame.Rect(left_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
            pygame.draw.rect(screen, GREY, left_block)
            pygame.draw.rect(screen, YELLOW, left_block, 3)  # Add border to the block

            # Right bridge
            right_block = pygame.Rect(right_bridge_x, bridge_y + i * (block_height + block_spacing), block_width, block_height)
            pygame.draw.rect(screen, GREY, right_block)
            pygame.draw.rect(screen, YELLOW, right_block, 3)  # Add border to the block

    # Function to display text
    def draw_text(text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect(center=(x, y))
        screen.blit(text_surface, text_rect)

    # Start screen
    def start_screen():
        screen.blit(start_background, (0, 0))  # Display the start background image
        draw_text("Click to start", spooky_font, YELLOW, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.flip()
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    waiting = False

    # Main game loop
    def game_loop():
        player_position = 0  # Current block index
        current_bridge = "left"  # Current bridge ("left" or "right")
        game_over = False
        win = False
        start_time = time.time()
        frame_index = 0  # Index for cycling through .webp frames

        while not game_over:
            # Draw the current frame of the .webp animation
            if frames:  # Ensure frames are loaded
                screen.blit(frames[frame_index], (0, 0))
                frame_index = (frame_index + 1) % len(frames)  # Cycle through frames

            # Draw the bridges
            draw_bridges()

            # Draw player
            if current_bridge == "left":
                player_x = left_bridge_x + (block_width - 40) // 2
            else:
                player_x = right_bridge_x + (block_width - 40) // 2
            player_y = bridge_y + player_position * (block_height + block_spacing) + (block_height - 40) // 2
            screen.blit(player_image, (player_x, player_y))

            # Display timer
            elapsed_time = int(time.time() - start_time)
            timer_text = f"Time Left: {30 - elapsed_time}s"
            draw_text(timer_text, small_spooky_font, WHITE, SCREEN_WIDTH // 2, 50)

            # Check if time is up
            if elapsed_time >= 30:
                game_over = True
                win = False

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Check if the player clicked on the next block on either bridge
                    if player_position < bridge_length - 1:
                        # Left bridge next block
                        left_block = pygame.Rect(left_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
                        if left_block.collidepoint(mouse_x, mouse_y):
                            player_position += 1
                            current_bridge = "left"
                            if player_position in defective_blocks_left:
                                game_over = True
                                win = False
                            elif player_position == bridge_length - 1:
                                game_over = True
                                win = True

                        # Right bridge next block
                        right_block = pygame.Rect(right_bridge_x, bridge_y + (player_position + 1) * (block_height + block_spacing), block_width, block_height)
                        if right_block.collidepoint(mouse_x, mouse_y):
                            player_position += 1
                            current_bridge = "right"
                            if player_position in defective_blocks_right:
                                game_over = True
                                win = False
                            elif player_position == bridge_length - 1:
                                game_over = True
                                win = True

            # Check if the player has reached the last block
            if player_position == bridge_length - 1:
                game_over = True
                win = True

            pygame.display.flip()

        # Display win/lose message
        screen.blit(end_background, (0, 0))  # Display the end background image
        if win:
            draw_text("YOU WIN!", spooky_font, GREEN, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        else:
            draw_text("YOU LOSE!", spooky_font, RED, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.flip()
        pygame.time.wait(3000)

        # Play again option
        screen.blit(end_background, (0, 0))  # Display the end background image
        draw_text("Play again? (Y/N)", small_spooky_font, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        pygame.display.flip()

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_y:
                        waiting = False
                        game_loop()
                    if event.key == pygame.K_n:
                        pygame.quit()
                        sys.exit()

    # Run the game
    start_screen()
    game_loop()