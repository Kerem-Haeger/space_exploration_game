# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import numpy as np


class Galaxy:
    def __init__(self, size=20):
        self.size = size
        self.grid = np.zeros((size, size), dtype=int)
        self.objects = []

    def place_object(self, x, y, object_type):
        """
        Place an object at the x, y coordinates
        """
        self.grid[x, y] = object_type
        self.objects.append((x, y, object_type))

    def generate_galaxy(self, num_stars=1, num_planets=5, num_spaceships=1):
        """
        Randomly place stars, plantes, and the spaceship
        """
        sun_x, sun_y = np.random.randint(0, self.size, size=2)
        self.place_object(sun_x, sun_y, 2)

        for _ in range(5):
            x, y = np.random.randint(0, self.size, size=2)
            while self.grid[x, y] != 0:
                x, y = np.random.randint(0, self.size, size=2)
            self.place_object(x, y, 1)

        spaceship_x, spaceship_y = np.random.randint(0, self.size, size=2)
        while self.grid[spaceship_x, spaceship_y] != 0:
            spaceship_x, spaceship_y = np.random.randint(0, self.size, size=2)
        self.place_object(spaceship_x, spaceship_y, 3)

    def display_galaxy(self):
        """
        Display the galaxy grid in the terminal
        """
        display_grid = np.full((self.size, self.size), '.', dtype=str)
        for x, y, object_type in self.objects:
            if object_type == 1:
                display_grid[x, y] = 'P'
            elif object_type == 2:
                display_grid[x, y] = 'S'
            elif object_type == 3:
                display_grid[x, y] = 'X'

        for row in display_grid:
            print(" ".join(row))


def main():
    # Create a galaxy of size 10x10
    galaxy = Galaxy(size=20)

    # Generate stars, planets, and a spaceship
    galaxy.generate_galaxy(num_stars=3, num_planets=4, num_spaceships=1)

    # Display the galaxy grid
    print("Exploring the Galaxy:")
    galaxy.display_galaxy()


main()
