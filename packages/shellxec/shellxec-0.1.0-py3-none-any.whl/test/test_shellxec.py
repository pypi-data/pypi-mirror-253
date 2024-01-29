import unittest
from unittest.mock import patch
from shellxec.core import ShellExec

class TestShellExec(unittest.TestCase):
    @patch('subprocess.run')
    def test_run_command(self, mock_run):
        shell_exec = ShellExec()
        command = "echo 'Hello, ShellExec!'"
        shell_exec.run_command(command)
        mock_run.assert_called_once_with(command, shell=True, check=True)

    @patch('subprocess.run')
    def test_run_command_with_output(self, mock_run):
        shell_exec = ShellExec()
        command = "echo 'Hello, ShellExec!'"
        shell_exec.run_command_with_output(command)
        mock_run.assert_called_once_with(command, shell=True, check=True, capture_output=True, text=True)

    @patch('subprocess.run')
    def test_run_command_in_directory(self, mock_run):
        shell_exec = ShellExec()
        command = "echo 'Hello, ShellExec!'"
        directory = '/path/to/directory'
        shell_exec.run_command_in_directory(command, directory)
        mock_run.assert_called_once_with(command, shell=True, check=True, cwd=directory)

    @patch('subprocess.run')
    def run_command_with_env_var(self, mock_run):
        shell_exec = ShellExec()
        command = "echo 'Hello, ShellExec!'"
        env_var = {'VAR': 'value'}
        shell_exec.run_command_with_env_var(command, env_var)
        mock_run.assert_called_once_with(command, shell=True, check=True, env_var=env_var)

    def test_run_commands_batch(self):
        # Mock subprocess.run since we're not interested in its actual execution in this test
        with patch('subprocess.run'):
            shell_exec = ShellExec()
            commands = ["echo 'Command 1'", "echo 'Command 2'", "echo 'Command 3'"]
            shell_exec.run_commands_batch(commands)

    # Add tests for the shorthand functions if you included them in the core.py

if __name__ == "__main__":
    unittest.main()