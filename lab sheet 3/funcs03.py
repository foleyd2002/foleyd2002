def get_price(age):
    under_sixteen = 5
    over_sixty = 7
    remainder = 10
    if age < 16:
        return under_sixteen
    elif age > 60:
        return over_sixty
    else:
        return remainder


def weird_case(some_str):
    result = ""
    switch_case = True  # Start with lowercase

    for char in some_str:
        if char.isalpha():
            result += char.lower() if switch_case else char.upper()
            switch_case = not switch_case
        else:
            result += char

    return result

def every_third(l1, l2):
    joined_lists = l1 + l2
    output_list = []
    i = 2
    while i < len(joined_lists):
        output_list.append(joined_lists[i])
        i = i + 3
    return output_list

def is_neg(num):
    if num < 0:
        return True
    else:
        return False

def remove_neg(lst):

    lst[:] = [num for num in lst if not is_neg(num)]
    return lst


import time
def countdown(num):
    for i in range(num, 0, -1):
        print(i)
        time.sleep(0.01)

    print("LIFT OFF!")

def search(str,letter):
    true_indicator = 0
    false_indicator = 0
    i = 0
    while i < len(str):
        if str[i] == letter:
            true_indicator += 1
        else:
            false_indicator += 1
        i = i + 1

    if true_indicator > 0:
        return True
    else:
        return False

def index(str, letter):
    for i, char in enumerate(str):
        if char == letter:
            return i
    return -1

def previous_two(n):
    num_sequence =[0,1]
    if n == 0:
        return 0
    elif n ==1:
        return  1
    else:
        while len(num_sequence) < n + 1:
            next_number = num_sequence[-1] + num_sequence[-2]
            num_sequence.append(next_number)

    return num_sequence[len(num_sequence) - 1]

if __name__ == '__main__':
    print(get_price(60))
if __name__ == '__main__':
    print(weird_case('change the case'))
if __name__ == '__main__':
    print(every_third([4,5,6],[7]))
if __name__ == '__main__':
    print(is_neg(77))
if __name__ == '__main__':
    print(remove_neg([-40, -1, 9]))
if __name__ == '__main__':
    print(countdown(1))
if __name__ == '__main__':
    print(search('python','a'))
if __name__ == '__main__':
    print(index('python','h'))
if __name__ == '__main__':
    print(previous_two(3))