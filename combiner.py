import json

def selector(image1,filename2):
    lines = open(filename2,'r').readlines()
    # grab the first line, JSON parse it and fetch the 'drawing' array
    raw_drawing1 = image1
    summary  = json.loads(lines[-1])

    num_contact1 = len(raw_drawing1["contact1"])
    num_contact2 = len(raw_drawing1["contact2"])


    possible_combine_list = summary[str(num_contact1)][str(num_contact2)]
    for possible_combine in possible_combine_list:
        result_graph = True
        raw_drawingP = json.loads(lines[possible_combine])
        for i in range(num_contact1):
            if not abs(raw_drawing1["contact1"][i] - raw_drawingP["contact1"][i]) <= 7:
                result_graph = False
                break
        
        if result_graph:
            for i in range(num_contact2):
                if not abs(raw_drawing1["contact2"][i] - raw_drawingP["contact2"][i]) <= 7:
                    result_graph = False
                    break
        
        if result_graph:
            #don't select themself when same type
            if possible_combine != -1: #image_num
                result_graph = possible_combine
                return result_graph
            
    return None


