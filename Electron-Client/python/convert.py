def json_data_convert(output_file):
    path = "F:/Denis/GraphS/Graph_Stitiching/Electron-Client/Json"
    filename = path + "/Curr_Stroke.json"
    my_open= open(filename,'r')
    infor = my_open.readlines()
    my_open.close()

    my_write = open(path+output_file, 'w')
    raw_data = infor[0]
    
    data1 = raw_data.replace('[','')
    data2 = data1.replace(']','')
    data2 += ','
    str_list = []
    while len(data2) != 0:
        comma_index = data2.find(',')
        str_list.append(float(data2[:comma_index]))
        data2 = data2[comma_index+1:]
    index = 0
    while index != len(str_list):
        my_list = ''
        my_list += str(round(str_list[index]/255,5))
        my_list += ','
        my_list += str(round(str_list[index+1]/255,5))
        my_list += ','
        my_list += '1,0'
        my_write.write(str(my_list) + '\n')
        index += 2
    return


json_data_convert('test_file.txt')