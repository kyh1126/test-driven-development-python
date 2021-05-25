from chapter27.TestResult import TestResult
from chapter27.WasRun import WasRun


# 1: 이벤트 리스너를 위해 만든 별도의 이벤트 통보 횟수 세는 객체
class ResultListener(object):
    def __init__(self):
        self.count = 0

    def startTest(self):
        self.count += 1


class ResultListenerTest:
    def testNotification(self):
        result = TestResult()
        listener = ResultListener()
        result.addListener(listener)
        WasRun("testMethod").run(result)
        assert 1 == listener.count


ResultListenerTest().testNotification()
