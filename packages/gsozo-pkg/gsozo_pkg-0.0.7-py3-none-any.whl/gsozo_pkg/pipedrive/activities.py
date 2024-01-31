from pipedrive.activities import Activities as BaseActivities


class Activities(BaseActivities):
    def __init__(self, client):
        super().__init__(client)

    def get_activity_types(self, **kwargs):
        url = "activityTypes"
        return self._client._get(self._client.BASE_URL + url, **kwargs)
