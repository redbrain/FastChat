Adding new openai api compatible model:

1. Add model registry in `fastchat/model/model_registry.py`.

2. Add model adapter in `fastchat/model/model_adapter.py`.

3. Add model conv template in `fastchat/conversation.py`.

4. Add json file "openai_compatible_models.json" with the format as below:
```
{
    "vicuna-7b": {
        "model_name": "vicuna-7b-v1.5",
        "api_base": "http://8.8.8.55:5555/v1",
        "api_key": "password"
    },
}
```

5. Launch controller and then webserver with the option `register-openai-compatible-models`. Below is an example:
```
python3 -m fastchat.serve.gradio_web_server --share --register-openai-compatible-models openai_compatible_models.json
```
6. Test on your local server.
