def replace_dashes_as_one(s):
    new = ''
    spaces = ''
    dash_status = False
    for i in s:
        if i == '-':
            if not dash_status:
                new += i
                dash_status = True
            else:
                spaces = ''
        elif i != '-' and dash_status:
            if i.isspace():
                spaces += i
            else:
                new += spaces + i
                dash_status = False
                spaces = ''
        elif not dash_status:
            new += i
    return new + spaces
