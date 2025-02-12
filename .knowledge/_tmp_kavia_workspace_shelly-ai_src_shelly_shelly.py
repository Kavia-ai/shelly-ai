{
  "is_source_file": true,
  "format": "Python",
  "description": "This file implements a command-line tool that interacts with a pseudo-terminal (PTY), captures and logs command outputs and errors, and analyzes errors using an LLM parser.",
  "external_files": [
    ".llm_parser",
    ".web_socket_error_message_sink"
  ],
  "external_methods": [
    "LLMParser.analyze_error",
    "HTTPErrorMessageSink.send_error_message",
    "LLMParser.save_analysis"
  ],
  "published": [
    "main",
    "debug_log",
    "write_to_file",
    "analyze_error"
  ],
  "classes": [
    {
      "name": "CircularBuffer",
      "description": "A class to manage a circular buffer for storing a limited number of strings."
    },
    {
      "name": "CommandLogger",
      "description": "A class to log the commands executed and their outputs, allowing access to command history and saving results."
    }
  ],
  "methods": [
    {
      "name": "debug_log",
      "description": "Logs debug messages to a specified log file."
    },
    {
      "name": "write_to_file",
      "description": "Writes binary data to a specified file."
    },
    {
      "name": "analyze_error",
      "description": "Analyzes errors in command execution, gathering details from command history and sending structured error information."
    },
    {
      "name": "main",
      "description": "The main entry point of the program that sets up the environment and runs the command logging process."
    }
  ],
  "calls": [
    "os.isatty",
    "pty.openpty",
    "os.fork",
    "os.execvp",
    "os.read",
    "os.write",
    "nest_asyncio.run"
  ],
  "search-terms": [
    "command logger",
    "error analysis",
    "circular buffer"
  ],
  "state": 2,
  "ctags": [],
  "filename": "/tmp/kavia/workspace/shelly-ai/src/shelly/shelly.py",
  "hash": "b98f601453a717579f7e1614dae2d98d",
  "format-version": 3,
  "code-base-name": "b07296v"
}