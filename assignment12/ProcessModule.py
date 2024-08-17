import psutil
import os

def DisplayProcesses():
    listOfProcesses = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        listOfProcesses.append(proc.info)

    return listOfProcesses


def ChkProcess(ProcessName):
	listprocess = []

	try:
		pinfo = [p.info for p in psutil.process_iter(attrs=['pid', 'name','username']) if ProcessName in p.info['name']]
		#pinfo['vms'] = proc.memory_info().vms / (1024*1024)
		print(pinfo)

		listprocess.append(pinfo)
		
	except (psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess) as E:
		print(E)
	return listprocess


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


