import os
import json
import argparse
from console import Console
from .version import __version__


console = Console()

class CLI:
    def __init__(self) -> None:
        self.config = {}

        # Command Line Argument
        self.parser = argparse.ArgumentParser(description="Star - Command Line Tool")
        self.parser.add_argument("script", metavar="script", nargs="?", default=None, help="Name of the script to run")
        self.parser.add_argument("-v", "--version", action="store_true", help="Display the version of Star")
        self.parser.add_argument("-l", "--list", action="store_true", help="List all available scripts", default=False)

        self.args = self.parser.parse_args()
        self.read_config_file()

        # Check for version flag
        if self.args.version:
            self.display_version()
        elif self.args.list or self.args.script is None:
            self.display_script_list()
        else:
            self.run_script(self.args.script)


    def read_config_file(self) -> None:
        """Read the configuration file."""
        file_path = os.path.join(os.getcwd(), "star.json")
        with open(file_path, "r") as file:
            self.config = json.loads(file.read())


    def display_version(self) -> None:
        """Display the version of Star."""
        print(f"Star CLI - Version {__version__}")

    
    def display_script_list(self) -> None:
        """Display a list of all commands in the star.json file."""
        script_list = self.config.get("scripts", {}).keys()
        if script_list:
            console.secondary("Available scripts:")
            for script_name in script_list:
                print(f" - {script_name}")
        else:
            console.secondary("No scripts found in star.json")


    def run_script(self, script_name: str) -> None:
        """Run the specified script."""
        try:
            scripts = self.config["scripts"][script_name]

            if isinstance(scripts, str):
                # Display the command.
                console.secondary(f"$ {scripts}")

                # Run the single command in the terminal.
                os.system(scripts)
            elif isinstance(scripts, list):
                # Display the commands.
                console.secondary(f"$ {' && '.join(scripts)}")

                # Run the multiple commands in the terminal.
                for script in scripts:
                    os.system(script)
            else:
                console.error("error", end=" ")
                print("Cannot convert an unknown type to a primitive value")
        except KeyError:
            console.error("error", end=" ")
            print(f"Command \"{script_name}\" not found.")


    # For unwanted <star.cli.CLI object at ...> message
    def __str__(self) -> str:
        return ""
