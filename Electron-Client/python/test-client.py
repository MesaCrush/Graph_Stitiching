import json,os
from PIL import Image, ImageDraw
#调用combiner里面的selector去筛选

def textSplit(text):
   text = text.replace("(","[")
   text = text.replace(")","]")
   text = text[3:-3]
   temparr = text.split("]], [[")
   temparr = [item.split("], [")for item in temparr]
   resarr = []
   #print(temparr)
   for arr in temparr:
      newarr = []
      for item in arr:
         #print(item)
         try:
            x,y = item.split(",")
            newarr.append([float(x),float(y)])
         except:
            print(item)
            break
      resarr.append(newarr)

   return resarr



def draw(image,canvas,p1,number):

   for polyline in p1:
      newline = [tuple(item) for item in polyline]
      try:
         canvas.line(newline,fill=(0, 0, 0),width=3)
      except:
         #print(newline)
         print("error in drawing line")
         

   image.resize((255,255))  # 设置缩略图大小
   image.save(os.path.dirname(os.path.realpath(__file__)) + '/../images/img' + str(number) +'.jpg')
   
   # display image
   #image.show()



def main():
   # read ndjson lines
   lines = open(os.path.dirname(os.path.realpath(__file__)) + '/../Json/Recieve.json','r').readlines()
   

   #initial picture
   images =  (json.loads(lines[0]))["text"]
   images = images.strip("\n").split("+")
   images_processed = {}
   type_processed = {}
   for i in range(0,len(images)-2,2):
      the_key = "img" + str(i//2+1)
      images_processed[the_key] = textSplit(images[i+1])
      type_processed[the_key] = images[i]

   data_draw = json.dumps(images_processed)
   data_type = json.dumps(type_processed)
   with open('Json/Recieve.json', 'w') as outfile:
      outfile.write(data_draw)
   with open('Json/Recieve_type.json', 'w') as outfile:
      outfile.write(data_type)
   #Display origin image 1
   keys = list(images_processed.keys())
   for i in range(1,len(keys)+1):
      pil_img1 = Image.new("RGB", (240, 270), (255,255,255))
      cav1 = ImageDraw.Draw(pil_img1)
      draw(pil_img1,cav1,images_processed[keys[i-1]],i)
   
   # original graph 1
   
   

main()