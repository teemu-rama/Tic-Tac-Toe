'''
TODO:
- Peliruudun alapalkki ei skaalaudu atm
- Mousebuttondown-eventit (& valinnan trackaus): https://medium.com/@01one/how-to-create-clickable-button-in-pygame-8dd608d17f1b
- Laudan koko peli-ikkunassa
- Jokaiselle oma Rect-objekti --> collidepointilla trackaus (mousebuttonup rectin alueella --> muuttujaan mikä kyseessä). Pelimoodissa rectin perusteella vain funktiokutsu (& error handle)
- Spacing + boksin oma leveys erona toiseen, korkeus aina vakio
'''

import pygame as pg
import random

class TicTacToe:

    def __init__(self):

        self.white = (255,255,255)
        self.black = (0,0,0)
        self.grey = (220,220,220)
        self.clock = pg.time.Clock()
        TicTacToe.starting_screen(self)

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

        win_conditions = pg.font.SysFont('cambria.ttf', 24).render("To win, either place three (for 3x3) or four (for 5x5 and 7x7) X's in a horizontal, vertical or diagonal row.", True, self.white)
        surface.blit(win_conditions, win_conditions.get_rect(center=(width // 2, 200)))

        # Clickable buttons:
        button_font = pg.font.SysFont('cambria.ttf', 24) #kippaa looppiin, ei tarvi omaa muuttujaa
        
        button_texts = ("3x3", "5x5", "7x7")
        for txt in range(len(button_texts)):
            button_surface = pg.Surface((150, 50))

            # Button size & equal spacing:
            button_size_spacing = [(150, 50), ((width - (len(button_texts)*button_surface.get_width())) // 4)]
            button_text = button_font.render(txt, True, self.white)
            surface.blit(button_text, button_text.get_rect())

        
        button_rect = button_text.get_rect(center=(750, 250)) # leveys, korkeus
        surface.blit(button_text, button_rect)


        button_surface = pg.Surface((150, 50)) # koko
        button_obj = pg.Rect(width // 2, height // 2, 150, 50)#button_surface.get_width(), button_surface.get_height())
        #surface.blit(button_surface, (button_obj.x, button_obj.y))

        pg.draw.rect(surface, color=self.grey, rect=button_obj)
        pg.draw.rect(surface, color=self.white, rect=button_obj, width=3)

        pg.display.flip()
        pg.display.update()

        while True:
            self.clock.tick(60)
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
            self.clock.tick(60)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    raise SystemExit

if __name__ == '__main__':
    TicTacToe()
