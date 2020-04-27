# 1) Реализовать класс «Дата», функция-конструктор которого должна принимать дату
# в виде строки формата «день-месяц-год». В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
import re
import datetime

now = datetime.datetime.now()


class Date:

    def __init__(self, date_str):
        self.date_str = str(date_str)

    @classmethod
    def method(cls, date_str):

        date_list = re.findall(r'\d+', date_str)
        return int(date_list[0]), int(date_list[1]), int(date_list[2])

    @staticmethod
    def valid(day, month, year):
        if now.year > year >= 0:
            if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):  # - то это обычный год
                if 1 <= month <= 12:
                    if month == 4 or month == 6 or month == 9 or month == 11:
                        if 1 <= day <= 30:
                            return f"Корректная дата."
                        else:
                            return f"В этом месяце не может быть больше 30 дней."
                    elif month == 2:
                        if 1 <= day <= 28:
                            return f"Корректная дата."
                        else:
                            return f"В феврале {year} года не могло быть больше 28 дней."
                    else:
                        if 1 <= day <= 31:
                            return f"Корректная дата."
                        else:
                            return f"В месяце не может быть больше, чем 31 день."
                else:
                    return f"В году не может быть больше чем 12 месяцев."
            else:
                if 1 <= month <= 12:
                    if month == 4 or month == 6 or month == 9 or month == 11:
                        if 1 <= day <= 30:
                            return f"Корректная дата."
                        else:
                            return f"В этом месяце не может быть больше 30 дней."
                    elif month == 2:
                        if 1 <= day <= 29:
                            return f"Корректная дата."
                        else:
                            return f"В феврале {year} года не могло быть больше 29 дней."
                    else:
                        if 1 <= day <= 31:
                            return f"Корректная дата."
                        else:
                            return f"В этом месяце не может быть больше, чем 31 день."
                else:
                    return f"В году не может быть больше чем 12 месяцев."
        elif now.year == year:
            if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
                if 0 < month < now.month:
                    if month == 4 or month == 6 or month == 9 or month == 11:
                        if 1 <= day <= 30:
                            return f"Корректная дата."
                        else:
                            return f"В этом месяце не может быть больше 30 дней."
                    elif month == 2:
                        if 1 <= day <= 28:
                            return f"Корректная дата."
                        else:
                            return f"В феврале этого года не могло быть больше 28 дней."
                    else:
                        if 1 <= day <= 31:
                            return f"Корректная дата."
                        else:
                            return f"В месяце не может быть больше, чем 31 день."
                elif month == now.month:
                    if day <= now.day:
                        return f"Корректная дата."
                    else:
                        return "Этот день еще не наступил в этом месяце."
                else:
                    return f"Этот месяц еще не наступил в этом году."
            else:
                if 0 < month < now.month:
                    if month == 4 or month == 6 or month == 9 or month == 11:
                        if 1 <= day <= 30:
                            return f"Корректная дата."
                        else:
                            return f"В этом месяце не может быть больше 30 дней."
                    elif month == 2:
                        if 1 <= day <= 29:
                            return f"Корректная дата."
                        else:
                            return f"В феврале этого года не могло быть больше 29 дней."
                    else:
                        if 1 <= day <= 31:
                            return f"Корректная дата."
                        else:
                            return f"В месяце не может быть больше, чем 31 день."
                elif month == now.month:
                    if day <= now.day:
                        return f"Корректная дата."
                    else:
                        return f"Этот день еще не наступил в этом месяце."
                else:
                    return f"Этот месяц еще не наступил в этом году."
        else:
            return f"Этот год еще не наступил."

    def __str__(self):
        return f"Введенная дата {(Date.method(self.date_str))}"


date_str1 = Date("30-05-2019")
print(date_str1)
print(date_str1.valid(30, 5, 2019))
print()
date_str2 = Date("29-02-2019")
print(date_str2)
print(date_str2.valid(29, 2, 2019))
print()
date_str3 = Date("30-02-2020")
print(date_str3)
print(date_str3.valid(30, 2, 2020))
print()
date_str4 = Date("30-02-2021")
print(date_str4)
print(date_str4.valid(30, 2, 2021))
print()
date_str5 = Date("30-05-2020")
print(date_str5)
print(date_str5.valid(30, 5, 2020))
print()
date_str6 = Date("30-04-2020")
print(date_str6)
print(date_str6.valid(30, 4, 2020))
print()
date_str7 = Date("-31-04-2019")
print(date_str7)
print(date_str7.valid(31, 4, 2019))
