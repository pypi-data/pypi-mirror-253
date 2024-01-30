from resellerinterface_api_client_python.Response.ApiResponse import ApiResponse


class ApiResponseDownload(ApiResponse):
    def __init__(self, response, fileName, fileSize, fileType):
        super().__init__(response)
        self._response = {
            'state': 1000,
            'stateParam': "",
            'stateName': "OK",
            'file': response,
            'fileName': fileName,
            'fileSize': fileSize,
            'fileType': fileType,
        }

    def getFile(self):
        return self._response['file'] if 'file' in self._response else None

    def getFileSize(self):
        return self._response['fileSize'] if 'fileSize' in self._response else None

    def getFileName(self):
        return self._response['fileName'] if 'fileName' in self._response else None

    def getFileType(self):
        return self._response['fileType'] if 'fileType' in self._response else None
