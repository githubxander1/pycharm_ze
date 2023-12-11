import os

VIDEO_EXTENTIONS = ['.avi', '.AVI', '.mp4','.jpg']  # 可以添加更多后缀类型


def is_video_file(filename):
    return any(filename.endswith(extension) for extension in VIDEO_EXTENSIONS)


def select_videos(dir_root):
    videos = []

    for root, _, fnames in os.walk(dir_root):
        for fname in fnames:
            if is_video_file(fname):
                path = os.path.join(root, fname)
                videos.append(path)

    return videos
