from collections import Counter


def load_domains(path):
    domains = []
    with open(path) as f:
        for line in f:
            address = line.strip()
            if "@" in address:
                domains.append(address.split("@")[-1])
    return domains


def most_common_domain(domains):
    counts = Counter(domains)
    return counts.most_common(1)[0]


def main():
    domains = load_domains("emails.txt")
    domain, count = most_common_domain(domains)
    print(f"Most common domain: {domain} ({count} address(es))")


if __name__ == "__main__":
    main()
