import os
import time

def whoAmI():
    try:
        username = os.getenv('USERNAME')
        
        if username:
            return username
        else:
            raise Exception('It was not possible to determine the user.')
    
    except Exception as e:
        raise Exception(f"Error getting username: {str(e)}")
    

def waitForDownload(clickElementToStartDownload, timeoutInSeconds=30, downloadPath=os.path.expanduser("~/Downloads")):
    if not os.path.exists(downloadPath):
        raise Exception(f"The specified download folder does not exists: {downloadPath}")

    filesBeforeAction = [f for f in os.listdir(downloadPath)]
    try:
        clickElementToStartDownload.click()
    except Exception as e:
        raise Exception(f"Error to perform the action to start download: {str(e)}")

    end_time = time.time() + timeoutInSeconds
    
    while time.time() < end_time:
        filesAfterAction = [f for f in os.listdir(downloadPath)]
        
        target_files = [file for file in filesAfterAction if file not in filesBeforeAction and not file.endswith(('.tmp', '.dll'))]
        
        if target_files:
            return os.path.join(downloadPath, target_files[0])
        
        time.sleep(1)

    raise TimeoutError(f"Timeout reached to find the current download in '{downloadPath}'")