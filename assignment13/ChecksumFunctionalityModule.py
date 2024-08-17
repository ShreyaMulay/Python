import os
import hashlib

def hashfile(path, blocksize = 1024):
    afile = open(path, 'rb')
    hasher = hashlib.md5()
    buf = afile.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
    afile.close()
    return hasher.hexdigest()


def removeDuplicate(DirName):
    List = FileDuplicate(DirName)
    print("::List",List)
    
    for file in List:
        os.remove(file)
    return List

def FileDuplicate(DirName):
    dictionary = GetChecksum(DirName)
    return GetDuplicateFile(dictionary)

# def GetChecksumFile(path):
#     flag = os.path.isabs(path)

#     dups = {}
   
#     if flag == False:
#         path = os.path.abspath(path)
#         exists = os.path.isdir(path)
    
#     if exists:
#         for dirName, subdirs, filelist in os.walk(path): 
#             print("Current folder is: "+dirName)
#             for file in filelist:
#                 path = os.path.join(dirName, file)
#                 file_hash = hashfile(path)
#                 if(file_hash in dups):
#                     dups[file_hash].append(path)
#                 else:
#                     dups[file_hash] = [path]
#                 print("Checksum : ",file_hash)
#         return dups
   
#     else:
#         print("Invalid Path")

def GetChecksum(DirName):
    if(not os.path.isabs(DirName)):
        DirName = os.path.abspath(DirName)
    
    if(os.path.isdir(DirName)):
        duplicate = {}
        
        for folder, subfolder, files in os.walk(DirName):
            for file in files:
                DirName = os.path.join(folder,file)
                file_hash = hashfile(DirName)
                if(file_hash in duplicate):
                    duplicate[file_hash].append(DirName)
                else:
                    duplicate[file_hash] = [DirName]
    return duplicate

def GetDuplicateFile(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    print("results",len(results))
    List = list()
    
    fileCnt = 0
    for result in results:
        for subresult in result:
            fileCnt +=1
            if(fileCnt >= 2):
                List.append(subresult)
        fileCnt = 0
    return List


