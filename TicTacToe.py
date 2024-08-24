'''
TODO:
- Peliruudun alapalkki ei skaalaudu atm
- Aloitusruutu: 1. ruudun koko 2. yksin- vai moninpeli (& error catch)
- Mousebuttondown-eventit (& valinnan trackaus): https://medium.com/@01one/how-to-create-clickable-button-in-pygame-8dd608d17f1b
- Laudan koko peli-ikkunassa
'''

import pygame as pg
import random

class TicTacToe:

    def __init__(self):

        self.white = (255,255,255)
        self.black = (0,0,0)
        TicTacToe.starting_screen(self) # tsek

    def starting_screen(self):

        width = 800
        height = 600
        
        pg.init()
        clock = pg.time.Clock()

        surface = pg.display.set_mode((width, height))
        pg.display.set_caption('Tic-Tac-Toe')

        # Title & welcome msg:
        title = pg.font.SysFont('cambria.ttf', 62).render('Tic-Tac-Toe', True, self.white)
        title_rect = title.get_rect()
        title_rect.center = (width // 2, 50)
        surface.blit(title, title_rect)

        msg = pg.font.SysFont('cambria.ttf', 28).render(
            'Welcome! To play, first select the wanted grid size and choose your game mode.',
            True, self.white
        )

        msg_rect = msg.get_rect()
        msg_rect.center = (width // 2, 150)
        surface.blit(msg, msg_rect)

        # Clickable buttons:
        button_font = pg.font.SysFont('cambria.ttf', 14)

        #for i in range(3):


        button_text = button_font.render('3x3', True, self.white)
        button_rect = button_text.get_rect() # Voi olla myös näin: text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))
        button_rect.center = (width // 2, 250) # tsek

        button_obj = pg.Rect(125,125,150,50)
        surface.blit(button_rect, button_obj) # Tsek





        pg.display.flip()
        pg.display.update()

        while True:
            clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit

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

    def mainloop(self): # Tämä saa parametrina aiemmasta ikkunasta ruudukon koon, nimi muutettava

        grid_size = (3,3)
        width = grid_size[0]*100
        height = width+50
        
        pg.init()
        surface = pg.display.set_mode((width,height))
        pg.display.set_caption('Tic-Tac-Toe')

        TicTacToe.draw_grid(self, surface, width, grid_size)
        pg.display.flip()
            
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit

if __name__ == '__main__':
    TicTacToe()
