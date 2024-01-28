import logging

log = logging.getLogger(__name__)

class RequestHeaders:

    def __init__(self,filePath):
        self.filePath = filePath
        self.cookies = self.__private_loadCookies()
        self.headers = self.__private_loadHeaders()

    def dumpToFile(self):
        with open(self.filePath,'w') as fileObj:
            for i, (key, value) in enumerate(self.headers.items()):
                fileObj.write(key+":"+value+"\n")
            if len(self.cookies)>0:
                fileObj.write(self.__private_dumpCookies())

    def __private_loadCookies(self):
        cookies = {}
        with open(self.filePath, "r") as fileObj:
            for line in fileObj.readlines():
                line = line.strip('\n')
                if line.__contains__('Cookie'):
                    cookieKeyAndValues = line.replace('Cookie: ', '').replace('Cookie:', '').split("; ")
                    for cookieKeyAndValue in cookieKeyAndValues:
                        keyvalues = cookieKeyAndValue.split("=")
                        cookies[keyvalues[0]] = keyvalues[1]

        log.debug(cookies)
        return cookies

    def __private_loadHeaders(self):
        headers = {}
        with open(self.filePath, "r") as fileObj:
            for line in fileObj.readlines():
                line = line.strip('\n')
                if not line.__contains__('Cookie'):
                    cookieKeyAndValue = line.split(":")
                    headers[cookieKeyAndValue[0].strip()] = cookieKeyAndValue[1].strip()
        log.debug(headers)
        return headers

    def __private_dumpCookies(self):
        cookieStr = "Cookie:"
        for i, (key, value) in enumerate(self.cookies.items()):
            if i==(len(self.cookies)-1):
                cookieStr = cookieStr + key + "=" + value
            else:
                cookieStr = cookieStr + key + "=" + value + "; "
        return cookieStr

    def updateCookiesByKey(self,cookieKey,cookieValue):
        self.cookies[cookieKey] = cookieValue

    def updateHeadersByKey(self,headerKey,headerValue):
        self.headers[headerKey] = headerValue