import math

class Character(object):

    def __init__(self, name, hit_points, damage, armor):
        self.name = name
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor
        self.inventory_value = 0
        self.inventory = []

    def attacks(self, target):
        damage_dealt = max(self.damage - target.armor, 1)
        target.hit_points -= damage_dealt

    def is_alive(self):
        return (self.hit_points > 0)

    def can_i_beat(self, target):
        # How many hits can the target take from this character?
        damage_per_attack = max(self.damage - target.armor, 1)
        target_dies_in = math.ceil(target.hit_points / damage_per_attack)
        # How many hits can this character take from the target?
        damage_per_attack = max(target.damage - self.armor, 1)
        i_die_in = math.ceil(self.hit_points / damage_per_attack)
        if i_die_in < target_dies_in:
            return False
        return True

    def equip(self, item):
        self.damage += item.damage
        self.armor += item.armor
        self.inventory_value += item.cost
        self.inventory.append(item)

    def unquip(self):
        # unequips the last item added to the inventory
        if self.inventory:
            item = self.inventory.pop()
            self.damage -= item.damage
            self.armor -= item.armor
            self.inventory_value -= item.cost

    def clear_inventory(self):
        self.damage = 0
        self.armor = 0
        self.inventory_value = 0
        self.inventory = []

    def show_inventory(self):
        output = ''
        for item in self.inventory:
            output += item.name + ' '
        return output.strip()

player = Character('Hero', 100, 0, 0)
monster = Character('Godzilla', 100, 8, 2)

class Item(object):

    def __init__(self, name, cost, damage, armor):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.armor = armor

weapons = []
weapons.append(Item('Dagger', 8, 4, 0))
weapons.append(Item('Shortsword', 10, 5, 0))
weapons.append(Item('Warhammer', 25, 5, 0))
weapons.append(Item('Longsword', 40, 7, 0))
weapons.append(Item('Greataxe', 74, 8, 0))

armors = []
armors.append(Item('Naked', 0, 0, 0))
armors.append(Item('Leather', 13, 0, 1))
armors.append(Item('Chainmail', 31, 0, 2))
armors.append(Item('Splitmail', 53, 0, 3))
armors.append(Item('Bandedmail', 75, 0, 4))
armors.append(Item('Platemail', 102, 0, 5))

rings = [
    Item('No Ring 1', 0, 0, 0),
    Item('No Ring 2', 0, 0, 0),
    Item('Damage +1', 25, 1, 0),
    Item('Damage +2', 50, 2, 0),
    Item('Damage +3', 100, 3, 0),
    Item('Defense +1', 20, 0, 1),
    Item('Defense +2', 40, 0, 2),
    Item('Defense +3', 80, 0, 3)]

maxcost = -1

for weapon in weapons:
    player.equip(weapon)
    for armor in armors:
        player.equip(armor)
        for r in range(0, len(rings)):
            player.equip(rings[r])
            for r2 in range(r+1, len(rings)):
                player.equip(rings[r2])
                if not player.can_i_beat(monster):
                    if player.inventory_value > maxcost:
                        maxcost = player.inventory_value
                        print('Player loses with {} costing {}'.format(player.show_inventory(), player.inventory_value))
                player.unquip()
            player.unquip()
        player.unquip()
    player.unquip()


    
