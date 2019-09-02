import cv2
import sys
import os.path

def detect(filename, output_filename, cascade_file = "lbpcascade_animeface.xml"):
    if not os.path.isfile(cascade_file):
        raise RuntimeError("%s: not found" % cascade_file)

    cascade = cv2.CascadeClassifier(cascade_file)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    
    faces = cascade.detectMultiScale(gray,
                                     # detector options
                                     scaleFactor = 1.1,
                                     minNeighbors = 5,
                                     minSize = (25, 25))
    i = 0
    for (x, y, w, h) in faces:
    	cropped = image[y: y+h, x: x+w]
    	cv2.imwrite(output_filename+str(i)+".png", cropped)
    	i += 1
        #cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

    #cv2.imshow("Anime Face Detection", image)
    #cv2.waitKey(0)
    #cv2.imwrite("out.png", image)

if len(sys.argv) != 3:
    sys.stderr.write("usage: detect.py <filename> <output_filename>\n")
    sys.exit(-1)
    
detect(sys.argv[1], sys.argv[2])