from .interface import ValidatorInterface

class CarneValidator:
    
    def validate(self,comida: str) ->bool:

        if comida == 'Carne': return True
        return False
    
    def action(self)-> None:
        print('O leão come Carne')
        
