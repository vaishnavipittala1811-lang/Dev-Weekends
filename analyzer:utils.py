def generate_statistics(parsed_data, top_n=10):
    entries = parsed_data["entries"]
    malformed = parsed_data["malformed"]

    method_counter = Counter()
    status_counter = Counter()
    endpoint_times = defaultdict(list)
    error_counter = Counter()
    ip_counter = Counter()

    for entry in entries:
        if entry.method:
            method_counter[entry.method] += 1

        if entry.status:
            status_counter[entry.status] += 1

        if entry.response_ms is not None:
            key = f"{entry.method} {entry.path}"
            endpoint_times[key].append(entry.response_ms)

        if entry.status and entry.status >= 400:
            error_counter[f"{entry.status} {entry.path}"] += 1

        if entry.ip:
            ip_counter[entry.ip] += 1

    slowest = []
    for endpoint, values in endpoint_times.items():
        avg = sum(values) / len(values)
        slowest.append((endpoint, avg))

    slowest.sort(key=lambda x: x[1], reverse=True)

    suspicious_ips = {
        ip: count
        for ip, count in ip_counter.items()
        if count > 100
    }
return {
        "processed": len(entries) + len(malformed),
        "valid": len(entries),
        "malformed": len(malformed),
        "methods": method_counter,
        "statuses": status_counter,
        "slowest": slowest[:top_n],
        "errors": error_counter.most_common(top_n),
        "suspicious_ips": suspicious_ips,
        "malformed_examples": malformed[:5],
    }