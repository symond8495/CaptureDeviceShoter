import cv2
import datetime

# VideoCapture オブジェクトを取得
# キャプボの他にWebカメラなど接続している場合は他の数字を指定する必要があるかも
# 0: AVerMedia
# 3: OBS Virtual Camera
capture = cv2.VideoCapture(0)
print(capture.isOpened())
capture.set(3, 1920)
capture.set(4, 1080)

ret, frame = capture.read()
dt_now = datetime.datetime.now()
cv2.imwrite('photo/' + dt_now.strftime('%Y%m%d-%H%M%S') +
            '.jpg', frame)

capture.release()
cv2.destroyAllWindows()
