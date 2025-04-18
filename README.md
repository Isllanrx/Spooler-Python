# Gerenciador de Serviço de Impressão 

Com finalidade de resolver problemas relacionado a fila de impressão no windows, desenvolvi essa aplicação em python e converti para .EXE.
Este é um simples aplicativo em Python com uma interface gráfica que permite reiniciar o serviço de impressão no sistema operacional Windows. O projeto utiliza a biblioteca `customtkinter` para criar a interface gráfica.

## Funcionalidades

- Reiniciar o serviço de impressão no Windows.
- Excluir arquivos de spool temporários.
- Interface gráfica simples e fácil de usar.

## Pré-requisitos

- Python 3.x instalado no sistema.
- Pacote `customtkinter` instalado. Você pode instalar o pacote via pip com o seguinte comando:
  ```
  pip install customtkinter
  ```

## Como usar para testes

1. Clone o repositório para o seu sistema local.
2. Navegue até o diretório onde o repositório foi clonado.
3. Execute o script Python `spooler1.py` com o seguinte comando:
   ```
   python spooler1.py
   ```
4. A interface gráfica será aberta. Clique no botão "Reiniciar Serviço de Impressão" para reiniciar o serviço de impressão.

## Como usar o executável

1. Abra o aplicativo como Administrador
2. Selecione o botão de "Reiniciar" e logo em seguida mostrará os avisos de cada processo
3. Aperte 'OK' em todos os avisos para validar.

## Final

1. Este projeto foi desenvolvido por [Isllan Toso] como parte do projeto [Spooler de Impressão] da [Podium TI].
