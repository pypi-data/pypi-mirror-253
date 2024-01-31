from pipedrive.organizations import Organizations as BasePersons


class Organizations(BasePersons):
    def __init__(self, client):
        super().__init__(client)

    def add_follower_to_organization(self, org_id, user_id, **kwargs):
        url = "organizations/{}/followers".format(org_id)
        data = { "user_id": user_id }
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)
