{
  "is_source_file": true,
  "format": "Python",
  "description": "This file defines the HTTPErrorMessageSink class, which handles error messages by sending them to a specified server endpoint. It includes methods for testing the connection to the server and sending error messages in a structured format.",
  "external_files": [
    "base_error_messag_sink"
  ],
  "external_methods": [
    "requests.get",
    "requests.post"
  ],
  "published": [
    "HTTPErrorMessageSink"
  ],
  "classes": [
    {
      "name": "HTTPErrorMessageSink",
      "description": "A class for sending error messages to a server, extending the functionality of BaseErrorMessageSink."
    }
  ],
  "methods": [
    {
      "name": "__init__",
      "description": "Initializes the HTTPErrorMessageSink, sets the server URL based on the environment, and tests the connection."
    },
    {
      "name": "_test_connection",
      "description": "Tests the connection to the server with a simple GET request to ensure the server is reachable."
    },
    {
      "name": "send_error_message",
      "description": "Sends an error message to the configured server endpoint, stores it locally, and handles any exceptions."
    },
    {
      "name": "__del__",
      "description": "Destructor for the HTTPErrorMessageSink, performing no specific clean-up actions."
    }
  ],
  "calls": [
    "os.path.exists",
    "uuid.uuid4",
    "datetime.utcnow",
    "requests.get",
    "requests.post"
  ],
  "search-terms": [
    "HTTPErrorMessageSink",
    "error message",
    "server connection",
    "send_message API"
  ],
  "state": 2,
  "ctags": [],
  "filename": "/tmp/kavia/workspace/shelly-ai/web_socket_error_message_sink.py",
  "hash": "aab639cd1c95b4c7af26ed503e422b83",
  "format-version": 3,
  "code-base-name": "b07296v"
}