import os, shutil

path = r""

filelist = os.listdir(path)

for files in filelist:
    fname, ext = os.path.splitext(files)
    ext = ext[1:]
    if ext == "":
        continue

    if os.path.exists(os.path.join(path, ext)):
        shutil.move(os.path.join(path, files), os.path.join(path, ext, files))
    else:
        os.makedirs(os.path.join(path, ext))
        shutil.move(os.path.join(path, files), os.path.join(path, ext, files))

print("Files sorted")

