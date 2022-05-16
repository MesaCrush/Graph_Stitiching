#一个输入要能被处理必须先通过这个将原文件转化

from recenter import recenter, get_spacing
from converter import line_spliter_horizon, line_spliter_vertical

# read ndjson lines
def json_converter(preprocess_drawing,x_target1 = 85,x_target2 = 170 ,y_target1 = None,y_target2 = None):

    x_spacing,y_spacing = get_spacing(preprocess_drawing)

    new_drawing = recenter(preprocess_drawing,x_spacing,y_spacing)

    # parse to horisontal 3 phase data
    new_line_dict = line_spliter_horizon(new_drawing,x_target1,x_target2)

    if y_target1:
        new_line_dict["part2"] = line_spliter_vertical(new_line_dict["part2"],y_target1,y_target2)

    return new_line_dict



