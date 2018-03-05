import math

class Spell(object):

    def __init__(self, name, mana_cost, damage, armor, heals, mana, lasts):
        self.name = name
        self.mana_cost = mana_cost
        self.damage = damage
        self.armor = armor
        self.heals = heals
        self.mana = mana
        self.lasts = lasts
        self.active = 0

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def cast(self, caster):
        # Start a spell being effective
        self.active = self.lasts
        caster.mana -= self.mana_cost
        print('Casting {}'.format(self.name))

spellbook = [
    Spell('Magic Missile', 53, 4, 0, 0, 0, 1),
    Spell('Drain', 73, 2, 0, 2, 0, 1),
    Spell('Shield', 113, 0, 7, 0, 0, 6),
    Spell('Poison', 173, 3, 0, 0, 0, 6),
    Spell('Recharge', 229, 0, 0, 0, 101, 5)
    ]

class Character(object):

    def __init__(self, name, hit_points, damage, armor, mana, spellbook):
        self.name = name
        self.hit_points = hit_points
        self.damage = damage
        self.armor = armor
        self.mana = mana
        self.spellbook = spellbook

    def __str__(self):
        output = '{} :: HP {} D {} A {} M {}'.format(self.name,
                 self.hit_points, self.damage, self.armor, self.mana)
        return output

    def available_spells(self):
        # Which of the spells in my spellbook are available to be called?
        if not self.spellbook:
            return []
        return [spell for spell in self.spellbook if \
                (self.mana >= spell.mana_cost and not spell.active)]

    def is_alive(self):
        return (self.hit_points > 0)

    def active_spell_effects(self):
        # Returns collective effects of active spells
        # Also ages all active spells by one turn
        damage = 0
        armor = 0
        heals = 0
        mana = 0
        for spell in spellbook:
            if spell.active > 0:
                print('Active spell: {}'.format(spell.name))
                damage += spell.damage
                armor += spell.armor
                heals += spell.heals
                mana += spell.mana
                spell.active -= 1 # age spell one turn
        return tuple([damage, armor, heals, mana])

    def apply_spell_effects(self, target, effects):
        self.armor = effects[1]
        self.hit_points += effects[2]
        self.mana += effects[3]
        magic_damage = effects[0] - target.armor
        target.hit_points -= magic_damage
        print('{} hits for {}'.format(self.name, magic_damage))

    def basic_attack(self, target):
        basic_damage = max(self.damage-target.armor, 1)
        target.hit_points -= basic_damage
        print('{} hits for {}'.format(self.name, basic_damage))

    def interactive_cast(self):
        print('Which spell should {} cast?'.format(self.name))
        available_spells = self.available_spells()
        allowed_indexes = []
        for x, spell in enumerate(spellbook):
            if spell in available_spells:
                allowed_indexes.append(x)
                print('  {} {}'.format(x, spell.name))
        spell_id = int(input(':'))
        if spell_id in allowed_indexes:
            self.spellbook[spell_id].cast(caster=self)
        else:
            'Invalid spell! Lose a turn.'

player = Character('Hero', 50, 0, 0, 500, spellbook)
monster = Character('Godzilla', 58, 9, 0, 0, None)
# player = Character('Hero', 10, 0, 0, 250, spellbook)
# monster = Character('Godzilla', 14, 8, 0, 0, None)

while player.is_alive() and player.available_spells() and monster.is_alive():
    player.apply_spell_effects(monster, player.active_spell_effects())
    print(player)
    print(monster)
    player.interactive_cast()
    player.apply_spell_effects(monster, player.active_spell_effects())
    if monster.is_alive():
        monster.basic_attack(player)
    print(player)
    print(monster)

if player.is_alive():
    print('{} WINS!'.format(player.name))
else:
    print('{} WINS!'.format(monster.name))

    
    
