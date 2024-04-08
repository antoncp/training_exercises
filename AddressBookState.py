states = {
    "AZ": "Arizona",
    "CA": "California",
    "ID": "Idaho",
    "IN": "Indiana",
    "MA": "Massachusetts",
    "OK": "Oklahoma",
    "PA": "Pennsylvania",
    "VA": "Virginia",
}


def by_state(st):
    sorted_locations = {}
    st = st.strip("\n")
    locations = st.split("\n")
    for loc in locations:
        state = loc[-2:]
        print(state)
        address = loc[:-3]
        if sorted_locations.get(states[state]):
            sorted_locations[states[state]] += [address]
        else:
            sorted_locations[states[state]] = [address]
    answer = ""
    for state, addresses in sorted(sorted_locations.items()):
        answer += f" {state}\r\n"
        for adr in sorted(addresses):
            answer += f"..... {adr.replace(',','')} {state}\r\n"
    return answer[1:-2]
