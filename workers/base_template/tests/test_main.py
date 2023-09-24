from unittest import mock
import pytest
from source import main


def test_main():
    assert main.main() == "OK"


def test_init():
    with mock.patch.object(main, "main", return_value=42):
        with mock.patch.object(main, "__name__", "__main__"):
            with mock.patch.object(main.sys, "exit") as mock_exit:
                main.init()
                assert mock_exit.call_args[0][0] == 42
