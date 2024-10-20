class Solution:
    def roman_to_int(self, roman):
        # Mapping of Roman numerals to their integer values
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate through the Roman numeral string in reverse order
        for char in reversed(roman):
            current_value = roman_numerals[char]
            
            # If the current value is less than the previous value, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
                
            prev_value = current_value
        
        return total

    # Adding the romanToInt attribute
    romanToInt = roman_to_int  # This creates an alias

# Example usage
solution = Solution()
roman_number = "MCMXCIV"  # Example: 1994
integer_value = solution.romanToInt(roman_number)  # Using the new attribute
print("The integer value of the Roman numeral '{roman_number}' is: {integer_value}")
