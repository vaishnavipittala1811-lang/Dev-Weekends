import json
import re
from analyzer.models import LogEntry
from analyzer.utils import parse_timestamp


STANDARD_REGEX = re.compile(
    r"^(?P<timestamp>\S+(?:\s\S+)?)\s+"
    r"(?P<ip>\d+\.\d+\.\d+\.\d+)\s+"
    r"(?P<method>GET|POST|PUT|DELETE|PATCH)\s+"
    r"(?P<path>/\S*)\s+"
    r"(?P<status>\d{3}|-)\s+"
    r"(?P<response>\S+)"
)



def parse_response_time(value):
    value = value.strip().lower()

    if value.endswith("ms"):
        return float(value[:-2])

    if value.endswith("s"):
        return float(value[:-1]) * 1000

    return float(value)

def parse_standard_line(line):
    match = STANDARD_REGEX.search(line)

    if not match:
        return None

    data = match.groupdict()

    status = None
    if data["status"] != "-":
        status = int(data["status"])

    try:
        response_ms = parse_response_time(data["response"])
    except Exception:
        response_ms = None

    return LogEntry(
        timestamp=parse_timestamp(data["timestamp"]),
        ip=data["ip"],
        method=data["method"],
        path=data["path"],
        status=status,
        response_ms=response_ms,
        raw=line,
    )

def parse_json_line(line):
    try:
        obj = json.loads(line)

        status = obj.get("status")
        if status == "-":
            status = None

        response = obj.get("response_time", "0")

        return LogEntry(
            timestamp=parse_timestamp(str(obj.get("timestamp", ""))),
            ip=obj.get("ip"),
            method=obj.get("method"),
            path=obj.get("path"),
            status=status,
            response_ms=parse_response_time(str(response)),
            raw=line,
        )

    except Exception:
        return None
    
    def parse_log_file(path):
    entries = []
    malformed = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                malformed.append("<blank line>")
                continue

            entry = None

            if line.startswith("{"):
                entry = parse_json_line(line)

            if not entry:
                entry = parse_standard_line(line)

            if entry:
                entries.append(entry)
            else:
                malformed.append(line)

    return {
        "entries": entries,
        "malformed": malformed,
    }
