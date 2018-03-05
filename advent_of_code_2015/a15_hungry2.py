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
        # if self.attributes['calories'] > 500:
        #    return 0
        if self.attributes['calories'] > ((500/100) * self.total_tsp):
            return 0
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

    def generate_states(self, levels, partial_state=list()):
        for ingredient in self.ingredients:
            partial_state.append(ingredient)
            if levels <= 1:
                yield partial_state[:]
            else:
                yield from self.generate_states(levels-1, partial_state)
            partial_state.pop()

    def pick_next_x(self, x):
        # Given the current bowl state, which set of x number of ingredients
        # improves it the most?
        best_score = 0
        best_set = None
        possible_sets = set()
        for state in self.generate_states(x):
            possible_sets.add(tuple(sorted(state)))
        # print(possible_sets)
        for group in possible_sets:
            for ingredient in group:
                self.add_ingredient(ingredient)
            local_score = self.score()
            # print(local_score)
            if local_score > best_score:
                best_score = local_score
                best_set = group[:]
            for ingredient in group:
                self.remove_ingredient(ingredient)
        print(best_score)
        print(best_set)
        return best_set

    def add_ingredients(self, list_of_ingredients):
        for ingredient in list_of_ingredients:
            self.add_ingredient(ingredient)

m = MixingBowl(ingredients)
'''
for i in ['Sprinkles', 'Chocolate', 'Butterscotch', 'Candy']:
    m.add_ingredient(i)
to_go = 100 - len(m.ingredient_history)
for _ in range(to_go):
    next_i = m.pick_next()
    print(next_i)
    m.add_ingredient(next_i)
print('High score cookie: ', m.score())
'''
chunk_size = 10
for i in range(100//chunk_size):
    m.add_ingredients(m.pick_next_x(chunk_size))
    print(m.elements)
    print(m.attributes)
    print('TSP: {}  SCORE: {}'.format(m.total_tsp, m.score()))
if (100%chunk_size):
    m.add_ingredients(m.pick_next_x(100%chunk_size))
    print(m.elements)
    print(m.attributes)
    print('TSP: {}  SCORE: {}'.format(m.total_tsp, m.score()))


