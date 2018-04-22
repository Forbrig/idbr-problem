import numpy as np
import cv2 # opencv for drawing

class track:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.constraint = 0

class layer:
    def __init__(self):
        self.name = "NEW_LAYER"
        self.orientation = "NONE"
        self.restriction = 0
        self.tracks = []

class design_boundary:
    def __init__(self):
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0
        self.layers = []

#class bit:

#class bus:


design_boundary = design_boundary()

f = open('test.in')
data = f.readlines()
f.close()
# create an image
#img = np.zeros((1024, 1024, 3), np.uint8)
reading_layers = 0
reading_tracks = 0
reading_buses = 0

for line in data:
    token = line.split(' ')

    # DESIGN BOUNDARY
    if token[0] == 'DESIGN_BOUNDARY':
        design_boundary.x1 = int(token[1].replace("(", ""))
        design_boundary.y1 = int(token[2].replace(")", ""))
        design_boundary.x2 = int(token[3].replace("(", ""))
        design_boundary.y2 = int(token[4].replace(")", ""))
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
            design_boundary.layers.append(new_layer)
    elif token[0] == 'TRACKS':
        reading_tracks = int(token[1])
        #print(n_tracks)
        continue
    elif reading_tracks != 0:
        reading_tracks += -1
        for layer in design_boundary.layers[:]: # iterator of layer in layers list
            if token[0] == layer.name: # search for the layer that we want
                new_track = track() # create a nre track class
                new_track.x1 = int(token[1].replace("(", ""))
                new_track.y1 = int(token[2].replace(")", ""))
                new_track.x2 = int(token[3].replace("(", ""))
                new_track.y2 = int(token[4].replace(")", ""))
                new_track.constraint = int(token[5])
                #print(new_track.x1, new_track.y1, new_track.x2, new_track.y2)
                layer.tracks.append(new_track) # insert track on the layer list of that layer
                break
    elif token[0] == 'ENDTRACKS\n':
        continue
    #elif reading_buses != 0:

    #new_layer = np.zeros((x2-x1, y2-y1, 3), np.uint8)




    #cv2.rectangle(img, (x1, y1), (x2, y2), (0, 50, 0), -1)
    #print(line.split(' '))

for layer in design_boundary.layers[:]:
    new_image = np.zeros((design_boundary.x2 - design_boundary.x1, design_boundary.y2 - design_boundary.y1, 3), np.uint8)
    for track in layer.tracks[:]:
        cv2.line(new_image, (track.x1, track.y1), (track.x2, track.y2), (0, 200, 40), track.constraint)

    cv2.imshow('image', new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
