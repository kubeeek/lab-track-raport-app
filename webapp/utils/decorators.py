from datetime import datetime
from functools import wraps


def parse_timestamp_range():
    def decorator(get_function):
        @wraps(get_function)
        def wrapper(*args, **kwargs):
            try:
                from_date = datetime.strptime(args[0].request.GET.get("from_date", ""), "%Y-%m-%d")
                to_date = datetime.strptime(args[0].request.GET.get("to_date", ""), "%Y-%m-%d")
            except ValueError:
                from_date = ''
                to_date = ''

            filter_params = {'from_date': from_date, 'to_date': to_date}
            if from_date == '' and to_date == '':
                filter_params = None

            return get_function(*args, filter_params, **kwargs)

        return wrapper

    return decorator
