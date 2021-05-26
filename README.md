# Library
## Библиотека с разными полезностями
### patronymic.py 
#### Модуль предназначен для преобразования имени в отчество по правилам русского языка.
##### Пример использования:
    from patronymic import Patronymic

    father0 = Patronymic('Аркадий')
    father1 = Patronymic('Валерий')
    father2 = Patronymic('Александр')

    print(f"""Я много слышал о Вас {father2.name} {father1.male}, Ваша дочь Ирина {father2.female} много рассказывала
    о Вас и вашем отце. Судя по ее словам, {father1.name} {father0.male} был хорошим человеком.""")
##### Результат:
>Я много слышал о Вас __Александр Валерьевич__, Ваша дочь Ирина __Александровна__ много рассказывала о 
>Вас и вашем отце. Судя по ее словам, __Валерий Аркадьевич__ был хорошим человеком.
---
### password.py 
#### Модуль предназначен для генерации случайных пароле с вариативным колличеством символом и сложностью.
##### Пример использования:
    from password import Password

    for i in range(0, 10):
        print(Password(length = 12, strong = 'medium'))
##### Результат:
>bg312sb1chc8
>kb1orvbw8ikw
>d05qh2rsd9by
>8b077lyg4r8e
>n1114bmii0bc
>x9lxmpwixtog
>mlkx9f5a8ovl
>kh8y7wyvwmru
>iglg67slqfcf
>pa0c7h2drare
---
