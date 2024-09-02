'''
TODO:
- Peliruudun alapalkki ei skaalaudu atm
- Surface-objektit (& hitboxit) kullekin ruudulle + mouseEventtien trackaus (& pelivuoron)
'''

import pygame as pg
import time
import random

class TicTacToe_start:

    def __init__(self):

        self.white = (255,255,255)
        self.black = (0,0,0)
        self.grey = (220,220,220)
        self.red = (255, 0, 0)
        self.clock = pg.time.Clock()
        TicTacToe_start.starting_screen(self)

    def starting_screen_buttons(self, surface, width) -> list:
        
        button_texts = ("3x3", "5x5", "7x7", "1v1", "2v2")
        button_objs = []

        for i in range(len(button_texts[:3])):

            button_surface = pg.Surface((125, 50))
            button_size = (125, 50)

            # (Total width - sum of button widths) / Amount of "empty spacing" needed:
            button_spacing = ((width - (len(button_texts[:3])*button_surface.get_width())) // 4)

            button_x = button_spacing*(i+1) + ((i+1)*(button_size[0] // 2))
            button_y = 250

            button_obj = pg.Rect(button_x, button_y, button_size[0], button_size[1])
            button_objs.append((button_obj, button_texts[i]))
            
            pg.draw.rect(surface, color=self.grey, rect=button_obj)
            pg.draw.rect(surface, color=self.white, rect=button_obj, width=3)
            
            button_font = pg.font.SysFont('cambria.ttf', 24).render(button_texts[:3][i], True, self.black)
            surface.blit(button_font, button_font.get_rect(center=(button_obj.centerx, button_obj.centery)))

        for i in range (len(button_texts[3:])):

            button_surface = pg.Surface((175, 100))
            button_size = (175, 100)

            button_spacing = ((width - (len(button_texts[3:])*button_surface.get_width())) // 3)

            button_x = button_spacing*(i+1) + (i*button_size[0])
            button_y = 420

            button_obj = pg.Rect(button_x, button_y, button_size[0], button_size[1])
            button_objs.append(button_obj)

            pg.draw.rect(surface, color=self.grey, rect=button_obj)
            pg.draw.rect(surface, color=self.white, rect=button_obj, width=3)
            
            button_font = pg.font.SysFont('cambria.ttf', 24).render(button_texts[3:][i], True, self.black)
            surface.blit(button_font, button_font.get_rect(center=(button_obj.centerx, button_obj.centery)))

        return button_objs
    
    def starting_screen(self):

        width = 800
        height = 600
        
        pg.init()

        surface = pg.display.set_mode((width, height))
        pg.display.set_caption('Tic-Tac-Toe')

        # Title, welcome msg and win condition description:
        title = pg.font.SysFont('cambria.ttf', 62).render('Tic-Tac-Toe', True, self.white)
        surface.blit(title, title.get_rect(center=(width // 2, 50)))

        welcome_msg = pg.font.SysFont('cambria.ttf', 28).render(
            'Welcome! To play, first select the wanted grid size and choose your game mode.',
            True, self.white)
        surface.blit(welcome_msg, welcome_msg.get_rect(center=(width // 2, 150)))

        win_conditions = pg.font.SysFont('cambria.ttf', 21).render(
            "To win, either place three (for 3x3) or four (for 5x5 and 7x7) X's (or O's) in a horizontal, vertical or diagonal row.", 
            True, self.white)
        surface.blit(win_conditions, win_conditions.get_rect(center=(width // 2, 200)))

        button_objs = self.starting_screen_buttons(surface, width)

        pg.display.flip()
        pg.display.update()

        gridSize = 0

        while True:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit
                
                # Check mouse events and return buttons to their initial status after a click:
                if event.type == pg.MOUSEBUTTONDOWN:
                    for obj in button_objs[:3]:
                        if obj[0].collidepoint(event.pos):
                            gridSize = obj[1][0]
                            self.starting_screen_buttons(surface, width)
                            pg.draw.rect(surface, color=self.red, rect=obj[0], width=3)
                            pg.display.update()
                    if button_objs[3].collidepoint(event.pos) and gridSize != 0:
                        time.sleep(1.0)
                        self.single_player(gridSize)
                    if button_objs[4].collidepoint(event.pos) and gridSize != 0:
                        time.sleep(1.0)
                        self.multiplayer(gridSize)

    def draw_grid(self, surface, width, grid_size):

        # Always n-1 lines (per plane) regardless of grid size:
        line_spacing = width / grid_size[0]
        line_coords = [line_spacing*(i+1) for i in range(grid_size[0]-1)]

        # Vertical lines:
        for i in range(len(line_coords)):
            pg.draw.line(surface, self.white, (line_coords[i], 0), (line_coords[i], width), width=5)

        # Horizontal lines:
        for i in range(len(line_coords)):
            pg.draw.line(surface, self.white, (0, line_coords[i]), (width, line_coords[i]), width=5)

    def single_player(self, gridSize):
        pass

    def multiplayer(self, gridSize):
        self.mainloop(gridSize)

    def mainloop(self, gridSize):

        grid_size = (int(gridSize),int(gridSize))
        width = grid_size[0]*100 # e.g. 3 * 100 
        height = width+50 # 300 + 50

        # Calculate each hitbox and form surfaces (only "insides" of each line)
        
        pg.init()
        surface = pg.display.set_mode((width,height))
        pg.display.set_caption('Tic-Tac-Toe')

        self.draw_grid(surface, width, grid_size)
        pg.display.flip()
            
        while True:
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit

if __name__ == '__main__':
    TicTacToe_start()
