import os


def main():
    path = '/Users/derek/Desktop/test'
    files = os.listdir(path)
    for file in files:
        end = ""
        if file.endswith(".8x10.tif"):
            end = ".8x10.tif"
        elif file.endswith(".wallet.tif"):
            end = ".wallet.tif"
        splice = file.replace(end, "")
        lastName = splice.rsplit(" ")[-1]
        splice = splice.replace(lastName, "")
        splice = splice.strip()
        os.rename(os.path.join(path, file), os.path.join(path, lastName + ", " + splice + end))

if __name__ == "__main__":
    main()
