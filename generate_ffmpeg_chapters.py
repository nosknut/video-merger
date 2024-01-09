import os
import math
import shutil
import subprocess
from os.path import join, basename
from moviepy.editor import VideoFileClip

def get_duration(file):
    clip = VideoFileClip(file)
    return math.ceil(clip.duration) * 1000

def get_chapters(files):
    chapters = []
    t = 0
    for i, file in enumerate(files):
        title = basename(file).split(".")[0]
        duration = get_duration(file)
        chapter = {
                "file": file,
                "title": title,
                "duration": duration,
                "start": t,
                "end": t + duration,
            }
        chapters.append(chapter)
        t += duration + 1
        print(f"Found chapter {i}/{len(files)} {title}")
    return chapters

def create_chapter_metadata(files):
    chapters = get_chapters(files)
    chapter_metadata = ""
    for chapter in chapters:
        chapter_metadata += "\n"
        chapter_metadata += f"[CHAPTER]\n"
        chapter_metadata += f"TIMEBASE=1/1000\n"
        chapter_metadata += f"START={chapter.get("start")}\n"
        chapter_metadata += f"END={chapter.get("end")}\n"
        chapter_metadata += f"title={chapter.get("title")}\n"
    return chapter_metadata

def append_chapters_to_meta(
    source_dir="dist/renamed",
    meta_path="dist/meta/FFMETADATAFILE.txt",
    out_path="dist/meta/FFMETADATAFILE_WITH_CHAPTERS.txt"
):
    files = [join(source_dir, file) for file in os.listdir(source_dir)]
    chapter_metadata = create_chapter_metadata(files)
    shutil.copy(meta_path, out_path)
    with open(out_path, "a") as f:
        f.write(chapter_metadata)

def dump_metadata(source_path="dist/joined/joined.mp4", meta_path="dist/meta/FFMETADATAFILE.txt"):
    # https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            source_path,
            "-f",
            "ffmetadata",
            meta_path,
            "-y",
        ]
    )
    
if __name__ == "__main__":
    dump_metadata()
    append_chapters_to_meta()
