colours = ["r", "o", "y", "g", "b", "i", "v"]
balls = []
for colour in colours:
    for i in range(10):
        balls.append(colour + str(i))
# print(balls)
#print(len(balls))

def combination(ballSet):
    if len(ballSet) > 1:
        for i in ballSet:
            print(ballSet)
            yield combination(ballSet.pop(0))

    else:
        yield ballSet[0]


for x in combination(colours): print(x)
