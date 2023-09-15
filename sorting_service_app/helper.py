def sort_key(item):
    parts = item[1]["ident"].split(".")
    key_parts = [int(part) if part.isdigit() else part for part in parts]
    print(key_parts)
    return key_parts