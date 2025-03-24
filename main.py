import pygame
from moviepy import*

# Import game functions
from dalgona.dalgona_game import run_dalgona_game
from creepy_doll.creepy_doll_game import run_creepy_doll_game
from bridge.bridge_game import run_bridge_game

# Constants
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 800
WHITE = (255, 255, 255)
PINK = (200, 0, 100)
BUTTON_WIDTH = 250
BUTTON_HEIGHT = 70

# Video position and size
VIDEO_WIDTH = 800
VIDEO_HEIGHT = 500
VIDEO_X = 100
VIDEO_Y = 200

pygame.init()
pygame.mixer.init()  # Initialize the mixer for background music
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Squid Game")
font = pygame.font.Font(None, 40)  # Smaller font for buttons
title_font = pygame.font.Font(None, 100)  # Larger font for the title
description_font = pygame.font.Font(None, 30)  # Font for the description

# Load images
rules_bg = pygame.image.load("rules_bg.png")
rules_bg = pygame.transform.scale(rules_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
games_bg = pygame.image.load("games_bg.png")
games_bg = pygame.transform.scale(games_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))
history_bg = pygame.image.load("history.png")  # Load the history background image
history_bg = pygame.transform.scale(history_bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Load and play background music
pygame.mixer.music.load("mingle.mp3")
pygame.mixer.music.play(-1)  # Play in an infinite loop
def draw_cross_button():
    # Position and size of the circle
    circle_radius = 25
    circle_center = (SCREEN_WIDTH - 100, 90)  # Adjusted position for visibility

    # Draw pink circle
    pygame.draw.circle(screen, PINK, circle_center, circle_radius)

    # Draw white cross inside the circle (tilted lines)
    cross_size = 15  # Size of the cross arms

    # Diagonal line from top-left to bottom-right
    pygame.draw.line(screen, WHITE,
                     (circle_center[0] - cross_size, circle_center[1] - cross_size),  # Top-left
                     (circle_center[0] + cross_size, circle_center[1] + cross_size),  # Bottom-right
                     3)

    # Diagonal line from top-right to bottom-left
    pygame.draw.line(screen, WHITE,
                     (circle_center[0] + cross_size, circle_center[1] - cross_size),  # Top-right
                     (circle_center[0] - cross_size, circle_center[1] + cross_size),  # Bottom-left
                     3)

    # Return the button's rect for click detection
    cross_button_rect = pygame.Rect(circle_center[0] - circle_radius, circle_center[1] - circle_radius,
                                   2 * circle_radius, 2 * circle_radius)
    return cross_button_rect

def draw_button(text, x, y, width, height, color, action=None):
    button_rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, button_rect, border_radius=15)
    text_surf = font.render(text, True, WHITE)
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surf, text_rect)
    return button_rect



def play_video():
    clip = VideoFileClip("cover_video.mp4").resized(height=VIDEO_HEIGHT)
    start_time = pygame.time.get_ticks()
    video_duration = clip.duration

    # Animation variables
    title_x = -500  # Start off-screen
    description_x = SCREEN_WIDTH  # Start off-screen
    button_x = SCREEN_WIDTH  # Start off-screen
    about_button_x = SCREEN_WIDTH  # Start off-screen
    animation_speed = 5  # Speed of sliding animations

    while True:
        current_time = (pygame.time.get_ticks() - start_time) / 1000
        if current_time >= video_duration:
            break

        # Get the current video frame
        frame = clip.get_frame(current_time)
        frame_surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

        # Clear the screen and display the video
        screen.fill((0, 0, 0))  # Black background
        screen.blit(frame_surface, (VIDEO_X, VIDEO_Y))

        # Animate the title sliding in from the left
        if title_x < 100:  # Stop at x = 100
            title_x += animation_speed
        title_text = title_font.render("Squid Games", True, PINK)
        shadow_text = title_font.render("Squid Games", True, WHITE)
        screen.blit(shadow_text, (title_x + 5, 55))  # Shadow effect
        screen.blit(title_text, (title_x, 50))  # Main text

        # Animate the description sliding in from the right
        if description_x > 800:  # Stop at x = 800
            description_x -= animation_speed
        description_lines = [
            "6 games for 42 million dollars,",
            "how long will you live miserable and",
            "you have a valuable opportunity to become one of the richest people? Let's play : ) 🟥🔺🔴"
        ]
        for i, line in enumerate(description_lines):
            description_text = description_font.render(line, True, WHITE)
            screen.blit(description_text, (description_x, 200 + i * 30))

        # Animate the "Start Now" button sliding in from the right
        if button_x > 1100:  # Stop at x = 1100
            button_x -= animation_speed
        start_button = draw_button("START NOW", button_x, 350, 200, 70, PINK)

        # Animate the "About" button sliding in from the right
        if about_button_x > 1100:  # Stop at x = 1100
            about_button_x -= animation_speed
        about_button = draw_button("ABOUT", about_button_x, 450, 200, 70, PINK)

        # Draw cross button (after other elements to ensure visibility)
        cross_button = draw_cross_button()

        pygame.display.flip()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    show_menu()
                    return
                elif about_button.collidepoint(event.pos):
                    show_history()
                    return
                elif cross_button.collidepoint(event.pos):
                    pygame.quit()
                    return

