class PensionFunds():
    """
    Access 'pension funds' api.
    Have some methods to direct access some endpoints.
    """

    def __init__(self, client):
        self.client = client
        self.base_url = 'api.xpi.com.br/pension-funds'
        self.subscription_key = '6d05a3fbc85c49bc9368981fc193d468'


    def get_from_url(self, api_path, params={}):
        '''
        Get something from the url 'api.xpi.com.br/pension-funds'.
        You don't need to pass the base route, only the path for this api.
        The path must start with '/'.

        e.g.: get_from_url('/investment-funds', {
            'status': 1,                # we don't know for what is this params
            'brand': 3                  #
        })
        '''

        full_url = self.base_url + api_path
        return self.client.request(full_url, params, self.subscription_key)


    def get_prev(self, params={}):
        '''
        Get all prev funds from xp open page:
        website ref.: https://institucional.xpi.com.br/previdencia-privada/lista-de-fundos/#/

        e.g.: get_prev({
            'status': 1,                # we don't know for what is this params
            'brand': 3                  #
        })
        '''
        return self.get_from_url('/investment-funds', params)
