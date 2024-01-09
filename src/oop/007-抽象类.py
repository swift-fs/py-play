from abc import ABC, abstractmethod


class Action(ABC):
    @abstractmethod
    def excute(self):
        raise NotImplementedError


class CreateAction(Action):
    def __init__(self, name: str) -> None:
        self.name = name

    def excute(self):
        print(f"create {self.name}")


class DeleteAction(Action):
    def __init__(self, name: str) -> None:
        self.name = name

    def excute(self):
        print(f"delete {self.name}")


def excute_action(action: Action):
    action.excute()


def main():
    del_action = DeleteAction(name="called")
    create_action = CreateAction(name="called")
    excute_action(create_action)
    excute_action(del_action)

    action = Action()
    excute_action(action)


if __name__ == "__main__":
    main()
