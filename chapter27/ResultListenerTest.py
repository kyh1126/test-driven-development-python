from chapter27.TestResult import TestResult
from chapter27.WasRun import WasRun


# 1: 이벤트 리스너를 위해 만든 별도의 이벤트 통보 횟수 세는 객체
class ResultListener(object):
    def __init__(self):
        self.count = 0

    def startTest(self):
        self.count += 1


# 2: 이벤트 리스너를 위해 별도의 객체를 만드는 대신 테스트 케이스 자체를 리스너로 쓴다.
class ResultListenerTest:
    def __init__(self):
        self.count = 0

    def testNotification(self):
        result = TestResult()
        result.addListener(self)
        WasRun("testMethod").run(result)
        assert 1 == self.count

    def startTest(self):
        self.count += 1
        print("test started")


ResultListenerTest().testNotification()
