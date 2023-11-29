# coding: utf-8
# license: GPLv3

import numpy as np

gravitational_constant = 6.67408E-11
"""Гравитационная постоянная Ньютона G"""


def calculate_force(body, space_objects):
    """Вычисляет силу, действующую на тело.

    Параметры:

    **body** — тело, для которого нужно вычислить дейстующую силу.

    **space_objects** — список объектов, которые воздействуют на тело.
    """

    body.Fx = body.Fy = 0
    for obj in space_objects:
        if body == obj:
            continue  # тело не действует гравитационной силой на само себя!

        r = np.array([body.x - obj.x, body.y - obj.y])  # Вектор, направленный от body к obj
        absr = np.linalg.norm(r)  # Модуль этого вектора

        eps = 10**7
        absr = np.sqrt(absr**2 + eps**2)

        body_force = ((gravitational_constant * body.m * obj.m) / absr**3) * -r

        # Вектор силы, действующей со стороны obj на body
        obj_force = - body_force

        # Покомпонентно раскладываем силы, действующие на тела
        body.Fx += body_force[0]
        body.Fy += body_force[1]

        #obj.Fx += obj_force[0]
        #obj.Fy += obj_force[1]


def move_space_object(body, dt):
    """Перемещает тело в соответствии с действующей на него силой.

    Параметры:

    **body** — тело, которое нужно переместить.
    """
    ax = body.Fx/body.m
    ay = body.Fy/body.m

    body.Vx += ax * dt
    body.Vy += ay * dt

    body.x += body.Vx * dt
    body.y += body.Vy * dt

    body.Fx = 0
    body.Fy = 0


def recalculate_space_objects_positions(space_objects, dt):
    """Пересчитывает координаты объектов.

    Параметры:

    **space_objects** — список оьъектов, для которых нужно пересчитать координаты.

    **dt** — шаг по времени
    """
    for body in space_objects:
        calculate_force(body, space_objects)
    for body in space_objects:
        move_space_object(body, dt)


if __name__ == "__main__":
    print("This module is not for direct call!")
