import cv2
import time
capture = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarCascadeXML.xml')
def hasFace():
	ret, frame = capture.read()
	time.sleep(.1)
	ret, frame = capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	detected, gray = detect(gray)
	cv2.imwrite('img.jpg', gray)
	return detected

def detect(image):
	val = False
	faces = cascade.detectMultiScale(
	    image,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE)

	if faces:
		print('true!')
		val = True
	else:
		print('false')
	print(type(faces))
	print(faces)
	return val, image
hasFace()
capture.release()