import json
import numpy as np
from PIL import Image, ImageDraw, ImageChops
#调用combiner里面的selector去筛选
from combiner import selector
from classifier import classifier
from json_converter import json_converter
from wordmap import word_cloud

def NormalizeData(data):
   return (data - np.min(data)) / (np.max(data) - np.min(data))

def draw(image,canvas,p1):

   for polyline in p1:
      canvas.line([tuple(item) for item in polyline],fill=(0, 0, 0),width=3)

   new_image = image.resize((28,28))
   new_image = new_image.convert("L")
   new_image = ImageChops.invert(new_image)
   
   img_csv = np.array(new_image)
   img_csv = NormalizeData(img_csv)
   
   
   res_csv = []
   for row in img_csv:
      res_row = []
      for item in row:
         res_row.append([item])
      res_csv.append(res_row)

   category = classifier(res_csv)
   return category[0]
   


def combiner (p1,p2,p3):
   resultarr = []
   resultarr += p1
   resultarr += p2
   resultarr += p3

   return resultarr

def main():
   # read ndjson lines
   file_data = open('temp/temp.json','r').read()
   file_data = json.loads(file_data)
   lines = file_data["text"]
   # 判断类别 获取 中间要插入的文件类
   pil_img = Image.new("RGB", (255, 255), (255,255,255)) # 生成空白画面图像
   canvas = ImageDraw.Draw(pil_img)
   category =draw(pil_img,canvas,lines)
   #print("category: ", category)
   cate_dict = ["crab","dolphin","frog","ant","fish","hedgehog","butterfly","octopus","bee","cat","lion","pnada","bear","crocodile"]
   combine_list = word_cloud(cate_dict[category])
   #combine_list.append(cate_dict[category])

   for item in combine_list:
      target_filename = 'horizon_partition/full_simplified_'+item+'.ndjson'
      lines2 = open(target_filename,'r').readlines()
      # grab the first line, JSON parse it and fetch the 'drawing' array
      raw_drawing = (json.loads(lines2[0]))["drawing"]
      image2 = [list(zip(polyline[0], polyline[1])) for polyline in raw_drawing]

      #converted picture
      x1 = file_data["select_x"]
      x2 = x1 + file_data["select_x_dist"]
      y1 = file_data["select_y"]
      y2 = y1 + file_data["select_y_dist"]
      image2 = json_converter(image2,x1,x2,y1,y2)

      image1 = json_converter(lines,x1,x2,y1,y2)

      part2 = combiner(image1["part2"]["part1"],image2["part2"]["part2"],image1["part2"]["part3"])

      new_image = combiner(image1["part1"],part2,image1["part3"])
      print(item,"+",new_image,end = "+")

   #print("finished")

main()