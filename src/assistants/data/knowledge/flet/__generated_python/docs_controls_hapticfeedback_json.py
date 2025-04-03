import flet as ft

def main(page: ft.Page):
    hf = ft.HapticFeedback()
    page.overlay.append(hf)
    
    def custom_vibration(e):
        hf.vibrate(duration=500)  # Vibra por 500 milissegundos
        print("Vibração customizada ativada!")
    
    page.add(
        ft.ElevatedButton("Vibração Customizada", on_click=custom_vibration),
    )

ft.app(main)

import flet as ft
   ```
   Esta linha importa a biblioteca Flet, que é usada para construir a interface do usuário.

2. **Definição da Função Principal**:
   ```python
   def main(page: ft.Page):
   ```
   A função `main` é definida com um parâmetro `page`, que é um objeto do tipo `ft.Page` fornecido pela biblioteca Flet. Este objeto representa a página ou tela principal onde os elementos da interface são adicionados.

3. **Criação de um Objeto HapticFeedback**:
   ```python
   hf = ft.HapticFeedback()
   ```
   Aqui, um objeto `HapticFeedback` é criado e armazenado na variável `hf`. Este objeto é usado para controlar o feedback háptico (vibrações) do dispositivo.

4. **Adicionando o HapticFeedback ao Overlay da Página**:
   ```python
   page.overlay.append(hf)
   ```
   O objeto `hf` é adicionado ao overlay da página. Em interfaces de usuário, um overlay pode ser usado para colocar elementos que devem aparecer sobre outros conteúdos, mas neste contexto específico, serve para garantir que o componente de haptic feedback esteja disponível e possa ser acionado.

5. **Adicionando Botões à Página**:
   ```python
   page.add(
       ft.ElevatedButton("Heavy impact", on_click=lambda _: hf.heavy_impact()),
       ft.ElevatedButton("Medium impact", on_click=lambda _: hf.medium_impact()),
       ft.ElevatedButton("Light impact", on_click=lambda _: hf.light_impact()),
       ft.ElevatedButton("Vibrate", on_click=lambda _: hf.vibrate()),
   )
   ```
   Nesta seção, diferentes botões são adicionados à página. Cada botão é uma instância de `ft.ElevatedButton`, que cria um botão com um efeito visual de elevação (sombra), dando uma sensação de profundidade. Cada botão é configurado com um rótulo e uma ação que é definida usando uma função lambda que é acionada quando o botão é clicado. As funções associadas a cada botão (`heavy_impact`, `medium_impact`, `light_impact`, e `vibrate`) são métodos do objeto `hf` que acionam diferentes níveis de feedback háptico.

6. **Inicialização do Aplicativo**:
   ```python
   ft.app(main)
   ```
   Esta linha inicia o aplicativo, passando a função `main` como o ponto de entrada do aplicativo. A função `main` é chamada quando o aplicativo é carregado, e ela configura a interface do usuário.

### Resumo
O código cria uma interface de usuário com quatro botões que permitem ao usuário experimentar diferentes tipos de feedback háptico (vibração) em um dispositivo compatível. Cada botão é configurado para produzir um tipo específico de vibração, variando de leve a pesado. Este exemplo é útil para entender como interagir com hardware do dispositivo usando Python e a biblioteca Flet.
Claro! Vamos criar exemplos adicionais que demonstram diferentes formas de uso do `HapticFeedback` no contexto de uma aplicação Flet. Esses exemplos ajudarão a explorar diferentes cenários onde os feedbacks táteis podem ser úteis.

### Exemplo 1: Usando Haptic Feedback com Botões de Ações Diferentes

Neste exemplo, vamos adicionar botões que representam diferentes ações em um aplicativo, como "Salvar", "Excluir" e "Cancelar", cada um com um tipo de feedback tátil diferente.

import flet as ft
import random

def main(page: ft.Page):
    hf = ft.HapticFeedback()
    page.overlay.append(hf)
    
    def play_game(e):
        if random.choice([True, False]):
            hf.heavy_impact()
            print("Você ganhou pontos!")
        else:
            hf.medium_impact()
            print("Você perdeu pontos!")
    
    page.add(
        ft.ElevatedButton("Jogar", on_click=play_game),
    )

ft.app(main)
