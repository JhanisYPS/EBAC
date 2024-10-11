class ScientificOperations:
    def __init__(self) -> None:
        pass
        
    def power(self, base: float, exponent: float) -> float:
        return base ** exponent
    
    def root(self, radicand: float, index: float) -> float:
        return self.power(radicand, 1 / index)
    
    def log(self, base: float, argument: float) -> float:
        # Verificações para valores inválidos
        if base <= 0 or base == 1 or argument <= 0:
            return None  # Retorna None se a base ou o argumento não são válidos

        guess = argument / base  # Começa com uma estimativa inicial
        tolerance = 0.00001  # Defina a precisão desejada

        while True:
            # f(x) = base^guess - argument
            power_result = self.power(base, guess)
            f_guess = power_result - argument

            # Derivada de f(x) = base^x * ln(base)
            # Aproximamos ln(base) usando (base - 1) / base como uma simplificação inicial
            ln_base = (base - 1) / base  
            derivative = power_result * ln_base

            # Atualiza o valor de 'guess' usando o Método de Newton
            new_guess = guess - f_guess / derivative

            # Se a diferença entre as aproximações for pequena o suficiente, paramos
            if abs(new_guess - guess) < tolerance:
                return round(new_guess, 5)
            
            guess = new_guess  # Atualiza a estimativa
