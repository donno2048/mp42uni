# mp4-to-unicode

Use this to show a video in the terminal (Unicode art)

## install

(on Linux you may need to run `sudo apt-get install ffmpeg libsm6 libxext6 -y` to use `opencv`)

### From PyPi

```sh
pip3 install mp42uni
```

### From GitHub

```sh
pip3 install git+https://github.com/donno2048/mp42uni
```

## Usage

Run `mp42uni <video.mp4>` with the terminal **maximized** to display _<video.mp4>_ as ascii art.

You can simply use `mp42uni` to use a prompt to choose a video file.

If you get `_curses.error: addwstr() returned ERR` try decreasing the font size.

If you get `ModuleNotFoundError: No module named '_curses'` on Windows try: `pip3 install windows-curses==2.2.0`
