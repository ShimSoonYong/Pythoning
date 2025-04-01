import cv2

print("OpenCV version:", cv2.__version__)

# 웹캠 열기 (0은 기본 카메라)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # 영상 표시
    cv2.imshow("Webcam Feed", frame)

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


