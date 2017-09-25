def header_name(header):
    return header[0]

def compare_sorted(actual, expected):
    actual = sorted(actual, key=header_name)
    expected = sorted(expected, key=header_name)
    return actual == expected
