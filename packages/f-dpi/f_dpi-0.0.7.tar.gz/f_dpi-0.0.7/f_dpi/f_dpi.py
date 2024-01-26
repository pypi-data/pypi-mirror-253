import os
import cv2
from PIL import Image, ImageDraw
import numpy as np

def test():
	print('test success')

def imshow(img):
    cv2.imshow('image', img)
    cv2.waitKey() 
    cv2.destroyAllWindows()

def macshow(img):
    _img = copy.deepcopy(img)
    p_img = Image.fromarray(_img)
    p_img.show()

def imgload(Imgpath):
    img = cv2.imread(Imgpath)
    if img is None:
        img = Image.open(Imgpath)
        img = cv2.cvtColor(np.uint8(img), cv2.COLOR_BGR2RGB)
    return img

def imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None

def imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def webcam(Index):
    cap = cv2.VideoCapture(Index)
    while cap.isOpened():
        
        ret, frame = cap.read()
        cv2.imshow('image', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release()
    cv2.destroyAllWindows()