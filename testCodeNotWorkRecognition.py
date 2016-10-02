# Append the images with the extension .sad into image_paths 
image_paths = [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.sad')] 
for image_path in image_paths: 
predict_image_pil = Image.open(image_path).convert('L') 
predict_image = np.array(predict_image_pil, 'uint8') 
faces = faceCascade.detectMultiScale(predict_image) 
for (x, y, w, h) in faces: 
	nbr_predicted, conf = recognizer.predict(predict_image[y: y + h, x: x + w]) 
	nbr_actual = int(os.path.split(image_path)[1].split(".")[0].replace("subject", "")) 
	if nbr_actual == nbr_predicted: 
		print "{} is Correctly Recognized with confidence {}".format(nbr_actual, conf) 
	else: 
		print "{} is Incorrectly Recognized as {}".format(nbr_actual, nbr_predicted) 
	cv2.imshow("Recognizing Face", predict_image[y: y + h, x: x + w]) 
	cv2.waitKey(1000)