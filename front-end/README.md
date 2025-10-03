# taqiCFD - Fast and Interactive CFD Prediction Tool

taqiCFD is a web-based interactive tool that allows users to simulate and analyze 2D flow around simple geometries using a pre-trained machine learning model. Instead of running complex CFD simulations, taqiCFD provides instant flow predictions based on input geometries and boundary conditions.

## Features

- Upload or draw a 2D geometry (circle, square, polygon, etc.).

- Configure boundary conditions, such as velocity, pressure, and domain size.

- Instant CFD predictions using a pre-trained model.

- Interactive UI with multiple tabs, buttons, and visualization tools.

- Fast and lightweight—no need for heavy CFD computations.

## Future Additions

- Advanced geometry manipulation.

- More boundary condition customization.

- Export and compare results.


Data: 13/06/2025

Realizei ajustes na estilização base do projeto, com foco em melhorar a consistência visual.

Iniciei o desenvolvimento de melhorias relacionadas à manipulação das formas geométricas, buscando facilitar a definição de tamanhos exatos.

Realizei uma reunião informal com o professor Castilho, na qual discutimos a proposta de criação de uma página “Quem Somos” com o intuito de registrar os participantes do projeto de forma permanente.

Conversei com meu colega Lucas sobre a organização do repositório, abordando a estruturação dos arquivos README e a separação de tarefas por branch.

Já possuo um direcionamento claro para o desenvolvimento das funcionalidades do front-end enquanto aguardo a disponibilização da API back-end.

Data: 20/06/2025

Iniciei a implementação da página “Sobre Nós”, conforme planejado anteriormente com o professor Castilho.

Estou no aguardo da próxima reunião para esclarecimentos sobre a API do back-end e início da integração com o front-end.

Neste momento, a estilização está sendo feita utilizando CSS puro, mas está prevista como tarefa futura a migração completa para Tailwind CSS.

Enfrentei algumas dificuldades pontuais relacionadas aos medidores de dimensão das formas geométricas na tela, os quais ainda estão em fase de ajustes.

Criei a view AboutUs.vue e o componente SobreTabs.vue, responsáveis pela estruturação da página “Sobre Nós”.

Essa estrutura permitirá exibir informações sobre os membros do projeto de forma organizada e acessível dentro da aplicação.






Enzo Salles 
Readme Front-End

O que é Open Foam

Simula o comportamento de fluidos (como ar, água, óleo, gases, etc.) e resolve equações físicas complexas como:

escoamento de fluidos (laminar ou turbulento)

transferência de calor

transporte de partículas

reações químicas, combustão

interação fluido-estrutura

Como funciona?
Você define:

a geometria do problema

a malha (divisão do espaço em pequenos volumes)

as condições de contorno e iniciais

os modelos físicos (como turbulência ou calor)

E o OpenFOAM resolve numericamente as equações de Navier-Stokes e outras associadas.

Como ele é usado?
Geralmente através de:

linhas de comando no Linux

arquivos de configuração (não tem GUI nativa)

Pode ser acoplado com softwares de geração de malha (ex: Gmsh ou Salome) e visualização (ex: ParaView)

Para quê usar?

Simular escoamentos de ar em túneis de vento

Testar aerodinâmica de carros ou aviões

Estudar comportamento de líquidos em tubulações

Projetos de engenharia térmica, naval, mecânica, etc.

--------------------------------------------------------------------------------------------------------------------

Como o front se conecta com o OpenFOAM?

Usando Vue.js no front-end do TaqiCFD, você não vai rodar o OpenFOAM diretamente no front-end. Em vez disso, o Vue.js vai servir como uma interface gráfica amigável para o usuário, enquanto o OpenFOAM roda no back-end, executando os cálculos pesados.

OpenFOAM não tem uma API nativa. Ele roda via terminal/comando Linux.

O que normalmente se faz:

O back-end (provavelmente em Python, Node, C++, etc.) recebe os parâmetros que você envia do front.

Esse back monta os arquivos de configuração do OpenFOAM (case) dinamicamente.

O back executa comandos do OpenFOAM no servidor (blockMesh, simpleFoam, snappyHexMesh, etc.).

Quando a simulação termina, o back lê os resultados (geralmente arquivos de malha, campos de velocidade, pressão, etc.).

O back envia esses resultados de volta pro front (como imagens, dados, gráficos ou arquivos).

Então o front é a interface bonitona que coleta os dados e exibe os resultados.
A conexão OpenFOAM ⇄ Front precisa do back no meio, obrigatoriamente.

O que fazer em cada página do front?
Página GeometryView (Geometria)
O que faz:

Interface para o usuário desenhar ou definir a geometria do problema.

Pode ser algo simples (escolher uma forma padrão: tubo, canal, caixa) ou mais complexo (desenhar no canvas).

Tarefas do front:

Inputs: dimensões (altura, largura, profundidade), tipo de domínio (retangular, cilíndrico, etc.).

Se tiver um canvas, o usuário pode literalmente desenhar a área.

Enviar esses dados pro backend gerar a malha (blockMesh ou snappyHexMesh).

Página SimulationView (Simulação)
O que faz:

Definir parâmetros da simulação.

Inputs típicos:

Velocidade de entrada (ex.: 2 m/s)

Pressão de saída

Viscosidade do fluido

Tipo de fluido

Número de iterações, tolerâncias, tipo de solver (simpleFoam, icoFoam, etc.)

Botão: "Iniciar Simulação"

Quando clica, manda isso tudo pro backend.

O back cria os arquivos, executa OpenFOAM e começa a simular.

Página ResultsView (Resultados)

O que faz:

Mostrar os resultados após a simulação.

Como mostrar:

Gráficos (ex.: velocidade x tempo, pressão, etc.).

Imagens ou renderizações (o backend pode gerar imagens da malha ou campos de velocidade usando o ParaView e enviar pro front).

Tabelas com dados.

Pode ter botão:

"Baixar resultados" (CSV, PNG, VTK, etc.)

"Visualizar Malha" ou até uma renderização simples no próprio front.

Sobre gerar malha:
Você, no front, vai apenas coletar os parâmetros da malha, como:

Comprimento, altura, profundidade.

Número de divisões (ex.: quantos blocos em cada direção: X, Y, Z).

Tipo de malha: estruturada (blockMesh) ou não estruturada (snappyHexMesh).


