# XPrompt client

client for XPrompt


## Example
```
import xprmopt
api_key_response = xprompt.login(user_email='..', password='..')

xprompt.api_key = api_key_response['access_token']
xprompt.openai_api_key = ""


prompt = """tell me a joke"""

r = xprompt.OpenAIChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt}], temperature=0)
print(r)
```

## Publish client
1. update the xprompt-common version in `pyproject.toml`
2. bump version in `pyproject.toml`
3. `poetry build`
4. `poetry publish`
5. `git tag -a v0.1.0 -m "version 0.1.0"`

Test out the client published
1. create a new venv
2. install the client `pip install xprompt`
3. run the example above
