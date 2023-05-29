from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    # inputs放這邊是因為我確定只有process會用到它
    def run(self, inputs):
        data = None
        for step in self.steps:
            try:
                # 把return出來的東西接手，傳進下一個step
                data = step.process(data, inputs)
            except StepException as e:
                print(f'Exception happened: {e}')
                break
        return data
