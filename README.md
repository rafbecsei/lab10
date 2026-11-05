# Laboratório 10 — Test-Driven Development (TDD)

## Exercício 1 — Contador de Palavras

### a) Ordem dos testes e justificativa

A ordem utilizada foi:

1. Texto vazio retorna um dicionário vazio.
2. Uma palavra simples retorna uma ocorrência.
3. Duas palavras diferentes são contadas separadamente.
4. Palavras repetidas têm suas ocorrências somadas.
5. Palavras maiúsculas e minúsculas são consideradas iguais.
6. Pontuação nas bordas das palavras é ignorada.
7. Espaços múltiplos separam palavras.
8. Quebras de linha separam palavras.
9. Hífen interno é preservado.
10. Texto contendo apenas pontuação retorna um dicionário vazio.
11. Pontuação no início e no fim das palavras é removida.
12. Outros sinais de pontuação são tratados corretamente.

O primeiro teste foi escolhido por ser o caso mais simples, permitindo começar com um retorno vazio. O segundo exigiu implementar a contagem de uma palavra, fazendo o código evoluir gradualmente.

### b) Desenvolvimento com TDD

A função `contar_palavras` foi desenvolvida utilizando o ciclo Red, Green e Refactor. Primeiro foi escrito um teste para o comportamento desejado, depois o código mínimo para fazê-lo passar. Os testes seguintes exigiram implementar a separação de palavras, contagem de ocorrências, conversão para minúsculas e remoção de pontuação.

### c) Histórico do Git

O histórico foi registrado com commits identificados por RED, GREEN, REFACTOR e TEST. Os commits RED e GREEN mostram a evolução da implementação. Não houve implementação de novos comportamentos sem testes anteriores. Os commits TEST representam verificações adicionais que já passavam.

O histórico completo pode ser consultado com:

`git log --oneline`

### d) Testes que passaram na primeira execução

Alguns testes adicionais passaram imediatamente, como os casos de espaços múltiplos, quebras de linha e preservação do hífen interno. Isso aconteceu porque a implementação existente já atendia a esses comportamentos.

Esses testes foram mantidos porque documentam os requisitos e ajudam a evitar regressões, mesmo não tendo exigido mudanças no código.

### e) Cobertura e mutação

- Testes aprovados: 13.
- Cobertura de ramos: 100%.
- Mutantes gerados: 15.
- Mutantes mortos: 14.
- Mutantes sobreviventes: 1.
- Escore de mutação: 93,33%.

O mutante sobrevivente alterava os caracteres removidos pelo método `strip`, incluindo a letra `X`. Como o texto já era convertido para minúsculas antes dessa operação, a alteração não produzia diferença observável nos casos testados.

## Exercício 2 — Fila de Atendimento

### a) Lista de testes

1. A fila inicia sem pessoas aguardando.
2. A primeira senha normal é N1.
3. As senhas normais seguem a sequência N1, N2.
4. A primeira senha prioritária é P1.
5. As numerações normal e prioritária são independentes.
6. Uma senha normal pode ser chamada.
7. Uma senha prioritária é chamada antes de uma normal.
8. Após duas prioritárias consecutivas, uma normal aguardando é atendida.
9. Chamar uma fila vazia lança `IndexError`.
10. Emitir uma senha com tipo inválido lança `ValueError`.

### b) Desenvolvimento com TDD

A classe `Fila` foi construída gradualmente com testes antes das implementações. Inicialmente foram desenvolvidas a emissão e a numeração das senhas. Depois foram implementadas as regras de atendimento, prioridade e controle de chamadas consecutivas.

Os ciclos foram registrados no Git, com commits RED e GREEN.

### c) Contagem das prioritárias e reinicialização

O teste que exigiu contar as prioritárias consecutivas foi aquele em que duas senhas prioritárias são atendidas e, em seguida, uma senha normal deve ser chamada.

A contagem precisa ser zerada após o atendimento de uma senha normal, para permitir que um novo ciclo de até duas prioritárias aconteça.

### d) Limite de duas prioritárias sem normal aguardando

O comportamento esperado é que, quando não existe nenhuma senha normal aguardando, as senhas prioritárias continuem sendo atendidas, mesmo após duas chamadas consecutivas.

Esse cenário não foi registrado como um teste específico na suíte final. Seria importante acrescentá-lo para verificar diretamente essa exceção à regra de prioridade.

### e) Testes de mutação

- Testes aprovados: 10.
- Cobertura de ramos: 100%.
- Mutantes gerados: 57.
- Mutantes mortos: 50.
- Mutantes sobreviventes: 7.
- Escore de mutação: 87,72%.

Os mutantes sobreviventes indicam que ainda existem comportamentos que poderiam ser verificados com testes mais específicos. Um exemplo é a continuidade do atendimento prioritário quando não há senhas normais aguardando.

Isso mostra que uma cobertura de 100% dos ramos não significa necessariamente que todos os comportamentos foram completamente testados.

## Exercício 3 — Carrinho de Compras

### a) Testes que contradiziam as novas regras

Os testes antigos que esperavam desconto de 10% para o cupom DEZ em subtotais de 5000 e 1000 centavos contradiziam a nova regra, pois agora o desconto só é aplicado a partir de 10000 centavos.

Antes de modificar o código, foi necessário atualizar esses testes para refletirem os novos requisitos. Dessa forma, os testes passaram a representar o comportamento correto esperado.

### b) Implementação das regras com TDD

As novas regras foram implementadas gradualmente, utilizando o ciclo Red, Green e Refactor.

Foram adicionados testes para:

- Cupom DEZ com desconto de 10% a partir de 10000 centavos.
- Cupom DEZ sem desconto abaixo do mínimo.
- Cupom VINTE com desconto de 20% a partir de 30000 centavos.
- Cupom VINTE sem desconto abaixo do mínimo.
- Aplicação do desconto ao atingir exatamente o subtotal mínimo.
- Substituição do primeiro cupom por um segundo.
- Rejeição de quantidade zero, negativa ou decimal.
- Verificação de mensagens de erro.

### c) Refatoração dos cupons

Na refatoração, a porcentagem de desconto e o subtotal mínimo foram agrupados na estrutura `CUPONS`.

Essa alteração melhorou a organização do código, evitando deixar as regras espalhadas pela implementação.

A execução dos testes antes e depois da refatoração mostrou que os comportamentos continuaram funcionando corretamente, sem necessidade de alterar os resultados esperados.

### d) Valores de quantidade testados

Foram utilizados valores válidos, como 1 e 2, e valores inválidos, como 0, números negativos e quantidades decimais.

Esses testes foram escolhidos para verificar as fronteiras da regra, garantindo que apenas quantidades inteiras e maiores ou iguais a 1 sejam aceitas.

### Resultados finais

- Testes aprovados: 19.
- Cobertura de ramos: 100%.
- Mutantes gerados: 25.
- Mutantes mortos: 25.
- Mutantes sobreviventes: 0.
- Escore de mutação: 100%.

Os resultados indicam que todos os mutantes gerados pelo Mutmut foram detectados pela suíte de testes.

## Conclusão

O laboratório permitiu aplicar o TDD na prática, desenvolvendo os programas de forma incremental e utilizando os testes para orientar cada alteração.

O histórico do Git registra as etapas do desenvolvimento, enquanto o Pytest, o Coverage e o Mutmut