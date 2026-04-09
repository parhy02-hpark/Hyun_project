# ============================================================================
# Copyright 2015 BRAIN Corporation. All rights reserved. This software is
# provided to you under BRAIN Corporation's Beta License Agreement and
# your use of the software is governed by the terms of that Beta License
# Agreement, found at http://www.braincorporation.com/betalicense.
# ============================================================================
import pytest
from subprocess import CalledProcessError
from shell_utils import execute_with_timeout, shell_command
from Queue import Empty


def test_shell_command():
    output = shell_command(['echo', "hello world"])
    assert output == "hello world\n"
    with pytest.raises(CalledProcessError) as failed_call:
        shell_command(["ls", "--aslkdjf"])
    assert failed_call.value.returncode > 0

def test_shell_command2():
    output = shell_command(['ifm3d'])
    assert output == "ifm3d: version=0.8.3\n"

def test_shell_go():
    output = shell_command(['go', "version"])
    assert output == "go version go1.7.5 linux/amd64\n"


def test_execute_with_timeout():
    with pytest.raises(Empty):
        execute_with_timeout(
            target=shell_command, args=(["sleep", "5"], ), timeout=1)
    output = execute_with_timeout(
        target=shell_command, args=(['echo', 'hello world'], ), timeout=1)
    assert output == 'hello world\n'


def test_execute_with_timeout_good_exception_message():
    # Doesn't seem to be possible in general
    # to propagate any python exception between processes, but
    # we can capture stack trace and exception string.
    with pytest.raises(Exception) as error:
        execute_with_timeout(
            target=shell_command, args=(['ls', '-laksdjf'], ), timeout=1)

    error_str = str(error.value)
    assert "File " in error_str  # Weak test that stacktrace is printed.
    assert "Command '['ls', '-laksdjf']' returned non-zero exit status 2 "
