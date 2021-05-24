from xUnit.TestCase import TestCase
from xUnit.WasRun import WasRun


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        # assert not test.wasRun
        self.test.run()
        assert self.test.wasRun

    def testSetUp(self):
        self.test.run()
        # assert self.test.wasSetUp
        assert "setUp " == self.test.log


TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
