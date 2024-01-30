import httpx
import platform
import re

from .Exception.InvalidRequestException import InvalidRequestException
from .Response.ApiResponse import ApiResponse
from .Response.ApiResponseDownload import ApiResponseDownload
from ._version import __version__


class Client:
    _baseUrl = None
    _version = None
    _userAgent = None
    _session = None
    _client = None

    RESPONSE_RESPONSE = "RESPONSE_RESPONSE"
    RESPONSE_DOWNLOAD = "RESPONSE_DOWNLOAD"

    IP_RESOLVE_V4 = "ipv4"
    IP_RESOLVE_V6 = "ipv6"
    IP_RESOLVE_ANY = "any"

    def __init__(self, baseUrl="https://core.resellerinterface.de/", version="stable", options={}):
        self._baseUrl = baseUrl.rstrip("/") + "/"
        if version == 'stable' or version == 'latest':
            self._version = version
        elif version and version == int(version):
            self._version = 'v' + str(int(version))
        else:
            raise RuntimeError('Invalid version provided.')

        self._client = httpx.AsyncClient()

        self.setUserAgent("api-client-python/" + __version__ + " python/" + platform.python_version())
        self.setOptions(options)

    def __build_post_array(self, current: dict, return_value=None, prefix=None):
        if return_value is None:
            return_value = {}
        for k, v in current.items():
            new_prefix = f"{prefix}[{k}]" if prefix else k
            if isinstance(v, dict):
                return_value = self.__build_post_array(v, return_value, new_prefix)
            else:
                if v is True:
                    v = "true"
                if v is False:
                    v = "false"
                return_value[new_prefix] = v
        return return_value

    async def __httpxWrapper(self, url, data):
        headers = {'user-agent': self._userAgent}

        if self._session:
            headers['cookie'] = "coreSID=" + self._session

        response = await self._client.post(url, data=data, headers=headers)
        if "set-cookie" in response.headers:
            match = re.search(r"coreSID=([^;]*)", response.headers['set-cookie'], re.IGNORECASE | re.MULTILINE)
            if match:
                self._session = match[1]

        return response

    def getBaseUrl(self):
        return self._baseUrl

    def getVersion(self):
        return self._version

    def setOptions(self, options):
        if "ipResolve" in options:
            self.setIpResolve(options["ipResolve"])

        if "userAgent" in options:
            self.setUserAgent(options["userAgent"])

    def setIpResolve(self, option):
        if option == self.IP_RESOLVE_V4:
            self._client = httpx.AsyncClient(transport=httpx.AsyncHTTPTransport(local_address="0.0.0.0"))
        elif option == self.IP_RESOLVE_V6:
            self._client = httpx.AsyncClient(transport=httpx.AsyncHTTPTransport(local_address="::"))
        else:
            self._client = httpx.AsyncClient(transport=httpx.AsyncHTTPTransport())

    def setUserAgent(self, option):
        self._userAgent = option

    def getUserAgent(self):
        return self._userAgent

    async def login(self, username, password, resellerId=None):
        query = {
            'username': username,
            'password': password,
        }
        if resellerId:
            query['resellerId'] = resellerId

        return await self.request('reseller/login', query)

    async def request(self, action, params, responseType=RESPONSE_RESPONSE):
        action = action.strip("/")
        path = action.split("/")

        if len(path) < 2:
            raise InvalidRequestException("invalid request action")

        url = self._baseUrl + self._version + "/"

        data = self.__build_post_array(params)

        response = await self.__httpxWrapper(url + action, data)

        if responseType == self.RESPONSE_RESPONSE:
            return ApiResponse(response.json())
        elif responseType == self.RESPONSE_DOWNLOAD:
            filename = response.headers['content-disposition']
            if filename is not None:
                match = re.search(r".*filename=['\"]?([^'\"]+)", filename)
                if match is not None:
                    filename = match.group(1)

            filesize = int(response.headers['content-length'])

            filetype = response.headers['content-type'].split(";")[0]

            return ApiResponseDownload(response.content, filename, filesize, filetype)

    def setSession(self, session):
        self._session = session

    def getSession(self):
        return self._session
