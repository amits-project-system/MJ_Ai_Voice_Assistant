class assistent:
    def __init__(self):
        
        from openai import OpenAI

        self.client = OpenAI(
          api_key="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"
        )
    def work(self,commond):
        from openai import OpenAI

        client = OpenAI(
          api_key="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"
        )

        response = client.responses.create(
          model="gpt-5-nano",
          input=[
                {
                    "role": "system",
                    "content": "you are virtual assistant,like alexa or google assistant",
                },
                {
                    "role": "user",
                    "content": commond,
                },
            ],
          store=True,
        )

        return response.output_text


 