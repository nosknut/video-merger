import os
import subprocess
from os.path import join, dirname


def generate_mylist(source_dir="dist/renamed", mylist_path="dist/meta/mylist.txt"):
    cwd = os.getcwd()
    source_files = [join(cwd, source_dir, file) for file in os.listdir(source_dir)]
    source_files.sort()
    mylist = "\n".join([f"file '{file}'" for file in source_files])
    os.makedirs(dirname(mylist_path), exist_ok=True)
    with open(mylist_path, "w") as f:
        f.write(mylist)


def join_videos(
    mylist_path="dist/meta/mylist.txt", output_path="dist/joined/joined.mp4"
):
    os.makedirs(dirname(output_path), exist_ok=True)
    # https://trac.ffmpeg.org/wiki/Concatenate
    subprocess.run(
        [
            "ffmpeg",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            mylist_path,
            "-c",
            "copy",
            output_path,
            "-y",
        ],
    )


if __name__ == "__main__":
    generate_mylist()
    join_videos()
