class Files:
    def __init__(self, client):
        self._client = client

    def get_all_files(self, params=None, **kwargs):
        url = "files"
        return self._client._get(self._client.BASE_URL + url, params=params, **kwargs)

    def update_file(self, file_id, data, **kwargs):
        url = "files/{}".format(file_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)
