
class ValidatorClass:
    def __init__(self, *args, *kwargs)
        self.request_data = kwargs['request_data']
        self.user = kwargs['user']
        self.access_token = kwargs['access_token']

    def validate_request_data(self):
        return self.request_data

    def validate(self):
        dict_ = dict()
        dict_['some_key'] = self.validate_request_data()
        return dict_ 
