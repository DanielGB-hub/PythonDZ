#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

sec = int(input("Привет! Введи время в секундах, и я верну ответ в стандартном виде чч:мм:сс: "))
minutes = sec // 60
hours = minutes // 60
print("%02d:%02d:%02d" % (hours, minutes % 60, sec % 60))



