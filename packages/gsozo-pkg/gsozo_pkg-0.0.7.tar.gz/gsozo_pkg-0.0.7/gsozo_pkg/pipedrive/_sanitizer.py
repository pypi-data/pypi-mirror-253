import re
import pandas as pd
import numpy as np


class Sanitizer:
    def __init__(self, client):
        self._client = client

    def get_duplicates(self):
        all_persons = self._get_all_persons()

        all_persons_filtered = []
        unique_fields = ["name", "xp_code", "email"]
        duplicated_persons = {}

        for person in all_persons:
            all_persons_filtered.append(
                {
                    "id": person["id"],
                    "name": person["name"].lower(),
                    "xp_code": person["9d6794606b66471270c5ae7437fa8a58b3a6f224"],
                    "email": person["email"][0]["value"].lower(),
                }
            )

        df = pd.DataFrame(all_persons_filtered).set_index("id")

        df = df.replace("", np.nan)
        df["xp_code"] = df["xp_code"].replace(0, np.nan)
        df["email"] = df["email"].replace("-", np.nan)

        for field in unique_fields:
            df_not_nan = df.loc[df[field].notna()]
            duplicated_in_this_field = df_not_nan.loc[
                df_not_nan[field].duplicated(keep=False)
            ]
            duplicated_persons[field] = duplicated_in_this_field.sort_values([field])

        return duplicated_persons

    def get_invalid_names(self):
        all_persons = self._get_all_persons()

        invalid_persons = []

        for person in all_persons:
            name = person["name"]
            string_check = re.compile(r"[@_!#$%^&*()<>?/\|}{~:]")

            if string_check.search(name) != None:
                invalid_persons.append(person)

        return invalid_persons

    def _get_all_persons(self):
        return self._client._get_all_from(self._client.persons.get_all_persons)
