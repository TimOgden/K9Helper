import cv2
import time
capture = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier('haarCascadeXML.xml')

def hasFace(display=False):
	ret, frame = capture.read()
	if not ret:
		time.sleep(.1)
		ret, frame = capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	detected, gray = detect(gray, display=display)
	cv2.imwrite('img.jpeg', gray)
	
	cv2.destroyAllWindows()
	return detected

def detect(image, display=False):
	val = False
	if type(image) is str:
		image = cv2.imread(image, 0)
	faces = cascade.detectMultiScale(
	    image,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE)

	if len(faces)>0:
		val = True
		# Draw a rectangle around the faces
		for (x, y, w, h) in faces:
			cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
			if display:
				if len(faces) == 1:
					cv2.imshow('Found 1 face!', image)
				else:
					cv2.imshow('Found {} faces!'.format(len(faces)), image)
				cv2.waitKey(3000)
		
	return val, image

def close():
	capture.release()

#hasFace(True)


#detect('face.jpeg')