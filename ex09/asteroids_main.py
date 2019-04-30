from ship import Ship
from asteroid import Asteroid
from screen import Screen
from torpedo import Torpedo
import sys
import random


SHIP_RADIOS = 1
SHIP_MAX_SPEED = 10
DEFAULT_ASTEROIDS_NUM = 5
TURNING_LEFT = 7
TURNING_RIGHT = -7
BIG_ASTEROID = 3
MIDDLE_ASTEROID = 2
SMALL_ASTEROID = 1
SCORES_BIG_ASTEROID = 20
SCORES_MIDDLE_ASTEROID = 50
SCORES_SMALL_ASTEROID = 100
TITLE_ENDGAME = "Game Over"
LIFE_MESSAGE = "You run out of life"
QUIT_PRESS_MESSAGE = "You clicked 'quit'"
Q_PRESS_MESSAGE = "You clicked 'q'"
ASTEROID_LST_OVER_MESSAGE = "You won the game!"
LIFE_LOST_MESSAGE = " Extra Lives Remaining:"
LIFE_LOST_TITLE = "Uh-Oh an asteroid hit you!"
SPEED_PARAMETER_FOR_ASTEROID_1 = 1
SPEED_PARAMETER_FOR_ASTEROID_2 = -1


class GameRunner:
    """
    Thia is the class the main game run in
    """
    def __init__(self, asteroids_amount):
        """
        :param asteroids_amount: the number of asteroids that are in the start
        of the game by user input or defult if there is no input
        :initializing: the parameters to the game
        """
        self._screen = Screen()
        self.ship = Ship()
        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y
        self.asteroids_amount = asteroids_amount
        self.torpedo_lst = []
        self.asteroid_lst = []
        for i in range(self.asteroids_amount):
            # update asteroids
            asteroid = Asteroid(self.ship)
            self.asteroid_lst.append(asteroid)
            self._screen.register_asteroid(asteroid, asteroid.get_size())
        self.score = 0
        self.rotation = random.random() * 5

    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop, 5)

    def move(self, obj):
        """
        :param obj:taking a given object and moving it to another place
        """
        old_x = obj.get_lx()
        old_y = obj.get_ly()
        dx = obj.get_dx()
        dy = obj.get_dy()
        obj.set_lx((dx + old_x - self.screen_min_x) %
                (self.screen_max_x - self.screen_min_x) + self.screen_min_x)
        obj.set_ly((dy + old_y - self.screen_min_y) %
                (self.screen_max_y - self.screen_min_y) + self.screen_min_y)

    def set_asteroid(self, asteroid, lx, ly, size):
        """
        :param asteroid: the id of a given asteroid
        :param lx: the location on the x scale we want to set
        :param ly: the location on the y scale we want to set
        :param size: the new size of the asteroid
        :return:set a new asteroid
        """
        asteroid.set_lx(lx)
        asteroid.set_ly(ly)
        asteroid.set_size(size)
        return asteroid

    def move_ship(self):
        """
        a function that call's the ship to the screen and moves the ship
        across the screen
        """
        self.move(self.ship)
        self._screen.draw_ship(self.ship.get_lx(), self.ship.get_ly(),
                               self.ship.get_heading())
        if self._screen.is_left_pressed():
            self.ship.turn(TURNING_LEFT)
        elif self._screen.is_right_pressed():
            self.ship.turn(TURNING_RIGHT)
        elif self._screen.is_up_pressed():
            self.ship.fire_engine()

    def move_torpedo(self):
        """
        moves the torpedo in the direction it was fire and update the game
        score when we hit an asteroid
        """
        if self._screen.is_space_pressed() and len(self.torpedo_lst) <= 15:
            torpedo = Torpedo(self.ship)
            torpedo.set_dx()
            torpedo.set_dy()
            self._screen.register_torpedo(torpedo)
            self.torpedo_lst.append(torpedo)
        dead_torpedo_lst = []
        for i, torpedo in enumerate(self.torpedo_lst):
            if torpedo.get_life() > 0:
                self.move(torpedo)
                self._screen.draw_torpedo(torpedo, torpedo.get_lx(),
                                          torpedo.get_ly(),
                                          torpedo.get_heading())
                torpedo.life_update()
            else:
                dead_torpedo_lst.append(i)
            for j, ast in enumerate(self.asteroid_lst):
                if ast.has_intersection(torpedo):
                    self.score_update(ast.get_size())
                    self.torpedo_hit(ast, torpedo, i, j)
                    dead_torpedo_lst.append(i)
        new_torpedo_list = []
        for i in range(len(self.torpedo_lst)):
            if i not in dead_torpedo_lst:
                new_torpedo_list.append(self.torpedo_lst[i])
            if i in dead_torpedo_lst:
                self._screen.unregister_torpedo(self.torpedo_lst[i])
        self.torpedo_lst = new_torpedo_list

    def move_asteroid(self, asteroid):
        """
        this function calls the asteroid to the screen and moves them
        across the screen.
        also if an asteroid hits a ship the function update the ship life and
        removes the asteroid
        """
        self.move(asteroid)
        self._screen.draw_asteroid(asteroid,
                                   asteroid.get_lx(), asteroid.get_ly())
        if asteroid.has_intersection(self.ship):
            self._screen.remove_life()
            self.ship.life_update()
            if self.ship.get_life() != 0:
                self._screen.show_message(LIFE_LOST_TITLE,
                                          LIFE_LOST_MESSAGE + str(
                                              self.ship.get_life()))
            self._screen.unregister_asteroid(asteroid)
            for i, new_asteroid in enumerate(self.asteroid_lst):
                if new_asteroid.get_lx() == asteroid.get_lx() and \
                        new_asteroid.get_ly() == asteroid.get_ly():
                    self.asteroid_lst = \
                        self.remove_from_list(self.asteroid_lst, i)

    def _game_loop(self):
        """
        this function controls the game and helps run everything in one loop
        """
        self.move_ship()
        for asteroid in self.asteroid_lst:
            self.move_asteroid(asteroid)
        self.move_torpedo()
        self.game_end()

    def score_update(self, size):
        """
        :param size: gets the size of the asteroid we hit
        :return: update the game score
        """
        if size == BIG_ASTEROID:
            self.score += SCORES_BIG_ASTEROID
        if size == MIDDLE_ASTEROID:
            self.score += SCORES_MIDDLE_ASTEROID
        if size == SMALL_ASTEROID:
            self.score += SCORES_SMALL_ASTEROID
        self._screen.set_score(self.score)

    def remove_from_list(self, list_of_obj, i):
        """
        :param list_of_obj: a given list of object to update
        :param i: the index of the object we want to remove
        :return: returns the updated list of objects
        """
        list_of_obj = list_of_obj[:i] + list_of_obj[i + 1:]
        return list_of_obj

    def torpedo_hit(self, asteroid, torpedo, i, j):
        """
        :param asteroid: the asteroid that the torpedo hit
        :param torpedo: the torpedo that hit the asteroid
        :param i: the torpedo index
        :param j: the asteroid index
        register two new smaller asteroid that are created from the larger
        asteroid if it's a small asteroid the function remove it from play
        """
        if asteroid.get_size() > SMALL_ASTEROID:
            new_asteroid1 = Asteroid(self.ship)
            new_asteroid2 = Asteroid(self.ship)
            new_asteroid1.set_hit_speed(SPEED_PARAMETER_FOR_ASTEROID_1,
                                        torpedo, asteroid)
            new_asteroid2.set_hit_speed(SPEED_PARAMETER_FOR_ASTEROID_2,
                                        torpedo, asteroid)
            new_asteroid1 = self.set_asteroid(new_asteroid1,
                                              asteroid.get_lx(),
                                              asteroid.get_ly(),
                                              (asteroid.get_size() - 1))
            new_asteroid2 = self.set_asteroid(new_asteroid2,
                                              asteroid.get_lx(),
                                              asteroid.get_ly(),
                                              (asteroid.get_size() - 1))
            self.asteroid_lst.append(new_asteroid1)
            self.asteroid_lst.append(new_asteroid2)
            self._screen.register_asteroid(new_asteroid1,
                                           asteroid.get_size() - 1)
            self._screen.register_asteroid(new_asteroid2,
                                           asteroid.get_size() - 1)
        self._screen.unregister_asteroid(asteroid)
        self.asteroid_lst = self.remove_from_list(self.asteroid_lst, j)

    def game_end(self):
        """
        checks if the game is over or if the user has quit the game
        """
        if len(self.asteroid_lst) == 0:
            self._screen.show_message(TITLE_ENDGAME, ASTEROID_LST_OVER_MESSAGE)
        elif self.ship.get_life() == 0:
            self._screen.show_message(TITLE_ENDGAME, LIFE_MESSAGE)
        elif self._screen.should_end():
            self._screen.show_message(TITLE_ENDGAME, Q_PRESS_MESSAGE)
        else:
            return False
        self._screen.end_game()
        sys.exit()


def main(amount):
    runner = GameRunner(amount)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
