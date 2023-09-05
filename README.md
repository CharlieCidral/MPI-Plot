# Computação Paralela e Distribuida.

## Computação Paralela:
Imagine que você tem uma tarefa grande para fazer, como pintar uma parede muito grande. Na computação paralela, você convida várias pessoas para ajudar a pintar a parede ao mesmo tempo. Cada pessoa pinta uma parte da parede, tornando o trabalho mais rápido. Isso é como os computadores trabalham juntos em paralelo para resolver problemas complexos mais rapidamente. Eles dividem o trabalho e colaboram para chegar mais rápido ao resultado.

Exemplos:
 - Simulações de física, como simulações de fluidos ou simulações climáticas.
 - Processamento de imagem, como reconhecimento facial ou de objetos.
 - Otimização de problemas, como encontrar o caminho mais curto entre dois pontos.

## Computação Distribuída:
Agora, pense em ter várias pessoas em lugares diferentes, cada uma com uma parede para pintar. Elas podem se comunicar através de telefones ou mensagens para coordenar o trabalho, mesmo estando longe umas das outras. Na computação distribuída, vários computadores em diferentes locais trabalham juntos em uma tarefa. Eles se comunicam pela internet para compartilhar informações e resolver problemas, como se estivessem próximos, mesmo estando separados geograficamente.

Exemplos:
 - Computação em nuvem, como o Google Cloud ou o Amazon Web Services.
 - Redes sociais, como o Facebook ou o Twitter.
 - Jogos online, como o World of Warcraft ou o Fortnite.

### Resumindo:

Computação Paralela é quando vários computadores trabalham juntos ao mesmo tempo para resolver um problema grande e dividem o trabalho.
Computação Distribuída é quando computadores em lugares diferentes colaboram pela internet para realizar tarefas, como se estivessem próximos.

### Diferença:

A principal diferença entre computação paralela e distribuída é a forma como os recursos são compartilhados. Na computação paralela, todos os processadores têm acesso à mesma memória e armazenamento. Isso permite que eles compartilhem informações e dados facilmente, o que é essencial para a execução de cálculos em paralelo.

Na computação distribuída, cada computador tem sua própria memória e armazenamento. Isso significa que os computadores precisam se comunicar uns com os outros para compartilhar informações e dados. Isso pode ser mais lento do que a computação paralela, mas também pode ser mais escalonável.

| Característica  | Computação paralela  | 	Computação distribuída  |
| ------------ | ------------ | ------------ |
| Compartilhamento de recursos  | Todos os processadores têm acesso à mesma memória e armazenamento  | Cada computador tem sua própria memória e armazenamento  |
| Comunicação entre processadores  |  processadores	Direta  | 	Indirecta  |
| Desempenho  | Mais rápido  | Mais lento  |
| Escalonabilidade  | 	Menor  | 	Maior  |

### Uso:
Em geral, a computação paralela é mais adequada para aplicações que requerem um alto desempenho, como simulações científicas ou processamento de imagem. A computação distribuída é mais adequada para aplicações que requerem um grande número de recursos, como computação em nuvem ou jogos online.

### Modelos Comuns:

MPI é um modelo de programação de comunicação entre processos. Ele é usado para distribuir tarefas entre vários computadores ou processadores em um único computador. MPI é um modelo de programação de baixo nível, o que significa que requer o programador ter um conhecimento profundo da arquitetura do computador e da rede.

OpenMP é um modelo de programação de threads. Ele é usado para paralelizar tarefas em um único computador com vários processadores. OpenMP é um modelo de programação de alto nível, o que significa que é mais fácil de usar do que MPI.

Hadoop é um framework de processamento de dados em cluster. Ele é usado para processar grandes volumes de dados em um cluster de computadores. Hadoop é um modelo de programação de alto nível, o que significa que é mais fácil de usar do que MPI ou OpenMP.

| Modelo  | Aplicações  | Pontos Fortes  | Pontos Fracos  |
| ------------ | ------------ | ------------ | ------------ |
| MPI  | Simulações científicas, processamento de imagem, processamento de vídeo  | Desempenho, escalabilidade  | Complexidade, aprendizado  |
| OpenMP  | Processamento de dados, análise de dados, machine learning  | Facilidade de uso, desempenho  | 	Não escalável para grandes sistemas  |
| Hadoop  | Big data, análise de dados, machine learning  | 	Facilidade de uso, escalabilidade  | 	Desempenho, custo  |

### Ideia:

Utilizando um dataset do Kaggle carregando um plot das correlações a cada 1000 linhas com mpi4py. Não é um cenario que faz sentido, mas sim para aprender um pouco sobre o uso das ferramentas e contribuir como objeto de estudo para outros alunos.

## Passos:

 - Instalações(Programas e Dependências).
 - Dowload da base de dados.
 - Analise.

### Programas:

 - Python
 - MPI

Obs.: Após a instalação do MPI é necessario a reinicialização do computador.

### Dependências:
  - pip
  - mpi4py
  - pandas
  - seaborn
  - sklearn
  - matplotlib
  - numpy
  - subprocess

### Downloads:

 - Kaggle Dataset from Edgar Lopez.

Uso:
`
  python study_case.py
`

### Analise:

 ![Figure_1](https://github.com/CharlieCidral/MPI-Plot/assets/69029099/baf6d8fe-19ef-453d-96f7-deca91f53f22)



