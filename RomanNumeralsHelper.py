class RomanNumerals:
    rom_to_num = ({'I': 1, 'V': 5, 'X': 10, 'L': 50,
                   'C': 100, 'D': 500, 'M': 1000})
    num_to_rom = ({1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
                   100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X',
                   9: 'IX', 5: 'V', 4: 'IV', 1: 'I'})

    def to_roman(val):
        result = ''
        while val > 0:
            for x, y in RomanNumerals.num_to_rom.items():
                while val - x >= 0:
                    val -= x
                    result += y
        return result

    def from_roman(roman_num):
        result = 0
        for pos, i in enumerate(roman_num):
            if pos > 0 and (RomanNumerals.rom_to_num[roman_num[pos-1]]
                            < RomanNumerals.rom_to_num[i]):
                result += (RomanNumerals.rom_to_num[i] -
                           RomanNumerals.rom_to_num[roman_num[pos-1]] * 2)
            else:
                result += RomanNumerals.rom_to_num[i]
        return result
