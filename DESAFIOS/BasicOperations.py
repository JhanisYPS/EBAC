class BasicOperations:
    def __init__(self, input: float = 0) -> None:
        self.input = input
        
    def sums(self, value:float) -> float:
        addition = self.input + value
        return addition

    def sub(self, subtracting:float) -> float:
        minued = self.input
        subtraction = minued - subtracting
        return subtraction

    def mult(self, value:float) -> float:
        multiplication = self.input*value
        return multiplication

    def div(self, divisor:float) -> float:
        dividend = self.input
        try:
            quotient = dividend/divisor
        except ZeroDivisionError:
            quotient = None
        return quotient
