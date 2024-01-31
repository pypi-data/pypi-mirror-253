from pipedrive.stages import Stages as BaseStages


class Stages(BaseStages):
    def __init__(self, client):
        super().__init__(client)