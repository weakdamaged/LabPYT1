def seconds_to_time(seconds):
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)
    return days, hours, minutes, seconds


while True:
    user_input = int(input("Введите количество секунд (введите 0 для завершения): "))

    if user_input == 0:
        print("Программа завершена.")
        break

    days, hours, minutes, seconds = seconds_to_time(user_input)

    print(f"{days} дней, {hours} часов, {minutes} минут, {seconds} секунд")
