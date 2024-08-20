'''
TODO:
- Alapalkki ei skaalaudu atm
- Laudan koko (vapaa valinta vai ei, yksittäisen ruudun koko vakio))
- Konstruktori kokonaan
'''

import pygame as pg

class TicTacToe:

    grid_size = (3,3)
    width = grid_size[0]*100
    height = width+50
    white = (255,255,255)
    black = (0,0,0)

    # Määrittele
    def __init__(self, grid):
        self.grid_size_2 = (grid, grid)
        print(self.grid_size_2)


    def draw_grid(surface, width, white, grid_size):

        # Always n-1 lines (per plane) regardless of grid size:
        line_spacing = width / grid_size[0]
        line_coords = [line_spacing*(i+1) for i in range(grid_size[0]-1)]

        # Vertical lines:
        for i in range(len(line_coords)):
            pg.draw.line(surface, white, (line_coords[i], 0), (line_coords[i], width), width=5)

        # Horizontal lines:
        for i in range(len(line_coords)):
            pg.draw.line(surface, white, (0, line_coords[i]), (width, line_coords[i]), width=5)

        
    pg.init()
    surface = pg.display.set_mode((width,height))
    pg.display.set_caption('Tic-Tac-Toe')

    draw_grid(surface, width, white, grid_size)
    pg.display.flip()
        
    running = True

    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

    pg.quit()