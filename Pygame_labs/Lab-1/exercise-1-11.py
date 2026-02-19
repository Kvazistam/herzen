import time
import numpy as np
import pygame

import pygame
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
black = (0, 0, 0)


def task_1():
    x, y = map(int, input("Введите координаты точки (x y): ").split())
    pygame.init()

    width, height = 600, 400
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Task_1")

    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    X = np.matrix([[x], [y]])
    t = np.matrix([[1, 3], [4, 1]])
    X_new = t * X
    new_x, new_y = X_new[0][0].item(), X_new[1][0].item()
    print(f"Исходные координаты: ({x}, {y})")
    print(f"Преобразованные координаты: ({new_x}, {new_y})")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(white)

        pygame.draw.circle(window, red, (x + width // 2, height // 2 - y), 5)

        pygame.draw.circle(window, blue, (int(new_x) + width //
                                          2, height // 2 - int(new_y)), 5)

        pygame.display.flip()

    pygame.quit()


def task_2():
    pygame.init()

    width, height = 800, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Task_2")

    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)
    text = 'Nikita Makoveev'
    font = pygame.font.SysFont(None, 24)
    text_surface = font.render(text, True, green)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(white)

        pygame.draw.line(window, red, (200, 300), (400, 500), 2)
        pygame.draw.circle(window, blue, (500, 500), 50, 1)
        window.blit(text_surface, (50, 50))

        pygame.display.flip()

    pygame.quit()


def task_3():
    start_x, start_y = map(int, input(
        "Введите координаты начала отрезка (x y): ").split())
    end_x, end_y = map(int, input(
        "Введите координаты конца отрезка (x y): ").split())
    X = np.matrix([[start_x, start_y], [end_x, end_y]])
    t = np.matrix([[1, 3], [4, 1]])
    X_new = t * X
    new_x0, new_y0 = X_new[0, 0], X_new[0, 1].item()
    new_x1, new_y1 = X_new[1, 0].item(), X_new[1, 1].item()

    pygame.init()

    width, height = 800, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Task_2")

    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    green = (0, 255, 0)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(white)

        pygame.draw.line(window, red, (start_x, start_y), (end_x, end_y), 4)
        pygame.draw.line(window, blue, (new_x0, new_y0), (new_x1, new_y1), 4)

        pygame.display.flip()

    pygame.quit()


def task_4():
    start_x, start_y = 0, 100
    end_x, end_y = 200, 300
    middle_x, middle_y = (start_x+end_x)/2, (start_y+end_y)/2
    X = np.matrix([[start_x, start_y], [end_x, end_y]])
    t = np.matrix([[1, 2], [3, 1]])
    X_new = t * X
    new_x0, new_y0 = X_new[0, 0], X_new[0, 1].item()
    new_x1, new_y1 = X_new[1, 0].item(), X_new[1, 1].item()
    new_middle_x, new_middle_y = (new_x0+new_x1)/2, (new_y0+new_y1)/2

    pygame.init()

    width, height = 600, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Task_2")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(white)

        pygame.draw.line(window, red, (start_x, start_y), (end_x, end_y), 4)
        pygame.draw.circle(window, black, (middle_x, middle_y), 4)
        pygame.draw.line(window, blue, (new_x0, new_y0), (new_x1, new_y1), 4)
        pygame.draw.circle(window, black, (new_middle_x, new_middle_y), 4)

        pygame.display.flip()

    pygame.quit()


def task_5():
    x0, y0 = 50, 100
    x1, y1 = 250, 200
    x2, y2 = 50, 200
    x3, y3 = 250, 300
    X = np.matrix([[x0, y0], [x1, y1], [x2, y2], [x3, y3]])
    t = np.matrix([[1, 2], [3, 1]])
    X_new = X * t
    print("Изначальный коэффициент:", (y1-y0)/(x1-x0))
    print("Преобразованный коэффициент:",
          (X_new[0, 1]-X_new[1, 1])/(X_new[0, 0]-X_new[1, 0]))
    pygame.init()

    width, height = 600, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Task_2")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(white)

        for i in range(0, len(X), 2):
            pygame.draw.line(
                window, red, (X[i, 0], X[i, 1]), (X[i+1, 0], X[i+1, 1]),  5)
        for i in range(0, len(X_new), 2):
            pygame.draw.line(
                window, blue, (X_new[i, 0], X_new[i, 1]), (X_new[i+1, 0], X_new[i+1, 1]), 5)

        pygame.display.flip()

    pygame.quit()


def task_6():
    L = np.matrix([
        [-1/2, 3/2],
        [3, -2],
        [-1, -1],
        [3, 5/3]
    ]) * 100

    T = np.matrix([
        [1, 2],
        [1, -3]
    ])

    L_new = L * T
    offset = np.array([300, 400])
    L += offset
    L_new += offset

    pygame.init()
    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Task_6")

    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(white)

        for i in range(0, len(L), 2):
            pygame.draw.line(
                window, red, (L[i, 0], L[i, 1]), (L[i + 1, 0], L[i + 1, 1]), 3)

        for i in range(0, len(L_new), 2):
            pygame.draw.line(window, blue, (L_new[i, 0], L_new[i, 1]),
                             (L_new[i + 1, 0], L_new[i + 1, 1]), 3)

        pygame.display.flip()

    pygame.quit()


def task_7():
    L = np.matrix([
        [3, -1],
        [4, 1],
        [2, 1]
    ]) * 100

    T = np.matrix([
        [0, 1],
        [-1, 0]
    ])

    L_transformed = L * T
    offset = np.array([100, 200])
    L += offset
    L_transformed += offset

    pygame.init()
    width, height = 1100, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Task 7")

    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(white)

        pygame.draw.polygon(
            window, red, [(L[i, 0], L[i, 1]) for i in range(len(L))], 2)
        pygame.draw.polygon(window, blue, [(
            L_transformed[i, 0], L_transformed[i, 1]) for i in range(len(L_transformed))], 2)

        pygame.display.flip()

    pygame.quit()


def task_8():
    L = np.matrix([
        [8, 1],
        [7, 3],
        [6, 2]
    ]) * 100

    T = np.matrix([
        [0, 1],
        [1, 0]
    ])

    L_transformed = L * T
    offset = np.array([-100, -100])
    L += offset
    L_transformed += offset

    pygame.init()
    width, height = 1200, 800
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Task 8")

    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(white)

        pygame.draw.polygon(
            window, red, [(L[i, 0], L[i, 1]) for i in range(len(L))], 2)
        pygame.draw.polygon(window, blue, [(
            L_transformed[i, 0], L_transformed[i, 1]) for i in range(len(L_transformed))], 2)

        pygame.display.flip()

    pygame.quit()


def task_9():
    L = np.matrix([
        [5, 1],
        [5, 2],
        [3, 2]
    ]) * 100

    T = np.matrix([
        [2, 0],
        [0, 2]
    ])

    L_transformed = L * T
    offset = np.array([-300, 100])
    L += offset
    L_transformed += offset

    pygame.init()
    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Task 9")

    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(white)

        pygame.draw.polygon(
            window, red, [(L[i, 0], L[i, 1]) for i in range(len(L))], 2)
        pygame.draw.polygon(window, blue, [(
            L_transformed[i, 0], L_transformed[i, 1]) for i in range(len(L_transformed))], 2)

        pygame.display.flip()

    pygame.quit()


def task_10():
    pygame.init()
    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Task 10")

    white = (255, 255, 255)
    black = (0, 0, 0)

    a = 100
    b = 50

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(white)

        for theta in np.arange(0, 128 * np.pi, 0.01):
            r = b + 2 * a * np.cos(theta)
            x = int(r * np.cos(theta)) + 300 // 2
            y = int(r * np.sin(theta)) + 300 // 2
            pygame.draw.circle(window, black, (x, y), 1)

        pygame.display.flip()

    pygame.quit()


def task_11():
    L = np.matrix([
        [2, -2],
        [-2, -2],
        [-2, 2],
        [2, 2]
    ]) * 100

    center = np.array([0, 0])
    offset = np.array([300, 300])

    T_scale = np.matrix([
        [0.9, 0],
        [0, 0.9]
    ])

    angle = np.pi / 32
    T_rotate = np.matrix([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle), np.cos(angle)]
    ])

    L += offset

    pygame.init()
    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Task 11")

    white = (255, 255, 255)
    black = (0, 0, 0)

    running = True
    for _ in range(20):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        window.fill(white)

        pygame.draw.polygon(
            window, black, [(L[i, 0], L[i, 1]) for i in range(len(L))], 2)
        pygame.display.flip()
        time.sleep(0.3)
        L -= offset
        L = L * T_scale * T_rotate
        L += offset
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()


if __name__ == "__main__":
    # task_7()
    # task_8()
    # task_9()
    # task_10()
    task_11()
