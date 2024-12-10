from .interface import ValidatorInterface

class NosValidator:
    
    def validate(self,comida: str) ->bool:

        if comida == 'Nos': return True
        return False
    
    def action(self)-> None:
        print('O esquilo come Nos')
        
