salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

sum = 0
for _ in range(months):
    sum = sum + salary - spend
    spend = spend + spend *increase
sum = round(sum * (-1))
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", sum)

