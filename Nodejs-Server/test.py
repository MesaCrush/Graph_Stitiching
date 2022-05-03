
#这是主程序

import json
from PIL import Image, ImageDraw
#调用combiner里面的selector去筛选
from combiner import selector

def draw(image,canvas,p1,p2,p3):
   for polyline in p1:
      canvas.line([tuple(item) for item in polyline],fill=(0, 0, 0),width=3)

   for polyline in p2:
      canvas.line([tuple(item) for item in polyline],fill=(0, 0, 0),width=3)

   for polyline in p3:
      canvas.line([tuple(item) for item in polyline],fill=(0, 0, 0),width=3)

   # display image
   image.show()





# read ndjson lines
lines = open('horizon_partition/horizon_partition_banana.json','r').readlines()
# 中间要插入的文件类
target_filename = 'horizon_partition/horizon_partition_airplane.json'
lines2 = open(target_filename,'r').readlines()
# grab the first line, JSON parse it and fetch the 'drawing' array



#initial picture
image1 = json.loads(lines[0])

#选合适中间插入的图
mid_image_num = selector(image1,target_filename)
print(mid_image_num)



raw_drawing = image1
pil_img1 = Image.new("RGB", (240, 270), (255,255,255))
cav1 = ImageDraw.Draw(pil_img1)
# original graph 1
draw(pil_img1,cav1,raw_drawing["part1"],raw_drawing["part2"],raw_drawing["part3"])




raw_drawing2 = json.loads(lines2[mid_image_num])

#part2 = modifier(image1["contact1"],image1["contact2"],raw_drawing2)

#print('before',raw_drawing)
# zip x,y coordinates for each point in every polyline
#polylines = [list(zip(polyline[0], polyline[1])) for polyline in raw_drawing]
# notice how the data is shuffled to (x1,y1),(x2,y2) order
#print('after',polylines)
#polylines = [sorted(polyline)for polyline in polylines]
#print('sort',polylines)

# make a new image

pil_img2 = Image.new("RGB", (240, 270), (255,255,255))
pil_imgc = Image.new("RGB", (240, 270), (255,255,255))
# get a drawing context
cav2 = ImageDraw.Draw(pil_img2)
cavc = ImageDraw.Draw(pil_imgc)


new_line_dict2 = raw_drawing2

new_line_dict = raw_drawing
# render each polyline



# original matched graph
draw(pil_img2,cav2,raw_drawing2["part1"],raw_drawing2["part2"],raw_drawing2["part3"])

# combined graph
draw(pil_imgc,cavc,raw_drawing["part1"],raw_drawing2["part2"],raw_drawing["part3"])

