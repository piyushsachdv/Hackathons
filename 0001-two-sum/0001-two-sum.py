class Solution:
    def two_sum(self, nums, target):
        # Create a dictionary to store the index of each number
        num_to_index = {}
        
        # Iterate through the list of numbers
        for index, num in enumerate(nums):
            # Calculate the number needed to reach the target
            complement = target - num
            
            # Check if the complement exists in the dictionary
            if complement in num_to_index:
                # If found, return the indices
                return [num_to_index[complement], index]
            
            # If not found, store the index of the current number
            num_to_index[num] = index

        # If no solution is found (though the problem states there will always be one)
        return []

    # Adding the twoSum attribute
    twoSum = two_sum  # This creates an alias for the method

# Example usage
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)  # Using the new attribute
print("The indices of the two numbers that add up to {target} are: {result}")
