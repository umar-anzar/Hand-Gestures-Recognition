import cv2, uuid, os, time
IMGS_PATH = 'Tensorflow/workspace/images/capturedImages'
labels = ['ThankYou']#['Hello', 'Yes', 'No', 'ILoveYou','GoodJob','ThankYou']
number_of_imgs = 20
for label in labels:
    command = f'cmd /c "mkdir Tensorflow\workspace\images\capturedImages\{label}"'
    os.system(command)
    cap = cv2.VideoCapture(1)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    for imgnum in range(number_of_imgs):
        ret, frame = cap.read()
        imgname = os.path.join(IMGS_PATH, label, label+'.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imgname, frame)
        cv2.imshow('frame', frame)
        print(f"{imgnum}")
        time.sleep(2)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
