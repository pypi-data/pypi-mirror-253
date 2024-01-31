import pickle
from loguru import logger


class Manipulator:
    def __init__(self, client):
        self._client = client

    """
    Move the persons data to another persons, based on persons id, and keep they all as active as clone (Don't do auto merge)

    Parameters
    ----------
    ids_from: str or list(str)
        pipedrive person id to get person data

    ids_to: str or list(str)
        pipedrive person id to set person data

    exclude_fields: list(str)
        fields to not update

    Example
    --------
    # Move the data from person with id=1 to person with id=2, NOTE: at the end we will have 2 persons with the same data
    .move_person_data('1', '2')

    # Exchange person data with each other
    .move_person_data(['1','2'], ['2','1'])
    """

    def move_persons_data(
        self,
        ids_from,
        ids_to,
        exclude_fields=[
            "add_time",
            "visible_to",
            "org_name",
            "org_id",
            "label",
            "picture_id",
        ],
        must_use_pickle=False,
    ):
        id_persons_from, id_persons_to = self._sanitize_ids_from_to(ids_from, ids_to)

        exclude_field_list = exclude_fields + ["id"]
        unique_ids = self._get_unique_ids_from_to(ids_from, ids_to)

        if must_use_pickle:
            persons_data = pickle.load(open("persons_data.p", "rb"))
        else:
            persons_data = self._get_persons_by_ids(unique_ids, exclude_field_list)
            pickle.dump(persons_data, open("persons_data.p", "wb"))

        for i in range(0, len(id_persons_from)):
            person_from = id_persons_from[i]
            person_to = id_persons_to[i]
            person_data = persons_data[person_from]

            person_data["owner_id"] = person_data["owner_id"]["id"]

            res = self._client.persons.update_person(person_to, person_data)
            if res["success"] != True:
                raise Exception(
                    "Move data from id={} to id={} not succeed!\nResponse:\n{}".format(
                        person_from, person_to, res
                    )
                )

            logger.info(
                "Moved person id={} data to person id={}".format(person_from, person_to)
            )
            key = input("press enter to keep going: ")
            if key != "":
                return

        for id_person in unique_ids:
            res = self._client.persons.update_person(id_person, {"active_flag": True})
            if res["success"] != True:
                raise Exception(
                    "Set person id={} as active not succeed!\nResponse:\n{}".format(
                        id_person, res
                    )
                )

    """
    Move all person deal that match the date, to another person. can be used in batch, passing multiple persons
    NOTE: Pipe deals has the figure of participants (persons present in the deal, but no the central one).
          At this point of time the pipedrive DON'T auto change participants when changed the central person,
          so this function make the change and leaves the others participants unchanged

    Parameters
    ----------
    ids_from: str or list(str)
        pipedrive person id to get person data

    ids_to: str or list(str)
        pipedrive person id to set person data

    start_date: str
        filter deals for created from this date. Leave empty to min date

    end_date: str
        filter deals for created before this date. Leave empty to max date
    Example
    --------
    # Move the deals from person id=1 to person id=2
    .move_persons_deals('1', '2')

    # Move the deals created before 2019-08-08 from person id=1 to person id=2
    .move_persons_deals('1', '2', end_date='2019-08-08')

    # Exchange person deals with each other
    .move_persons_deals(['1','2'], ['2','1'])
    """

    def move_persons_deals(
        self,
        ids_from,
        ids_to,
        start_date="0000-00-00",
        end_date="9999-99-99",
        must_use_pickle=False,
    ):
        self._move_persons_records_to(
            "deals", ids_from, ids_to, start_date, end_date, must_use_pickle
        )

    """
    Move all person activities that match the date, to another person. can be used in batch, passing multiple persons.
    NOTE: Pipe activities has the figure of participants (persons present in the activity, but no the central one).
          At this point of time the pipedrive auto change participants when changed the central person, leaving the others participants unchanged

    Parameters
    ----------
    ids_from: str or list(str)
        pipedrive person id to get person data

    ids_to: str or list(str)
        pipedrive person id to set person data

    start_date: str
        filter deals for created from this date. Leave empty to min date

    end_date: str
        filter deals for created before this date. Leave empty to max date
    Example
    --------
    # Move the activities from person id=1 to person id=2
    .move_persons_activities('1', '2')

    # Move the activities created before 2019-08-08 from person id=1 to person id=2
    .move_persons_activities('1', '2', end_date='2019-08-08')

    # Exchange person deals with each other
    .move_persons_activities(['1','2'], ['2','1'])
    """

    def move_persons_activities(
        self,
        ids_from,
        ids_to,
        start_date="0000-00-00",
        end_date="9999-99-99",
        must_use_pickle=False,
    ):
        self._move_persons_records_to(
            "activities", ids_from, ids_to, start_date, end_date, must_use_pickle
        )

    def move_persons_notes(
        self,
        ids_from,
        ids_to,
        start_date="0000-00-00",
        end_date="9999-99-99",
        must_use_pickle=False,
    ):
        self._move_persons_records_to(
            "notes", ids_from, ids_to, start_date, end_date, must_use_pickle
        )

    def move_persons_files(
        self,
        ids_from,
        ids_to,
        start_date="0000-00-00",
        end_date="9999-99-99",
        must_use_pickle=False,
    ):
        self._move_persons_records_to(
            "files", ids_from, ids_to, start_date, end_date, must_use_pickle
        )

    def _sanitize_ids_from_to(self, ids_from, ids_to):
        id_persons_from = ids_from
        id_persons_to = ids_to

        if isinstance(id_persons_from, list) and isinstance(id_persons_to, list):
            if len(id_persons_from) != len(id_persons_to):
                raise Exception("The lists have different length")
        elif isinstance(id_persons_from, str) and isinstance(id_persons_to, str):
            id_persons_from = [id_persons_from]
            id_persons_to = [id_persons_to]
        else:
            raise Exception("Invalid params type")

        return id_persons_from, id_persons_to

    def _get_unique_ids_from_to(self, ids_from, ids_to):
        return ids_from + list(set(ids_to) - set(ids_from))

    def _move_persons_records_to(
        self,
        r_type,
        ids_from,
        ids_to,
        start_date="0000-00-00",
        end_date="9999-99-99",
        must_use_pickle=False,
    ):
        get_records = {
            "activities": {
                "function": self._get_persons_activities_by_ids,
                "pickle": "persons_activities.p",
            },
            "deals": {
                "function": self._get_persons_deals_by_ids,
                "pickle": "persons_deals.p",
            },
            "notes": {
                "function": self._get_persons_notes_by_ids,
                "pickle": "persons_notes.p",
            },
            "files": {
                "function": self._get_persons_files_by_ids,
                "pickle": "persons_files.p",
            },
        }

        move_recods = {
            "activities": self._move_activity_to,
            "deals": self._move_deal_to,
            "notes": self._move_note_to,
            "files": self._move_file_to,
        }

        id_persons_from, id_persons_to = self._sanitize_ids_from_to(ids_from, ids_to)
        unique_ids = self._get_unique_ids_from_to(ids_from, ids_to)

        if must_use_pickle:
            persons_records = pickle.load(open(get_records[r_type]["pickle"], "rb"))
        else:
            persons_records = get_records[r_type]["function"](
                unique_ids, start_date, end_date
            )
            pickle.dump(persons_records, open(get_records[r_type]["pickle"], "wb"))

        for i in range(0, len(id_persons_from)):
            person_from = id_persons_from[i]
            person_to = id_persons_to[i]
            records = persons_records[person_from]

            for record in records:
                move_recods[r_type](record["id"], person_from, person_to)

            logger.info(
                "Moved {} {} from person id={} to person id={}".format(
                    len(records), r_type, person_from, person_to
                )
            )
            key = input("press enter to keep going: ")
            if key != "":
                return

    def _move_activity_to(self, activity_id, id_person_from, id_person_to):
        res = self._client.activities.update_activity(
            activity_id, {"person_id": id_person_to}
        )

        if res["success"] != True:
            raise Exception(
                "Move activity id={} from person id={} to id={} not succeed!\nResponse:\n{}".format(
                    activity_id, id_person_from, id_person_to, res
                )
            )

    def _move_deal_to(self, deal_id, id_person_from, id_person_to):
        res = self._client.deals.update_deal(str(deal_id), {"person_id": id_person_to})

        if res["success"] == True:
            res = self._client.deals.delete_participant_to_deal_by_person_id(
                deal_id, id_person_from
            )

            if res["success"] != True:
                raise Exception(
                    "Delete person id={} from deal id={} not succeed!\nResponse:\n{}".format(
                        id_person_from, deal_id, res
                    )
                )
        else:
            raise Exception(
                "Move deal id={} from person id={} to id={} not succeed!\nResponse:\n{}".format(
                    deal_id, id_person_from, id_person_to, res
                )
            )

    def _move_note_to(self, note_id, id_person_from, id_person_to):
        res = self._client.notes.update_note(str(note_id), {"person_id": id_person_to})

        if res["success"] != True:
            raise Exception(
                "Move note id={} from person id={} to id={} not succeed!\nResponse:\n{}".format(
                    note_id, id_person_from, id_person_to, res
                )
            )

    def _move_file_to(self, file_id, id_person_from, id_person_to):
        res = self._client.files.update_file(str(file_id), {"person_id": id_person_to})

        if res["success"] != True:
            raise Exception(
                "Move file id={} from person id={} to id={} not succeed!\nResponse:\n{}".format(
                    file_id, id_person_from, id_person_to, res
                )
            )

    def _get_persons_by_ids(self, list_ids, exclude_fields=[]):
        ret = {}
        for person_id in list_ids:
            person_data = self._client.persons.get_person(str(person_id))["data"]

            for field in exclude_fields:
                del person_data[field]

            ret[person_id] = person_data

        return ret

    def _get_persons_deals_by_ids(
        self, list_ids, start_date="0000-00-00", end_date="9999-99-99"
    ):
        filter_data_funct = lambda x: (x["add_time"][:10] >= start_date) and (
            x["add_time"][:10] < end_date
        )
        ret = {}

        for person_id in list_ids:
            all_person_deals = self._client.persons.get_person_deals(
                str(person_id), params={"limit": "500"}
            )["data"]

            if (all_person_deals != None) and (len(all_person_deals) > 0):
                filtered_deals = list(filter(filter_data_funct, all_person_deals))
            else:
                filtered_deals = []

            ret[person_id] = filtered_deals

        return ret

    def _get_persons_activities_by_ids(
        self, list_ids, start_date="0000-00-00", end_date="9999-99-99"
    ):
        filter_data_funct = lambda x: (x["add_time"][:10] >= start_date) and (
            x["add_time"][:10] < end_date
        )
        ret = {}

        for person_id in list_ids:
            all_person_activities = self._client.persons.get_person_activities(
                str(person_id), params={"limit": "500"}
            )["data"]

            if (all_person_activities != None) and (len(all_person_activities) > 0):
                filtered_activities = list(
                    filter(filter_data_funct, all_person_activities)
                )
            else:
                filtered_activities = []

            ret[person_id] = filtered_activities

        return ret

    def _get_persons_notes_by_ids(
        self, list_ids, start_date="0000-00-00", end_date="9999-99-99"
    ):
        filter_data_funct = lambda x: (x["add_time"][:10] >= start_date) and (
            x["add_time"][:10] < end_date
        )

        ret = {id: [] for id in list_ids}

        all_notes = self._client._get_all_from(self._client.notes.get_all_notes)

        if (all_notes != None) and (len(all_notes) > 0):
            filtered_notes = list(filter(filter_data_funct, all_notes))
        else:
            filtered_notes = []

        for note in filtered_notes:
            for person_id in list_ids:
                if str(note["person_id"]) == str(person_id):
                    ret[person_id].append(note)

        return ret

    def _get_persons_files_by_ids(
        self, list_ids, start_date="0000-00-00", end_date="9999-99-99"
    ):
        filter_data_funct = lambda x: (x["add_time"][:10] >= start_date) and (
            x["add_time"][:10] < end_date
        )
        ret = {}

        for person_id in list_ids:
            filter_by_person_funct = lambda x: str(x["person_id"]) == str(person_id)
            all_person_files = self._client.persons.get_person_attaches(
                str(person_id), params={"limit": "500"}
            )["data"]

            if (all_person_files != None) and (len(all_person_files) > 0):
                filtered_files = list(filter(filter_data_funct, all_person_files))

                # Filter by person, because files attached to a deal that is attached to an person is listed too
                filtered_files = list(filter(filter_by_person_funct, filtered_files))
            else:
                filtered_files = []

            ret[person_id] = filtered_files

        return ret
