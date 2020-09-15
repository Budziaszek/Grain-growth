import pygame
from copy import deepcopy
import threading
import random
import math
from tkinter import *
from tkinter import messagebox


class Image(threading.Thread):
    def __init__(self, gui, width, heigth, box_size, neighbourhood, conditions, time_step=1):
        threading.Thread.__init__(self)

        self.gui = gui

        self.COLORS = [[(176, 23, 31), 0],
                       [(220, 20, 60), 1],
                       [(255, 174, 185), 2],
                       [(238, 162, 173), 3],
                       [(205, 140, 149), 4],
                       [(139, 95, 101), 5],
                       [(219, 112, 147), 6],
                       [(255, 130, 171), 7],
                       [(238, 121, 159), 8],
                       [(205, 104, 137), 9],
                       [(139, 71, 93), 10],
                       [(205, 193, 197), 11],
                       [(139, 131, 134), 12],
                       [(255, 62, 150), 13],
                       [(238, 58, 140), 14],
                       [(205, 50, 120), 15],
                       [(139, 34, 82), 16],
                       [(255, 105, 180), 17],
                       [(238, 106, 167), 18],
                       [(205, 96, 144), 19],
                       [(139, 58, 98), 20],
                       [(135, 38, 87), 21],
                       [(255, 20, 147), 22],
                       [(238, 18, 137), 23],
                       [(205, 16, 118), 24],
                       [(139, 10, 80), 25],
                       [(255, 52, 179), 26],
                       [(238, 48, 167), 27],
                       [(205, 41, 144), 28],
                       [(139, 28, 98), 29],
                       [(199, 21, 133), 30],
                       [(208, 32, 144), 31],
                       [(218, 112, 214), 32],
                       [(255, 131, 250), 33],
                       [(238, 122, 233), 34],
                       [(205, 105, 201), 35],
                       [(139, 71, 137), 36],
                       [(216, 191, 216), 37],
                       [(139, 123, 139), 38],
                       [(255, 187, 255), 39],
                       [(238, 174, 238), 40],
                       [(205, 150, 205), 41],
                       [(139, 102, 139), 42],
                       [(221, 160, 221), 43],
                       [(238, 130, 238), 44],
                       [(255, 0, 255), 45],
                       [(238, 0, 238), 46],
                       [(205, 0, 205), 47],
                       [(139, 0, 139), 48],
                       [(128, 0, 128), 49],
                       [(186, 85, 211), 50],
                       [(224, 102, 255), 51],
                       [(209, 95, 238), 52],
                       [(180, 82, 205), 53],
                       [(122, 55, 139), 54],
                       [(148, 0, 211), 55],
                       [(153, 50, 204), 56],
                       [(191, 62, 255), 57],
                       [(178, 58, 238), 58],
                       [(154, 50, 205), 59],
                       [(104, 34, 139), 60],
                       [(75, 0, 130), 61],
                       [(138, 43, 226), 62],
                       [(155, 48, 255), 63],
                       [(145, 44, 238), 64],
                       [(125, 38, 205), 65],
                       [(85, 26, 139), 66],
                       [(147, 112, 219), 67],
                       [(171, 130, 255), 68],
                       [(159, 121, 238), 69],
                       [(137, 104, 205), 70],
                       [(93, 71, 139), 71],
                       [(72, 61, 139), 72],
                       [(132, 112, 255), 73],
                       [(106, 90, 205), 74],
                       [(0, 0, 255), 75],
                       [(0, 0, 139), 76],
                       [(25, 25, 112), 77],
                       [(61, 89, 171), 78],
                       [(72, 118, 255), 79],
                       [(58, 95, 205), 80],
                       [(39, 64, 139), 81],
                       [(100, 149, 237), 82],
                       [(176, 196, 222), 83],
                       [(202, 225, 255), 84],
                       [(188, 210, 238), 85],
                       [(162, 181, 205), 86],
                       [(159, 182, 205), 87],
                       [(108, 123, 139), 88],
                       [(30, 144, 255), 89],
                       [(28, 134, 238), 90],
                       [(24, 116, 205), 91],
                       [(16, 78, 139), 92],
                       [(70, 130, 180), 93],
                       [(99, 184, 255), 94],
                       [(92, 172, 238), 95],
                       [(79, 148, 205), 96],
                       [(54, 100, 139), 97],
                       [(135, 206, 250), 98],
                       [(176, 226, 255), 99],
                       [(164, 211, 238), 100],
                       [(141, 182, 205), 101],
                       [(96, 123, 139), 102],
                       [(135, 206, 255), 103],
                       [(126, 192, 238), 104],
                       [(108, 166, 205), 105],
                       [(74, 112, 139), 106],
                       [(135, 206, 235), 107],
                       [(0, 191, 255), 108],
                       [(0, 178, 238), 109],
                       [(0, 154, 205), 110],
                       [(0, 104, 139), 111],
                       [(51, 161, 201), 112],
                       [(173, 216, 230), 113],
                       [(191, 239, 255), 114],
                       [(178, 223, 238), 115],
                       [(154, 192, 205), 116],
                       [(104, 131, 139), 117],
                       [(176, 224, 230), 118],
                       [(152, 245, 255), 119],
                       [(142, 229, 238), 120],
                       [(122, 197, 205), 121],
                       [(83, 134, 139), 122],
                       [(0, 245, 255), 123],
                       [(0, 229, 238), 124],
                       [(0, 197, 205), 125],
                       [(0, 134, 139), 126],
                       [(95, 158, 160), 127],
                       [(0, 206, 209), 128],
                       [(193, 205, 205), 129],
                       [(131, 139, 139), 130],
                       [(224, 255, 255), 131],
                       [(209, 238, 238), 132],
                       [(180, 205, 205), 133],
                       [(122, 139, 139), 134],
                       [(187, 255, 255), 135],
                       [(174, 238, 238), 136],
                       [(150, 205, 205), 137],
                       [(102, 139, 139), 138],
                       [(47, 79, 79), 139],
                       [(151, 255, 255), 140],
                       [(141, 238, 238), 141],
                       [(121, 205, 205), 142],
                       [(82, 139, 139), 143],
                       [(0, 255, 255), 144],
                       [(0, 238, 238), 145],
                       [(0, 205, 205), 146],
                       [(0, 139, 139), 147],
                       [(0, 128, 128), 148],
                       [(72, 209, 204), 149],
                       [(32, 178, 170), 150],
                       [(3, 168, 158), 151],
                       [(64, 224, 208), 152],
                       [(128, 138, 135), 153],
                       [(0, 199, 140), 154],
                       [(127, 255, 212), 155],
                       [(118, 238, 198), 156],
                       [(102, 205, 170), 157],
                       [(69, 139, 116), 158],
                       [(0, 250, 154), 159],
                       [(0, 238, 118), 160],
                       [(0, 205, 102), 161],
                       [(0, 139, 69), 162],
                       [(60, 179, 113), 163],
                       [(84, 255, 159), 164],
                       [(78, 238, 148), 165],
                       [(67, 205, 128), 166],
                       [(46, 139, 87), 167],
                       [(0, 201, 87), 168],
                       [(189, 252, 201), 169],
                       [(61, 145, 64), 170],
                       [(224, 238, 224), 171],
                       [(193, 205, 193), 172],
                       [(131, 139, 131), 173],
                       [(143, 188, 143), 174],
                       [(193, 255, 193), 175],
                       [(180, 238, 180), 176],
                       [(155, 205, 155), 177],
                       [(105, 139, 105), 178],
                       [(152, 251, 152), 179],
                       [(154, 255, 154), 180],
                       [(144, 238, 144), 181],
                       [(124, 205, 124), 182],
                       [(84, 139, 84), 183],
                       [(50, 205, 50), 184],
                       [(34, 139, 34), 185],
                       [(0, 255, 0), 186],
                       [(0, 238, 0), 187],
                       [(0, 205, 0), 188],
                       [(0, 139, 0), 189],
                       [(0, 128, 0), 190],
                       [(0, 100, 0), 191],
                       [(48, 128, 20), 192],
                       [(124, 252, 0), 193],
                       [(127, 255, 0), 194],
                       [(118, 238, 0), 195],
                       [(102, 205, 0), 196],
                       [(69, 139, 0), 197],
                       [(173, 255, 47), 198],
                       [(202, 255, 112), 199],
                       [(188, 238, 104), 200],
                       [(162, 205, 90), 201],
                       [(110, 139, 61), 202],
                       [(85, 107, 47), 203],
                       [(107, 142, 35), 204],
                       [(192, 255, 62), 205],
                       [(179, 238, 58), 206],
                       [(154, 205, 50), 207],
                       [(105, 139, 34), 208],
                       [(139, 139, 131), 209],
                       [(205, 205, 180), 210],
                       [(139, 139, 122), 211],
                       [(255, 255, 0), 212],
                       [(238, 238, 0), 213],
                       [(205, 205, 0), 214],
                       [(139, 139, 0), 215],
                       [(128, 128, 105), 216],
                       [(128, 128, 0), 217],
                       [(189, 183, 107), 218],
                       [(255, 246, 143), 219],
                       [(238, 230, 133), 220],
                       [(205, 198, 115), 221],
                       [(139, 134, 78), 222],
                       [(240, 230, 140), 223],
                       [(238, 232, 170), 224],
                       [(205, 201, 165), 225],
                       [(139, 137, 112), 226],
                       [(255, 236, 139), 227],
                       [(238, 220, 130), 228],
                       [(205, 190, 112), 229],
                       [(139, 129, 76), 230],
                       [(227, 207, 87), 231],
                       [(255, 215, 0), 232],
                       [(238, 201, 0), 233],
                       [(205, 173, 0), 234],
                       [(139, 117, 0), 235],
                       [(205, 200, 177), 236],
                       [(139, 136, 120), 237],
                       [(218, 165, 32), 238],
                       [(255, 193, 37), 239],
                       [(238, 180, 34), 240],
                       [(205, 155, 29), 241],
                       [(139, 105, 20), 242],
                       [(184, 134, 11), 243],
                       [(255, 185, 15), 244],
                       [(238, 173, 14), 245],
                       [(205, 149, 12), 246],
                       [(139, 101, 8), 247],
                       [(255, 165, 0), 248],
                       [(238, 154, 0), 249],
                       [(205, 133, 0), 250],
                       [(139, 90, 0), 251],
                       [(245, 222, 179), 252],
                       [(255, 231, 186), 253],
                       [(238, 216, 174), 254],
                       [(205, 186, 150), 255],
                       [(139, 126, 102), 256],
                       [(255, 228, 181), 257],
                       [(255, 239, 213), 258],
                       [(255, 235, 205), 259],
                       [(255, 222, 173), 260],
                       [(238, 207, 161), 261],
                       [(205, 179, 139), 262],
                       [(139, 121, 94), 263],
                       [(252, 230, 201), 264],
                       [(210, 180, 140), 265],
                       [(156, 102, 31), 266],
                       [(255, 153, 18), 267],
                       [(205, 192, 176), 268],
                       [(139, 131, 120), 269],
                       [(222, 184, 135), 270],
                       [(255, 211, 155), 271],
                       [(238, 197, 145), 272],
                       [(205, 170, 125), 273],
                       [(139, 115, 85), 274],
                       [(255, 228, 196), 275],
                       [(238, 213, 183), 276],
                       [(205, 183, 158), 277],
                       [(139, 125, 107), 278],
                       [(227, 168, 105), 279],
                       [(237, 145, 33), 280],
                       [(255, 140, 0), 281],
                       [(255, 127, 0), 282],
                       [(238, 118, 0), 283],
                       [(205, 102, 0), 284],
                       [(139, 69, 0), 285],
                       [(255, 128, 0), 286],
                       [(255, 165, 79), 287],
                       [(238, 154, 73), 288],
                       [(205, 133, 63), 289],
                       [(139, 90, 43), 290],
                       [(255, 218, 185), 291],
                       [(238, 203, 173), 292],
                       [(205, 175, 149), 293],
                       [(139, 119, 101), 294],
                       [(205, 197, 191), 295],
                       [(139, 134, 130), 296],
                       [(244, 164, 96), 297],
                       [(199, 97, 20), 298],
                       [(210, 105, 30), 299],
                       [(255, 127, 36), 300],
                       [(238, 118, 33), 301],
                       [(205, 102, 29), 302],
                       [(139, 69, 19), 303],
                       [(41, 36, 33), 304],
                       [(255, 125, 64), 305],
                       [(255, 97, 3), 306],
                       [(138, 54, 15), 307],
                       [(160, 82, 45), 308],
                       [(255, 130, 71), 309],
                       [(238, 121, 66), 310],
                       [(205, 104, 57), 311],
                       [(139, 71, 38), 312],
                       [(255, 160, 122), 313],
                       [(238, 149, 114), 314],
                       [(205, 129, 98), 315],
                       [(139, 87, 66), 316],
                       [(255, 127, 80), 317],
                       [(255, 69, 0), 318],
                       [(238, 64, 0), 319],
                       [(205, 55, 0), 320],
                       [(139, 37, 0), 321],
                       [(94, 38, 18), 322],
                       [(233, 150, 122), 323],
                       [(255, 140, 105), 324],
                       [(238, 130, 98), 325],
                       [(205, 112, 84), 326],
                       [(139, 76, 57), 327],
                       [(255, 114, 86), 328],
                       [(238, 106, 80), 329],
                       [(205, 91, 69), 330],
                       [(139, 62, 47), 331],
                       [(138, 51, 36), 332],
                       [(255, 99, 71), 333],
                       [(238, 92, 66), 334],
                       [(205, 79, 57), 335],
                       [(139, 54, 38), 336],
                       [(250, 128, 114), 337],
                       [(255, 228, 225), 338],
                       [(238, 213, 210), 339],
                       [(205, 183, 181), 340],
                       [(139, 125, 123), 341],
                       [(205, 201, 201), 342],
                       [(139, 137, 137), 343],
                       [(188, 143, 143), 344],
                       [(255, 193, 193), 345],
                       [(238, 180, 180), 346],
                       [(205, 155, 155), 347],
                       [(139, 105, 105), 348],
                       [(240, 128, 128), 349],
                       [(205, 92, 92), 350],
                       [(255, 106, 106), 351],
                       [(238, 99, 99), 352],
                       [(139, 58, 58), 353],
                       [(205, 85, 85), 354],
                       [(165, 42, 42), 355],
                       [(255, 64, 64), 356],
                       [(238, 59, 59), 357],
                       [(205, 51, 51), 358],
                       [(139, 35, 35), 359],
                       [(178, 34, 34), 360],
                       [(255, 48, 48), 361],
                       [(238, 44, 44), 362],
                       [(205, 38, 38), 363],
                       [(139, 26, 26), 364],
                       [(255, 0, 0), 365],
                       [(238, 0, 0), 366],
                       [(205, 0, 0), 367],
                       [(139, 0, 0), 368],
                       [(128, 0, 0), 369],
                       [(142, 56, 142), 370],
                       [(113, 113, 198), 371],
                       [(125, 158, 192), 372],
                       [(56, 142, 142), 373],
                       [(113, 198, 113), 374],
                       [(142, 142, 56), 375],
                       [(197, 193, 170), 376],
                       [(198, 113, 113), 377],
                       [(85, 85, 85), 378],
                       [(30, 30, 30), 379],
                       [(40, 40, 40), 380],
                       [(81, 81, 81), 381],
                       [(91, 91, 91), 382],
                       [(132, 132, 132), 383],
                       [(142, 142, 142), 384],
                       [(170, 170, 170), 385],
                       [(183, 183, 183), 386],
                       [(193, 193, 193), 387],
                       [(220, 220, 220), 388],
                       [(211, 211, 211), 389],
                       [(192, 192, 192), 390],
                       [(169, 169, 169), 391],
                       [(128, 128, 128), 392],
                       [(105, 105, 105), 393],
                       [(0, 0, 0), 394]]
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)

        self.WIDTH = width
        self.HEIGHT = heigth
        self.BOX_SIZE = box_size
        if width >= 1000 or heigth >= 1000:
            self.MARGIN = 0
        else:
            self.MARGIN = 1

        self.colors = []
        self.direction = None

        self.grid = []
        self.saved_grid = None
        self.cells_taken = 0
        self.clean()

        self.time_step = time_step
        self.neighbourhood = neighbourhood
        self.conditions = conditions

        # Initialize pygame
        pygame.init()

        # Set the HEIGHT and WIDTH of the screen
        self.WINDOW_SIZE = [self.WIDTH * (self.BOX_SIZE + self.MARGIN), self.HEIGHT * (self.BOX_SIZE + self.MARGIN)]
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE)

        # Set title of screen
        pygame.display.set_caption("Grid")

        # Loop until the user clicks the close button.
        self.done = False
        self.paused = True
        self.clock = pygame.time.Clock()

    def clean(self):
        self.cells_taken = 0
        self.grid = []
        for row in range(self.WIDTH):
            self.grid.append([])
            for column in range(self.HEIGHT):
                self.grid[row].append(0)  # Append a cell
        self.colors.clear()
        for c in self.COLORS:
            c[1] = 0
        self.saved_grid = deepcopy(self.grid)

    def restore(self):
        self.grid = deepcopy(self.saved_grid)
        self.cells_taken = len(self.colors)

    def take_cell(self, color, x, y, update_saved=True):
        if update_saved:
            self.saved_grid[x][y] = color
        self.grid[x][y] = color
        self.cells_taken += 1

        if self.cells_taken == self.WIDTH * self.HEIGHT:
            self.gui.SetStatusText("The process has been completed")
            self.paused = True

    def free_cell(self, x, y):
        self.saved_grid[x][y] = 0
        self.colors.remove(self.grid[x][y])
        self.grid[x][y] = 0
        self.cells_taken -= 1

    def add_seeds_evenly(self, number_of_seeds):
        if number_of_seeds <= 0:
            return
        area = self.WIDTH * self.HEIGHT
        seed_area = area / number_of_seeds
        seed_area_radius = math.floor(math.sqrt(seed_area))
        offset = math.ceil(seed_area_radius / 2)

        o_x = offset - 1
        o_y = offset - 1

        for i in range(number_of_seeds):
            random_color = self.get_random_color()
            if o_x >= self.WIDTH - offset + 1:
                o_y += offset * 2 - 1
                o_x = offset - 1
            try:
                if self.grid[o_x][o_y] == 0:
                    self.take_cell(random_color, o_x, o_y)
            except IndexError:
                pass
            o_x += offset * 2 - 1

    def add_seeds_radius(self, number_of_seeds, r):
        added = 0
        if number_of_seeds <= 0:
            return
        r = r + 1

        grid_radius = []
        for row in range(self.WIDTH):
            grid_radius.append([])
            for column in range(self.HEIGHT):
                grid_radius[row].append(0)  # Append a cell
        taken = 0
        for i in range(number_of_seeds):
            if taken >= self.WIDTH * self.HEIGHT:
                return added
            random_color = self.get_random_color()
            random_x = random.randint(0, self.WIDTH - 1)
            random_y = random.randint(0, self.HEIGHT - 1)
            while self.grid[random_x][random_y] != 0 or grid_radius[random_x][random_y] != 0:
                random_x = random.randint(0, self.WIDTH - 1)
                random_y = random.randint(0, self.HEIGHT - 1)
            if self.grid[random_x][random_y] == 0 and grid_radius[random_x][random_y] == 0:
                self.take_cell(random_color, random_x, random_y)
                added += 1
                for x in range(random_x - r, random_x + r):
                    for y in range(random_y - r, random_y + r):
                        if (random_x - x) * (random_x - x) + (random_y - y) * (random_y - y) <= r * r:
                            if 0 <= x < self.WIDTH and 0 <= y < self.HEIGHT:
                                if grid_radius[x][y] == 0:
                                    grid_radius[x][y] = 1
                                    taken += 1
        return added

    def add_seed_randomly(self):
        random_x = random.randint(0, self.WIDTH - 1)
        random_y = random.randint(0, self.HEIGHT - 1)
        if self.saved_grid[random_x][random_y] == 0:
            random_color = self.get_random_color()
            self.take_cell(random_color, random_x, random_y)
        elif self.cells_taken < self.WIDTH*self.HEIGHT:
            self.add_seed_randomly()

    def run(self):
        while not self.done:
            if not self.paused and self.cells_taken < self.WIDTH * self.HEIGHT:
                self.do_next()
            else:
                self.show()

    def show(self):
        # Some event occurred
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[1] // (self.BOX_SIZE + self.MARGIN)
                row = pos[0] // (self.BOX_SIZE + self.MARGIN)
                if self.grid[row][column] == 0:
                    self.take_cell(self.get_random_color(), row, column)
                else:
                    self.free_cell(row, column)
        # Draw the grid
        self.draw_image(60)

    def do_next(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.done = True

        old_grid = deepcopy(self.grid)
        # Random directions if needed
        i = None
        if self.neighbourhood == 'Hexagonal random' or self.neighbourhood == 'Pentagonal random':
            i = 3
            if self.neighbourhood == 'Hexagonal random':
                i = 1

        # Modify the grid
        for row in range(self.WIDTH):
            for column in range(self.HEIGHT):
                if old_grid[row][column] == 0:
                    if i is not None:
                        self.direction = random.randint(0, i)
                    self.check_neighbors_and_actualize(old_grid, row, column)
        # Draw
        self.draw_image(self.time_step)

    def check_neighbour(self, counter, old_grid, row, column, x, y):
        if self.conditions == 'periodical':
            if row + x < 0:
                row = self.WIDTH - 1
            elif row + x >= self.WIDTH:
                row = 0
            if column + y < 0:
                column = self.HEIGHT - 1
            elif column + y >= self.HEIGHT:
                column = 0
        if 0 <= row + x < self.WIDTH and 0 <= column + y < self.HEIGHT:
            if old_grid[row + x][column + y] != 0:
                counter[self.colors.index(old_grid[row + x][column + y])] += 1

    def check_neighbors_and_actualize(self, old_grid, row, column):
        if self.paused:
            return

        counter = []
        for x in range(len(self.colors)):
            counter.append(0)

        if self.neighbourhood == 'Von Neumann' or self.neighbourhood == 'Moore' \
                or self.neighbourhood == 'Hexagonal left' or self.neighbourhood == 'Hexagonal right' \
                or self.neighbourhood == 'Hexagonal random':
            self.check_neighbour(counter, old_grid, row, column, 1, 0)
            self.check_neighbour(counter, old_grid, row, column, -1, 0)
            self.check_neighbour(counter, old_grid, row, column, 0, 1)
            self.check_neighbour(counter, old_grid, row, column, 0, -1)
            if self.neighbourhood == 'Hexagonal left' or self.neighbourhood == 'Moore' \
                    or (self.neighbourhood == 'Hexagonal random' and self.direction == 0):
                self.check_neighbour(counter, old_grid, row, column, 1, 1)
                self.check_neighbour(counter, old_grid, row, column, -1, -1)
            if self.neighbourhood == 'Hexagonal right' or self.neighbourhood == 'Moore' \
                    or (self.neighbourhood == 'Hexagonal random' and self.direction == 1):
                self.check_neighbour(counter, old_grid, row, column, 1, -1)
                self.check_neighbour(counter, old_grid, row, column, -1, 1)
        if self.neighbourhood == 'Pentagonal random':
            if self.direction == 0:
                self.check_neighbour(counter, old_grid, row, column, -1, 0)
                self.check_neighbour(counter, old_grid, row, column, 1, 0)
                self.check_neighbour(counter, old_grid, row, column, -1, -1)
                self.check_neighbour(counter, old_grid, row, column, 0, -1)
                self.check_neighbour(counter, old_grid, row, column, 1, -1)
            if self.direction == 1:
                self.check_neighbour(counter, old_grid, row, column, 1, 1)
                self.check_neighbour(counter, old_grid, row, column, 0, 1)
                self.check_neighbour(counter, old_grid, row, column, 1, 1)
                self.check_neighbour(counter, old_grid, row, column, -1, 0)
                self.check_neighbour(counter, old_grid, row, column, 1, 0)
            if self.direction == 2:
                self.check_neighbour(counter, old_grid, row, column, 1, -1)
                self.check_neighbour(counter, old_grid, row, column, 0, -1)
                self.check_neighbour(counter, old_grid, row, column, -1, -1)
                self.check_neighbour(counter, old_grid, row, column, 0, -1)
                self.check_neighbour(counter, old_grid, row, column, 0, 1)
            if self.direction == 3:
                self.check_neighbour(counter, old_grid, row, column, 1, 1)
                self.check_neighbour(counter, old_grid, row, column, 0, 1)
                self.check_neighbour(counter, old_grid, row, column, -1, 1)
                self.check_neighbour(counter, old_grid, row, column, 0, -1)
                self.check_neighbour(counter, old_grid, row, column, 0, 1)
        try:
            max_index = counter.index(max(counter))
            if counter[max_index] > 0:
                self.take_cell(self.colors[max_index], row, column, False)
        except ValueError:
            self.paused = True
            Tk().wm_withdraw()
            messagebox.showerror('Error', 'Add some seeds before starting the program!')
            self.gui.SetStatusText("Canceled")

    def draw_image(self, tick):
        self.screen.fill(self.BLACK)
        for row in range(self.WIDTH):
            for column in range(self.HEIGHT):
                color = self.WHITE
                if self.grid[row][column] != 0:
                    color = self.grid[row][column]
                pygame.draw.rect(self.screen,
                                 color,
                                 [(self.MARGIN + self.BOX_SIZE) * row + self.MARGIN,
                                  (self.MARGIN + self.BOX_SIZE) * column + self.MARGIN,
                                  self.BOX_SIZE,
                                  self.BOX_SIZE])
        self.clock.tick(tick)
        pygame.display.flip()

    def get_random_color(self):
        while True:
            random_int = random.randint(0, len(self.COLORS) - 1)

            if len(self.colors) == len(self.COLORS):
                for c in self.COLORS:
                    c[1] = 0

            if self.COLORS[random_int][1] == 0:
                random_color = self.COLORS[random_int][0]
                self.COLORS[random_int][1] = 1
                self.colors.append(random_color)
                return random_color
