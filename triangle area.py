import math

# Method 1: Calculate area using base and height
def triangle_area_base_height(base, height):
    return 0.5 * base * height

# Method 2: Calculate area using Heron's formula (three sides)
def triangle_area_heron(a, b, c):
    s = (a + b + c) / 2  # Semi-perimeter
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

# Method 3: Calculate area using coordinates of the triangle vertices
def triangle_area_coordinates(x1, y1, x2, y2, x3, y3):
    return abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2)) / 2

# Main program to interact with user
def main():
    print("Choose method to calculate triangle area:")
    print("1. Base and Height")
    print("2. Heron's Formula (Three sides)")
    print("3. Coordinates of vertices")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        area = triangle_area_base_height(base, height)
        print(f"The area of the triangle is: {area}")

    elif choice == "2":
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        c = float(input("Enter the length of side c: "))
        area = triangle_area_heron(a, b, c)
        print(f"The area of the triangle is: {area}")

    elif choice == "3":
        x1, y1 = map(float, input("Enter the coordinates of vertex 1 (x1, y1): ").split())
        x2, y2 = map(float, input("Enter the coordinates of vertex 2 (x2, y2): ").split())
        x3, y3 = map(float, input("Enter the coordinates of vertex 3 (x3, y3): ").split())
        area = triangle_area_coordinates(x1, y1, x2, y2, x3, y3)
        print(f"The area of the triangle is: {area}")

    else:
        print("Invalid choice! Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
