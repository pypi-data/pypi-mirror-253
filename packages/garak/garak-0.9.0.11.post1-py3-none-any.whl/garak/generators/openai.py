#!/usr/bin/env python3
"""OpenAI API generator

Supports chat + chatcompletion models. Put your OpenAI API key in
an environment variable called OPENAI_API_KEY. Put the name of the
model you want in either the --model_name command line parameter, or
pass it as an argument to the OpenAIGenerator constructor.

sources:
* https://platform.openai.com/docs/models/model-endpoint-compatibility
* https://platform.openai.com/docs/model-index-for-researchers
"""

import os
import re
from typing import List

import openai
import backoff

from garak.generators.base import Generator

completion_models = (
    "gpt-3.5-turbo-instruct",
    "text-davinci-003",
    "text-davinci-002",
    "text-curie-001",
    "text-babbage-001",
    "text-ada-001",
    "code-davinci-002",
    "code-davinci-001",
    "davinci-instruct-beta",
    "davinci",
    "curie",
    "babbage",
    "ada",
)
chat_models = (
    "gpt-4",
    "gpt-4-32k",
    "gpt-3.5-turbo",
    "gpt-3.5-turbo-1106",
    "gpt-3.5-turbo-16k",
    "gpt-3.5-turbo-0613",
    "gpt-3.5-turbo-16k-0613",
    "gpt-3.5-turbo-0301",
)


class OpenAIGenerator(Generator):
    """Generator wrapper for OpenAI text2text models. Expects API key in the OPENAI_API_KEY environment variable"""

    supports_multiple_generations = True
    generator_family_name = "OpenAI"

    temperature = 0.7
    top_p = 1.0
    frequency_penalty = 0.0
    presence_penalty = 0.0
    stop = ["#", ";"]

    def __init__(self, name, generations=10):
        self.name = name
        self.fullname = f"OpenAI {self.name}"

        super().__init__(name, generations=generations)

        openai.api_key = os.getenv("OPENAI_API_KEY", default=None)
        if openai.api_key is None:
            raise ValueError(
                'Put the OpenAI API key in the OPENAI_API_KEY environment variable (this was empty)\n \
                e.g.: export OPENAI_API_KEY="sk-123XXXXXXXXXXXX"'
            )

        if self.name in completion_models:
            self.generator = openai.Completion
        elif self.name in chat_models:
            self.generator = openai.ChatCompletion
        elif "-".join(self.name.split("-")[:-1]) in chat_models and re.match(
            r"^.+-[01][0-9][0-3][0-9]$", self.name
        ):  # handle model names -MMDDish suffix
            self.generator = openai.ChatCompletion

        elif self.name == "":
            openai_model_list = sorted([m["id"] for m in openai.Model().list()["data"]])
            raise ValueError(
                "Model name is required for OpenAI, use --model_name\n"
                + "  API returns following available models: ▶️   "
                + "  ".join(openai_model_list)
                + "\n"
                + "  ⚠️  Not all these are text generation models"
            )
        else:
            raise ValueError(
                f"No OpenAI API defined for '{self.name}' in generators/openai.py - please add one!"
            )

    @backoff.on_exception(
        backoff.fibo,
        (
            openai.error.RateLimitError,
            openai.error.ServiceUnavailableError,
            openai.error.APIError,
            openai.error.Timeout,
            openai.error.APIConnectionError,
        ),
        max_value=70,
    )
    def _call_model(self, prompt: str) -> List[str]:
        if self.generator == openai.Completion:
            response = self.generator.create(
                model=self.name,
                prompt=prompt,
                temperature=self.temperature,
                max_tokens=self.max_tokens,
                n=self.generations,
                top_p=self.top_p,
                frequency_penalty=self.frequency_penalty,
                presence_penalty=self.presence_penalty,
                stop=self.stop,
            )
            return [c["text"] for c in response["choices"]]

        elif self.generator == openai.ChatCompletion:
            response = self.generator.create(
                model=self.name,
                messages=[{"role": "user", "content": prompt}],
                temperature=self.temperature,
                top_p=self.top_p,
                n=self.generations,
                stop=self.stop,
                max_tokens=self.max_tokens,
                presence_penalty=self.presence_penalty,
                frequency_penalty=self.frequency_penalty,
            )
            return [c["message"]["content"] for c in response["choices"]]

        else:
            raise ValueError(
                "Unsupported model at generation time in generators/openai.py - please add a clause!"
            )


default_class = "OpenAIGenerator"
