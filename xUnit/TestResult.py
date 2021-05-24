class TestResult:
    def __init__(self):
        self.runCount = 0
        self.failureCount = 0

    def testStarted(self):
        self.runCount += 1

    def testFailed(self):
        self.failureCount += 1

    def summary(self):
        return "%d run, %d failed" % (self.runCount, self.failureCount)
