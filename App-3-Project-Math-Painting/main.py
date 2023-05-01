from canvas import Canvas
from shapes import Square, Rectangle

canvas_width = int(input('Enter canvas width:  '))
canvas_height = int(input('Enter canvas height:  '))
canvas_color = {'white': (255, 255, 255), 'black': (0, 0, 0)}
color = input('Enter color (white or black): ').lower()

canvas = Canvas(height=canvas_height, width=canvas_width,
                color=canvas_color[color])

while True:
    # defines shape type
    shape_type = input('Shape type (square or rectangle): ')

    if shape_type.lower() == 'rectangle':
        # set rectangle values
        rec_x = int(input('Enter rectangle x: '))
        rec_y = int(input('Enter rectangle y: '))
        rec_height = int(input('Enter rectangle height: '))
        rec_width = int(input('Enter rectangle width: '))
        rec_red = int(input('Enter rectangle amount red: '))
        rec_green = int(input('Enter rectangle amount green: '))
        rec_blue = int(input('Enter rectangle amount blue: '))

        # create rectangle object
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height,
                       width=rec_width, color=(rec_red, rec_green, rec_blue))
        r1.draw(canvas)

    if shape_type.lower() == 'square':
        # set square values
        sqr_x = int(input('Enter square x: '))
        sqr_y = int(input('Enter square y: '))
        sqr_side = int(input('Enter square\'s side of size: '))
        sqr_red = int(input('Enter square amount red: '))
        sqr_green = int(input('Enter square amount green: '))
        sqr_blue = int(input('Enter square amount blue: '))

        # create square object
        s1 = Square(x=sqr_x, y=sqr_y, side=sqr_side,
                    color=(sqr_side, sqr_green, sqr_blue))
        s1.draw(canvas)

    # Create canvas
    canvas.make('canvas.png')
