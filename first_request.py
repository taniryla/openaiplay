import openai

openai.Completion.create(
    model="text-davinci-003",
    prompt="The dog says "
)