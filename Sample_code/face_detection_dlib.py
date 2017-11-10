import dlib
import cv2


def detectFact(gray_img, orig_img):
    detector = dlib.get_frontal_face_detector()
    dects = detector(gray_img, 1)    
    for i,rect in enumerate(dects):
        left,right,top,bottom = rect.left(),rect.right(),rect.top(),rect.bottom()
        cv2.rectangle(orig_img,(left,top),(right,bottom),0,0,255)

    return orig_img

def getVideoFrame():
    capture = cv2.VideoCapture(0)
#    capture = skvideo.io.vread(0)
    cnt = 0
    while True:
        ret, frame = capture.read()   
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
        frame = detectFact(gray, frame)

        cv2.imshow('Video',frame)
        if cv2.waitKey(10)&0xff == ord('q'):
            break
        cnt += 1
    capture.release()
    cv2.destroyAllWindows()  

if __name__ == '__main__':
    getVideoFrame()
