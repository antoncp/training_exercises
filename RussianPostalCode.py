def zipvalidate(postcode):
    if (
        len(postcode) != 6
        or postcode.startswith(("0", "5", "7", "8", "9"))
        or not postcode.isdigit()
    ):
        return False
    return True
