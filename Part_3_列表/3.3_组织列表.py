areas = ['tokyo', 'danish', 'netherlands', 'kunming', 'malaysia']
print("Original order:" + str(areas))
#第三个问题,不改变列表，打印出反向按字母排序列表, 学习传参
print(sorted(areas, reverse=True))
#第五个问题，reverse的使用，负负得正
areas.reverse()
print(areas)
areas.reverse()
print(areas)
#按字母排序
areas.sort()
print(areas)
#改变列表，打印出反向按字母排序列表
areas.sort(reverse=True)
print(areas)
#len()获取列表长度
print(len(areas))