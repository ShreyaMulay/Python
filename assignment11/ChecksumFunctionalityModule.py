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

def GetChecksum(path):
    flag = os.path.isabs(path)

    dups = {}
   
    if flag == False:
        path = os.path.abspath(path)
        exists = os.path.isdir(path)
    
    if exists:
        for dirName, subdirs, filelist in os.walk(path): 
            print("Current folder is: "+dirName)
            for file in filelist:
                path = os.path.join(dirName, file)
                file_hash = hashfile(path)
                if(file_hash in dups):
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]
                # print("File name : ",path)
                print("Checksum : ",file_hash)
        # print("::dups",dups)   
        return dups
   
    else:
        print("Invalid Path")


def ChkFileExists(filename,cnt = 0):	#checks if file exists and return the new file name for eg Demo_Copy.txt, Demo_Copy_1.txt	
	if(not os.path.exists(filename)):
		return filename
	elif("_Copy" not in filename):	
		a = filename.split('.')
		newfilename = a[0] + "_Copy." + a[1] 
		filename = newfilename
	else:
		a = filename.split('_Copy')
		b = filename.split('.')
		newfilename = a[0] + "_Copy_" + str(cnt) +"."+ b[1]
		filename = newfilename		
	cnt += 1
	return ChkFileExists(filename,cnt)	



def printDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    print("results",len(results))
    List = list()
    if(len(results)>0):
        print("Duplicate found:")
        print(results)
        count =0
        # if(len(results) > 0):
        for result in results:
            for subresult in result:
                count += 1
                if(count >= 2):
                    # os.remove(subresult)
                    List.append(result)
            count = 0
        print("list : ",List)
    else:
        print("No duplicates found")
    
    return List


def removeDuplicate(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    print("results",len(results))
    List = list()
    if(len(results)>0):
        print("Duplicate found:")
        print(results)
        count =0
        # if(len(results) > 0):
        for result in results:
            for subresult in result:
                count += 1
                if(count >= 2):
                    os.remove(subresult)
                    List.append(subresult)
                    print(subresult)
            count = 0
    else:
        print("No duplicates found")
    
    return List

   

