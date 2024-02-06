def compare_versions(version1,version2):
    v1, v2 = version1.split('.'), version2.split('.')
    for x, y in zip(v1, v2):
        if int(x) < int(y):
            return False
    return True if len(v1) >= len(v2) else False
