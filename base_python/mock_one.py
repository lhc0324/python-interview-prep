def parse_query(query):
    counts = {}
    parts = query.split('&')
    for part in parts:
        cut = part.split('=',1)
        if len(cut) < 2:
            continue
        else:
            key = cut[0]
            value = cut[1]
            counts[key] = value
    return counts



if __name__ == "__main__":
    result = parse_query("name=zhangsan&age=23&city=beijing")
    print(result)
    print(parse_query("id=1001"))
    print(parse_query("name=&age=&city="))
    print(parse_query("debug"))