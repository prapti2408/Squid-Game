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



