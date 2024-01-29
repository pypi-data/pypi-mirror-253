import subprocess
import platform

class ShellExec:
    def __init__(self):
        self.platform = platform.system()

    def run_command(self, command):
        try:
            if self.platform == "Windows":
                subprocess.run(command, shell=True, check=True)
            else:
                subprocess.run(command, shell=True, check=True, executable="/bin/bash")
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    def run_command_with_output(self, command):
        try:
            if self.platform == "Windows":
                result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
            else:
                result = subprocess.run(command, shell=True, check=True, executable="/bin/bash", capture_output=True, text=True)
            
            return result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")
            return None

    def run_command_in_directory(self, command, directory):
        try:
            if self.platform == "Windows":
                subprocess.run(command, shell=True, check=True, cwd=directory)
            else:
                subprocess.run(command, shell=True, check=True, executable="/bin/bash", cwd=directory)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    def run_command_with_env_var(self, command, env_var=None):
        try:
            if self.platform == "Windows":
                subprocess.run(command, shell=True, check=True, env_var=env_var)
            else:
                subprocess.run(command, shell=True, check=True, executable="/bin/bash", env_var=env_var)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

    def run_commands_batch(self, commands):
        for command in commands:
            self.run_command(command)


# Create an instance of ShellExec for easy access
shellexec = ShellExec()


