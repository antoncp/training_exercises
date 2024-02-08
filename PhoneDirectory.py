def phone(strng, num):
    ad = strng.split("\n")
    numbers = []
    for i in ad:
        if num in i and not i[i.index(num) - 1].isdigit():
            numbers.append(i)
    if not numbers:
        return f"Error => Not found: {num}"
    if len(numbers) > 1:
        return f"Error => Too many people: {num}"
    line = numbers[0]
    name, address = None, []
    for i in line.split():
        if i.startswith("<"):
            name = i[1:]
        elif i.endswith(">"):
            name += f" {i[:-1]}"
    pre_address = line.replace(name, "").replace(num, "")
    name = "".join(i for i in name if i not in ("<", ">"))
    for i in pre_address.split():
        part = ""
        for x in i:
            if x.isalnum() or x in ("-", "."):
                part += x
            else:
                part += " "
        if part.strip():
            address.append(part.strip())
    address = " ".join(address).strip()
    return f"Phone => {num}, Name => {name}, Address => {address}"
