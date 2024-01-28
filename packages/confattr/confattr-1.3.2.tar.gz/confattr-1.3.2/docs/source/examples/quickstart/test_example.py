#!../../../../venv/bin/pytest

import os
import sys
import shlex
import subprocess
import pathlib

import pytest

from utils import run_and_get_stdout, force_import_quickstart

APP_NAME = 'test-app'

# ------- utils -------

PATH = os.path.dirname(__file__)
def run_example_shell(monkeypatch: 'pytest.MonkeyPatch', fn: str) -> str:
	cmd = shlex.split(read_file(fn).strip())
	monkeypatch.setattr(sys, 'argv', cmd)
	return run_and_get_stdout('example.py', nextto=__file__, no_system_exit=True)

def read_file(fn: str) -> str:
	if not os.path.isabs(fn):
		fn = os.path.join(PATH, fn)
	with open(fn, 'rt') as f:
		return f.read()

# ------- tests -------

def test_without_args(monkeypatch: 'pytest.MonkeyPatch') -> None:
	force_import_quickstart()
	assert run_example_shell(monkeypatch, 'call_without_args.sh') == read_file('expected_without_args.txt')

def test_version(monkeypatch: 'pytest.MonkeyPatch') -> None:
	force_import_quickstart()
	assert run_example_shell(monkeypatch, 'call_version.sh') == read_file('expected_version.txt')

def test_help(monkeypatch: 'pytest.MonkeyPatch') -> None:
	force_import_quickstart()
	written_help = run_example_shell(monkeypatch, 'call_help.sh')
	expected_help = read_file('expected_help.txt')
	if sys.version_info < (3, 10):
		expected_help = expected_help.replace('options:', 'optional arguments:')
	assert written_help == expected_help

def test_help_config(monkeypatch: 'pytest.MonkeyPatch') -> None:
	monkeypatch.setenv('TEST_APP_CONFIG_DIRECTORY', '~/.config/test-app/')

	force_import_quickstart()
	written_help = run_example_shell(monkeypatch, 'call_help_config.sh')
	expected_help = read_file('expected_help_config.txt')
	if sys.version_info < (3, 10):
		expected_help = expected_help.replace('options:', 'optional arguments:')
	assert written_help == expected_help

def test_config(monkeypatch: 'pytest.MonkeyPatch', tmp_path: pathlib.Path) -> None:
	force_import_quickstart()
	monkeypatch.setenv('TEST_APP_CONFIG_DIRECTORY', str(tmp_path))
	monkeypatch.setenv('EDITOR', 'echo')
	run_example_shell(monkeypatch, 'call_edit.sh')

	written_config = read_file(str(tmp_path/'config'))
	expected_config = read_file('expected_config.txt')
	assert written_config == expected_config
