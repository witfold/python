from lesson7.Task2.Coat import Coat
from lesson7.Task2.Suit import Suit

coat = Coat('Coat1', 10)
suit = Suit('Suit1', 5)

print(f'V={coat.v}, fabric={coat.calc()}')
print(f'H={suit.h}, fabric={suit.calc()}')
