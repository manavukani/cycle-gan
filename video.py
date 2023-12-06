import cv2
from style_converter import stylise

video_capture = cv2.VideoCapture('my_video.mp4')

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = video_capture.get(cv2.CAP_PROP_FPS)
frame_size = (640, 480)


out = cv2.VideoWriter('processed_video.mp4', fourcc, fps, frame_size)

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    processed_frame = stylise(frame)

    out.write(processed_frame)

    cv2.imshow('Processed Frame', processed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
out.release()
cv2.destroyAllWindows()
