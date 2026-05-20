import timeit
import string

def task_1_lists():
    print("--- Завдання 1. Списки ---")
    data = [10.5, 22.1, 8.4, 55.0, 12.3, 9.9, 42.8]
    print("Початковий список:", data)

    print("Індекси (0 та -1):", data[0], data[-1])
    print("Зрізи:", data[:3], data[::2], data[::-1])

    data.append(100.0)
    data.pop(2)
    data[1:3] = [0.0, 0.0]
    print("Після мутацій:", data, "\n")


def task_2_tuples():
    print("--- Завдання 2. Кортежі ---")
    students = [
        (1, "Коваленко", "КН-21", [90, 85, 92]),
        (2, "Шевченко", "КН-21", [75, 80, 78]),
        (3, "Бойко", "КН-22", [95, 98, 99])
    ]

    def print_student_info(student):
        st_id, name, group, grades = student 
        print(f"Студент {name} (ID: {st_id}), Група: {group}")

    print_student_info(students[0])

    def calculate_average(students_list):
        total, count = 0, 0
        for _, _, _, grades in students_list:
            total += sum(grades)
            count += len(grades)
        return round(total / count, 2) if count else 0

    print("Середній бал:", calculate_average(students))

    st = students[0]
    try:
        st[1] = "Петренко"
    except TypeError as e:
        print("Помилка зміни кортежу:", e)

    st[3].append(100)
    print("Але вкладений список змінився:", st, "\n")


def task_3_dictionaries():
    print("--- Завдання 3. Словники ---")
    text = "Python is great. Python is dynamic! Dictionaries in Python are fast."
    
    words = text.lower().translate(str.maketrans('', '', string.punctuation)).split()
    
    freq_dict = {}
    for word in words:
        freq_dict[word] = freq_dict.get(word, 0) + 1

    sorted_freq = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    print("Частоти:", sorted_freq)

    frequent_words = {k: v for k, v in freq_dict.items() if v > 1}
    print("Слова > 1 разу (comprehension):", frequent_words, "\n")


def task_4_sets():
    print("--- Завдання 4. Множини ---")
    list_a = ["user1", "user2", "user3", "user2", "user4"]
    list_b = ["user3", "user4", "user5", "user6", "user3"]

    set_a, set_b = set(list_a), set(list_b)

    print("Перетин:", set_a & set_b)
    print("Об'єднання:", set_a | set_b)
    print("Симетрична різниця:", set_a ^ set_b)

    subset = {"user1", "user2"}
    print("Чи subset <= set_a?", subset <= set_a)
    print("Чи subset <= set_b?", subset <= set_b, "\n")


def task_5_complexity():
    print("--- Завдання 5. Алгоритмічна складність ---")
    sizes = [1000, 10000, 50000]
    print(f"{'n':<8} | {'Пошук List(c)':<15} | {'Пошук Set(c)':<15} | {'Унік List(c)':<15} | {'Унік Set(c)'}")
    print("-" * 75)

    for n in sizes:
        test_list = list(range(n))
        test_set = set(test_list)
        search_val = n - 1 

        t_list_search = timeit.timeit(lambda: search_val in test_list, number=1000)
        t_set_search = timeit.timeit(lambda: search_val in test_set, number=1000)

        data_with_dups = test_list + [1, 2, 3] * 10 
        
        def unique_via_list():
            res = []
            for item in data_with_dups:
                if item not in res:
                    res.append(item)
            return res

        def unique_via_set():
            res = set()
            for item in data_with_dups:
                res.add(item)
            return res

        t_uniq_list = timeit.timeit(unique_via_list, number=10)
        t_uniq_set = timeit.timeit(unique_via_set, number=10)

        print(f"{n:<8} | {t_list_search:<15.5f} | {t_set_search:<15.5f} | {t_uniq_list:<15.5f} | {t_uniq_set:.5f}")

if __name__ == "__main__":
    task_1_lists()
    task_2_tuples()
    task_3_dictionaries()
    task_4_sets()
    task_5_complexity()