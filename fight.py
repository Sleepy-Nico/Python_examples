fighter1 = input("Choose your name! ")
fighter1hp = 10
fighter2 = ("Opponent")
fighter2hp = 10

import random
Damage_option = [1, 2, 3, 4, 5]

while (fighter1hp > 0 and fighter2hp > 0):
    print("new round")
 
    fighter1_damage = random.choice(Damage_option)
    fighter2_damage = random.choice(Damage_option)
    
    fighter1hp -= fighter1_damage
    fighter2hp -= fighter2_damage

    print(f"{fighter1} takes {fighter1_damage} damage, health now: {fighter1hp}")
    print(f"{fighter2} takes {fighter2_damage} damage, health now: {fighter2hp}")
    
    if (fighter1hp <= 0 or fighter2hp <= 0):
        break

if fighter1hp <= 0 and fighter2hp <= 0:
    print("\nIt's a draw!")
elif fighter1hp <= 0:
    print(f"\n{fighter1} has lost! {fighter2} wins!")
    # print(fighter1, "has lost!",fighter2,"wins!")
    # print(fighter1+ " has lost! " + fighter2 + " wins!")
elif fighter2hp <= 0:
    print(f"\n{fighter2} has lost! {fighter1} wins!")