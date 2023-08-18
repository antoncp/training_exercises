import codewars_test as test
import re


def drop_cap(words):
    return ''.join(word.title() if len(word) > 2 else word for word in re.split(r'(\s+)', words))


sample_test_cases = [
#     words               expected
    ('apple',            'Apple'),
    ('apple of banana',  'Apple of Banana'),
    ('one   space',      'One   Space'),
    ('   space WALK   ', '   Space Walk   '),
    ('',                 ''),
]

@test.describe('Sample tests')
def sample_tests():
    for words, expected in sample_test_cases:
        @test.it(f'drop_cap({words!r})')
        def _():
            test.assert_equals(drop_cap(words), expected)