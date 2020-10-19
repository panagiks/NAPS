#!/usr/bin/env python

"""Tests for `naps` package."""

from click.testing import CliRunner

from naps import naps
from naps import cli


def test_command_line_interface_help():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
