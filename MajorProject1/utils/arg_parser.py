def parse_flags(args):
    flags = {}
    i = 0
    
    while i < len(args):
        if i+1 > len(args):
            raise ValueError(f"Missing value for flag {args[i]}")

        key = args[i].lstrip("-")
        value = args[i+1]
        flags[key] = value
        i+=2
    
    return flags