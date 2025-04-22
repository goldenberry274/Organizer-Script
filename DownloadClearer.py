import os
import collections

EXT_DOCS = ['pdf', 'docx', 'PDF', 'doc', 'txt']
EXT_PROGRAMS = ['java', 'py']
EXT_AUDIO = ['mp3', 'wav', 'raw', 'mna', 'mid', 'midi']
EXT_VIDEO = ['mp4', 'mpg', 'mpeg', 'avi', 'nov', 'flv']
EXT_IMGS = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'tiff', 'tif', 'webp']
EXT_COMPR = ['zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
EXT_INSTAL = ['dmg', 'exe', 'iso']

#step 1: Create dicrectories where we want to store the files
BASE_PATH = os.path.expanduser('~')
DEST_DIRS = ['Music', 'Movies', 'Pictures', 'Documents', 'Applications', 'Other', 'TEST_FIRST_PART']

for d in DEST_DIRS:
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

#Step 2: Map files from downloads folder based on their file extension
DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

for file_name in files_list:
    if file_name[0] != '.':
        file_ext = file_name.split('.')[-1]
        files_mapping[file_ext].append(file_name)

for f_ext, f_list in files_mapping.items():

    if f_ext in EXT_INSTAL:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Applications', file))
    elif f_ext in EXT_AUDIO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Music', file))
    elif f_ext in EXT_VIDEO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Movies', file))
    elif f_ext in EXT_IMGS:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Pictures', file))
    elif f_ext in EXT_DOCS or f_ext in EXT_COMPR:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Documents', file))
    elif f_ext in EXT_AUDIO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Music', file))

    else:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Other', file))