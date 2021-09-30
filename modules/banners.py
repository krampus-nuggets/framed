from os import system


banners = {
    "header-start": """
 ____ ____ ____ ____ ____ ____ 
||F |||R |||A |||M |||E |||D ||
||__|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/__\|/__\|
by: krampus-nuggets
    """,
    "header-stop": """
 ____ ____ ____ 
||B |||Y |||E ||
||__|||__|||__||
|/__\|/__\|/__\|
    """,
    "user-options": """
All available options listed below:

1. Extract frames from video files
2. Close program
    """
}

def print_banner(ban_type, *banner):
    if ban_type == "single":
        system("cls")
        print(banners[banner[0]])
    elif ban_type == "double":
        system("cls")
        print(banners[banner[0]])
        print(banners[banner[1]])
    elif ban_type == "no-clear":
        print(banners[banner[0]])