import re
import os
text = "The quick brown fox jumps over the lazy dog"
list_jenis_dokument = [
    {
        "new": "",
        "old": "Ijazah"
    }
]


def to_text(list, path):
    with open(path, 'w') as f:
        f.write('\n'.join(list))
    print("done file at the", path)


path_write = "C:\\Users\\Rifo\\Desktop\\output2.txt"
path_directory = "c:\\dmsUploadExperiment\\"

list_folder = os.listdir(path_directory)
list_files = []
for folder in list_folder:
    path_folder = os.path.join(path_directory + folder)
    list_document = os.listdir(path_directory + folder)

    for document in list_document:
        doc = 1
        for keyval in list_jenis_dokument:
            name = keyval["name"]

            if (re.search(name.lower(), document.lower())):
                print(name.lower() + "-" + document.lower())
                doc = 0
        if doc == 1:
            list_files.append(os.path.join(
                path_directory + folder + "\\" + document))
to_text(list_files, path_write)
