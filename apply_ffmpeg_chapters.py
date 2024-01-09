import subprocess

def apply_chapters(
    input_path="dist/joined/joined.mp4",
    meta_path="dist/meta/FFMETADATAFILE_WITH_CHAPTERS.txt",
    output_path="dist/joined/joined_with_chapters.mp4",
):
    # https://ikyle.me/blog/2020/add-mp4-chapters-ffmpeg
    subprocess.run(
        [
            "ffmpeg",
            "-i",
            input_path,
            "-i",
            meta_path,
            "-map_metadata",
            "1",
            "-codec",
            "copy",
            output_path,
            "-y",
        ],
    )
    
if __name__ == "__main__":
    apply_chapters()
