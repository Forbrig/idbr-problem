import numpy as np
import cv2 # opencv for drawing

f = open('test.in')

data = f.readlines()

# create an image
#img = np.zeros((1024, 1024, 3), np.uint8)

for line in data:
    token = line.split(' ')
    # DESIGN BOUNDARY
    for i in range(len(token)):
        if token[i] == 'DESIGN_BOUNDARY':
            #print(token[i+1], token[i+2])
            x1 = int(token[i+1].replace("(", ""))
            y1 = int(token[i+2].replace(")", ""))
            x2 = int(token[i+3].replace("(", ""))
            y2 = int(token[i+4].replace(")", ""))
            #print(x1, y1, x2, y2)
            print(x2-x1, y2-y1)
            img = np.zeros((x2-x1, y2-y1, 3), np.uint8)

    # LAYERS

            #cv2.rectangle(img, (x1, y1), (x2, y2), (0, 50, 0), -1)
    #print(line.split(' '))



cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
