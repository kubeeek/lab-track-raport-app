from functools import wraps


def parse_timestamp_range(model):

    def decorator(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            from_date = args[1].GET.get("from_date", "")
            to_date = args[1].GET.get("to_date", "")

            if from_date == '':
                from_date = None

            if to_date == '':
                to_date = None

            return function(*args, from_date, to_date, **kwargs)

        return wrapper

    return decorator
