import turtle
import math

# Создаем окно для рисования
window = turtle.Screen()

# Создаем черепаху
spiral_turtle = turtle.Turtle()
spiral_turtle.color('grey')
sintr = turtle.Turtle()
sintr.color('blue')

# Устанавливаем начальные значения
a = 15  # Параметр архимедовой спирали
theta = 2 * math.pi  # Угол

# Рисуем архимедову спираль
while theta <= 6 * math.pi:  # Ограничиваем длину спирали
    r = a * theta
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    spiral_turtle.goto(x, y)

    d = 1 + 0.2 * math.sin(theta*6)

    dx = x * d
    dy = y * d
    sintr.goto(dx,dy)

    theta += 0.1  # Шаг изменения угла

# Завершаем рисование
window.exitonclick()
