#данный алгоритм проходит проверку на 2 из 3 представленных тестов.

def appearance(intervals):
    count = 0
    begin = -1
    time = 0
    start_list = create_intervals_list(intervals)
    for elem in start_list:
        count += elem[1]
        if count == 3:
            begin = elem[0]
        if count == 2 and begin > 0:
            time += elem[0] - begin
            begin = -1
    return time


def create_intervals_list(dictionary):
    def check_index(index):
        return 1 if index % 2 == 0 else -1

    start_list = list()
    for key in dictionary:
        new_elem = dictionary[key]
        for i, obj in enumerate(new_elem):
            start_list.append((obj, check_index(i)))
    return sorted(start_list)


tests = [
    {'data': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'data': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
    {'data': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },

]

if __name__ == '__main__':
   for i, test in enumerate(tests):
       test_answer = appearance(test['data'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
