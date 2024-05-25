from collections import defaultdict


def allocate_rooms(customers):
    rooms = defaultdict(list)
    key = 1
    for customer in sorted(customers):
        added = False
        for k, v in rooms.items():
            if v[-1][-1] < customer[0]:
                rooms[k].append(customer)
                added = True
                break
        if not added:
            rooms[key].append(customer)
            key += 1
    rooms_list = []
    for customer in customers:
        for k, v in rooms.items():
            if customer in v:
                rooms_list.append(k)
                v.remove(customer)
                break
    return rooms_list
