# Democratizador de Notícias

<br>

Projeto voltado para pessoas que não tem conhecimento de html e css e quer ler notícias em sites que bloqueiam o acesso. Porém, a informação já está do lado do cliente e a alteração pode ser feita para exibi-la. O que de certa forma é uma vulnerabilidade do modo de programar os sites, visto que o Estadão envia 5 linhas iniciais e o restante dos dados vão para o cliente quando ele tem a conta com assinatura.

E incluo que faço uso, pois diminui muito o tempo necessário desbloquando o site, investigando para derrubar o paywall.

<br>

Funciona nos sites: Uol, O Globo, Super Interessante, e outros.

<br>

Pelo peso do código por conta das bibliotecas do python, o git não conseguiu subir o arquivo zip com o executavel pronto para uso no git hub.

<br>

A curiosidade é que este código foi totalmente feito pelo chat GPT, porém foi necessário conhecimento básico de html e css para montar um texto, pseudocódigo, detalhando o que o chat GPT iria programar. O que eu calculo que levaria umas 3 semanas de trabalho para programar esse código do zero, buscando informações, tirando duvidas, vendo algumas aulas, consultando as documentações, e etc, levou apenas 3 horas para verificar o funcionamento do site que queremos alterar, montar o pseudocódigo, esperar o chatgpt gerar, e testá-lo.

"*Faça um código que crie um uma interface quadrada usando a biblioteca tkinter, onde nesta interface terá um local para receber um link de um site, esse link será verificado usando regex, e sendo verdadeiramente o link de algum site então o código vai abrir este link em um webdiver.Firefox(), esperar 4 segundos, depois o código vai buscar a class da primeira tag body do html para altera-la para vazio e tambem modificar seu overflow de hidden para auto, incluindo a modificação do overflow da tag html de hidden para auto, e todas as outras tags do css com overflow == hidden precisam ser trocados por auto, e em todas as tags div do nó raiz dentro da tag html precisam ter o valor do display dentro do style alterado para none, para que todo o conteúdo do site seja visto pelo usário sem os bloqueios anteriores*"
