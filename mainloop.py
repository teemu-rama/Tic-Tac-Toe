import pygame as pg

width = 420
height = 450
white = (255,255,255)
black = (0,0,0)

# Ruudukkoon vaadittavat viivat, 2 vaaka + 2 pysty
# Palauta tuple tms. line-objekteja
# Toinen koordinaatti aina 0 alkupisteessä, 400 loppupisteessä

def draw_lines(surface, width, white, ):
    (positions) = width / 3, 3
    pos_1 = width / 3
    pos_2 = pos_1 * 2
    
    # Draw 2 vertical & 2 horizontal lines, combine separate arrays
    # Return a single array
    
    # Alku x, y
    # Loppu x, y
    
    for i in range(len((pos_1, pos_2))):
        
        horizontal = [pg.draw.line(surface, white, (pos_1, 0), (pos_1, width))]

        # Tästä puuttuu loop, osaa tehdä ekan pystysuoran viivan kait?
    
    
    
    
    
#     return pg.draw.line(
#         surface,
#         white,
#         (x,y),
#         (50, 400),
#         width=5)
    
pg.init()
surface = pg.display.set_mode((width,height))
pg.display.set_caption('Tic-Tac-Toe')

# for i in range(2):
print(draw_lines(surface, width, white))
pg.display.flip()
    
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

pg.quit()