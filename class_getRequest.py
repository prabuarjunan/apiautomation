import requests
import json
import time

#Base URL



#Headers
HEADERS = {
    'content-type': 'application/json',
    'api-key': CVAPI_APIKEY,
    'secret-key': CVAPI_SECRETKEY
    }

getfilesystemDetailsHeaders = {
    'content-type': 'application/json',
    'api-key': CVAPI_APIKEY,
    'secret-key': CVAPI_SECRETKEY
}


filesystemURL = CVAPI_BASEURL + "/FileSystems"
filesystemDetails = CVAPI_BASEURL + "/FileSystems" + "/c756d817-d46e-3d09-8080-790bec931401/MountTargets"
filesystemCreateURL = CVAPI_BASEURL

class cvsAPI(object):
    # get FileSystems
    def get_fileSystems(self):
        getResult = requests.get(url=filesystemURL, headers=HEADERS)
        print("File system creation success, the response code : ", getResult.status_code)
        fileSystemsData = getResult.json()
        for i in fileSystemsData[:-1]:
            fileSystemId = (i['fileSystemId'])
            name = (i['name'])
            print("FileSystemId : ", fileSystemId, " =   VolumeName : ", name)

    # get details of the single filesystem
    def get_fileSystemsdetails(self):
        getdetailsfileSystems = requests.get(url=filesystemDetails, headers=HEADERS)
        print(filesystemDetails, getdetailsfileSystems.status_code)
        selectedfileSystems = getdetailsfileSystems.json()
        for i in selectedfileSystems:
            fileSystemId1 = (i['fileSystemId'])
            print("FileSystemId : ", fileSystemId1)

    # create Volume/filssystem
    def create_fileSystems(self):
        payload = {
            "name": "PythonScriptTest48",
            "creationToken": "Prabu-test-volume48",
            "region": "us-east",
            "serviceLevel": "basic",
            "quotaInBytes": 1000000000000
        }
        postfileSystems = requests.post(filesystemURL, data=json.dumps(payload), headers=HEADERS)
        print("FileSystem Created", filesystemURL, postfileSystems.content)
        datafilesystems = postfileSystems.json()
        datafilesystems1 = datafilesystems['fileSystemId']
        exportname = datafilesystems['creationToken']
        time.sleep(30)
        datafilesystems1 = datafilesystems['fileSystemId']
        self.test = datafilesystems1
        self.export = exportname
        return datafilesystems1, exportname

    #update Created Volume/Filesystem
    def update_fileSystems(self):
        payload1 = {
        "creationToken": "Prabu-test-volume",
        "region": "us-east",
        "serviceLevel": "extreme",
        "quotaInBytes": 10000000000000
        }
        filesystemID = create_fileSystems()
        updateURL = filesystemURL + "/" + filesystemID
        putfileSystems = requests.put(updateURL, data=json.dumps(payload1), headers=HEADERS)
        print("update", updateURL, putfileSystems.content)

    #delete the created file system "Caution : this command will delete the file system",API deletion dont ask for the confirmation
    def delete_filesystems(self):
        filesystemID = create_fileSystems()
        updateURL = filesystemURL + "/" + filesystemID
        deletefileSystems = requests.delete(updateURL, headers=HEADERS)
        print("delete", updateURL, deletefileSystems.content)

    # Creating snapshots of the volume created.
    def create_snapshot(self):
        payload2 = {
            "name": "snappy",
            "region": "us-east"
        }
        filesystemID = create_fileSystems()
        time.sleep(60)
        createsnapshotURL = filesystemURL + "/" + filesystemID + "/" + "Snapshots"
        createSnapshot = requests.post(createsnapshotURL, data=json.dumps(payload2), headers=HEADERS)
        if createSnapshot.status_code == 202:
            print("snapshot creation Successful", createsnapshotURL, createSnapshot.content)
        else:
            print("snapshot creation failed", createSnapshot.content)

    # Target IP address information
    def target_information(self):
        filesystemID = self.test
        gettargetInfoURL = filesystemURL + "/" + filesystemID + "/" + "MountTargets"
        gettargetinfo = requests.get(gettargetInfoURL, headers=HEADERS)
        time.sleep(30)
        targetJSON = gettargetinfo.json()
        time.sleep(30)
        targetIPaddress = targetJSON[0]['ipAddress']
        print("Target IP address is :", targetIPaddress)
        self.targetIP = targetIPaddress
        return targetIPaddress

    def buildMountnameforCFT(self):
        export = self.export
        ipAddress = self.targetIP
        mountname = ipAddress + ":/" + export
        self.mountname = mountname
        print("Export name : ", mountname)
        return mountname







