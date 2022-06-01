import random
import json
import sys

words =['aircraft carrier', 'airplane', 'alarm clock', 'ambulance', 'ant', 'anvil', 'apple', 'arm', 'axe',
        'backpack', 'banana', 'bandage', 'barn', 'baseball', 'baseball bat', 'basket', 'basketball', 'bat', 'bathtub',
        'beach', 'bear', 'beard', 'bed', 'bee', 'belt', 'bench', 'bicycle', 'binoculars', 'bird', 'birthday cake',
        'blackberry', 'blueberry', 'book', 'boomerang', 'bowtie', 'bracelet', 'brain', 'bread', 'bridge', 'broccoli',
        'broom', 'bucket', 'bulldozer', 'bus', 'bush', 'butterfly', 'cactus', 'cake', 'calculator', 'calendar',
        'camel',
        'camera', 'camouflage', 'campfire', 'candle', 'cannon', 'canoe', 'car', 'carrot', 'castle', 'cat',
        'ceiling fan',
        'cello', 'cell phone', 'chair', 'chandelier', 'church', 'clarinet', 'clock', 'cloud', 'coffee cup', 'compass',
        'computer', 'cookie', 'cooler', 'couch', 'cow', 'crab', 'crayon', 'crocodile', 'crown', 'cruise ship', 'cup',
        'diamond', 'dishwasher', 'dog', 'dolphin', 'donut', 'dresser', 'drill', 'drums', 'duck', 'dumbbell', 'ear',
        'elephant', 'eraser', 'eye', 'eyeglasses', 'face', 'fan', 'feather', 'fence', 'finger', 'fire hydrant',
        'firetruck', 'fish', 'flamingo', 'flashlight', 'flip flops', 'floor lamp', 'flower', 'foot', 'fork', 'frog',
        'frying pan', 'garden', 'garden hose', 'giraffe', 'golf club', 'grapes', 'grass', 'guitar', 'hamburger',
        'hammer', 'hand', 'harp', 'hat', 'headphones', 'hedgehog', 'helicopter', 'helmet', 'hockey puck',
        'hockey stick',
        'horse', 'hospital', 'hot air balloon', 'hot dog', 'hot tub', 'hourglass', 'house', 'house plant', 'ice cream',
        'jacket', 'kangaroo', 'key', 'keyboard', 'knife', 'ladder', 'lantern', 'laptop', 'leaf', 'leg', 'light bulb',
        'lighter', 'lighthouse', 'lion', 'lipstick', 'lobster', 'lollipop', 'mailbox', 'marker', 'microphone',
        'microwave', 'monkey', 'moon', 'mosquito', 'motorbike', 'mountain', 'mouth', 'mug', 'mushroom', 'nail',
        'necklace', 'nose', 'octopus', 'onion', 'oven', 'owl', 'paintbrush', 'paint can', 'palm tree', 'panda',
        'pants',
        'paper clip', 'parachute', 'parrot', 'passport', 'peanut', 'pear', 'peas', 'pencil', 'penguin', 'piano',
        'pickup truck', 'picture frame', 'pig', 'pillow', 'pineapple', 'pizza', 'pliers', 'police car', 'pool',
        'popsicle', 'postcard', 'potato', 'purse', 'rabbit', 'raccoon', 'radio', 'rain', 'rainbow', 'rake',
        'rhinoceros',
        'rifle', 'roller coaster', 'rollerskates', 'sailboat', 'sandwich', 'saw', 'saxophone', 'school bus',
        'scorpion', 'screwdriver', 'sea turtle', 'see saw', 'shark', 'sheep', 'shoe', 'shorts', 'shovel', 'sink',
        'sleeping bag', 'snail', 'snake', 'snorkel', 'snowflake', 'snowman', 'soccer ball', 'sock', 'speedboat',
        'spider', 'spoon', 'squirrel', 'star', 'steak', 'stereo', 'stove', 'strawberry', 'streetlight', 'submarine',
        'suitcase', 'sun', 'swan', 'sweater', 'swing set', 'sword', 'syringe', 'table', 'teapot', 'teddy-bear',
        'telephone', 'television', 'tennis racquet', 'tent', 'tiger', 'toaster', 'toilet', 'tooth', 'toothbrush',
        'toothpaste', 'tractor', 'traffic light', 'train', 'tree', 'trombone', 'truck', 'trumpet', 't-shirt',
        'umbrella', 'underwear', 'van', 'violin', 'washing machine', 'watermelon', 'whale', 'wheel', 'wine bottle',
        'zebra'
    ]




def combine(sentence):

    a = None
    b = None
    s = sentence.split()
    for ele in s:
        if ele in words and a is None:
            a = ele
        elif ele in words:
            b = ele

    if (a and b):
        print("Y")
    elif (a):
        print(str(a))
    else:
        print("N")


combine(str(sys.argv[1]))


