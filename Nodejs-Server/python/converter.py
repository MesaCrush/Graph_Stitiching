#这个用来分开左中右的具体运行代码，被file——converter调用，然后确定交点

def contact_point_cal_x(x1,y1,x2,y2,c):
    k = (float(y2)-y1)/(x2-x1) #斜率
    yt = y1+ (c-x1)*k
    return round(yt,1)

def contact_point_cal_y(x1,y1,x2,y2,c):
    k = (float(x2)-x1)/(y2-y1) #斜率
    xt = x1+ (c-y1)*k
    return round(xt,1)


def line_spliter_horizon(line_list,x_target1,x_target2):
    #part1,2,3 为分区图像，contact1，2 为交界点
    new_line_list= {"part1":[],"part2":[],"part3":[],"contact1":[],"contact2":[]}
    for line in line_list:
        for i in range(len(line)-1):
            if line[i] < line[i+1]:
                rev = False
                x1,y1 = line[i]
                x2,y2 = line[i+1]
            else:
                rev = True
                x1,y1 = line[i+1]
                x2,y2 = line[i]

            #x_target1 contact point 没handle
            if x1<x_target1:
                if x2 < x_target1: #CASE1 1-1
                    new_line_list["part1"].append([line[i],line[i+1]])

                else:#CASE2 1-2
                    #处理x_target1分界线
                    y_x_target1 = contact_point_cal_x(x1,y1,x2,y2,x_target1)
                    new_line_list["contact1"].append(y_x_target1)
                    if not rev:
                        new_line_list["part1"].append([line[i],(x_target1,y_x_target1)])
                    else:
                        new_line_list["part1"].append([line[i+1],(x_target1,y_x_target1)])
                    

                    if x_target2<=x2:
                        #处理x_target2分界线
                        y_x_target2 = contact_point_cal_x(x1,y1,x2,y2,x_target2)
                        new_line_list["contact2"].append(y_x_target2)
                        if not rev:
                            new_line_list["part1"].append([line[i],(x_target1,y_x_target1)])
                            new_line_list["part2"].append([(x_target1,y_x_target1),(x_target2,y_x_target2)])
                            new_line_list["part3"].append([(x_target2,y_x_target2),line[i+1]])
                        else:
                            new_line_list["part1"].append([line[i+1],(x_target1,y_x_target1)])
                            new_line_list["part2"].append([(x_target1,y_x_target1),(x_target2,y_x_target2)])
                            new_line_list["part3"].append([(x_target2,y_x_target2),line[i]])
                    else:
                        if not rev:   
                            new_line_list["part2"].append([(x_target1,y_x_target1),line[i+1]])
                        else:
                            new_line_list["part2"].append([(x_target1,y_x_target1),line[i]])
                            
            elif x_target1<= x1 <x_target2: 
                if x2 < x_target2: #CASE4 2-2
                    new_line_list["part2"].append([line[i],line[i+1]])

                else: #CASE5 2-3
                    y_x_target2 = contact_point_cal_x(x1,y1,x2,y2,x_target2)
                    new_line_list["contact2"].append(y_x_target2)
                    if not rev:
                        new_line_list["part2"].append([line[i],(x_target2,y_x_target2)])
                        new_line_list["part3"].append([(x_target2,y_x_target2),line[i+1]])
                    else:
                        new_line_list["part2"].append([line[i+1],(x_target2,y_x_target2)])
                        new_line_list["part3"].append([(x_target2,y_x_target2),line[i]])

                    
            else:#CASE6 3-3
                new_line_list["part3"].append([line[i],line[i+1]])
            
    new_line_list["contact1"] = sorted(new_line_list["contact1"])
    new_line_list["contact2"] = sorted(new_line_list["contact2"])

    return new_line_list


def line_spliter_vertical(line_list,y_target1,y_target2):
    #part1,2,3 为分区图像，contact1，2 为交界点
    new_line_list= {"part1":[],"part2":[],"part3":[],"contact1":[],"contact2":[]}
    for line in line_list:
        for i in range(len(line)-1):
            if line[i][1] < line[i+1][1]:
                rev = False
                x1,y1 = line[i]
                x2,y2 = line[i+1]
            else:
                rev = True
                x1,y1 = line[i+1]
                x2,y2 = line[i]

            #y_target1 contact point 没handle
            if y1<y_target1:
                if y2 < y_target1: #CASE1 1-1
                    new_line_list["part1"].append([line[i],line[i+1]])

                else:#CASE2 1-2
                    #处理y_target1分界线
                    x_y_target1 = contact_point_cal_y(x1,y1,x2,y2,y_target1)
                    new_line_list["contact1"].append(x_y_target1)
                    if not rev:
                        new_line_list["part1"].append([line[i],(x_y_target1,y_target1)])
                    else:
                        new_line_list["part1"].append([line[i+1],(x_y_target1,y_target1)])
                    

                    if y_target2<=y2:
                        #处理y_target2分界线
                        x_y_target2 = contact_point_cal_y(x1,y1,x2,y2,y_target2)
                        new_line_list["contact2"].append(x_y_target2)
                        if not rev:
                            new_line_list["part1"].append([line[i],(x_y_target1, y_target1)])
                            new_line_list["part2"].append([(x_y_target1, y_target1),(x_y_target2, y_target2)])
                            new_line_list["part3"].append([(x_y_target2, y_target2),line[i+1]])
                        else:
                            new_line_list["part1"].append([line[i+1],(x_y_target1,y_target1)])
                            new_line_list["part2"].append([(x_y_target1, y_target1),(x_y_target2, y_target2)])
                            new_line_list["part3"].append([(x_y_target2, y_target2),line[i]])
                    else:
                        if not rev:   
                            new_line_list["part2"].append([(x_y_target1,y_target1),line[i+1]])
                        else:
                            new_line_list["part2"].append([(x_y_target1,y_target1),line[i]])
                            
            elif y_target1<= y1 <y_target2: 
                if y2 < y_target2: #CASE4 2-2
                    new_line_list["part2"].append([line[i],line[i+1]])

                else: #CASE5 2-3
                    x_y_target2 = contact_point_cal_y(x1,y1,x2,y2,y_target2)
                    new_line_list["contact2"].append(x_y_target2)
                    if not rev:
                        new_line_list["part2"].append([line[i],(x_y_target2, y_target2)])
                        new_line_list["part3"].append([(x_y_target2, y_target2),line[i+1]])
                    else:
                        new_line_list["part2"].append([line[i+1],(x_y_target2, y_target2)])
                        new_line_list["part3"].append([(x_y_target2,y_target2,),line[i]])

                    
            else:#CASE6 3-3
                new_line_list["part3"].append([line[i],line[i+1]])
            
    new_line_list["contact1"] = sorted(new_line_list["contact1"])
    new_line_list["contact2"] = sorted(new_line_list["contact2"])

    return new_line_list



                        
                        

                        
                    
