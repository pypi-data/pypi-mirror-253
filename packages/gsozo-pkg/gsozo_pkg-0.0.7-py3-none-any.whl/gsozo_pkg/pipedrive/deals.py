from pipedrive.deals import Deals as BaseDeals


class Deals(BaseDeals):
    def __init__(self, client):
        super().__init__(client)

    def delete_participant_to_deal_by_person_id(self, deal_id, person_id):
        find_participant_funct = lambda x: str(x["person"]["id"]) == str(person_id)

        all_participants = self.get_deal_participants(str(deal_id))["data"]
        filtered_participant = list(filter(find_participant_funct, all_participants))

        if len(filtered_participant) == 1:
            return self.delete_participant_to_deal(
                deal_id, filtered_participant[0]["id"]
            )
        else:
            raise Exception(
                "Not find participant id={} in the deal id={}".format(
                    person_id, deal_id
                )
            )

    def get_deal_one_field(self, field_id, **kwargs):
        url = "dealFields/{}".format(field_id)
        return self._client._get(self._client.BASE_URL + url, **kwargs)

    def update_deal_field(self, field_id, data, **kwargs):
        url = "dealFields/{}".format(field_id)
        return self._client._put(self._client.BASE_URL + url, json=data, **kwargs)
