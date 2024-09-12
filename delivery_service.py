# ID успешной посылки: 117792597


def get_platforms_quantity(robots: list, limit: int) -> int:
    """Основная функция проекта. Обрабатывает массив из весов роботов,
    для 'отгрузки' их по двое на платформы с заданным лимитом по весу
    """
    list.sort(robots)

    platforms_counter: int = 0

    left_pointer: int = 0
    right_pointer: int = len(robots) - 1

    while robots:
        """Цикл, работающий пока все роботы не выгрузятся на платформы.
        Сравнивает попарно веса в массиве, чтобы 'вытащить' их.
        При самом эффективном расположении удаляет значения из массива
        и увеличивает счётчик платформ.
        """
        if len(robots) == 1:
            """"""
            if robots[0] <= limit:
                del robots[0]
                platforms_counter += 1
            else:
                raise ValueError('Один из роботов превысил лимит по весу')

        if left_pointer < right_pointer:
            light_robot = robots[left_pointer]
            heavy_robot = robots[right_pointer]

            if light_robot == limit:
                del robots[left_pointer]
                platforms_counter += 1
            elif heavy_robot == limit:
                del robots[right_pointer]
                platforms_counter += 1

            result: int = light_robot + heavy_robot

            if result > limit:
                right_pointer -= 1
            elif result == limit:
                del robots[left_pointer]
                del robots[right_pointer - 1]
                right_pointer = len(robots) - 1
                platforms_counter += 1
            elif (result < limit
                  and right_pointer == len(robots) - 1):
                del robots[left_pointer]
                del robots[right_pointer - 1]
                right_pointer = len(robots) - 1
                platforms_counter += 1
            elif (result < limit
                  and light_robot + robots[right_pointer + 1] > limit):
                del robots[left_pointer]
                del robots[right_pointer - 1]
                right_pointer = len(robots) - 1
                platforms_counter += 1
            else:
                left_pointer += 1
        else:
            for robot_index in range(len(robots)):
                if robots[robot_index] <= limit:
                    platforms_counter += 1
                else:
                    raise ValueError('Один из роботов превысил лимит по весу')

            return platforms_counter

    return platforms_counter


if __name__ == '__main__':
    input_robots: list = list(map(int, input().split()))
    input_limit: int = int(input())
    print(get_platforms_quantity(input_robots, input_limit))
