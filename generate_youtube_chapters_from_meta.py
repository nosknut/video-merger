import math
import os
from os.path import dirname


def seconds_to_timestamp(seconds):
    hours = math.floor(seconds / 3600e3)
    minutes = math.floor((seconds - hours * 3600e3) / 60e3)
    seconds = math.floor((seconds - hours * 3600e3 - minutes * 60e3) / 1e3)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def get_titles(meta_lines):
    titles = []
    for line in meta_lines:
        if line.startswith("title="):
            title = line.split("=")[1]
            titles.append(title)
    return titles


def get_start_times(meta_lines):
    start_times = []
    for line in meta_lines:
        if line.startswith("START="):
            start_time = int(line.split("=")[1])
            start_times.append(start_time)
    return start_times


def generate_youtube_chapters_from_meta(
    meta_path="dist/meta/FFMETADATAFILE_WITH_CHAPTERS.txt",
    out_path="dist/meta/youtube_chapters.txt",
):
    """Generates youtube chapters from an ffmpeg metadata file."""

    with open(meta_path, "r") as meta_file:
        meta = meta_file.read()

    lines = meta.split("\n")
    start_times = get_start_times(lines)
    titles = get_titles(lines)

    youtube_chapters = ""
    for start_time, title in zip(start_times, titles):
        timestamp = seconds_to_timestamp(start_time)
        youtube_chapters += f"{timestamp} {title}\n"

    os.makedirs(dirname(out_path), exist_ok=True)
    with open(out_path, "w") as out_file:
        out_file.write(youtube_chapters)


if __name__ == "__main__":
    generate_youtube_chapters_from_meta()
