class TestResult:
    def __init__(self):
        self.listeners = []

    def addListener(self, listener):
        self.listeners.append(listener)

    def testStarted(self):
        for listener in self.listeners:
            listener.startTest()
            print("listener added")

    def testFailed(self):
        pass
