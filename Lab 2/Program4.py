"""
(5 points) Program 4: Is a Sequence Sorted
1. Search for the meaning of sequences in Python, and explain what is a 
sequence in python?
A sequence is an ordered collection of items that can be accessed using an 
index.
2. Create a function is_ordered that receives a sequence and returns true if 
the elements are in sorted order (ascending and/or alphabetical). Test your 
function with sorted and unsorted lists, tuples and strings.
"""

def is_ordered(sequence):
    # return if the sequence is in ascending order
    return all(sequence[i] <= sequence[i+1] for i in range(len(sequence) - 1))

def get_sequence_from_input(input_str):
    # evaluate the input string to a Python object
    try:
        # evaluates if input can be treated as a literal list, tuple, or string
        return eval(input_str)
    except:
        return input_str # if evaluation fails, return the string itself

if __name__ == "__main__":
    user_input = input("Enter a sequence (list, tuple, or string): ")
    sequence = get_sequence_from_input(user_input)
    if isinstance(sequence, (list, tuple, str)):
        result = is_ordered(sequence)
        print(f"The sequence is ordered: {result}")
    else:
        print("Invalid sequence type. Please enter a list, tuple, or string.")