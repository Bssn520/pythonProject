alien1 = {'color': 'green', 'position': 5, 'speed': 'medium', 'x_position': 0, 'y_position': 50}
print(f"Original position:({alien1['x_position']}, {alien1['y_position']})")
if alien1['speed'] == 'slow':
    speeds = 1
elif alien1['speed'] == 'medium':
    speeds = 2
else:
    speeds = 3
print(speeds)
alien1['x_position'] = alien1['x_position'] + speeds
print(f"Original position:({alien1['x_position']}, {alien1['y_position']})")