# WebUI-LLM
This is a simple web user interface that allows you to enter text input and format the output using the LLM (Language Model) API.

## Prerequisites
To run this project, you will need to have the following installed:

- Python 3.8 or later
- Flask
- Requests

## Getting Started
To get started with this project, follow these steps:

1. Clone the repository:
```git clone https://github.com/k-farruh/webui-llm.git```
2. Install the dependencies:
```pip install -r requirements.txt```
3. Set the following environment variables:
```
export LLM_API_URL=<URL of the LLM API>
export LLM_API_KEY=<API key for the LLM API>
```
4. Run the Flask application:
```python app.py```
5. Open a web browser and go to http://localhost:5000/.

## Usage
To use the web interface, follow these steps:

1. Enter text in the input field.
1. Select the LLM model and output format.
1. Click the "Answer" button.
1. The answer from LLM output will be displayed below the input field.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request.

Before submitting a pull request, make sure to run pytest to ensure that all tests pass.

## Acknowledgments
This project uses the LLM environment provided by [Alibaba Cloud](https://www.alibabacloud.com/). Special thanks to the team at Alibaba Cloud for providing such a powerful and accessible environment.

