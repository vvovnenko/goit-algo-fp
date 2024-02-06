import turtle


def pythagoras_tree(t, order, size):
    t.forward(size)

    if order > 0:
        angle = 45
        t.left(angle)
        pythagoras_tree(t, order - 1, size / 1.3)
        t.right(angle * 2)
        pythagoras_tree(t, order - 1, size / 1.3)
        t.left(angle)

    t.back(size)


def draw_pythagoras_tree(order):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, -(150 * 1.3))
    t.pendown()
    t.left(90)

    pythagoras_tree(t, order, 150)

    window.mainloop()


def main():
    try:
        order = int(input("Enter an order: "))
    except ValueError:
        print('Error: integer expected')
        return
    draw_pythagoras_tree(order)


if __name__ == "__main__":
    main()
