from ..classes import BaseExecutor


class Handlers(dict):
    instances = {}

    def add_handler(self, data_type: str, handler: BaseExecutor):
        self.update({data_type: handler})
        if handler not in self.instances:
            self.instances.update({handler: handler()})

    def get_instance(self, instance_type):
        return self.instances.get(instance_type)


handlers = Handlers()
