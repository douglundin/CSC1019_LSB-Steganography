from LSBSteg import LSBSteg
import cv2

#Text encoding:

#encoding
try:
    steg = LSBSteg(cv2.imread("original.png"))
    img_encoded = steg.encode_text("Embedding a secret message, Hello World!")
    cv2.imwrite("encoded.png", img_encoded)
except: # catch *all* exceptions
    exit(1)


#decoding
try:
    im = cv2.imread("encoded.png")
    steg = LSBSteg(im)
    print("Text value:",steg.decode_text())
except: # catch *all exceptions
    exit(2)
