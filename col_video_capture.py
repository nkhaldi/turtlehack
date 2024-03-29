import cv2

det_color = 'orange'

cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

while (cap.isOpened()):
	ret, frame = cap.read()
	if (ret == True):

		cv2.imshow('frame', frame)
		frameCopy = frame.copy()

		if (det_color == 'orange'):
			min_col = (0, 175, 15)
			max_col = (12, 255, 255)
		else:
			min_col = (85, 110, 0)
			max_col = (255, 255, 255)

		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		hsv = cv2.blur(hsv, (5,5))
		mask = cv2.inRange(hsv, min_col, max_col)

		mask = cv2.erode(mask, None, iterations = 2)
		mask = cv2.dilate(mask, None, iterations = 4)

		cont = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
		cont = cont[0]
		if (cont):
			sorted(cont, key = cv2.contourArea, reverse = True)
			cv2.drawContours(frame, cont, 0, (255, 0, 255), 3)
			cv2.imshow("Contours", frame)
			for i in range(len(cont)):
				(x, y, w, h) = cv2.boundingRect(cont[i])
				cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 3)
				cv2.imshow('frame', frame)

		if (cv2.waitKey(1) & 0xFF == ord('q')):
			break
	else:
		break
cap.release()
cv2.destroyAllWindows()
