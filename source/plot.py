import numpy as np
import cv2 # opencv for drawing

class layer:
    def __init__(self):
        self.name = "NEW_LAYER"
        self.orientation = "NONE"
        self.restriction = 0

layers = []

f = open('test.in')
data = f.readlines()
f.close()
# create an image
#img = np.zeros((1024, 1024, 3), np.uint8)
reading_layers = 0
reading_tracks = 0

for line in data:
    token = line.split(' ')

    # DESIGN BOUNDARY
    if token[0] == 'DESIGN_BOUNDARY':
        #print(token[i+1], token[i+2])
        x1 = int(token[1].replace("(", ""))
        y1 = int(token[2].replace(")", ""))
        x2 = int(token[3].replace("(", ""))
        y2 = int(token[4].replace(")", ""))
        #print(x1, y1, x2, y2)
        #print(x2-x1, y2-y1)

    # LAYERS
    elif token[0] == 'LAYERS':
        reading_layers = 1
        n_layers = int(token[1])
        #print(n_layers)
    elif reading_layers == 1:
        #print(token)
        if token[0] == 'ENDLAYERS\n':
            reading_layers = 0
            continue # jump to next line
        for i in range(n_layers):
            #token = line.split(' ')
            #print(token)
            new_layer = layer() # init a struct (or class) layer
            new_layer.name = token[0]
            new_layer.orientation = token[1]
            new_layer.restriction = int(token[2].replace("\n", ""))
            layers.append(new_layer)
    elif token[0] == 'TRACKS':
        reading_tracks = int(token[1])
        #print(n_tracks)
        continue
    elif reading_tracks != 0:
        reading_tracks += -1


    #new_layer = np.zeros((x2-x1, y2-y1, 3), np.uint8)




    #cv2.rectangle(img, (x1, y1), (x2, y2), (0, 50, 0), -1)
    #print(line.split(' '))



#cv2.imshow('image', img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
