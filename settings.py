# this module gives the program the 3d-list settings at a global scope
# don't know if this is the best way of doing it, but it works


def typecast(datapoint):
    if datapoint.isdigit():
        return int(datapoint)
    elif datapoint.replace(".", "").isdigit():
        return float(datapoint)
    else:
        return datapoint


def get_settings():
    with open("saves//settings_data.cfg", "r") as list_3d:
        list_3d = list_3d.read().split("\n")  # 1d list

    for each_line in range(len(list_3d)):
        list_3d[each_line] = list_3d[each_line].split(",")  # 2d list

        for each_item in range(len(list_3d[each_line])):

            if "/" in list_3d[each_line][each_item]:
                list_3d[each_line][each_item] = list_3d[each_line][each_item].split("/")  # 3d list
                for each_val in range(len(list_3d[each_line][each_item])):
                    list_3d[each_line][each_item][each_val] = typecast(list_3d[each_line][each_item][each_val])
            else:
                list_3d[each_line][each_item] = typecast(list_3d[each_line][each_item])

    return list_3d


settings = get_settings()
