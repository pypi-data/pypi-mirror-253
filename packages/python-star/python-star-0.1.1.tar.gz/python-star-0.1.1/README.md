# Star - Command Line Tool

Star is a command-line tool designed to simplify project setup, testing, and development tasks by providing a unified interface for running scripts and commands. It allows you to define and manage scripts in a configuration file, making it easy to execute complex workflows with a single command.

## Features

-   **Script Configuration**: Define scripts in a configuration file (`star.json`) to specify tasks for setup, testing, or development.

-   **Unified Interface**: Run scripts using a single command, reducing the need to remember complex command sequences.

-   **Flexibility**: Execute both single commands and sequences of commands defined in the configuration file.

-   **Easy to Use**: Simplify your workflow by streamlining common tasks with predefined scripts.

## Installation

Star can be installed using `pip`. Open a terminal and run:

```bash
pip install python-star
```

## Documentation (Usage)

#### Adding Commands

Define your custom scripts in the star.json file located in the root directory of your project. Example:

```json
{
	"scripts": {
		"custom_script": "echo 'Running custom script'",
		"test": ["echo 'Test 1 Pass'", "echo 'Test 1 Pass'"]
	}
}
```

### Running Commands

To run a script, use the following command:

```bash
star <script-name>
```

Replace `<script-name>` with the name of the script defined in your star.json file.

### Example

Assuming you have a star.json file with the following content:

```json
{
	"scripts": {
		"setup": "python setup.py",
		"test": ["pytest", "flake8"]
	}
}
```

You can run the "setup" script using

```bash
star setup
```

Or run the "test" script sequence using:

```bash
star test
```

### Other Command

| Short Form | Long Form | Description                     |
| ---------- | --------- | ------------------------------- |
| -h         | --help    | Show this help message and exit |
| -v         | --version | Display the version of Star     |
| -l         | --list    | List all available scripts      |

## Contributing

For guidance on setting up a development environment and how to make a contribution to Star, see the
