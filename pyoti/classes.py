class API:
    def __init__(self, api_key=None, api_url=None):
        self._api_key = api_key
        self._api_url = api_url

    @property
    def api_key(self):
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        self._api_key = value

    @property
    def api_url(self):
        return self._api_url

    @api_url.setter
    def api_url(self, value):
        self._api_url = value


class Domain(API):
    def __init__(self, api_key=None, api_url=None, domain=None):
        self._domain = domain
        API.__init__(self, api_key, api_url)

    @property
    def domain(self):
        return self._domain

    @domain.setter
    def domain(self, value):
        self._domain = value


class FileHash(API):
    def __init__(self, api_key=None, api_url=None, file_hash=None):
        self._file_hash = file_hash
        API.__init__(self, api_key, api_url)

    @property
    def file_hash(self):
        return self._file_hash

    @file_hash.setter
    def file_hash(self, value):
        self._file_hash = value


class IPAddress(API):
    def __init__(self, api_key=None, api_url=None, ip=None):
        self._ip = ip
        API.__init__(self, api_key, api_url)

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, value):
        self._ip = value


class URL(API):
    def __init__(self, api_key=None, api_url=None, url=None):
        self._url = url
        API.__init__(self, api_key, api_url)

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value


class Multi(Domain, FileHash, IPAddress, URL):
    def __init__(self, api_key=None, api_url=None, domain=None, file_hash=None, ip=None, url=None):
        API.__init__(self, api_key, api_url)
        Domain.__init__(self, domain)
        IPAddress.__init__(self, ip)
        FileHash.__init__(self, file_hash)
        URL.__init__(self, url)