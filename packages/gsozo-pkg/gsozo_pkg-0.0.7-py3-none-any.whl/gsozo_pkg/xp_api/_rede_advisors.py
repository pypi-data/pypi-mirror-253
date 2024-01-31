class RedeAdvisors():
    """
    Access 'rede advisor' api.
    Have some methods to direct access some endpoints.
    """

    def __init__(self, client):
        self.client = client
        self.base_url = 'api.xpi.com.br/rede-advisors'
        self.subscription_key = 'b63f9758680845afb25dbd47a5e95c4a'


    def get_from_url(self, api_path, params={}):
        '''
        Get something from the url 'api.xpi.com.br/rede-advisors'.
        You don't need to pass the base route, only the path for this api.
        The path must start with '/'.

        e.g.: get_from_url('/v1/advisors/customer-wallets', params)
        '''

        full_url = self.base_url + api_path
        return self.client.request(full_url, params, self.subscription_key)

    def get_customer_wallet(self, params={}):
        '''
        Get customer wallet from xp api

        e.g.: get_customer_wallet({
            'limit': 0              # the param limit = 0 return all the customers (if you get an 404, try change the limit to 100)
        })
        '''
        return self.get_from_url('/v1/advisors/customer-wallets', params)

    def get_current_portfolios(self, params={}):
        return self.get_from_url('/v1/advisors/current-portfolios', params)
