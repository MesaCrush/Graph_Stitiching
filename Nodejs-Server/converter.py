#这个用来分开左中右的具体运行代码，被file——converter调用，然后确定交点

def contact_point_cal_x(x1,y1,x2,y2,c):
    k = (float(y2)-y1)/(x2-x1) #斜率
    yt = y1+ (c-x1)*k
    return round(yt,1)

def contact_point_cal_y(x1,y1,x2,y2,c):
    k = (float(x2)-x1)/(y2-y1) #斜率
    xt = x1+ (c-y1)*k
    return round(xt,1)


def line_spliter_horizon(line_list):
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

            #85 contact point 没handle
            if x1<85:
                if x2 < 85: #CASE1 1-1
                    new_line_list["part1"].append([line[i],line[i+1]])

                else:#CASE2 1-2
                    #处理85分界线
                    y_85 = contact_point_cal_x(x1,y1,x2,y2,85)
                    new_line_list["contact1"].append(y_85)
                    if not rev:
                        new_line_list["part1"].append([line[i],(85,y_85)])
                    else:
                        new_line_list["part1"].append([line[i+1],(85,y_85)])
                    

                    if 170<=x2:
                        #处理170分界线
                        y_170 = contact_point_cal_x(x1,y1,x2,y2,170)
                        new_line_list["contact2"].append(y_170)
                        if not rev:
                            new_line_list["part1"].append([line[i],(85,y_85)])
                            new_line_list["part2"].append([(85,y_85),(170,y_170)])
                            new_line_list["part3"].append([(170,y_170),line[i+1]])
                        else:
                            new_line_list["part1"].append([line[i+1],(85,y_85)])
                            new_line_list["part2"].append([(85,y_85),(170,y_170)])
                            new_line_list["part3"].append([(170,y_170),line[i]])
                    else:
                        if not rev:   
                            new_line_list["part2"].append([(85,y_85),line[i+1]])
                        else:
                            new_line_list["part2"].append([(85,y_85),line[i]])
                            
            elif 85<= x1 <170: 
                if x2 < 170: #CASE4 2-2
                    new_line_list["part2"].append([line[i],line[i+1]])

                else: #CASE5 2-3
                    y_170 = contact_point_cal_x(x1,y1,x2,y2,170)
                    new_line_list["contact2"].append(y_170)
                    if not rev:
                        new_line_list["part2"].append([line[i],(170,y_170)])
                        new_line_list["part3"].append([(170,y_170),line[i+1]])
                    else:
                        new_line_list["part2"].append([line[i+1],(170,y_170)])
                        new_line_list["part3"].append([(170,y_170),line[i]])

                    
            else:#CASE6 3-3
                new_line_list["part3"].append([line[i],line[i+1]])
            
    new_line_list["contact1"] = sorted(new_line_list["contact1"])
    new_line_list["contact2"] = sorted(new_line_list["contact2"])

    return new_line_list



                        
                        

                        
                    
