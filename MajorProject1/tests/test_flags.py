from utils.arg_parser import parse_flags

def test_parse_flags():
    flags = parse_flags(["--name", "Amit", "--age", "21"])
    assert flags["name"] == "Amit"
    assert flags["age"] == "21"
