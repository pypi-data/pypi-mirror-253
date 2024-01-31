import pickle
from loguru import logger


class Backup:
    def __init__(self, client):
        self._client = client

    def save_persons(self, path):
        data = self._client._get_all_from(self._client.persons.get_all_persons)

        pickle.dump(data, open(path, "wb"))
        logger.info("Saved in backup_persons.p {} persons".format(len(data)))

    def save_deals(self, path):
        data = self._client._get_all_from(self._client.deals.get_all_deals)

        pickle.dump(data, open(path, "wb"))
        logger.info("Saved in backup_deals.p {} deals".format(len(data)))

    def save_activities(self, path):
        data = self._client._get_all_from(
            self._client.activities.get_all_activities, {"user_id": 0}
        )

        pickle.dump(data, open(path, "wb"))
        logger.info("Saved in backup_activities.p {} activities".format(len(data)))

    def save_filters(self, path):
        data = self._client.filters.get_all_filters()["data"]

        pickle.dump(data, open(path, "wb"))
        logger.info("Saved in backup_filters.p {} filters".format(len(data)))

    def save_notes(self, path):
        data = self._client._get_all_from(self._client.notes.get_all_notes)

        pickle.dump(data, open(path, "wb"))
        logger.info("Saved in backup_notes.p {} notes".format(len(data)))

    def save_organizations(self, path):
        data = self._client._get_all_from(
            self._client.organizations.get_all_organizations
        )

        pickle.dump(data, open(path, "wb"))
        logger.info(
            "Saved in backup_organizations.p {} organizations".format(len(data))
        )

    def save_pipelines(self, path):
        data = self._client.pipelines.get_all_pipelines()['data']

        pickle.dump(data, open(path, "wb"))
        logger.info("Saved in backup_pipelines.p {} pipelines".format(len(data)))

    def save_products(self, path):
        data = self._client._get_all_from(self._client.products.get_all_products)

        pickle.dump(data, open(path, "wb"))
        logger.info("Saved in backup_products.p {} products".format(len(data)))

    def save_users(self, path):
        data = self._client.users.get_all_users()['data']

        pickle.dump(data, open(path, "wb"))
        logger.info("Saved in backup_users.p {} users".format(len(data)))

    def save_files(self, path):
        data = self._client.files.get_all_files()['data']

        pickle.dump(data, open(path, "wb"))
        logger.info("Saved in backup_files.p {} files".format(len(data)))
