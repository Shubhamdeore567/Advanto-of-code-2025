### Day - 2 ###

# INPUT
ranges = [
"19391-47353","9354357-9434558","4646427538-4646497433","273-830","612658-674925","6639011-6699773","4426384-4463095","527495356-527575097","22323258-22422396","412175-431622","492524-611114","77-122","992964846-993029776","165081-338962","925961-994113","7967153617-7967231799",
    "71518058-71542434","64164836-64292066","4495586-4655083","2-17","432139-454960",
    "4645-14066","6073872-6232058","9999984021-10000017929","704216-909374","48425929-48543963",
    "52767-94156","26-76","1252-3919","123-228"
]

invalid_ids = []

for r in ranges:
    start, end = map(int, r.split("-"))

    for num in range(start, end + 1):
        s = str(num)

        if len(s) % 2 != 0:
            continue

        mid = len(s) // 2

        if s[:mid] == s[mid:]:
            invalid_ids.append(num)

print("sum:", sum(invalid_ids))


parsed_ranges = [(int(a), int(b)) for a, b in (r.split("-") for r in ranges.split(","))]


LOW = min(a for a, b in parsed_ranges)
HIGH = max(b for a, b in parsed_ranges)


def inside_ranges(n):
    for a, b in parsed_ranges:
        if a <= n <= b:
            return True
    return False


invalid_ids = set()

max_len = len(str(HIGH))

for block_len in range(1, max_len // 2 + 1):
    start = 10 ** (block_len - 1)
    end = 10 ** block_len

    for base in range(start, end):
        s = str(base)

        repeat = 2
        while True:
            num = int(s * repeat)

            if num > HIGH:
                break

            if num >= LOW and inside_ranges(num):
                invalid_ids.add(num)

            repeat += 1


result = sum(invalid_ids)

print("part 2 ans", result)
