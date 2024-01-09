# Video Merger

## How to use this project

- Clone this repository
- Create a `source` directory next to the script files
    - If you wish to operate with the `source` and `dist` directories on different harddrives than the repository, you can create [symlinks](https://www.howtogeek.com/16226/complete-guide-to-symbolic-links-symlinks-on-windows-or-linux/)
- If you wish to download recordings from blackboard, paste the contents of [blackboard-download.js](./blackboard-download.js) into the browser [devtools](https://docs.devsamurai.com/teamboard-proscheduler/how-to-open-web-console-on-different-browsers) console while on the recordings page
- Put your video files into the source directory
- Run the commands below in order

```
python3 copy_and_rename_collaborate_videos.py
python3 join_videos.py
python3 generate_ffmpeg_chapters.py
python3 generate_youtube_chapters_from_meta.py
python3 apply_ffmpeg_chapters.py
```

## Output

- `dist/renamed` is a directory that contains copies of the videos in the `source` directory, but their names will be without the collaborate formatting.
- `dist/joined/joined.mp4` is the combination of all the videos in the `source` directory
- `dist/joined/joined_with_chapters.mp4` is a version of the `joined.mp4` file that also has chapters chapters embedded into its metadata. Each chapter corresponds to a video in the `source` directory.
  - Use an advanced video player like [VLC](https://www.videolan.org/vlc/) to access these chapters
- `dist/meta/youtube_chapters.txt` is a list of timestamps for the chapters that comprise `joined.mp4`, that is compatible with [youtube&#39;s chapter format](https://support.google.com/youtube/answer/9884579?hl=en)
