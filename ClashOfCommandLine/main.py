import os, time

from Core.FighterBase import FighterBase
from Core.Enums.FighterType import FighterType

ascii_cat = (
""" /\_/\ 
( o.o )
 > ^ <""")

ascii_alligator = (
"""       .-._   _ _ _ _ _ _ _ _
 .-''-.__.-'00  '-' ' ' ' ' ' ' '-.
'.___ '    .   .--_'-' '-' '-' _'-' '._
 V: V 'vv-'   '_   '.       .'  _..' '.'.
   '=.____.=_.--'   :_.__.__:_   '.   : :
           (((____.-'        '-.  /   : :
                             (((-'\ .' /
                           _____..'  .'
                          '-._____.-'
"""    
)
os.system('cls')

fighter = FighterBase("Will Parsons", FighterType.AIR, ascii_alligator)
fighter.print_combat_visualization()

time.sleep(1)
os.system("cls")
fighter.add_experience(110)
fighter.print_combat_visualization()

time.sleep(1)
os.system("cls")
fighter.take_health(125)
fighter.print_combat_visualization()

time.sleep(1)
os.system("cls")
fighter.give_health(925)
fighter.print_combat_visualization()

time.sleep(1)
os.system("cls")
fighter.take_stamina(1000)
fighter.print_combat_visualization()

time.sleep(1)
os.system("cls")
fighter.give_stamina(1000)
fighter.print_combat_visualization()
