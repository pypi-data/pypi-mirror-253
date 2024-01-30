class ApiResponse:
    _response = None

    def __init__(self, response):
        self._response = response

    def getState(self):
        return self._response['state'] if 'state' in self._response else None

    def getStateName(self):
        return self._response['stateName'] if 'stateName' in self._response else None

    def getStateParam(self):
        return self._response['stateParam'] if 'stateParam' in self._response else None

    def getData(self):
        return self._response if self._response else None

    def isError(self):
        return not self.getState() or int(self.getState()) >= 2000

    def getErrors(self):
        return self._response['errors'] if 'errors' in self._response else []