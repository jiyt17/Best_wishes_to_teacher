class Student:
    def __init__(self, name:str) -> None:
        self.name = name
        self._knowledge = 0
        self.supervisor = None
    
    def set_supervisor(self, supervisor) -> None:
        self.supervisor = supervisor

    def increase_knowledge_by_listening(self) -> None:
        self._knowledge += 1

    def increase_knowledge_by_reporting(self) -> None:
        self._knowledge += 3
        print(self.name + " 's knowledge has increased a lot after making a PPT report!")

    @property
    def knowledge(self) -> int:
        return self._knowledge
