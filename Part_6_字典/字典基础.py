alien1 = {'color': 'green', 'position': 5, 'speed': 'medium', 'x_position': 0, 'y_position': 50}
print(alien1)
#删除键值对
del alien1['color']
print(alien1)
#使用方法get来避免值不存在时的报错
color_value = alien1.get('color', 'No color value assigned.')
print(color_value)



"""
if alien1['speed'] == 'slow':
    speeds = 1
elif alien1['speed'] == 'medium':
    speeds = 2
else:
    speeds = 3
print(speeds)
alien1['x_position'] = alien1['x_position'] + speeds
print(f"Original position:({alien1['x_position']}, {alien1['y_position']})")
alien1['speed'] = 'fast'
if alien1['speed'] == 'slow':
    speeds = 1
elif alien1['speed'] == 'medium':
    speeds = 2
else:
    speeds = 3
print(speeds)
alien1['x_position'] = alien1['x_position'] + speeds
print(f"Original position:({alien1['x_position']}, {alien1['y_position']})")
"""