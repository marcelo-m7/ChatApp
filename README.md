# Chat em Tempo Real com Flet e OpenAI

## Sobre o Projeto
Este projeto é um chat em tempo real desenvolvido em Python utilizando a biblioteca [Flet](https://flet.dev/). Ele permite que os usuários:
- Criem salas de conversa
- Compartilhem arquivos
- Interajam com um assistente virtual da OpenAI na sala "Bate-papo com Assistente", mencionando `@programador` na mensagem

O projeto foi desenvolvido como parte da disciplina de **Computação Móvel**.

**Aluno:** [Marcelo Santos (a79433)](https://flet.dev/)

## Requisitos
Antes de executar o projeto, certifique-se de ter o Python instalado e instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Como Executar
### Iniciar o Chat
Para iniciar a interface do chat, execute o seguinte comando:
```bash
python src/main.py
```

### Iniciar o Servidor
O servidor precisa ser executado para gerenciar o compartilhamento de arquivos. Para isso, rode:
```bash
uvicorn server.main:app --reload
```

Isso disponibilizará os arquivos compartilhados no chat através de um endpoint de API feita com FastAPI.

## Funcionalidades Principais
- **Criação de Salas**: Os usuários podem criar salas personalizadas para conversas específicas.
- **Compartilhamento de Arquivos**: Suporte para o envio de imagens, documentos e outros formatos. Os ficheiro são salvos na pasta `src/uploads`
- **Assistente Virtual**: Na sala "Bate-papo com Assistente", qualquer mensagem que inclua `@programador` será processada por uma API da OpenAI e receberá uma resposta automática.
- **Persistência do histórico entre novas sessõe**: O projeto base foi rearquitetado de maneira que haja um objeto que persiste os dados do aplicativo em execução.

## Tecnologias Utilizadas
- **Python**: Linguagem principal do projeto
- **Flet**: Framework para construção da interface gráfica
- **Uvicorn**: Servidor ASGI para disponibilizar os arquivos compartilhados
- **OpenAI API**: Para responder mensagens com o assistente virtual
