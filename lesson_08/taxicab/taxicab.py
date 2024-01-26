class Taxicab:
    '''FIRST CLASS EVER'''

    def __init__(moop, x_coord, y_coord):
        moop._x_coord = x_coord
        moop._y_coord = y_coord
        moop._odometer_reading = 0
    
    def get_x_coord(moop):
        return moop._x_coord
    def get_y_coord(moop):
        return moop._y_coord
    def shoot_lasers(moop):
        return 'pew pew pew'
    def get_odometer_reading(moop):
        return moop._odometer_reading
    
    def move_x(moop, left_right):
       moop._x_coord = moop.get_x_coord() + left_right
       moop._odometer_reading += abs(left_right)

    def move_y(moop, up_down):
        moop._y_coord = moop.get_y_coord() + up_down
        moop._odometer_reading += abs(up_down)

taxi_cab_one = Taxicab(5,-8)
taxi_cab_one.move_x(3)
taxi_cab_one.move_y(-4)
taxi_cab_one.move_x(-1)
print(taxi_cab_one.get_x_coord())
print(taxi_cab_one.get_y_coord())
print(taxi_cab_one.get_odometer_reading())
