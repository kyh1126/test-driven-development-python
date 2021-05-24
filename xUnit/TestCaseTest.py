from xUnit.TestCase import TestCase
from xUnit.WasRun import WasRun


class TestCaseTest(TestCase):
    # def setUp(self):
    #     self.test = WasRun("testMethod")

    # def testRunning(self):
    #     self.test.run()
    #     assert self.test.wasRun

    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod " == test.log


# TestCaseTest("testRunning").run()
# TestCaseTest("testSetUp").run()
TestCaseTest("testTemplateMethod").run()