def show_menu():
    running = True
    while running:
        screen.fill((0, 0, 0))  # Black background
        play_button = draw_button("START PLAYING", SCREEN_WIDTH // 2 - 150, 400, 300, 70, PINK)
        rules_button = draw_button("THE LAW", SCREEN_WIDTH // 2 - 150, 500, 300, 70, PINK)

        # Draw cross button (after other elements to ensure visibility)
        cross_button = draw_cross_button()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if rules_button.collidepoint(event.pos):
                    show_rules()
                    return
                elif play_button.collidepoint(event.pos):
                    show_game_selection()
                    return
                elif cross_button.collidepoint(event.pos):
                    pygame.quit()
                    return

def show_rules():
    running = True
    while running:
        screen.blit(rules_bg, (0, 0))
        back_button = draw_button("BACK", 50, 50, 150, 60, PINK)

        # Draw cross button (after other elements to ensure visibility)
        cross_button = draw_cross_button()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    show_menu()
                    return
                elif cross_button.collidepoint(event.pos):
                    pygame.quit()
                    return

def show_game_selection():
    running = True
    while running:
        screen.blit(games_bg, (0, 0))
        dalgona_btn = draw_button("DALGONA CHALLENGE", SCREEN_WIDTH // 2 - 200, 300, 400, 70, PINK)
        bridge_btn = draw_button("BRIDGE CROSS", SCREEN_WIDTH // 2 - 200, 400, 400, 70, PINK)
        doll_btn = draw_button("CREEPY DOLL", SCREEN_WIDTH // 2 - 200, 500, 400, 70, PINK)
        back_button = draw_button("BACK", 50, 50, 150, 60, PINK)

        # Draw cross button (after other elements to ensure visibility)
        cross_button = draw_cross_button()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if dalgona_btn.collidepoint(event.pos):
                    pygame.mixer.music.stop()  # Stop background music
                    if not run_dalgona_game():
                        show_game_selection()  # Redirect to game selection after game ends
                elif bridge_btn.collidepoint(event.pos):
                    pygame.mixer.music.stop()  # Stop background music
                    if not run_bridge_game():  # Start Bridge Cross
                        show_game_selection()  # Redirect to game selection after game ends
                elif doll_btn.collidepoint(event.pos):
                    pygame.mixer.music.stop()  # Stop background music
                    if not run_creepy_doll_game():
                        show_game_selection()  # Redirect to game selection after game ends
                elif back_button.collidepoint(event.pos):
                    show_menu()
                    return
                elif cross_button.collidepoint(event.pos):
                    pygame.quit()
                    return

def show_history():
    running = True
    while running:
        screen.blit(history_bg, (0, 0))  # Blit the image to cover the entire screen
        back_button = draw_button("BACK", 50, 50, 150, 60, PINK)  # Back button

        # Draw cross button (after other elements to ensure visibility)
        cross_button = draw_cross_button()

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    show_menu()
                    return
                elif cross_button.collidepoint(event.pos):
                    pygame.quit()
                    return

if __name__ == "__main__":
    play_video()