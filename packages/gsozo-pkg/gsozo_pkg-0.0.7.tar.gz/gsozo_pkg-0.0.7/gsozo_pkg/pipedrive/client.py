from pipedrive.client import Client as BaseClient

from ._sanitizer import Sanitizer
from ._manipulator import Manipulator
from ._backup import Backup

from .persons import Persons
from .deals import Deals
from .files import Files
from .activities import Activities
from .organizations import Organizations
from .stages import Stages

import copy

#from loguru import logger


class Client(BaseClient):
    def __init__(self, company_domain, api_token):
        super().__init__(domain="https://{}.pipedrive.com/".format(company_domain))
        super().set_api_token(api_token)

        self.persons = Persons(self)
        self.deals = Deals(self)
        self.files = Files(self)
        self.activities = Activities(self)
        self.organizations = Organizations(self)
        self.stages = Stages(self)

        self.sanitizer = Sanitizer(self)
        self.manipulator = Manipulator(self)
        self.backup = Backup(self)

    """
        Loop through all pages on record (because the pipe limit for a page is 500), getting all the records
        NOTE: different of the get_all from each record like persons.get_all_persons(), this function return direct the data

        Parameters
        ----------
        funct: function
            function of the record that will be looped through

        extra_params: dict
            extra params to be passed to the function besides the 'limit' and 'start', used for the pagination
    """

    def _get_all_from(self, func, *args, **kwargs):
        data = []
        start = 0
        _args = copy.deepcopy(list(args))
        _kwargs = copy.deepcopy(kwargs)

        if len(_args) > 0 and type(_args[0]) == dict:
            params = _args[0]
        elif len(_args) > 1 and type(_args[1]) == dict:
            params = _args[1]
        elif _kwargs.get('params'):
            params = _kwargs['params']
        else:
            _kwargs['params'] = {}
            params = _kwargs['params']

        params.update({"limit": "500", "start": start})

        while True:
            res = func(*_args, **_kwargs)

            data = data + res["data"] if res['data'] else data
            if not res["additional_data"]["pagination"]["more_items_in_collection"]:
                break
            else:
                params['start'] = res["additional_data"]["pagination"]["next_start"]

        return data
