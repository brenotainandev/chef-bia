
# Assistente de Culinária - Bia

Este projeto é um assistente de culinária que permite aos usuários buscar receitas, obter instruções de preparo, listar ingredientes e gerar receitas aleatórias por comando de voz.

## Funcionalidades

- **Pesquisar Receitas por Comando de Voz**: Você pode pedir ao assistente para encontrar receitas com base em suas preferências.

- **Obter Instruções de Preparo por Comando de Voz**: Pergunte ao assistente como preparar uma receita específica.

- **Listar Ingredientes por Comando de Voz**: Obtenha uma lista de ingredientes para uma receita.

- **Gerar Receitas Aleatórias por Comando de Voz**: Se você está indeciso, o assistente pode sugerir uma receita aleatória para você experimentar.

- **Finalizar aplicação por comando de Voz**: Encerre a aplicação com facilidade quando você terminar de usar.

## Como Usar

1. **Instale as Dependências**: Certifique-se de que as dependências necessárias estejam instaladas. Você pode usar o seguinte comando para instalar as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. **Execute o Arquivo `main.py`**: Inicie o assistente executando o arquivo `main.py` em seu terminal.

3. **Comandos de Voz**: Siga as instruções fornecidas pelo assistente e dê comandos por voz para usar as funcionalidades disponíveis.


## Dependências

O projeto depende das seguintes bibliotecas:

- **SpeechRecognition**: Esta biblioteca é essencial para reconhecer comandos de voz do usuário. Para instalá-la, utilize o seguinte comando:

   ```
   pip install SpeechRecognition
   ```

- **Pyaudio**: O Pyaudio é uma biblioteca para lidar com a entrada e saída de áudio, fundamental para a captura de comandos de voz. Instale-o com o comando:

   ```
   pip install pyaudio
   ```

- **NLTK (Natural Language Toolkit)**: Embora não esteja listado nas dependências mencionadas, o projeto faz uso da biblioteca NLTK para processamento de linguagem natural. Você pode instalar o NLTK com o comando:

   ```
   pip install nltk
   ```

Certifique-se de instalar todas essas dependências para garantir que o projeto funcione corretamente. Você também pode adicionar outras bibliotecas necessárias à lista acima, se for o caso.

## Configuração jsom

Para configurar a assistente de culinária Bia de acordo com suas preferências, você pode modificar o arquivo `config.json`. Neste arquivo, você pode definir o nome da assistente (por padrão, "Bia") e os comandos de voz associados a cada funcionalidade. Isso permite que o assistente compreenda várias maneiras de expressar os mesmos comandos, tornando-o mais flexível.

```json
{
  "nome": "Bia",
  "acoes": {
    "pesquisar receitas": ["pesquisar receitas", "encontrar receitas", "mostrar receitas"],
    "obter instruções de preparo": ["instruções de preparo", "como preparar"],
    "listar ingredientes": ["listar ingredientes", "ingredientes"],
    "gerar receitas aleatórias": ["receitas aleatórias", "uma receita"],
    "encerrar": ["encerrar", "finalizar", "fechar"]
  }
}
```

Aqui, você pode personalizar os comandos de voz para cada funcionalidade de acordo com suas preferências.


## Exemplos de Comandos por Voz

- **Pesquisar Receitas**:
  - "Bia, pesquisar receitas de macarrão."
  - "Bia, mostrar receitas de pratos vegetarianos."
  
- **Obter Instruções de Preparo**:
  - "Bia, como preparar uma deliciosa lasanha?"
  - "Bia, instruções de preparo para fazer um bolo de chocolate?"

- **Listar Ingredientes**:
  - "Bia, listar ingredientes para um purê de batata."
  - "Bia, diga-me os ingredientes de um risoto de cogumelos."

- **Gerar Receitas Aleatórias**:
  - "Bia, sugira uma receita para o jantar."
  - "Bia, me dê uma ideia de receitas aleatórias."

- **Finalizar a Aplicação**:
  - "Bia, finalizar o assistente."
  - "Bia, fechar a aplicação."


## Autor

- **Breno Tainan Aguiar** - [Perfil no GitHub](https://github.com/breno-tainan-dev)
