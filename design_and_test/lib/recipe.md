
As a user
So that I can find my tasks among all my notes
I want to check if a line from my notes includes the string `#TODO`.

<!-- 
1. Describe the Problem 
User wants to find string "#TODO" in line in notes
Error exceptions returned when one or more inputs missing
Return line that "#TODO" is on as a string

2. Design the Function Signature 
def diary_string_finder(note, word)
note - list
word - string

return - line
line - string (including keyword)

3. Create Examples as Tests
def test_no_input_returns_error():
    diary_string_finder([], "") == Error -> Exception to tell user it's empty

def test_only_list_input_return_error():
    diary_string_finder(["skjdfsjfh"], "") == Error -> Exception to tell user there is only a list

def test_only_string_input_return_error():
    diary_string_finder([], "#TODO") == Error -> Exception to tell user there is only a string

def test_both_inputs_present_no_keyword_included():
    diary_string_finder(["abdefghijkl], "#TODO") == "#TODO not found in notes"

def test_both_inputs_present_one_keyword_included():
    diary_string_finder(["ad #TODO kjhsd"], "#TODO") == "ad #TODO kjhsd"

(more than one keyword?)

4. Implement the Behaviour 
-->