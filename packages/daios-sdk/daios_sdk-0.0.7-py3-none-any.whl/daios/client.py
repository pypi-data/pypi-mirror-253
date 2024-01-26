import requests
import os


class Daios:
    _base_url = "https://daiostech--model-directory-models.modal.run"
    _default_model_id = "courage"

    def __init__(self, model_id=None, token=None):
        self.token = token
        if self.token is None:
            if "daios_token" in os.environ:
                self.token = os.environ["daios_token"]

        self.model_id = model_id
        if self.model_id is None:
            self.model_id = self._default_model_id

        headers = {
            "x-api-key": self.token
        }

        response = requests.get(self._base_url, headers=headers)
        if response.status_code != 200:
            raise Exception("Failed to get available models")
        
        available_models = [model for model in response.json().keys() if response.json()[model]["available"]]
        print("Available models:", available_models)
        available_models_str = "\n".join(available_models)

        if self.model_id not in response.json().keys() and self.model_id not in available_models:
            raise Exception("Model not found, available models: \n" + available_models_str)
        self.model_url = response.json()[self.model_id]["base_url"]

        # try:
        #     self.model_url = response.json()[self.model_id]["base_url"]
        # except KeyError:
        #     s = "\n".join(response.json().keys())
        #     raise Exception("Model not found, available models: \n" + s)

    def completion(self, question, stream=True):
        headers = {
            "x-api-key": self.token
        }
        params = {
            "question": question
        }

        response = requests.get(self.model_url, headers=headers, params=params, stream=stream)

        return response


def main():
    token = ""
    daios = Daios(token=token)
    query = "Write a brief slack message to my boss telling him that my coworker was unnecessarily chastised"
    response = daios.completion(query, stream=True)
    for chunk in response:
        print(chunk.decode(), end="")


if __name__ == '__main__':
    main()
