from abc import ABC, abstractmethod

class CommandInterface(ABC):
    @abstractmethod
    def exectute(self) -> None:
        pass 
    


