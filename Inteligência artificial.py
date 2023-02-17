# importar a biblioteca Openai
import openai

# Coloque a sua key da Openai
openai.api_key = "Entre com a sua key"

# isso faz um loop para que continuamos fazendo perguntas para o ChatGPT
while True:
    
    model_engine = "text-davinci-003"
    
    prompt = input('O que voce deseja saber: ')

    if 'exit' in prompt or 'quit' in prompt:
        break

    # Gerador de perguntas
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # extrai a resposta
    response = completion.choices[0].text
    
    # mostra a resposta na tela
    print(response)