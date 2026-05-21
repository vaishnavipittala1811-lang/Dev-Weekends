def print_report(stats):
    print("=" * 50)
    print("LOG ANALYSIS REPORT")
    print("=" * 50)

    print(f"Processed lines: {stats['processed']}")
    print(f"Valid entries: {stats['valid']}")
    print(f"Malformed lines: {stats['malformed']}")

    print("\nHTTP Methods:")
    for method, count in stats["methods"].items():
        print(f"  {method}: {count}")

    print("\nStatus Codes:")
    for status, count in stats["statuses"].items():
        print(f"  {status}: {count}")

    print("\nTop Slow Endpoints:")
    for endpoint, avg in stats["slowest"]:
        print(f"  {endpoint} -> avg {avg:.2f}ms")

    print("\nTop Error Endpoints:")
    for endpoint, count in stats["errors"]:
        print(f"  {endpoint} -> {count}")

    print("\nSuspicious IPs:")
    if stats["suspicious_ips"]:
        for ip, count in stats["suspicious_ips"].items():
            print(f"  {ip}: {count} requests")
    else:
        print("  None")

    print("\nMalformed Examples:")
    for line in stats["malformed_examples"]:
        print(f"  {line}")