# 1
def check_nearest_number(numbers_list: str, num: int) -> int:
    numbers_list = numbers_list.split(" ")
    task_list = []
    for i in numbers_list:
        task_list.append(int(i))

    task_list.append(num)
    for j in range(len(task_list)-1):
        for i in range(len(task_list)-1):
            if task_list[i] > task_list[i+1]:
                task_list[i], task_list[i+1] = task_list[i+1], task_list[i]

    for i in range(len(task_list)):
        if task_list[i] == num:
            return task_list[i-1] or task_list[i+1]


# 2
def text_exam(text: str):
    result = 0
    count_res = []
    text_list = text.split(" ")
    if len(text_list) > 0:
        for i in text_list:
            if i not in count_res:
                count_res.append(i)
    result = len(count_res)
    return result

# 3
def count_customers(birthday_list: list):
    count = 0
    for i in birthday_list:
        year = int(i[-4:])
        if year % 2 == 0:
            count += 1
    return count


#print(count_customers(['14.11.1990', '17.02.2022', '16.08.2010']))