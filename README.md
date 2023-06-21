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

2. **Criar Leilão** - aos usuários deve ser possível visitar uma página para a criação de um novo leilão. Na criação deve especificar obrigatoriamente:
    * Título;
    * Descrição;
    * Lance inicial.
    Deve ser opcional ao usuário fornecer:
    * Url para a imagem do leilão;
    * Categoria (ex. Moda, Brinquedo, Eletrônico, Casa, etc.).
    
3. **Página dos Leilões Ativos** - a rota padrão da sua aplicação deve exibir ao usuário uma lista de todos os leilões correntemente ativos. Para cada leilão ativo, a página deve exibir (no mínimo): 
    * Título;
    * Descrição;
    * Lance corrent;
    * Foto (se existir alguma).

4. **Página do Leilão** - clicando em um leilão o usuário deve ser redirecionado para a página específica daquele anúncio. Nessa página, o usuário deve ver todo o detalhe sobre o leilão.
    * Se o usuário estiver logado, deve ser habilitado a ele adicionar o item em sua *Lista de Desejos*. Se o item já estiver na sua lista, deve ser possível remover dela;
    * Se o usuário estiver logado, deve ser habilitado a ele dar um lance no item. O lance deve ser pelo menos maior do que o lance inicial e maior do que qualquer outro lance que foi dado (se tiver algum). Se nenhuma dessas condições forem satisfeitas, ao usuário deve ser apresentada uma mensagem de erro;
    * Se o usuário estiver logado e for quem criou o leilão, deve ser possível fechar o leilão a partir dessa página, o que torna o usuário do lance mais alto o vencedor do leilão e torna o leilão inativo;
    * Se o usuário estiver logado e na página de um leilão fechado e for ele o ganhador do leilão, a página deve informar isso para ele;
    * Usuários que estiverem logado devem ser habilitados para adicionar comentários à página do leilão. A página do leilão deve exibir todos os comentários feitos nele.

5. **Lista de Desejos** - usuários logados devem ser habilitados a visitar uma página de *Desejos*, o que deve exibir ao usuário todos os leilões que o usuário adicionou em seus *Lista de Desejos*.

6. **Categorias** - aos visitantes (logados ou não) deve ser possível visitar uma página que exibe todas as categorias dos leilões. Clicando em qualquer categoria, o usuário deve ser levado para uma página que exibe todos os leilões ativos naquela categoria específica.

7. **Django Admin Interface** - através do Django Admin Interface, ao administrador do site deve ser habilitado ver, adicionar, editar e deletar qualquer leilão, comentário e lance feito no site.