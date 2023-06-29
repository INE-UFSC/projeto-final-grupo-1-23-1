import pygame
from button import Button, ImageButton
from pygame import *
from abc import ABC, abstractmethod
from constantes import *
from utils import get_path

class Menu(ABC):
    def __init__(self, screen):
        self.screen = screen
        self.largura = self.screen.get_width()
        self.altura = self.screen.get_height()

    @abstractmethod
    def display_menu(self):
        pass
    
    def set_caption(self, titulo):
        self.titulo = titulo
        pygame.display.set_caption(f"{self.titulo}")

    def set_image(self, width, height, image):
        self.width, self.height = width, height
        self.image = pygame.image.load(f"{image}")
        self.image_rect = self.image.get_rect(center=(self.width, self.height))
        self.screen.blit(self.image, self.image_rect)

    """ def draw_text(self, text, size, width, height):
        font = self.get_font(size)
        text_surface = font.render(text, True, "Yellow")
        text_rect = text_surface.get_rect()
        text_rect.center = (width, height)
        self.screen.blit(text_surface, text_rect) """
    
    def draw_text(self, text_list, size, width, height, new_line = 15):
        font = self.get_font(size)
        self.labels = []
        for line in text_list:
            label = font.render(line, True, "yellow")
            label_rect = label.get_rect(center=(width, height))
            self.labels.append((label, label_rect))
            height += label.get_height() + new_line
        for label, label_rect in self.labels:
            self.screen.blit(label, label_rect)

    def get_font(self, size):
        return pygame.font.Font(get_path('assets', 'font.ttf'), size)
    
    def back_button(self):
        return Button(pos=(self.largura * 0.1, self.altura * 0.92), 
                    text_input="Back", 
                    font=self.get_font(25), 
                    base_color="Yellow", 
                    hovering_color="White")
    
    @abstractmethod
    def handle_events(self):
        pass

class MainMenu(Menu):
    def __init__(self, screen):
        Menu.__init__(self, screen)
        self.set_caption("Main menu")
        
        self.start_button = Button(pos=(self.largura / 2, self.altura * 0.45), 
                            text_input="START GAME", 
                            font=self.get_font(30), 
                            base_color="Yellow", 
                            hovering_color="White")
        self.how_to_play_button = Button(pos=(self.largura / 2, self.altura * 0.55), 
                                text_input="HOW TO PLAY", 
                                font=self.get_font(30), 
                                base_color="Yellow", 
                                hovering_color="White")
        self.credits_button = Button(pos=(self.largura / 2, self.altura * 0.65), 
                                text_input="CREDITS", 
                                font=self.get_font(30), 
                                base_color="Yellow", 
                                hovering_color="White")
        self.quit_button = Button(pos=(self.largura / 2, self.altura * 0.75), 
                                text_input="QUIT", 
                                font=self.get_font(30), 
                                base_color="Yellow", 
                                hovering_color="White")

    def display_menu(self):
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.set_image(self.largura / 2, self.altura * 0.18, get_path('imagens', 'logo.PNG'))
        
        for button in [self.start_button, self.how_to_play_button, self.credits_button, self.quit_button]:
            button.change_color(MENU_MOUSE_POS)
            button.update(self.screen)

        pygame.display.update()

    def handle_events(self, events: list[pygame.event.Event]):
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.start_button.check_for_input(MENU_MOUSE_POS):
                    pygame.event.post(pygame.event.Event(SHOW_MAP_MENU))
                if self.how_to_play_button.check_for_input(MENU_MOUSE_POS):
                    pygame.event.post(pygame.event.Event(SHOW_HOW_TO_MENU))
                if self.credits_button.check_for_input(MENU_MOUSE_POS):
                    pygame.event.post(pygame.event.Event(SHOW_CREDITS_MENU))
                if self.quit_button.check_for_input(MENU_MOUSE_POS):
                    pygame.event.post(pygame.event.Event(QUIT_MENU))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(QUIT_MENU))
            
