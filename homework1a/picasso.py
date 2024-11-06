
from byubit import Bit


@Bit.empty_world(8,8)
def picasso(bit):
    bit.move()
    bit.move()
    bit.paint('red')
    bit.left()
    bit.paint('green')
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.move()
    bit.right()
    bit.move()
    bit.paint('red')
    bit.move()
    bit.paint('green')
    bit.right()
    bit.move()
    bit.paint('blue')
    bit.move()
    bit.move()
    bit.paint('red')

if __name__ == '__main__':
    picasso(Bit.new_bit)