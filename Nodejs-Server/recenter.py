#这个文件主要是将图像归于中间被file converter调用

def get_spacing(raw_drawing):
    x_max = 0
    x_min = 255
    y_max = 0
    y_min = 255
    for polyline in raw_drawing:
        for item in polyline:
            its = tuple(item)
            x_max = max(x_max, its[0])
            x_min = min(x_min,its[0])
            y_max = max(y_max, its[1])
            y_min = min(y_min, its[1])
    x_spacing = (255-(x_max - x_min))/2
    y_spacing = (255-(y_max - y_min))/2
    return x_spacing-x_min, y_spacing-y_min

def recenter(raw_drawing,x_spacing,y_spacing):
    new_drawing = []
    for polyline in raw_drawing:
        new_poly = []
        for item in polyline:
            new_poly.append([item[0]+x_spacing,item[1]+y_spacing])
        new_drawing.append(new_poly)
    return new_drawing