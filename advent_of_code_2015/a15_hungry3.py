
howmany = 100
count = 0

def distribute(howmany, howmanycategories, prior=list()):
    if howmanycategories == 0:
        yield prior[:]
    else:
        for w in range(0 if howmanycategories>1 else howmany-sum(prior), howmany+1-sum(prior)):
            prior.append(w)
            yield from distribute(howmany = howmany,
                                  howmanycategories = howmanycategories-1,
                                  prior = prior)
            prior.pop()

for x in distribute(1000, 4):
	count += 1

print(count)
	
