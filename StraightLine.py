def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    first, second = coordinates[0], coordinates[1]
    for third in coordinates[2:]:
        if (second[0] - first[0]) * (third[1] - first[1]) - (
            third[0] - first[0]
        ) * (second[1] - first[1]):
            return False
    return True
