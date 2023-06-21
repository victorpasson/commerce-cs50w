# CS50W - Project 2 - Commerce

Repositório que contém o código para a solução do terceiro projeto do curso CS50W - Web Programming. O objetivo principal é permitir que os usuários se registrem, façam login, criem anúncios, fechem anúncios, favoritem os anúncios e façam comentários. A aplicação foi construída com o Django framework.

[![Page Wiki Project](https://i.ibb.co/CVnmvBX/Opera-Instant-neo-2023-05-25-214413-wiki-cs50w-vercel-app.png)](www.youtube.com/watch?v=u0peDMCmqAE&t)

## Página do Projeto

O projeto foi disponibilizado para interação por meio do [Python Any Where](https://wiki-cs50w.vercel.app).

## Youtube Vídeo

Um breve vídeo de demonstração do resultado do projeto foi feito e hospedado no [YouTube](https://www.youtube.com/watch?v=u0peDMCmqAE&t).

## Especificações do projeto

1. **Models** - sua aplicação deve conter no mínimo três modelos além do já existente *User*.
    * Um para a lista de leilões;
    * Um para os lances;
    * Um para os comentários feitos nos leilões.
    Você é livre para escolher quais campora cada modelo deve ter e os tipos desses campos. Para você é habilitado criar quaisquer modelos adicionais que desejar.

2. **Criar Leilão** - aos usuários deve ser possível visitar uma página para a criação de um novo leilão. Eles devem especificar 
    
3. **Pesquisa** - permita que o usuário escreva uma entrada de pesquisa para as páginas da enciclopédia.
    * Se a entrada corresponder ao nome de uma entrada da enciclopédia, o usuário deve ser redirecionado para aquela página; 
    * Se não corresponder ao nome de nenhuma entrada, o usuário deve ser redirecionado para uma página que exibe uma lista de todas páginas que possuem aquela palavra como substring. Por exemplo, se a pesquisa do usuário for *ython*, então *Python* deve aparecer no resultado da pesquisa;
    * Clicando no nome de qualquer um desses resultados de pesquisa, o usuário deve ser redirecionado para a página da enciclopédia daquele resultado.

4. **Nova Página** - clicando em "*Create New Page*” o usuário deve ser redirecionado para uma página onde pode criar uma nova página da enciclopédia.
    * Deve ser habilitado ao usuário: a) inserir um título para a página; b) inserir textos em Markdown, em uma *textarea*,  para o conteúdo da página;
    * Deve haver um botão para salvar as informações;
    * Quando a página é salva, se a entrada da enciclopédia já existir para aquele título, deve ser apresentado uma mensagem de erro ao usuário;
    * Caso contrário, a nova página será salva no diretório e o usuário será redirecionado a página criada.

5. **Editar Página** - Em cada página de resultado deve ser habilitado ao usuário clicar em um link que o leva para uma página onde pode editar o conteúdo Markdown daquela página em específico. Essa edição deve ser feita em uma *textarea*.
    * A *textarea* deve ser pré-preenchida com o conteúdo já existente para aquela página (isto é, o valor inicial de value já deve conter o conteúdo daquela página na *textarea*);
    * Ao usuário deve ser disponibilizado um botão para salvar as mudanças feitas;
    * Assim que salvar, o usuário deve ser redirecionado para a página modificada.

6. **Página Aleatória** - clicando em “*Random Page*” o usuário deve ser levado para uma entrada aleatória da enciclopédia.