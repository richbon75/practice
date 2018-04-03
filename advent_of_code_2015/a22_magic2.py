"""
General plan:
Conduct DFS scan of possible moves.
Record minimum mana cost on victory.
Stop following paths when:
    1. cumulative mana spent > minimum mana spent for win
    2. player dies
"""
from copy import copy

class Gamestate(object):
    def __init__(self, player_hp = 50, mana = 500, boss_hp = 58, boss_damage = 9):
        self.player_hp = player_hp
        self.mana = mana
        self.boss_hp = boss_hp
        self.boss_damage = boss_damage
        self.total_mana_spent = 0
        self.shield_on = 0
        self.poison_on = 0
        self.recharge_on = 0

    def turncycle(self):
        if self.shield_on:
            self.shield_on -= 1
        if self.poison_on:
            self.boss_hp -= 3
            self.poison_on -= 1
        if self.recharge_on:
            self.mana += 101
            self.recharge_on -= 1

    def bossattack(self):
        if self.shield_on:
            self.player_hp -= max(0, self.boss_damage - 7)
        else:
            self.player_hp -= self.boss_damage

class Spell(object):
    cost = 0
    @classmethod
    def can_cast(cls, gamestate):
        if gamestate.mana < cls.cost:
            return False
        return True
    
    @classmethod
    def cast(cls, gamestate):
        if not cls.can_cast(gamestate):
            raise RuntimeError("Can't cast {}".format(cls.__name__))
        # print('Root cast called.  Cost = {}'.format(cls.cost))
        gamestate.mana -= cls.cost
        gamestate.total_mana_spent += cls.cost
        
class MagicMissile(Spell):
    cost = 53
    @classmethod
    def cast(cls, gamestate):
        super().cast(gamestate)
        gamestate.boss_hp -= 4

class Drain(Spell):
    cost = 73
    @classmethod
    def cast(cls, gamestate):
        super().cast(gamestate)
        gamestate.boss_hp -= 2
        gamestate.player_hp += 2

class Shield(Spell):
    cost = 113
    @classmethod
    def can_cast(cls, gamestate):
        if not super().can_cast(gamestate) or gamestate.shield_on > 0:
            return False
        return True
    @classmethod
    def cast(cls, gamestate):
        super().cast(gamestate)
        gamestate.shield_on = 6

class Poison(Spell):
    cost = 173
    @classmethod
    def can_cast(cls, gamestate):
        if not super().can_cast(gamestate) or gamestate.poison_on > 0:
            return False
        return True
    @classmethod
    def cast(cls, gamestate):
        super().cast(gamestate)
        gamestate.poison_on = 6

class Recharge(Spell):
    cost = 229
    @classmethod
    def can_cast(cls, gamestate):
        if not super().can_cast(gamestate) or gamestate.recharge_on > 0:
            return False
        return True
    @classmethod
    def cast(cls, gamestate):
        super().cast(gamestate)
        gamestate.recharge_on = 5

spellbook = [MagicMissile, Drain, Shield, Poison, Recharge]

def validspells(gamestate):
    for spell in spellbook:
        if spell.can_cast(gamestate):
            yield spell

g = Gamestate()
min_mana = 10000  # assume this as an initial upper bound to avoid some infinite recursion

def find_minimum_mana(gamestate):
    global min_mana
    if gamestate.total_mana_spent >= min_mana:
        return
    # top of player turn
    gamestate.player_hp -= 1  # hard mode addition
    if gamestate.player_hp <= 0:
        # player has died, don't continue
        return
    gamestate.turncycle()
    if gamestate.boss_hp <= 0:
        if gamestate.total_mana_spent < min_mana:
            min_mana = gamestate.total_mana_spent
            print('New minimum found! {}'.format(min_mana))
        return
    # player turn
    for spell in validspells(gamestate):
        g = copy(gamestate)
        spell.cast(g)
        if g.boss_hp <= 0:
            if g.total_mana_spent < min_mana:
                min_mana = g.total_mana_spent
                print('New minimum found! {}'.format(min_mana))
            return
        # top of boss turn
        g.turncycle()
        if g.boss_hp <= 0:
            if g.total_mana_spent < min_mana:
                min_mana = g.total_mana_spent
                print('New minimum found! {}'.format(min_mana))
            return
        g.bossattack()
        if g.player_hp <= 0:
            # player died, don't continue
            return
        find_minimum_mana(copy(g))

find_minimum_mana(g)
print('Least mana needed: {}'.format(min_mana))

        
    
    
    


