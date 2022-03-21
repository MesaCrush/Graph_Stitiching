
def modifier(bridge_pt1, bridge_pt2,image):
    part2 = image["part2"].sort()
    for i in range(len(bridge_pt1)):
        part2[i][1] = bridge_pt1[i]
    for i in range(len(bridge_pt2)):
        part2[len(part2)-len(bridge_pt2)+i][1] = bridge_pt2[i]
    return part2