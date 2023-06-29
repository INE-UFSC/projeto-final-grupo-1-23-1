import pygame

class Button():
	def __init__(self, pos: list, text_input, font, base_color, hovering_color):
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		self.rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		screen.blit(self.text, self.text_rect)

	def check_for_input(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def change_color(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

class ImageButton():
	def __init__(self, screen, image, screen_width, screen_height, base_color, hovering_color, line_width):
		self.screen = screen
		self.screen_width, self.screen_height = screen_width, screen_height
		self.base_color, self.hovering_color = base_color, hovering_color
		self.line_width = line_width
		self.image = pygame.image.load(f"{image}")
		self.rect = self.image.get_rect(center=(self.screen_width, self.screen_height))

	def update(self, screen):
		screen.blit(self.image, self.rect)

	def check_for_input(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def change_color(self, position):
		#self.screen.blit(self.image, self.rect)
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			pygame.draw.rect(self.screen, self.hovering_color, self.rect, self.line_width)
		else:
			pygame.draw.rect(self.screen, self.base_color, self.rect, self.line_width)

