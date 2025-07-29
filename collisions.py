import math
import pygame

from circleshape import *
from triangleshape import *

def circle_circle_collision(circle1, circle2):
    return circle1.position.distance_to(circle2.position) <= circle1.radius + circle2.radius

def closest_point_on_segment(point, segment_start, segment_end):
    v = segment_end - segment_start
    u = point - segment_start
    t = u.dot(v)/v.dot(v)

    closest_point = None
    if t < 0:
        closest_point = segment_start
    elif t > 1:
        closest_point = segment_end
    else:
        closest_point = segment_start + t * v
    return closest_point

def distance(p1, p2):
    return math.sqrt((p1.x-p2.x) **2 + (p1.y-p2.y)**2)

def triangle_circle_collision(triangle, circle):
    triangle_points = triangle.calc_points()
    # Case One: Triangle vertex inside of circle
    # If distance from circle center to triangle vertex is less than radius,
    # the circle is touching the vertex.
    for point in triangle_points:
        if distance(circle.position, point) <= circle.radius:
            print(f'Case 1 Collision')
            return True

    # Case Two: Circle center is inside of triangle
    # Take edge of each triangle and cross product it with vector
    # from each vertex to circle center
    # If all cross products are positive, the circle center
    # is inside the triangle. This is because the
    # vectors of the triangle vertices are arranged clockwise
    point_a = triangle_points[0]
    point_b = triangle_points[1]
    point_c = triangle_points[2]

    vec_a_b = point_b - point_a
    vec_a_circle = circle.position - point_a
    vec_b_c = point_c  - point_b
    vec_b_circle = circle.position - point_b
    vec_c_a = point_a - point_c
    vec_c_circle = circle.position - point_c

    cross_products = [
        vec_a_b.cross(vec_a_circle),
        vec_b_c.cross(vec_b_circle),
        vec_c_a.cross(vec_c_circle)
    ]

    all_positive = True
    for product in cross_products:
        if product <= 0:
            all_positive = False
    if all_positive:
        print(f'Case 2 Collision')
        return True

    # Case Three: Circle center is outside triangle, and circle perimeter
    # extends into edge of triangle without touching a vertex.
    #   Step one: Get the nearest point on each edge of the triangle to the circle
    #   Step two: Get the minimum of these distances
    #   Step three: if the distance from the the circle center
    #   to the point on the segment is less than the radius, 
    #   there is a collision.
    proj_s_ab = closest_point_on_segment(circle.position, point_a, point_b)
    proj_s_bc = closest_point_on_segment(circle.position, point_b, point_c)
    proj_s_ca = closest_point_on_segment(circle.position, point_c, point_a)

    dist_s_ab = distance(circle.position, proj_s_ab)
    dist_s_bc = distance(circle.position, proj_s_bc)
    dist_s_ca = distance(circle.position, proj_s_ca)

    if dist_s_ab <= circle.radius or \
       dist_s_bc <= circle.radius or \
       dist_s_ca <= circle.radius:
        print(f'Case 3 Collision')
        return True

    return False

