import pygame, sys
from menu import *
from constantes import *

class Gui():
    def __init__(self):
        pygame.init()
        self.largura, self.altura = 1280, 720
        self.screen = pygame.display.set_mode((self.largura, self.altura))
        self.main_menu = MainMenu(self.screen)
        self.how_to_play = HowToMenu(self.screen)
        self.credits = CreditsMenu(self.screen)
        self.map = MapMenu(self.screen)
        self.quit_menu = QuitMenu(self.screen)
        self.menu_atual = self.main_menu

    def game_loop(self, events: list[pygame.event.Event]):
        self.menu_atual.screen.fill('black')
        self.menu_atual.display_menu()
        self.check_events(events)

    def check_events(self, events : list[pygame.event.Event]):
        for event in events:
            if event.type == SHOW_MAP_MENU:
                """ self.menu_atual = self.map
                self.menu_atual.displayMenu() """
                pygame.event.post(pygame.event.Event(START_GAME))
            if event.type == SHOW_MAIN_MENU:
                self.menu_atual = self.main_menu
                self.menu_atual.display_menu()
            if event.type == SHOW_HOW_TO_MENU:
                self.menu_atual = self.how_to_play
                self.menu_atual.display_menu()
            if event.type == SHOW_CREDITS_MENU:
                self.menu_atual = self.credits
                self.menu_atual.display_menu()
            if event.type == QUIT_MENU or event.type == pygame.QUIT:
                self.menu_atual = self.quit_menu
                self.menu_atual.display_menu() 
            if event.type == EXIT:
                pygame.quit()
                sys.exit()

        self.menu_atual.handle_events(events)