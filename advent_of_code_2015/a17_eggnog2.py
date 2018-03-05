containers = [11,30,47,31,32,36,3,1,5,3,32,36,15,11,46,26,28,1,19,3]
ways = {}
combos = 0
for i in range(2**20):
    total = 0
    containers_used = 0
    for j in range(20):
        i, use = divmod(i, 2)
        if use:
            total += containers[j]
            containers_used += 1
    if total == 150:
        if containers_used not in ways:
            ways[containers_used] = 0
        ways[containers_used] += 1
        combos += 1
print('combos that store 150 liters: ',combos)

min_containers = min([key for key in ways])
print('Minimum containers required = ', min_containers)
print('Ways to use them = ', ways[min_containers])
