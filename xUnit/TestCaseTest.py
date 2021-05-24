from xUnit.TestCase import TestCase
from xUnit.WasRun import WasRun


class TestCaseTest(TestCase):
    def testTemplateMethod(self):
        test = WasRun("testMethod")
        test.run()
        assert "setUp testMethod tearDown " == test.log


TestCaseTest("testTemplateMethod").run()
