def page_digits(pages):
    total = 0
    while pages > 9:
        pages_length = len(str(pages))
        dif = int('9'*(pages_length-1))
        last = pages-dif
        total += last*pages_length
        pages = dif
    return total + pages
