import json
from converter import line_spliter_horizon

# read ndjson lines
lines = open('ndjson/full_simplified_dolphin.ndjson','r').readlines()
filename = "horizon_partition/horizon_partition_" + json.loads(lines[0])['word'] + ".json"
write_file = open(filename,"w")

summary = {}

for i in range(len(lines)):
    # grab the first line, JSON parse it and fetch the 'drawing' array
    raw_drawing = json.loads(lines[i])['drawing']

    # zip x,y coordinates for each point in every polyline shuffled to (x1,y1),(x2,y2) order
    polylines = [list(zip(polyline[0], polyline[1])) for polyline in raw_drawing]


    # parse to horisontal 3 phase data
    new_line_dict = line_spliter_horizon(polylines)
    
    num_contact1 = len(new_line_dict["contact1"])
    num_contact2 = len(new_line_dict["contact2"])

    if num_contact1 in summary.keys():
        if num_contact2 in (summary[num_contact1]).keys():
            summary[num_contact1][num_contact2].append(i)
        else:
            summary[num_contact1][num_contact2] = [i]
    else:
        summary[num_contact1] = {}
        summary[num_contact1][num_contact2] = [i]

    json_string = json.dumps(new_line_dict)

    json_string += "\n"

    write_file.write(json_string)

summary_string  = json.dumps(summary)
write_file.write(summary_string)

write_file.close()

