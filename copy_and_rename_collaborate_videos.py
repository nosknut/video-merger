import os
from os.path import join, basename
import shutil

def extract_collaborate_video_title(file_path):
    file_name = basename(file_path)
    title_segments = file_name.split(" ")
    title = " ".join(title_segments[3:-1])
    title += " " + title_segments[-1].split("_")[0]
    title = title.replace("  ", " ")
    title = title.strip()
    title = title[0].upper() + title[1:]
    # Replaces all ' with ` to avoid issues with ffmpeg
    title = title.replace("'", "`")
    return title

def copy_and_rename_collaborate_video(file_path, dist_dir, video_index=None):
    title = extract_collaborate_video_title(file_path)
    extension = file_path.split(".")[-1]
    new_name = f"{title}.{extension}"
    if video_index is not None:
        new_name = f"{video_index:003d} {new_name}"
    new_path = join(dist_dir, new_name)
    os.makedirs(dist_dir, exist_ok=True)
    shutil.copy(file_path, new_path)
    return new_path

def copy_and_rename_collaborate_videos(source_dir="source", dist_dir="dist/renamed"):
    source_files = [join(source_dir, file) for file in os.listdir(source_dir)]
    source_files.sort()
    for i, file in enumerate(source_files):
        copy_and_rename_collaborate_video(file, dist_dir, video_index=i)

if __name__ == "__main__":
    copy_and_rename_collaborate_videos()