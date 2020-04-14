#  2) Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего
#  элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

print("Данная программа создаст новый список из тех элементов исходного списка, которые больше предыдущих перед ними")

m_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [m_list[el] for el in range(1, len(m_list)) if m_list[el] > m_list[el - 1]]
print(f"Исходный список: {m_list}")
print()
print(f"Новый список: {new_list}")