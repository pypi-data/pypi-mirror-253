import math

class GeometryUtils:

    def square_area(self, side):
        return side * side

    def rectangle_area(self, base, height):
        return base * height

    def triangle_area_heron(self, side_a, side_b, side_c):
        s = (side_a + side_b + side_c) / 2
        area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
        return area

    def triangle_area_equilateral(self, side):
        area = (math.sqrt(3) / 4) * side ** 2
        return area

    def triangle_area(self, base, height):
        area = (base * height) / 2
        return area

    def circle_area(self, radius):
        area = math.pi * radius ** 2
        return area

    def trapeze_area(self, base1, base2, height):
        area = ((base1 + base2) * height) / 2
        return area

    def parallelogram_area(self, base, height):
        area = base * height
        return area

    def rhombus_area(self, diagonal1, diagonal2):
        area = (diagonal1 * diagonal2) / 2
        return area

    def hexagon_area(self, side):
        area = (3 * math.sqrt(3) / 2) * side ** 2
        return area

    def pentagon_area(self, side):
        area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side ** 2
        return area

    def heptagon_area(self, side):
        pi = math.pi
        angle_rad = pi / 7.0
        area = (7.0 / 4.0) * side ** 2 / math.tan(angle_rad)
        return area

    def octagon_area(self, side):
        area = 2 * (1 + math.sqrt(2)) * side ** 2
        return area

    def square_perimeter(self, side):
        return side * 4

    def rectangle_perimeter(self, side):
        return side * 4

    def triangle_perimeter(self, side):
        return side * 3

    def circle_perimeter(self, radius):
        return 2 * math.pi * radius

    def trapeze_perimeter(self, side_a, side_b, side_c, side_d):
        return side_a + side_b + side_c + side_d

    def parallelogram_perimeter(self, side_a, side_b, side_c, side_d):
        return side_a + side_b + side_c + side_d

    def rhombus_perimeter(self, side):
        return side * 4

    def hexagon_perimeter(self, side):
        return side * 6

    def pentagon_perimeter(self, side):
        return side * 5

    def heptagon_perimeter(self, side):
        return side * 7

    def octagon_perimeter(self, side):
        return side * 8

    def cube_area(self, side):
        area = 6 * side ** 2
        return area

    def parallelepiped_area(self, length, width, height):
        area = 2 * (length * width + width * height + height * length)
        return area

    def sphere_area(self, radius):
        area = 4 * math.pi * radius ** 2
        return area

    def triangular_pyramid_area(self, side_a, side_b, side_c, height):
        semiperimeter = (side_a + side_b + side_c) / 2
        area_base = math.sqrt(semiperimeter * (semiperimeter - side_a) * (semiperimeter - side_b) * (semiperimeter - side_c))
        area_side = 0.5 * (side_a + side_b + side_c) * height
        return area_base + area_side

    def square_pyramid_area(self, side, height):
        area = side ** 2 + 4 * 0.5 * side * height
        return area

    def pentagon_pyramid_area(self, side_base, apothem):
        area_base = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_base ** 2
        base_perimeter = 5 * side_base
        return area_base + 0.5 * base_perimeter * apothem

    def hexagon_pyramid_area(self, side_base, apothem):
        area_base = (3 * math.sqrt(3) / 2) * side_base ** 2
        base_perimeter = 6 * side_base
        return area_base + 0.5 * base_perimeter * apothem

    def cylinder_area(self, radius, height):
        pi = math.pi
        base_area = 2 * pi * radius ** 2
        side_area = 2 * pi * radius * height
        return base_area + side_area

    def cone_area(self, radius, side_height):
        pi = math.pi
        base_area = pi * radius ** 2
        side_area = pi * radius * side_height
        return base_area + side_area

    def triangular_prism_area(self, side_a, side_b, prism_height):
        area_base = 0.5 * side_a * side_b
        base_perimeter = side_a + side_b + math.sqrt(side_a ** 2 + side_b ** 2)
        side_area = base_perimeter * prism_height
        return area_base + 2 * side_area

    def pentagon_prism_area(self, pentagon_side, prism_height):
        area_base = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pentagon_side ** 2
        base_perimeter = 5 * pentagon_side
        side_area = base_perimeter * prism_height
        return area_base + 5 * side_area

    def hexagon_prism_area(self, hexagon_side, prism_height):
        area_base = (3 * math.sqrt(3) / 2) * hexagon_side ** 2
        base_perimeter = 6 * hexagon_side
        side_area = base_perimeter * prism_height
        return area_base + 6 * side_area

    def cube_volume(self, side_cube):
        return side_cube ** 3

    def parallelepiped_volume(self, length, width, height):
        return length * width * height

    def sphere_volume(self, radius):
        return (4.0 / 3.0) * math.pi * radius ** 3

    def triangular_pyramid_volume(self, triangle_base, triangle_height, pyramid_height):
        base_area = 0.5 * triangle_base * triangle_height
        return (1.0 / 3.0) * base_area * pyramid_height

    def square_pyramid_volume(self, base_length, base_width, pyramid_height):
        area_base = base_length * base_width
        return (1.0 / 3.0) * area_base * pyramid_height

    def pentagon_pyramid_volume(self, pentagon_side, pyramid_height):
        base_area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pentagon_side ** 2
        return (1.0 / 3.0) * base_area * pyramid_height

    def hexagon_pyramid_volume(self, hexagon_side, pyramid_height):
        area_base = (3 * math.sqrt(3) / 2) * hexagon_side ** 2
        return (1.0 / 3.0) * area_base * pyramid_height

    def cylinder_volume(self, radius, cylinder_height):
        pi = math.pi
        return pi * radius ** 2 * cylinder_height

    def cone_volume(self, radius, cone_height):
        pi = math.pi
        return (1.0 / 3.0) * pi * radius ** 2 * cone_height

    def triangular_prism_volume(self, triangle_base, triangle_height, prism_height):
        base_area = 0.5 * triangle_base * triangle_height
        return base_area * prism_height

    def pentagon_prism_volume(self, pentagon_side, prism_height):
        base_area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * pentagon_side ** 2
        return base_area * prism_height

    def hexagon_prism_volume(self, hexagon_side, prism_height):
        base_area = (3 * math.sqrt(3) / 2) * hexagon_side ** 2
        return base_area * prism_height
