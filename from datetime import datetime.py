from datetime import datetime


TIMESTAMP_FORMATS = [
    "%Y-%m-%dT%H:%M:%SZ",
    "%Y/%m/%d %H:%M:%S",
    "%d-%b-%Y %H:%M:%S",
]



def parse_timestamp(value):
    value = value.strip()

    if value.isdigit():
        return datetime.fromtimestamp(int(value))

    for fmt in TIMESTAMP_FORMATS:
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue

    return None