import os
import CharacterDesigns.Alligators.Alligators as AD
import CharacterDesigns.Cats.Cats as CD

from Core.FighterBase import FighterBase
from Core.Enums.FighterType import FighterType

os.system('cls')

cat = FighterBase("Will Parsons", FighterType.AIR, CD.cat_1)
cat.print_combat_visualization()

