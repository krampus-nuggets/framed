import cv2 as cv
from progress.spinner import Spinner
from modules.banners import print_banner

def extract_frames(video_file, output_dir):
    frames = 0
    proc_state = False
    spinner = Spinner("Processing Frames: ")
    video_capture = cv.VideoCapture(video_file)

    if not video_capture.isOpened():
        print_banner("single", "header-start")
        print("ERROR: Cannot read video file")
        return False

    while True:
        ret, frame = video_capture.read()

        if not ret:
            print_banner("single", "header-start")
            print("ERROR: Can't receive frame")
            proc_state = False
            break

        str_frame = str(frames)
        file_name = f"{output_dir}\\{str_frame.zfill(10)}-video-frame.jpg"
        cv.imwrite(file_name, frame)
        proc_state = True
        spinner.next()
        frames += 1

    video_capture.release()
    cv.destroyAllWindows()

    return proc_state
