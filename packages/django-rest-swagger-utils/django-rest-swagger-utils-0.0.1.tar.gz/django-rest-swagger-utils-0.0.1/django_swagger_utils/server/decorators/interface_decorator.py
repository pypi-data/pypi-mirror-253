from functools import wraps
def validate_decorator(validator_class):
    @wraps(validator_class)
    def wrapper(request, *args, **kwargs):
        # Custom logic before the validator_class is called
        validator_instance = validator_class(request, *args, **kwargs)
        result = validator_instance.validate()
        # Custom logic after the validator_class is called
        return result  # You can return an HttpResponse or modify the response as needed