class MapMenu(Menu):
    def __init__(self, screen):
        Menu.__init__(self, screen)
        self.set_caption("Choose the map")
        self.back = self.back_button()
        self.mansion_button = ImageButton(self.screen, 
                                   get_path('imagens', 'test.png'), 
                                   self.largura * 0.25, 
                                   self.altura / 2, 
                                   "yellow", 
                                   "white", 
                                   1)
        self.football_button = ImageButton(self.screen, 
                                   get_path('imagens', 'test.png'), 
                                   self.largura / 2, 
                                   self.altura / 2, 
                                   "yellow", 
                                   "white", 
                                   1)
        self.transit_button = ImageButton(self.screen, 
                                   get_path('imagens', 'test.png'), 
                                   self.largura * 0.75, 
                                   self.altura / 2, 
                                   "yellow", 
                                   "white", 
                                   1)

    def display_menu(self):
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        self.draw_text(["Choose the map"], 40, self.largura / 2, self.altura * 0.12)
        self.draw_text(["Mansion"], 25, self.largura * 0.25, self.altura * 0.22)
        self.draw_text(["Football"], 25, self.largura / 2, self.altura * 0.22)
        self.draw_text(["Transit"], 25, self.largura * 0.75, self.altura * 0.22)

        for button in [self.mansion_button, self.football_button, self.transit_button, self.back]:
            button.update(self.screen)
            button.change_color(MENU_MOUSE_POS)
        
        pygame.display.update()

    def handle_events(self, events: list[pygame.event.Event]):
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(SHOW_MAIN_MENU))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.mansion_button.check_for_input(MENU_MOUSE_POS):
                    pygame.event.post(pygame.event.Event(MANSION_MAP))
                if self.football_button.check_for_input(MENU_MOUSE_POS):
                    pygame.event.post(pygame.event.Event(FOOTBALL_MAP))
                if self.transit_button.check_for_input(MENU_MOUSE_POS):
                    pygame.event.post(pygame.event.Event(TRANSIT_MAP))
                if self.back.check_for_input(MENU_MOUSE_POS):
                    pygame.event.post(pygame.event.Event(SHOW_MAIN_MENU))

class HowToMenu(Menu):
    def __init__(self, screen):
        Menu.__init__(self, screen)
        self.set_caption("How to Play")
        self.back = self.back_button()

    def display_menu(self):
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        self.draw_text(["How to play"], 30, self.largura / 2, self.altura * 0.12)
        self.set_image(self.largura / 2, self.altura * 0.4, get_path('imagens', 'Arrows.png')) 
        self.draw_text(["Movement"], 20, self.largura / 2, self.altura * 0.55)

        self.back.change_color(MENU_MOUSE_POS)
        self.back.update(self.screen)

        pygame.display.update()

    def handle_events(self, events: list[pygame.event.Event]):
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(SHOW_MAIN_MENU))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back.check_for_input(MENU_MOUSE_POS):
                    pygame.event.post(pygame.event.Event(SHOW_MAIN_MENU))

class CreditsMenu(Menu):
    def __init__(self, screen):
        Menu.__init__(self, screen)
        self.set_caption("Credits")
        self.back = self.back_button()

    def display_menu(self):
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        self.draw_text(["Credits"], 30, self.largura / 2, self.altura * 0.12)
        self.draw_text(['Antônio Escobar', 'Eric Alex', 'João Victor Cabral', 'João Vittor Braz'], 25, self.largura / 2, self.altura * 0.3)

        self.back.change_color(MENU_MOUSE_POS)
        self.back.update(self.screen)

        pygame.display.update()

    def handle_events(self, events: list[pygame.event.Event]):
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(SHOW_MAIN_MENU))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back.check_for_input(MENU_MOUSE_POS):
                    pygame.event.post(pygame.event.Event(SHOW_MAIN_MENU))

class QuitMenu(Menu):
    def __init__(self, screen):
        Menu.__init__(self, screen)
        self.set_caption("Quit game")
        self.yes_button = Button(pos=(self.largura * 0.4, self.altura / 2), 
                    text_input="Yes", 
                    font=self.get_font(25), 
                    base_color="Yellow", 
                    hovering_color="White")
        self.no_button = Button(pos=(self.largura * 0.6, self.altura / 2), 
                    text_input="No", 
                    font=self.get_font(25), 
                    base_color="Yellow", 
                    hovering_color="White")

    def display_menu(self):
        MENU_MOUSE_POS = pygame.mouse.get_pos()

        self.draw_text(["Are you sure you want to quit the game?"], 17, self.largura / 2, self.altura * 0.2)

        for button in [self.yes_button, self.no_button]:
            button.change_color(MENU_MOUSE_POS)
            button.update(self.screen)

        pygame.display.update()

    def handle_events(self, events: list[pygame.event.Event]):
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.event.post(pygame.event.Event(SHOW_MAIN_MENU))
                if event.key == pygame.K_RETURN:
                    pygame.event.post(pygame.event.Event(EXIT))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.yes_button.check_for_input(MENU_MOUSE_POS):
                    pygame.event.post(pygame.event.Event(EXIT))
                if self.no_button.check_for_input(MENU_MOUSE_POS):
                    pygame.event.post(pygame.event.Event(SHOW_MAIN_MENU))
