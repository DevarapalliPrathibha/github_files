import win32api
availableDrives = win32api.GetLogicalDriveStrings()
print(availableDrives)
drives = [drivestr for drivestr in availableDrives.split('\100') if drivestr]
#drives = drives.split('\100')[:-1]
print(drives)