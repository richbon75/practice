ingredients = {}

f = open('a15_input.txt','r')
for line in f:
    element = line.strip().split()
    ingredients[element[0].strip(':')] = {
        element[1]: int(element[2].strip(',')),
        element[3]: int(element[4].strip(',')),
        element[5]: int(element[6].strip(',')),
        element[7]: int(element[8].strip(',')),
        element[9]: int(element[10].strip(','))
        }
f.close()

class MixingBowl(object):

    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.attributes = {}
        self.elements = {}
        self.total_tsp = 0
        for ingredient in ingredients:
            self.elements[ingredient] = 0
            for attribute in ingredients[ingredient]:
                self.attributes[attribute] = 0
        self.ingredient_history = []

    def add_ingredient(self, ingredient):
        self.total_tsp += 1
        for attribute, value in self.ingredients[ingredient].items():
            self.attributes[attribute] += value
        self.elements[ingredient] += 1
        self.ingredient_history.append(ingredient)

    def pop_ingredient(self):
        self.remove_ingredient(self.ingredient[-1])

    def remove_ingredient(self, ingredient):
        if self.elements.get(ingredient, 0) <= 0:
            raise ValueError('Ingredient {} not in bowl.'.format(ingredient))
        self.total_tsp -= 1
        for attribute, value in self.ingredients[ingredient].items():
            self.attributes[attribute] -= value
        self.elements[ingredient] -= 1
        self.ingredient_history.pop(len(self.ingredient_history) -1 -self.ingredient_history[::-1].index(ingredient))

    def score(self):
        # score the current contents
        score = 1
        for attribute, value in self.attributes.items():
            if attribute != 'calories':
                if value <= 0:
                    return 0
                else:
                    score *= value
        return score

    def pick_next(self):
        # Given the current bowl state, which ingredient improves it the most?
        choices = {}
        for ingredient in self.ingredients:
            self.add_ingredient(ingredient)
            choices[ingredient] = self.score()
            self.remove_ingredient(ingredient)
        # print(choices)
        results = list(sorted(choices, key=lambda x:choices[x], reverse=True))
        return results[0]

m = MixingBowl(ingredients)
for i in ['Sprinkles', 'Chocolate', 'Butterscotch', 'Candy']:
    m.add_ingredient(i)
to_go = 100 - len(m.ingredient_history)
for _ in range(to_go):
    m.add_ingredient(m.pick_next())
print('High score cookie: ', m.score())
