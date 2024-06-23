# GenAISys

This is a meta project where we play with various prompts to llm and save their results with some tinking and document the evolution of llms to automate tasks that would take several hours otherwise.

### Development

    VSCode Settings :     "python.poetryPath": "/opt/homebrew/bin/poetry",
    

### Running Tests

    poetry install # this will install the package locally

    poetry run pytest # this will run all the tests

    Note: its seems its easier to run all tests in poetry quite easy, but bit difficult when
    running for a individual file

    pytest tests/systems # here we will run the systems tests only 

    pytest tests/systems --capture=no # in case you want to render the prints in tests

### Publishing

This is a poerty project and we are publishing the project to pypi.Make sure you have your pypi token or copy from your .pypirc file. Set the following before running poetry publish

    poetry config pypi-token.pypi <paste_pypi_token_here>

