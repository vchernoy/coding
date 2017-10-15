
import random, time

def punches(bags):
    bags = bags[:]
    n = len(bags)
    no_punches = 0
    while True:
        best_cost = 100
        best_inds = []
    
        for i in xrange(n):
            if bags[i] > 0:
                cost = bags[i]
                cost += ((i > 0)   and (bags[i-1] > 0))
                cost += ((i < n-1) and (bags[i+1] > 0))
                if cost < best_cost:
                    best_cost = cost
                    best_inds = [i]
                elif cost == best_cost:
                    best_inds.append(i)

        if len(best_inds) == 0:
            return no_punches
    
        i = best_inds[random.randint(0, len(best_inds)-1)]

        bags[i] = 0
        if (i > 0) and (bags[i-1] > 0):
            bags[i-1] -= 1
        if (i < n-1) and (bags[i+1] > 0):
            bags[i+1] -= 1

        no_punches += 1

end_tm = time.time() + 15.7 
random.seed()
bags = [ord(cost) - ord('0') for cost in raw_input()]
max_punches = punches(bags)
while time.time() < end_tm:
    for i in xrange(100):
        max_punches = max(max_punches, punches(bags))

print max_punches

