import os
import sys
import time
from modules.banners import print_banner
from modules.extract_video_frames import extract_frames
from modules.helpers import check_dir, video_list, invalid_option


working_dir = str(os.path.dirname(os.path.abspath(__file__)))

required_directories = [
    "\\data\\footage",
    "\\data\\frames"
]

absolute_directories = [working_dir + directory for directory in required_directories]

for directory in range(len(absolute_directories)):
    check_dir(absolute_directories[directory])

def main():
    video_names = video_list(absolute_directories[0])

    print_banner("double", "header-start", "user-options")

    user_selection = input("Please enter your selection below:\n")

    if user_selection == "1":
        print_banner("single", "header-start")
        print("All video files listed below:\n")

        for video in range(len(video_names)):
            print(f"{video + 1}. {video_names[video]}")

        user_selection = input("\nPlease enter your selection below:\n")

        try:
            print_banner("single", "header-start")

            project_name = f"\\{video_names[int(user_selection) - 1]}"
            video_file = absolute_directories[0] + project_name
            project_directory = absolute_directories[1] + project_name.replace(".mp4", "")

            check_dir(project_directory)

            if extract_frames(video_file, project_directory):
                print_banner("single", "header-start")
                print("PROC: Frame extraction completed | Program Reset")
                time.sleep(2)
                main()
            else:
                invalid_option(main, "ERROR: Frame extraction failed | Program Reset")

        except IndexError:
            invalid_option(main, "ERROR: Invalid option selected | Program Reset")
        except ValueError:
            invalid_option(main, "ERROR: Invalid option selected | Program Reset")

    elif user_selection == "2":
        print_banner("single", "header-stop")
        print("Closing program...")
        sys.exit(0)
    else:
        invalid_option(main, "ERROR: Invalid option selected | Program Reset")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_banner("single", "header-stop")
        print("Closing program...")
        sys.exit(0)
