# {'A-1': ['A-1-1-1', 'A-1-1-2'], 'A-2': ['A-2-1'], 'B-1': ['B-1'], 'C': ['C']}
data = {
    "A": {
        "A-1": {
            "A-1-1": {
                "A-1-1-1": "A-1",
                "A-1-1-2": "A-1"
            }
        },
        "A-2": {
            "A-2-1": "A-2"
        }
    },
    "B": {
        "B-1": "B-1"
    },
    "C": "C"
}


def dfs(last_kv_list: dict, d: dict):
    for key, value in d.items():
        if len(d[key]) != 0 and isinstance(d[key], str):
            if not last_kv_list.get(value):
                last_kv_list[value] = []
            last_kv_list[value].append(key)
        else:
            dfs(last_kv_list, d[key])
    return last_kv_list


if __name__ == "__main__":
    last_str_list_of_category = {}
    result: dict = dfs(last_str_list_of_category, data)
    print(result)
