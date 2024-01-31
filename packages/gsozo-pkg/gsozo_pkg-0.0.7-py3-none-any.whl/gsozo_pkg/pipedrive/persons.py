from pipedrive.persons import Persons as BasePersons


class Persons(BasePersons):
    def __init__(self, client):
        super().__init__(client)

    def get_person_activities(self, person_id, **kwargs):
        url = "persons/{}/activities".format(person_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_person_attaches(self, person_id, **kwargs):
        url = "persons/{}/files".format(person_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_person_emails(self, person_id, **kwargs):
        url = "persons/{}/mailMessages".format(person_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_all_persons(self, *args, pagination_on=True, **kwargs):
        if pagination_on:
            return super().get_all_persons(*args, **kwargs)
        else:
            return self._client._get_all_from(super().get_all_persons, *args, **kwargs)

    def get_person_one_field(self, field_id, **kwargs):
        url = "personFields/{}".format(field_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def get_person_followers(self, person_id, pagination_on=True, **kwargs):
        url = "persons/{}/followers".format(person_id)
        get_function = lambda **kwargs: self._client._get(self._client.BASE_URL + url, **kwargs)

        if pagination_on:
            return get_function()
        else:
            return self._client._get_all_from(get_function, **kwargs)

    def add_follower_to_person(self, person_id, user_id, **kwargs):
        url = "persons/{}/followers".format(person_id)
        data = { "user_id": user_id }
        return self._client._post(self._client.BASE_URL + url, json=data, **kwargs)

    def update_person_field(self, field_id, data, **kwargs):
        url = "personFields/{}".format(field_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)

    def delete_follower_to_person(self, person_id, user_id, **kwargs):
        followers = self.get_person_followers(person_id, pagination_on=False)
        follower_id = next((x['id'] for x in followers if x['user_id'] == user_id), None)

        if follower_id:
            url = "persons/{}/followers/{}".format(person_id, follower_id)
            return self._client._delete(self._client.BASE_URL + url, **kwargs)

    def merge_two_persons(self, person_to_keep, person_to_overwrite, **kwargs):
        url = "persons/{}/merge".format(person_to_overwrite)
        data = { "merge_with_id": person_to_keep }
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)
