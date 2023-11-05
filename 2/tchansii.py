res = {"x": 0, "y": 0}
with open('input.txt') as file:
   for line in file:
       cmd = line.split(" ")
       match cmd[0]:
        case 'down':
            res['y'] += int(cmd[1])
        case 'up':
            res['y'] -= int(cmd[1])
        case 'forward':
            res['x'] += int(cmd[1])
print(res["x"] * res["y"])