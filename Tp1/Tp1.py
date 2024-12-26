import turtle as t
import random

#program untuk membuat kotak warna warni 
def draw_square(color):
    t.penup()  
    t.setheading(0)
    t.fillcolor(color)
    t.pencolor(color)
    t.begin_fill()
    t.pendown()
    t.setheading(0)
    for side in range(4): #ngeloop untuk membuat sisi persegi
        t.forward(size_of_square)
        t.right(90)
    t.end_fill()
    t.penup()


# meminta input kepada user banyak nya baris dan luas persegi
number_of_rows = int(t.numinput("Olympic Logo and Colorful Chessboard", "Enter the number of rows: ", None, 2, 25))
size_of_square = t.numinput("Olympic Logo and Colorful Chessboard", "Enter the square size (pixels): ", None, 5, 50)

black = (0, 0, 0)
red = (238, 51, 78)
orange = (252, 177, 49)
green = (0, 166, 81)
blue = (0, 129, 200)


t.speed(0)
t.pensize(10)
t.pendown()
t.colormode(255)

# program untuk membuat pola lingkaran bagian atas 
t.pencolor(black)
t.penup()
t.goto(0, 200)
t.pendown()
t.circle(50)

t.pencolor(red)
t.penup()
t.goto(120, 200)
t.pendown()
t.circle(50)

t.pencolor(blue)
t.penup()
t.goto(-120, 200)
t.pendown()
t.circle(50)

t.pencolor(orange)
t.penup()
t.goto(-60, 150)
t.pendown()
t.circle(50)

t.pencolor(green)
t.penup()
t.goto(60, 150)
t.pendown()
t.circle(50)

# program untuk menimpa ulang beberapa lingkaran pola bagian atas
t.pencolor(black)
t.penup()
t.goto(0, 200)
t.pendown()
t.circle(50, -45)

t.penup()
t.goto(50, 250)
t.setheading(90)
t.pendown()
t.circle(50, -45)

t.penup()
t.goto(120, 200)
t.pencolor(red)
t.setheading(0)
t.pendown()
t.circle(50, -45)

t.penup()
t.goto(-70, 250)
t.pencolor(blue)
t.setheading(90)
t.pendown()
t.circle(50, -45)

# program untuk membuat pola lingkaran bagian bawah 
t.setheading(0)
t.pensize(10)
t.pendown()
t.colormode(255)

t.pencolor(black)
t.penup()
t.goto(0, 0)
t.pendown()
t.circle(50)

t.pencolor(red)
t.penup()
t.goto(120, 0)
t.pendown()
t.circle(50)

t.pencolor(blue)
t.penup()
t.goto(-120, 0)
t.pendown()
t.circle(50)

t.pencolor(orange)
t.penup()
t.goto(-60, 0)
t.pendown()
t.circle(50)

t.pencolor(green)
t.penup()
t.goto(60, 0)
t.pendown()
t.circle(50)

#  program untuk menimpa ulang beberapa lingkaran pola bagian bawah
t.penup()
t.goto(-70, 50)
t.pencolor(blue)
t.setheading(90)
t.pendown()
t.circle(50, 90)

t.penup()
t.goto(50, 50)
t.pencolor(black)
t.setheading(90)
t.pendown()
t.circle(50, 90)

t.penup()
t.goto(0, 0)
t.pencolor(black)
t.setheading(0)
t.pendown()
t.circle(50, -90)

t.penup()
t.goto(120, 0)
t.pencolor(red)
t.setheading(-360)
t.pendown()
t.circle(50, -90)

t.penup()

#menyimpan luas persegi panjang yang di gambar
total_height = size_of_square * number_of_rows

# untuk menghitung jumlah jarak antara lingkaran dan persegi 
start_y = - total_height / 2


# Membuat chessboard 
t.pensize(1)
for row in range(number_of_rows):
    for col in range(number_of_rows):
        x_pos = -number_of_rows * size_of_square / 2 + col * size_of_square
        y_pos = start_y + row * -size_of_square  
        t.goto(x_pos, y_pos)
        color = (int(random.random() * 255), int(random.random() * 255), int(random.random() * 255))
        draw_square(color)

t.penup()
t.goto(0, start_y + number_of_rows * -size_of_square - 50)  
t.pencolor(0,0,245)  
t.pendown()
t.write(f"Olympic Logo and Colorful Chessboard of {number_of_rows*number_of_rows} Squares", align="center", font=("Arial", 20, "normal"))

t.hideturtle()
t.done()
