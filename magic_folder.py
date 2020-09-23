import os
import time
import shutil

PHOTO_EXT = ("jpg", "jpeg", "png", "psd", "tif")
VIDEO_EXT = ("mp4", "avi", "mov")
DOCUMENT_EXT = ("pdf", "docx", "doc", "txt")


def main():
    magic_folder_path = "/Users/derek/Desktop/test"
    # while not os.path.exists(magic_folder_path):
    #     magic_folder_path = input("Path to folder to sort:")
    photo_f = magic_folder_path + "/Photos"
    video_f = magic_folder_path + "/Videos"
    document_f = magic_folder_path + "/Documents"
    other_f = magic_folder_path + "/Other"
    while True:
        file_list = os.listdir(magic_folder_path)
        num_files = len(file_list)
        for file in file_list:
            nm, ext = os.path.splitext(file)
            ext = ext[1:]
            if ext in PHOTO_EXT:
                if not os.path.exists(photo_f):
                    os.makedirs(photo_f)
                shutil.move(magic_folder_path + "/" + file, photo_f)
            elif ext in VIDEO_EXT:
                if not os.path.exists(video_f):
                    os.makedirs(video_f)
                shutil.move(magic_folder_path + "/" + file, video_f)
            elif ext in DOCUMENT_EXT:
                if not os.path.exists(document_f):
                    os.makedirs(document_f)
                shutil.move(magic_folder_path + "/" + file, document_f)
        while num_files == len(os.listdir(magic_folder_path)):
            time.sleep(5)


if __name__ == '__main__':
    main()
