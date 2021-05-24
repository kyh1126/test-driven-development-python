from xUnit.TestCase import TestCase
from xUnit.TestResult import TestResult
from xUnit.WasRun import WasRun


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log

    def testResult(self):
        test = WasRun("testMethod")
        result = test.run()
        assert "1 run, 0 failed" == result.summary()

    def testFailedResult(self):
        test = WasRun("testBrokenMethod")
        result = test.run()
        assert "1 run, 1 failed" == result.summary()

    def testFailedResultFormatting(self):
        result = TestResult()
        result.testStarted()
        result.testFailed()
        assert "1 run, 1 failed" == result.summary()


print("testTemplateMethod:", TestCaseTest("testTemplateMethod").run().summary())
print("testResult:", TestCaseTest("testResult").run().summary())
print("testFailedResult:", TestCaseTest("testFailedResult").run().summary())
print("testFailedResultFormatting:", TestCaseTest("testFailedResultFormatting").run().summary())
