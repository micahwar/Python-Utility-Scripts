from PIL import Image
from os import rename, path, listdir
from gc import collect
root = "D:\\"
subfolder = "Maths Classwork"
subfolderroot = path.join(root, subfolder) + "\\"
pdf = ""
accChars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.!- ()',&\\:"
imagelist = []

def fixFolderNames(Folders):
    for Folder in Folders:
        try:
            rename(Folder, ''.join([char for char in Folder if char in accChars]))
        except WindowsError as e:
            print(e)
def get_subFolders(Folder):
    return [path.join(Folder, x) for x in listdir(Folder)]

def images_to_PDF(imageList, pdfoutput):
    imageList[0].save(pdfoutput, "PDF", resolution=100.0, save_all=True, append_images=imageList[1:])

fixFolderNames(get_subFolders(subfolderroot))
sub_folders = get_subFolders(subfolderroot)

PDFs = [x for x in sub_folders if path.isfile(x) and x.endswith(".pdf")]
Folders = [x for x in sub_folders if path.isdir(x)]
if len(PDFs) != 0:
    Folders = Folders[Folders.index(PDFs[len(PDFs) - 1][:-4]) + 1:]
    
for folder in Folders:
    sortedListDir = sorted(listdir(folder), key=lambda file: int("".join([char for char in file.split(".")[0] if char.isnumeric()])))
    print(sortedListDir)
    imagelist = [Image.open(path.join(folder, x)) for x in sortedListDir]
    for image in imagelist:
        image.load()
    images_to_PDF(imagelist, path.join(subfolderroot, folder) + ".pdf")
    print (folder)
    collect()
