import codewars_test as test


def to24hourtime(hour, minute, period):
    if period == 'am':
        if hour < 10:
            hour = '0' + str(hour)
        if hour == 12:
            hour = '00'
    else:
        hour = hour+12
        if hour == 24:
            hour = 12
    minute = '0' + str(minute) if len(str(minute)) < 2 else str(minute)
    return f'{hour}{minute}'


@test.describe("to24hourtime test")
def to24hourtime_test():

    @test.it("Example Tests")
    def example_tests():
        test.assert_equals(to24hourtime( 1,  0, 'am'), '0100')
        test.assert_equals(to24hourtime( 1,  0, 'pm'), '1300')
        test.assert_equals(to24hourtime(12,  0, 'am'), '0000')
        test.assert_equals(to24hourtime(12,  0, 'pm'), '1200')
        test.assert_equals(to24hourtime( 6, 30, 'am'), '0630')
        test.assert_equals(to24hourtime( 9, 45, 'pm'), '2145')
