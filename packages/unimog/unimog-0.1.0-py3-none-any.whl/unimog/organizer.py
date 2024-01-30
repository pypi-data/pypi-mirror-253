from unimog.action import Action


class Organizer(Action):
    def __init__(self, *actions: type[Action]):
        super().__init__()

        self.actions = actions

    def perform(self) -> None:
        for action_class in self.actions:
            if self.context.is_failure():
                raise Exception(self.context.error)

            action = action_class()
            result = action(context=self.context)
            self.context = result
