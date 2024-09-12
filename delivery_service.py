# ID успешной посылки: 117838639

def get_platforms_quantity(robots: list, limit: int) -> int:
    """Основная функция проекта. Обрабатывает массив из весов роботов,
    используя метод двух указателей,
    чтобы сравнить сумму двух весов роботов с переданным лимитом,
    инкременировать переменную счетчик
    и вернуть минимальное необходимое количество платформ для роботов.
    """
    list.sort(robots)

    platforms_counter: int = 0

    left_pointer: int = 0
    right_pointer: int = len(robots) - 1

    while left_pointer <= right_pointer:
        """Цикл по методу двух указателей. Сравнивает сумму весов роботов,
        на которые указывают указатели. Если суммы, большие или равные лимиту,
        не были найдены в массиве, то считает количество пар на платформу.
        """
        weight_sum: int = robots[left_pointer] + robots[right_pointer]

        if weight_sum < limit:
            left_pointer += 1
            continue
        elif weight_sum == limit:
            left_pointer += 1

        right_pointer -= 1
        platforms_counter += 1

    else:
        if platforms_counter == 0:
            platforms_counter = (len(robots) + 1) // 2

    return platforms_counter


if __name__ == '__main__':
    input_robots: list = list(map(int, input().split()))
    input_limit: int = int(input())
    print(get_platforms_quantity(input_robots, input_limit))
