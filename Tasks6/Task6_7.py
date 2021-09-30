from functools import total_ordering
@total_ordering
class Money:
    """Implement a class Money to represent value and currency.
     You need to implement methods to use all basic arithmetics expressions (comparison, division, multiplication,
      addition and subtraction). Tip: use class attribute exchange rate which is dictionary and stores information about
       exchange rates to your default currency"""
    exchange_rate = {
        "EUR": 0.93,
        "BYN": 2.1,
        "USD": 1,
        "JPY": 111.55
    }

    def __init__(self, value: float, currency="USD"):
        self.value = value
        self.currency = currency

    def __str__(self):
        return f"{self.value:.2f} {self.currency}"

    def __add__(self, other):
        if isinstance(other, (int, float)):
            result = self.value + other
        else:
            result = self.value + (other.value * Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency])
        return Money(result, self.currency)

    def __radd__(self, other):
        return Money(other + self.value, self.currency)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result = self.value * other
        else:
            result = self.value * (other.value * Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency])
        return Money(result, self.currency)

    def __rmul__(self, other):
        return Money(other * self.value, self.currency)

    def __truediv__(self, other):
        try:
            if isinstance(other, (int, float)):
                result = self.value / other
                return Money(result, self.currency)
        except ZeroDivisionError:
                print("you can't divide on zero")
        else:
            try:
                result = self.value * (other.value * Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency])
                return Money(result, self.currency)
            except ZeroDivisionError:
                print("you can't divide on zero")

    def __rtruediv__(self, other):
        try:
            return Money(other / self.value, self.currency)
        except:
            print("you can't divide on zero")

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            result = self.value - other
        else:
            result = self.value - (
                        other.value * Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency])
        return Money(result, self.currency)

    def __rsub__(self, other):
        return Money(other - self.value, self.currency)

    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.value == other
        else:
            return self.value == other.value * Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency]

    def __ne__(self, other):
        if isinstance(other, (int, float)):
            return self.value != other
        else:
            return self.value != other.value * Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency]

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.value < other
        else:
            return self.value < other.value * Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency]

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.value > other
        else:
            return self.value > other.value * Money.exchange_rate[self.currency] / Money.exchange_rate[other.currency]

x = Money(10, "BYN")
y = Money(11) # define your own default value, e.g. “USD”
z = Money(12.34, "EUR")
print(z + 3.11 * x + y * 0.8) # result in “EUR”
#>>34.30 EUR

lst = [Money(10,"BYN"), Money(11), Money(12.01, "JPY")]
s = sum(lst)
print(s) #result in “BYN”
#33.33 BYN
