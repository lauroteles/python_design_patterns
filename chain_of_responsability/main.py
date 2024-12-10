# '''Metodologia não recomendada '''


# class Validador:
#     def validar(self,comida: str):
#         if (comida == 'banana'):
#             self.__acao1()
#         elif (comida == 'nos'):
#             self.__acao2()
#         elif (comida == 'carne'):
#             self.__acao3()
#         else:
#             self.__acaoDefault()    

#     def __acao1(self):
#         print('O macaco come banana')
#     def __acao2(self):
#         print('O esquilo come a nos')
#     def __acao3(self):
#         print('O leao come carne')
#     def __acaoDefault(self):
#         print('Comida indefinida')    

from .validatoris import BananaValidator, CarneValidator, NosValidator


class Validacao:
    
    def __init__(self) -> None:
        self.val = [
        BananaValidator(),
        CarneValidator(),
        NosValidator()]

    def process(self, comida: str):
        for v in self.val:
            if v.validate(comida): return v.action()

validacao = Validacao()
validacao.process('banana')
