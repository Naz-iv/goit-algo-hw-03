import turtle
import sys


def koch_curve(t, rec_level, size):
    if rec_level == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, rec_level - 1, size / 2)
            t.left(angle)


def draw_koch_curve(rec_level: int = 4, size: int = 100):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(10)
    t.penup()
    t.goto(-size, 100)
    t.pendown()
    koch_curve(t, rec_level, size)

    t.right(90)
    koch_curve(t, rec_level, size)

    t.right(90)
    koch_curve(t, rec_level, size)

    t.right(90)
    koch_curve(t, rec_level, size)

    window.mainloop()


if __name__ == "__main__":
    try:
        order = int(input("Enter the recursion level: "))
        draw_koch_curve(order)
    except ValueError:
        print("Invalid recursion level entered, using default value: 4")
        draw_koch_curve()
