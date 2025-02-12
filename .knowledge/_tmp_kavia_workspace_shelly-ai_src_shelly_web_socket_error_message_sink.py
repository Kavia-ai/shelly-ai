{
  "is_source_file": true,
  "format": "Python",
  "description": "This file defines the HTTPErrorMessageSink class that handles sending error messages over HTTP to a server. It inherits from BaseErrorMessageSink and includes methods for testing server connectivity and sending error messages.",
  "external_files": [
    "base_error_messag_sink"
  ],
  "external_methods": [
    "BaseErrorMessageSink.__init__",
    "requests.get",
    "requests.post"
  ],
  "published": [
    "HTTPErrorMessageSink"
  ],
  "classes": [
    {
      "name": "HTTPErrorMessageSink",
      "description": "Handles sending error messages to an HTTP server."
    }
  ],
  "methods": [
    {
      "name": "__init__",
      "description": "Initializes the HTTPErrorMessageSink, determines the server URL based on the environment, and tests the connection."
    },
    {
      "name": "_test_connection",
      "description": "Tests the connection to the server with a simple GET request."
    },
    {
      "name": "send_error_message",
      "description": "Formats and sends an error message to the configured API endpoint."
    },
    {
      "name": "__del__",
      "description": "Destructor for the HTTPErrorMessageSink, no cleanup required."
    }
  ],
  "calls": [
    "os.path.exists",
    "requests.get",
    "requests.post",
    "print"
  ],
  "search-terms": [
    "HTTPErrorMessageSink",
    "send_error_message",
    "test_connection"
  ],
  "state": 2,
  "ctags": [],
  "filename": "/tmp/kavia/workspace/shelly-ai/src/shelly/web_socket_error_message_sink.py",
  "hash": "1f73027167e74792dd18a387b2ce0207",
  "format-version": 3,
  "code-base-name": "b07296v"
}