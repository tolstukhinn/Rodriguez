import pytest

class TestExample:

    @pytest.mark.usefixtures("WDI")
    def test_example(self):
        self.driver.get("https://google.com")

