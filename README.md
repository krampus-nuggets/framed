<p align="center">
<img src="https://res.cloudinary.com/wemakeart/image/upload/v1633016783/github-projects/framed/framed-gif_uncnqm.gif" width=150px height="150px"  alt="docs-icon"/>
</p>

# FRAMED

---

FRAMED is a simple tool for converting a video file to individual frames. This tool was created for processing videos into frames so that the images can be fed into **labelImg** for image annotation. The processed images will then be ready for ingest when training with **YOLO v5**.

**NOTE** - This tool does not set dimensions so you'll have to set your video dimensions before hand (ex. 640x640)

## Usage

---

<p align="center">
<img src="https://res.cloudinary.com/wemakeart/image/upload/v1633018505/github-projects/framed/45_mkferb.png" width=100%  alt="docs-icon"/>
</p>

1. Clone the repository and install the requirements.txt file (*Create a venv first*)
2. Run the program - *py main.py*
3. The program will create the following directories in the cwd - *data/footage* & *data/frames*
4. It will auto-detect any **MP4** video files in the *data/footage* directory and display it in the CLI
5. Select a video to process and a progress spinner will appear, wait till it completes
6. Once completed all the frames from the video will be in the *data/frames/<video-name>* directory

**Example** - [Video Link](https://res.cloudinary.com/wemakeart/video/upload/v1633018666/github-projects/framed/framed-example_vq5xrn.mp4)