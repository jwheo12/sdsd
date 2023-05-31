import cv2
import os

image_folder = '/workspace/sdsd/stable-diffusion-webui/outputs/mov2mov-images/2023-05-30'  # 이미지 폴더 경로
video_name = 'output_video.mp4'  # 출력되는 동영상 파일명

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg") or img.endswith(".png")]
images.sort()

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, cv2.VideoWriter_fourcc(*'mp4v'), 30, (width, height))

for image in images:
    frame = cv2.imread(os.path.join(image_folder, image))
    video.write(frame)

cv2.destroyAllWindows()
video.release()
