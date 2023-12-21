import os, time
import Configurations.Constants as Constants

class FighterBase:
    def __init__(self, name, fighterType, ascii_representation = None):
        self._name = name
        self._fighter_type = fighterType

        self._current_level = 1

        self._current_experience = 0
        self._experience_to_next_level = 100

        self._total_health_points = 100
        self._current_health_points = 100

        self._total_stamina_points = 50
        self._current_stamina_points = 50

        self._is_alive = True
        self._has_stamina = True

        self._ascii_representation = (
            Constants.DEFAULT_CHARACTER_REPRESENTATION if ascii_representation is None 
            else ascii_representation
        )

    # region Property definitions

    @property
    def name(self):
        return self._name

    @property
    def fighter_type(self):
        return self._fighter_type
    
    @property
    def total_health_points(self):
        return self._total_health_points
    
    @property
    def current_health_points(self):
        return self._current_health_points
    
    @property 
    def total_stamina_points(self):
        return self._total_stamina_points
    
    @property
    def current_stamina_points(self):
        return self._current_stamina_points
    
    @property
    def current_experience(self):
        return self._current_experience
    
    @property
    def experience_to_next_level(self):
        return self._experience_to_next_level
    
    @property
    def current_level(self):
        return self._current_level
    
    @property
    def is_alive(self):
        return self._is_alive
    
    @property
    def has_stamina(self):
        return self._has_stamina
    
    @property
    def ascii_representation(self):
        return self._ascii_representation
    
    # endregion

    # region Property Setters
    
    @fighter_type.setter
    def fighter_type(self, value):
        self._fighter_type = value

    @total_health_points.setter
    def total_health_points(self, value):
        self._total_health_points = value

    @current_health_points.setter
    def current_health_points(self, value):
        self._current_health_points = value

    @total_stamina_points.setter
    def total_stamina_points(self, value):
        self._total_stamina_points = value

    @current_stamina_points.setter
    def current_stamina_points(self, value):
        self._current_stamina_points = value

    @current_experience.setter
    def current_experience(self, value):
        self._current_experience = value

    @experience_to_next_level.setter
    def experience_to_next_level(self, value):
        self._experience_to_next_level = value

    @current_level.setter
    def current_level(self, value):
        self._current_level = value

    @is_alive.setter
    def is_alive(self, value):
        self._is_alive = value

    @has_stamina.setter
    def has_stamina(self, value):
        self._has_stamina = value

    @ascii_representation.setter
    def ascii_representation(self, value):
        self._ascii_representation = value

    # endregion

    # region Public Methods

    # Add experience to the character. If the new level of experience
    # sets us over the limit to level up. We will level up the character
    # and determine / set what the new _experience_to_next_level will be.
    def add_experience(self, value):
        self.current_experience += value

        if self.current_experience >= self.experience_to_next_level:
            self._level_up()

    # Takes away <value> amount of health from the character;
    # if we hit 0 or below the character will not be considered alive.
    def take_health(self, value):
        self.current_health_points = (
            self.current_health_points - value
            if (self.current_health_points - value) > 0
            else 0
        )

        self.is_alive = self.current_health_points > 0

    # Gives <value> amount of health to the character;
    # the maximum amount of health will be <self.total_health_points>.
    def give_health(self, value):
        self.current_health_points = (
            self.current_health_points + value
            if (self.current_health_points + value ) <= self.total_health_points
            else self.total_health_points
        )

        self.is_alive = self.current_health_points > 0

    # Takes away <value> amount of stamina from the character;
    # if we hit 0 the character will not be considered to have stamina.
    def take_stamina(self, value):
        self.current_stamina_points = (
            self.current_stamina_points - value
            if (self.current_stamina_points - value ) > 0
            else 0
        )

        self.has_stamina = self.current_stamina_points > 0

    # Gives <value> amount of stamina to the character;
    # the maximum amount of stamina will be <self.total_stamina_points>.
    def give_stamina(self, value):
        self.current_stamina_points = (
            self.current_stamina_points + value
            if (self.current_stamina_points + value ) <= self.total_stamina_points
            else self.total_stamina_points
        )

    # Sets the character's health and stamina to their full values.
    def reset_health_and_stamina(self):
        self.current_health_points = self.total_health_points
        self.current_stamina_points = self.total_stamina_points

    def print_player_stats(self):
        print(f"{self.name}")
        print(f"HP ({self.current_health_points}/{self.total_health_points})")
        print(f"Lvl {self.current_level} ({self.current_experience}/{self.experience_to_next_level})")
        print(f"Alive {self.is_alive}\n\n")

    def print_player_representation(self):
        print(self.ascii_representation)

    def print_combat_visualization(self):
        health_str = f"HP: {self.current_health_points}/{self.total_health_points}"
        stamina_str = f"SP: {self.current_stamina_points}/{self.total_stamina_points}"
        xp_str = f"XP: {self.current_experience}/{self.experience_to_next_level}"
        lvl_str = f"Lvl: {self.current_level}"

        print(self.ascii_representation)
        print(self.name)
        print(f"{health_str}\t{xp_str}")
        print(f"{stamina_str}\t{lvl_str}")

    # endregion

    # region Private Methods

    def _level_up(self):
        # Keep track of the previous xp needed to level up.
        prev_xp = self.experience_to_next_level

        # Update our new level stats.
        self.current_level += 1
        self.experience_to_next_level = int(self.experience_to_next_level * Constants.EXPERIENCE_TO_NEXT_LEVEL_FACTOR)
        self.total_health_points = int(self.total_health_points * Constants.HEALTH_LEVEL_UP_FACTOR)
        self.total_stamina_points = int(self.total_stamina_points * Constants.STAMINA_LEVEL_UP_FACTOR)

        # When we level up we should refill health and stamina to our new levels.
        self.reset_health_and_stamina()

        # How much xp are we carrying over to the next level.
        remainingXP = self.current_experience - prev_xp

        # Add the remaining xp to character. This will end up calling this method recursively
        # in the event the amount of xp added allows the player to level up multiple times.
        self.current_experience = 0 # This will get updated in the add_experience call.
        self.add_experience(remainingXP)

    # endregion