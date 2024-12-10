# menu.py

import pygame
import sys


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 50)
        self.options = ["Start Game", "Options", "Exit"]
        self.selected = 0
        self.menu_active = True  # Added to control the menu loop

    def display_menu(self):
        while self.menu_active:
            self.screen.fill((0, 0, 0))
            self._handle_events()
            self._draw_menu()
            pygame.display.flip()
            self.clock.tick(60)

    def _handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.selected = (self.selected - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.selected = (self.selected + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    self._execute_option()

    def _draw_menu(self):
        for idx, option in enumerate(self.options):
            color = (255, 255, 0) if idx == self.selected else (255, 255, 255)
            text_surface = self.font.render(option, True, color)
            x = self.screen.get_width() // 2 - text_surface.get_width() // 2
            y = self.screen.get_height() // 2 + idx * 60
            self.screen.blit(text_surface, (x, y))

    def _execute_option(self):
        selected_option = self.options[self.selected]
        if selected_option == "Start Game":
            self.menu_active = False  # Exit the menu loop
        elif selected_option == "Options":
            self._options_menu()
        elif selected_option == "Exit":
            pygame.quit()
            sys.exit()

    def _options_menu(self):
        options_active = True
        back_option = ["Back to Main Menu", "Exit Game"]
        selected = 0

        while options_active:
            self.screen.fill((50, 50, 50))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(back_option)
                    elif event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(back_option)
                    elif event.key == pygame.K_RETURN:
                        if back_option[selected] == "Back to Main Menu":
                            options_active = False
                        elif back_option[selected] == "Exit Game":
                            pygame.quit()
                            sys.exit()

            for idx, option in enumerate(back_option):
                color = (255, 255, 0) if idx == selected else (255, 255, 255)
                text_surface = self.font.render(option, True, color)
                x = self.screen.get_width() // 2 - text_surface.get_width() // 2
                y = self.screen.get_height() // 2 + idx * 60
                self.screen.blit(text_surface, (x, y))

            pygame.display.flip()
            self.clock.tick(60)
