calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    up_str = string.upper()
    lo_str = string.lower()
    return len(string), up_str, lo_str
def is_contains(string,list_to_search):
    count_calls()
    return string.lower() in [item.lower() for item in list_to_search]
print(string_info('hello'))
print(string_info('Язва'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
