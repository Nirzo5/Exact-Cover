from itertools import combinations

def parse_input(input_str):
    input_str = input_str.strip('[]')  # Remove square brackets at the beginning and end
    pairs = input_str.split('],[')  # Split the string into pairs

    result = []
    for pair in pairs:
        nums = pair.split(',')
        parsed_nums = []
        for num in nums:
            if num.isdigit():  # Check if the string represents a digit
                parsed_nums.append(int(num))  # Convert to integer and append to parsed_nums
            else:
                return 0
        result.append(parsed_nums)  # Append parsed_nums to the result list
    return result

def check_brackets(lst):
    stack = []  # Initialize an empty stack to keep track of opening square brackets

    # Iterate through each sublist in the nested list
    for sublist in lst:
        # Iterate through each character in the sublist
        for char in sublist:
            # If the character is an opening square bracket, push it onto the stack
            if char == '[':
                stack.append(char)
            # If the character is a closing square bracket
            elif char == ']':
                # Check if the stack is empty or the top of the stack doesn't match the current closing bracket
                if not stack or stack[-1] != '[':
                    return False  # Return False if there's no matching opening bracket
                stack.pop()  # If the bracket matches, pop the opening bracket from the stack
            # If the character is a digit change its type to integer

    # Check if the stack is empty after processing all characters
    return len(stack) == 0  # If the stack is empty, all opening brackets have been matched and it's valid

def check_sublists_union(target, sublists):
    # Creating a function to calculate the union of sublists
    def union(sublists):
        result = []
        for sublist in sublists:
            result.extend(sublist)
        return result

    # Go over all possible combinations of sublists
    for sublist_count in range(1, len(sublists) + 1):
        for sublist_combo in combinations(sublists, sublist_count):
            # Create the union of every sublist combination
            if union(sublist_combo) == target:
                # if the union of sublists matches the target return it
                return list(sublist_combo)
    # If no union matches the target return 0
    return 0

def is_intersection_empty(list_of_sublists):
    if type(list_of_sublists) != list:
        return "No Exact cover of the target list"
    # Go over each pair of sublists
    for i in range(len(list_of_sublists)):
        for j in range(i + 1, len(list_of_sublists)):
            # Get the first sublist
            sublist1 = list_of_sublists[i]
            # Get the second sublist
            sublist2 = list_of_sublists[j]
            # Compare all elements in the two sublists
            if not any(item in sublist1 for item in sublist2):
                continue
            # If there are two identical element the intersection is not empty
            return False
    # If we haven't found identical elements the intersection is empty
    return list_of_sublists

def turn_to_int(target):
    result = []
    # Checks if the input is a list
    if type(target) != list:
        if type(target) == str:
            # If it is a str we will split it around the comas
            target = target.split(',')
        else:
            # If it is not a list and not a string alert the user
            return 0
    for i in target:
        if type(i)!=int:
            # Checks if the elements in target ar all digits
            if i.isdigit()==False:
                # If an element from the list is not a digit alert the user
                return 1
            else:
                # If an element is a digit add it to the output list
                result.append(int(i))
        else:
            result.append(i)
    return result

def Exact_cover(target, input_str):
    # Check if the target list is valid input
    y = check_brackets(target)
    # If the input is invalid alert the user
    if y == False:
        return f"The group A is not a valid list. Check the amount of parenthesis entered"
    # Check if the nested list is valid input
    z = check_brackets(input_str)
    # If the input is invalid alert the user
    if z == False:
        return f"The group S is not a valid list. Check the amount of parenthesis entered"
    # Create a list of sublists from the input
    a = parse_input(input_str)
    if a == 0:
        return "The group S includes a non integer"
    # Check the target list type and element type
    b = turn_to_int(target)
    if b == 1:
        return "Group A includes a non integer"
    if b == 0:
        return "Input must be a string or list"
    # Check if the union of sublists matches the target
    c = check_sublists_union(b, a)
    # Check if the intersection of the sublists from the previous function is empty
    return is_intersection_empty(c)


def is_valid_sublist(a):
    flag = True
    if not check_brackets(a):
        flag = False
    if parse_input(a) == 0:
        flag = False
  
    return flag





groupS = "[1,2,3],[4],[5,6],[7,8],[9,10],[10,12],[13],12"

groupA = '1,2,3,4,5,6,7,8'


