class InvestmentFunds():
    """
    Access 'investment funds' api.
    Have some methods to direct access some endpoints.
    """

    def __init__(self, client):
        self.client = client
        self.base_url = 'api.xpi.com.br/investment-funds'
        self.subscription_key = '602224c06c434f35b6352ca902c5020a'


    def get_from_url(self, api_path, params={}):
        '''
        Get something from the url 'api.xpi.com.br/investment-funds'.
        You don't need to pass the base route, only the path for this api.
        The path must start with '/'.

        e.g.: get_from_url(
            '/yield-rede/v2/investment-funds-rede',
            params
        )
        '''

        full_url = self.base_url + api_path
        return self.client.request(full_url, params, self.subscription_key)


    def get_hub_funds(self, params={}):
        '''
        Get all funds from xp hub page
        website ref.:

        e.g.: get_hub_funds(params)
        '''
        return self.get_from_url('/yield-rede/v2/investment-funds-rede')


    def get_open_funds(self, params={}):
        '''
        Get all funds from xp open page
        website ref.: https://www.xpi.com.br/investimentos/fundos-de-investimento/lista/#/

        e.g.: get_open_funds({
            'onlyrpps': False,                  # We don't know for what is this params
            'family': None                      # but to work must be used
        })
        '''
        return self.get_from_url('/yield-portal/v2/investment-funds', params)
