# Analisis computacional-cognitivo-conductual del juego de cartas Truco Argentino.

![](http://www.tornquistdistrital.com.ar/wp-content/uploads/2017/09/Trucoo.jpg "") 

[DESAFIO] **¿Cómo hacer que una computadora juegue mejor que un humano al truco?**
¿Podemos crear una IA para el truco?

**Resumen:** El Truco es un juego de cartas Argentino popularmente jugado en el todo el país y el cono sur. 
Es un juego de estrategia competitivo basado en turnos, de suma cero, estados finitos e información incompleta, lo cúal quiere decir que los jugadores basaran sus estrategias en base a especulaciones en cuanto a las cartas de los demas.
En los últimos tiempos, han existido numerosos articulos cientificos implementando modelos de aprendizaje reforzado en juegos de dichas caracteristicas. No obstante, aun no hay ningun trabajo que haya analizado este particular juego Argentino.
El próposito de este proyecto es analizar este juego desde un aspecto computacional para poder, luego, modelar un agente de aprendizaje reforzado.
Para dicho fin, primero vamos a hacer una revisión de los trabajos cientificos en juegos similares (como el poker), luego conceptualizar algunos terminos clave para abordar dicho problema, proponemos en este trabajo un modelado del oponente en función del comportamiento y estilo cognitivo de jugadores de truco y finalmente, invitamos a la comunidad al involucramiento en el desarrollo de un agente de aprendizaje reforzado para resolver este problema. ¿Cuál creen qué es el mejor enfoque para abordar el problema? ¿Qué algoritmo usarias?


**Nota:** Estamos analizando el truco Argentino **sin** flor y de **a dos** jugadores.

## ¿Cómo contribuir?

* Si te interesa participar simplemente clona este repositorio y unite al slack **haciendo clic** a este link: http://iaar-slack.herokuapp.com/
* Si ya estas en slack podes ingresar con este link: http://iaar.slack.com

## Facilitador

Patricio J. Gerpe

## Preliminares
### Revisión de literatura

En tanto no se han encontrado artículos cientificos en respecto al juego de cartas 'Truco' si existe artículos cientificos que abordan juegos de cartas de información imperfecta tal como el Poker.
Ejemplos incluyen:

* Heinrich, J., & Silver, D. (2016). Deep reinforcement learning from self-play in imperfect-information games. arXiv preprint arXiv:1603.01121. https://arxiv.org/pdf/1603.01121.pdf
* Mealing, R., & Shapiro, J. L. (2017). Opponent Modeling by Expectation-Maximization and Sequence Prediction in Simplified Poker. IEEE Trans. Comput. Intellig. and AI in Games, 9(1), 11-24.
* Kitchen, A., & Benedetti, M. (2018). ExpIt-OOS: Towards Learning from Planning in Imperfect Information Games. arXiv preprint arXiv:1808.10120. https://arxiv.org/pdf/1808.10120.pdf
* Yakovenko, N., Cao, L., Raffel, C., & Fan, J. (2016, February). Poker-CNN: A Pattern Learning Strategy for Making Draws and Bets in Poker Games Using Convolutional Networks. In AAAI (pp. 360-368).
* Ganzfried, S., & Yusuf, F. (2017). Computing human-understandable strategies: Deducing fundamental rules of poker strategy. Games, 8(4), 49.
* Bowling, M., Burch, N., Johanson, M., & Tammelin, O. (2017). Heads-up limit hold'em poker is solved. Communications of the ACM, 60(11), 81-88.
* Li, X., & Miikkulainen, R. (2018, July). Opponent modeling and exploitation in poker using evolved recurrent neural networks. In Proceedings of the Genetic and Evolutionary Computation Conference (pp. 189-196). ACM.
* Dahl, F. A. (2001, September). A reinforcement learning algorithm applied to simplified two-player Texas Hold’em poker. In European Conference on Machine Learning (pp. 85-96). Springer, Berlin, Heidelberg.
* Teófilo, L. F., Passos, N., Reis, L. P., & Cardoso, H. L. (2012). Adapting strategies to opponent models in incomplete information games: a reinforcement learning approach for poker. In Autonomous and Intelligent Systems (pp. 220-227). Springer, Berlin, Heidelberg.
* Erev, I., & Barron, G. (2005). On adaptation, maximization, and reinforcement learning among cognitive strategies. Psychological review, 112(4), 912. https://www.researchgate.net/profile/Ido_Erev/publication/7505648_On_Adaptation_Maximization_and_Reinforcement_Learning_Among_Cognitive_Strategies/links/00b49524696d50e515000000.pdf
* Szita, I. (2012). Reinforcement learning in games. In Reinforcement Learning (pp. 539-577). Springer, Berlin, Heidelberg.
* Kovacic, M. (2015). Opponent Modelling in Games with Imperfect Information.
* Hernandez-Leal, P., Taylor, M. E., Rosman, B., Sucar, L. E., & Munoz de Cote, E. (2016). Identifying and tracking switching, non-stationary opponents: A Bayesian approach.
* Albrecht, S. V., & Stone, P. (2018). Autonomous agents modelling other agents: A comprehensive survey and open problems. Artificial Intelligence, 258, 66-95.
* Kawamura, K., Mizukami, N., & Tsuruoka, Y. (2017, August). Neural Fictitious Self-Play in Imperfect Information Games with Many Players. In Workshop on Computer Games (pp. 61-74). Springer, Cham.
* Ponsen, M. J., Gerritsen, G., & Chaslot, G. (2010). Integrating Opponent Models with Monte-Carlo Tree Search in Poker. Interactive Decision Theory and Game Theory, 82.
* Bard, N., & Bowling, M. (2007, July). Particle filtering for dynamic agent modelling in simplified poker. In Proceedings of the National Conference on Artificial Intelligence (Vol. 22, No. 1, p. 515). Menlo Park, CA; Cambridge, MA; London; AAAI Press; MIT Press; 1999.
* Hernandez-Leal, P., Zhan, Y., Taylor, M. E., Sucar, L. E., & de Cote, E. M. (2017). An exploration strategy for non-stationary opponents. Autonomous Agents and Multi-Agent Systems, 31(5), 971-1002.


### Conceptos Clave

* **Modelado del oponente**:
Dado que no podemos saber qué cartas tiene nuestro oponente es necesario poder modelar el estilo del juego del mismo.
El modelado del oponente busca clasificar a nuestro oponente en base a su estilo estilo cognitivo (Toma deciciones de manera racional VS toma decisiones de manera intuitiva) así como su comportamiento. ¿Con qué frecuencia el oponente cambia su estilo de juego? 
¿Cuál es la frecuencia en la qué miente? ¿Tiene predominancia el comportamiento agresivo (Ejem.: Aumentar apuestas) o el comportamiento defensivo (Ejem.: Rechazar apuestas en contextos de malas cartas).

* **Equilibrio de Nash**:
Se llama equilibrio de Nash a  situaciones en las que las decisiones que ambos jugadores tomaron no pudiesen haber maximizado la utilidad para ambos de otra mejor alternativa.

* **Valor esperado**:
El valor esperado (EV) es el puntaje que podemos ganar al tomar una acción (Ejemplo: Ganar envido vs Perder envido) multiplicado por la probabilidad de ocurrencia de dicho desenlance.

* **Expectativa positiva**:
EV+ , o expectativa positiva, es aquella acción que maxima la utilidad en función de su probabilidad de ocurrencia dados ciertas jugadas en contextos de información incompleta.

* **Teorema fundamental del Poker.** (Aplica para el Truco)
El teorema fundamental del poker, propuesto por David Sklansky, afirma que 'Siempre que un jugador juegue de manera distinta a la que lo habría hecho si conociera las cartas del rival, su rival saca ventaja; siempre que un jugador haga el mismo movimiento que haría si conociera las cartas del rival, él saca ventaja.'

* **Pozo del juego (Game's Equity)**:
El pozo del juego es la cantidad de puntos en juego durante la partida. (Ejem. Si se canta truco y re truco serán 3).

* **Pozo del jugador (Player's equity)**:
El pozo del jugador es el pozo del juego multiplicado por la probabilidad del jugador de ganar sobre el pozo del juego multiplicado por la probabilidad del jugador de perder.


* **Valor de la mano (Hand's value)**:
Es un puntaje obtenido en base a la posición de las cartas en función del truco y los tantos multiplicado por la probabilidad de obtenerlos.

* **Combinatoria:**
Es el estudio de la probabilidad de obtener diferentes manos en particular.

### Modelado de cartas y manos.

**P = Probabilidad**


#### Cartas


Vamos a usar lógica difusa para clasificar nuestras cartas:

####  P d/ derrotar a otra carta       
| Expresión matematica       | Termino linguistico       | 
| ------------- |:-------------:|
| A = 1      				 | Absoluta     |
| A = 0.93      				 | Casi Absoluta      |
| A = (0.78, 0.86)      				 | Muy alta     |
| A = (0.57, 0.71)      				 | Alta     |
| A = (0.35, 0.50)      				 | Media     |
| A = (0, 0.21)      				 | Baja     |


#### P d/ obtener carta      
| Expresión matematica       | Termino linguistico       | 
| ------------- |:-------------:|
| A = 0.277     				 | Alta      |
| A = 0.146      				 | Media     |
| A = 0.075      				 | Baja    |

Vamos a rankear las cartas:

| Carta         | Ranking       | P d/ derrotar a otra carta  | P d/ obtener carta  |
| ------------- |:-------------:|:-----:|:-----:|
|   ![](images/espada/1.jpg "") 																				  | 1 | 1.0 |  0.075 |
| ![](images/basto/1.jpg "")     																				 | 2     |   0.97 | 0.075 |
| ![](images/espada/7.jpg "")  																					   | 3      |    0.95 | 0.075 |
| ![](images/oro/7.jpg "")   																					  | 4      |    0.92 | 0.075 |
| ![](images/espada/3.jpg "") ![](images/basto/3.jpg "") ![](images/oro/3.jpg "") ![](images/copa/3.jpg "")       | 5      |    0.82 | 0.277|
| ![](images/espada/2.jpg "") ![](images/basto/2.jpg "") ![](images/oro/2.jpg "") ![](images/copa/2.jpg "")       | 6      |    0.72 | 0.277 |
| ![](images/oro/1.jpg "") ![](images/copa/1.jpg "")     														  | 7      |    0.66 | 0.146 |
| ![](images/espada/12.jpg "") ![](images/basto/12.jpg "") ![](images/oro/12.jpg "") ![](images/copa/12.jpg "")       | 8      |    0.56 | 0.277 |
| ![](images/espada/11.jpg "") ![](images/basto/11.jpg "") ![](images/oro/11.jpg "") ![](images/copa/11.jpg "")       | 9      |    0.46 | 0.277 |
| ![](images/espada/10.jpg "") ![](images/basto/10.jpg "") ![](images/oro/10.jpg "") ![](images/copa/10.jpg "")       | 10      |    0.36 | 0.277 |
|  ![](images/basto/7.jpg "")  ![](images/copa/7.jpg "")       															| 11      |    0.31 | 0.146 |
| ![](images/espada/6.jpg "") ![](images/basto/6.jpg "") ![](images/oro/6.jpg "") ![](images/copa/6.jpg "")       | 12      |    0.21 | 0.277 |
| ![](images/espada/5.jpg "") ![](images/basto/5.jpg "") ![](images/oro/5.jpg "") ![](images/copa/5.jpg "")       | 13      |    0.10 | 0.277 |
| ![](images/espada/4.jpg "") ![](images/basto/4.jpg "") ![](images/oro/4.jpg "") ![](images/copa/4.jpg "")       | 14      |    0 | 0.277 |

Formula de p/d ganar:

`casos en los que gana la carta / total de casos.`

Formula de p d/ obtener carta en una mano:
Manos con la carta : `C(casos,2) = n`

Tener un 7 de basto o un 7 de copa:
`p(A or B) =`

Tener algun 4:
`p(A or B or C or D) =`


Cantidad de manos : `9,880`



#### Combinatoria de manos

Formula: 

`P = 40! / (40 - 3)! =  40! / 37! = (40 * 39 * 38) / 6 = 9,880`

**59,280** son la cantidad de combinaciones posibles que tenemos. Es un número muy grande así que vamos a clasificar esas manos con el uso de lógica difusa.

Si consideramos la diferentes combinación en función de si sos mano o pie las posibilidades son:

`9880 * 2 =` **19,760**

Vamos a clasificar la mano por:

* (A) Su valor en el juego del envido.
* (B) Su valor en el juego del truco.


Vamos por su valor en el **envido**:

E = **Envido**
m = 'Soy mano'
p = 'Soy pie'

| Expresión matematica       | Puntaje  |     Termino linguistico       |  P de ganar       | Termino linguistico       | 
| ------------- |:-------------:| ------------- | ------------- |:-------------:|
| Em = 33      					| 21	 | Máximo     | 1.0 | Absoluta |
| Ep = 33      					| 21 |      | 0.95 | Casi Absoluta |
| Em = (28, 32)      			|	(16,20) | Muy Alto    | 0.85~ | Muy Alta |
| Ep = (28, 32)      			|	(16,20) |      | 0.80~ | |
| Em = (26, 27)      			|	(14,15) | Alto     | 0.66~ | Alta |
| Ep = (26, 27)      			|	(14,15) |      | 0.64~ |  |
| Em = (20, 25)      			|	(8,13) | Bajo     | 0.50~ | Media |
| Ep = (20, 25)      			|	(8,13) |      | 0.45~ | |
| Em = (1, 7)      				|	(1,7) | Muy Bajo   | 0.19~ | Muy baja |
| Ep = (1, 7)      				|	(1,7) |     | 0.14~ | |


Probabilidad de ganar se calcula en base al total de casos que mi mano puede ganar el envido sobre el total de casos posibles de envido que tenga el oponente

Casos posibles =
`[33,32,31,30,29,28,27,26,25,24,23,22,21,20,7,6,5,4,3,2,1]`


Osea 21 casos posibles. Ejem.: Si tengo 33 pero no soy mano entonces mis probabilidades de ganar son 20/21 = 0.95

Para los que sean intervalos, calculamos para cada caso y luego computamos promedio.

Ejem:

Em = (28, 32)
Ep = (28, 32)

`P(g)Em = (0.95 + 0.90 + 0.85 + 0.81 + 0.76) / 5 = 0.85 
P(g)Ep = (0.90 + 0.85 + 0.81 + 0.76 + 0.71) / 5 = 0.80`



Vamos por su valor en el **truco**:


Para el truco vamos darle un puntaje a cada carta de nuestra mano en base a su ranking.

Ejemplo: Si tengo un ancho de espada, es decir ranking 1 son 14 puntos (inversamente proporcional a la cantidad de casos)

| Carta         | Ranking       |  Puntaje  | Expresión linguistica  |
| ------------- |:-------------:|:-----:| :-----:|
|   ![](images/espada/1.jpg "") 																				  | 1 | 14 | Muy Alto  |
| ![](images/basto/1.jpg "")     																				 | 2     |   13 |   |
| ![](images/espada/7.jpg "")  																					   | 3      |    12 |    | 
| ![](images/oro/7.jpg "")   																					  | 4      |    11 |    |
| ![](images/espada/3.jpg "") ![](images/basto/3.jpg "") ![](images/oro/3.jpg "") ![](images/copa/3.jpg "")       | 5      |    10 |  Alto  |
| ![](images/espada/2.jpg "") ![](images/basto/2.jpg "") ![](images/oro/2.jpg "") ![](images/copa/2.jpg "")       | 6      |    9 |    |
| ![](images/oro/1.jpg "") ![](images/copa/1.jpg "")     														  | 7      |    8 |  Medio |
| ![](images/espada/12.jpg "") ![](images/basto/12.jpg "") ![](images/oro/12.jpg "") ![](images/copa/12.jpg "")       | 8      |    7 |   | 
| ![](images/espada/11.jpg "") ![](images/basto/11.jpg "") ![](images/oro/11.jpg "") ![](images/copa/11.jpg "")       | 9      |    6 |    |
| ![](images/espada/10.jpg "") ![](images/basto/10.jpg "") ![](images/oro/10.jpg "") ![](images/copa/10.jpg "")       | 10      |    5 |    |
|  ![](images/basto/7.jpg "")  ![](images/copa/7.jpg "")       															| 11      |    4 |  Bajo  |
| ![](images/espada/6.jpg "") ![](images/basto/6.jpg "") ![](images/oro/6.jpg "") ![](images/copa/6.jpg "")       | 12      |    3 |    |
| ![](images/espada/5.jpg "") ![](images/basto/5.jpg "") ![](images/oro/5.jpg "") ![](images/copa/5.jpg "")       | 13      |    2 |    |
| ![](images/espada/4.jpg "") ![](images/basto/4.jpg "") ![](images/oro/4.jpg "") ![](images/copa/4.jpg "")       | 14      |    1 |    |



Entonces por ejemplo...

**P** = Puntaje
**Pr** = Probabilidad

| Mano                                                                                         | Ranking       | Pr de mano         | P d/ envido  | P d/  truco  | Pr d/ ganar envido  | Pr d/ ganar truco  | Valor min de tanto  | Valor min de truco  | Valor max de tanto  | Valor max de truco  | Valor de la mano  |
| ---------------------------------------------------------------------------------------------|:-------------:|:------------------:|:------------:|:------------:|:-------------------:|:------------------:|:-------------------:|:-------------------:|:-------------------:|:-------------------:|:-------------------:|		
| ![](images/espada/1.jpg "") ![](images/espada/7.jpg "") ![](images/espada/6.jpg "") de mano  |  1           |        0.0015581    |  21/21       |  29/39       |  1               | 0.95               |  2               | 1.90                |   7  | 3.8 | 10.8 |
| ![](images/basto/1.jpg "") ![](images/espada/7.jpg "") ![](images/espada/6.jpg "") de mano   |  2           |        0.0015581    |  21/21       |  28/39       |  1               | 0.92               |  2               | 1.84                |   7  | 3.7 | 10.7 |					
| ![](images/espada/1.jpg "") ![](images/oro/7.jpg "") ![](images/oro/6.jpg "") de mano   |  2           |        0.0015581    |  21/21       |  28/39            |  1               | 0.92               |  2               | 1.84              |   7  | 3.7 | 10.7 |
| ![](images/basto/1.jpg "") ![](images/oro/7.jpg "") ![](images/oro/6.jpg "") de mano   |  3           |        0.0015581    |  21/21       |  27/39             |  1               | 0.89               |  2               | 1.78              |   7  | 3.56 | 10.56 |
| ![](images/espada/7.jpg "") ![](images/oro/7.jpg "") ![](images/oro/6.jpg "") OR ![](images/espada/6.jpg "") de mano   |  4           |        0.0008212    |  21/21       |  26/39             |  1               | 0.87               |  2               | 1.74             |   7  | 3.48 | 10.48 |
| ![](images/espada/1.jpg "") ![](images/espada/7.jpg "") ![](images/espada/3.jpg "") de mano   |  ?           |        0.0004220    |  18/21       |  36/39       |  0.86               | 0.95               |  1.72            | 1.90              |   6  | 3.8 | 9.80 |
| ![](images/espada/1.jpg "") ![](images/espada/7.jpg "") ![](images/basto/1.jpg "") de mano   |  ?           |        0.0004220    |  16/21       |  39/39       |  0.76               | 1               |  1.52            | 2               |   5.32  | 4 | 9.32 |


**ESTAS PROBABILIDADDES NECESITAN REVISION**

Calculo de probabilidad de obtener mano:
`p(A and B and C) =`

La probabilidad de ganar truco se basa en la probabilidad conjunta de que ganes dos manos con tus mejores cartas. El valor minimo de tanto es lo minimo que podes ganar (Envido) multiplicado por la probabilidad de ganar esos puntos. Mismo con el truco. El valor máximo es en el envido el (envido,envido, real envido = 7 puntos) y en el truco (quiero vale 4 = 4), en ambos casos se multiplica por la probabilidad de obtener dichos puntos.

Basado en este sistema de puntaje seria bueno averiguar si realmente esta mano es la más valiosa. Si uno tiene en cuenta el valor (equity) de la mano, pareceria que tener buen envido es más valioso que tener puntos para el truco. **¿A vos qué te parece?**

  	

### Modelado de acciones, jugadas y tácticas:


#### Acciones (Actions)

| Acción         | Denominación       |
| ------------- |:-------------:|
| Tirar carta         | check       |
| Irse al mazo         | fold       |
| Envido         | bet       |
| Envido Envido         | raise       |
| Real envido         | raise       |
| Envido Real envido         | raise       |
| Falta envido         | raise && allIn       |
| Truco        | bet       |
| Re Truco        | raise       |
| Vale cuatro        | raise       |
| Quiero        | call      |
| No Quiero (Envido)        | pass       |
| No Quiero (Truco)       | fold       |

#### Jugadas (Plays)

| Jugada         | Descripción      |
| ------------- |:-------------:|
| Ir a la pesca         | Se tiene tanto o truco medio o alto, no se canta y se espera a que el contrincante cante para doblar la apuesta o aceptar.    |
| Envido de Cobertura         | Se tiene buen tanto pero malas cartas para el  truco, el oponente canta truco en la primera mano, y se dice "el envido esta primero" para postergar el truco y obtener puntos del tanto antes de retirarse.     |
| Mentira del tanto         | No se tienen buen tanto, se canta o se acepta y al momento de decir los puntos se miente por un nro más alto, esperando a que se termine la partida y el rival haya olvidado pedir que se muestren los tantos.      |
| Trampa del truco        | Se tiene muy buenas cartas de envio y cartas medias/buenas de truco, en la primera mano cantamos truco esperando que nuestro oponente nos diga "el envido esta primero" de manera tal que podamos doblar la apuesta.      |
| Achicar         | No se tiene buenas cartas (tanto o truco), el oponente canta primero y  dobla la apuesta buscando que el oponente la rechace.     |
| Hacerlos entrar         | Se tiene buenas cartas, el contricante canta primero y se dobla la apuesta para buscar  más puntos.      |
| Jugar callado        | No se tiene buenas cartas, y no se canta nada esperando que pase desapercibido para el oponente y tampoco lo haga.      |
| Hacersela        | Apurar a un oponente para que juege cuando no es su turno, de manera que tire y queme su carta.       |
| El error        | Estar hablando y simular que se te escapó la palabra truco o envido de manera que los oponentes quieran tomar provecho, acepten y/o doblen la apuesta esperando que nosotros no tengamos nada.       |
| Falta envido de Cobertura      | El oponente esta a pocos puntos de ganar (menos de 3) , vos no tenes muchos tantos, te canta tanto o te dobla una apuesta. Para minimizar riesgos le cantas falta envido para reducir los puntos en juego.      |
| Apriete        | Nuestro oponente esta a pocos puntos de perder, tenemos cartas y sabiendo que sí o sí debe aceptar, cantamos tanto o truco para acepte y pierda.    |


### Modelado de perfiles de jugadores


#### Según su perfil de estrategia


**Formula del indice de mentira:**

`Mi = ((bets,raises, calls when mano = 'malas' || 'muy malas')  / (bets + raises + calls) ) * 100`

`Mi = (0,1)`

| Expresión matematica       | Termino linguistico       | 
| ------------- |:-------------:|
| A = 1     				 | Absoluto      |
| A = (0.80, 1)     				 | Muy alto     |
| A = (0.60, 0.80)     				 | Alto     |
| A = (0.40, 0.60)     				 | Medio     |
| A = (0.20, 0.40)     				 | Bajo     |
| A = (0, 0.20)     				 | Muy Bajo     |
| A = (0,1)     				 | Impredecible    |



**Formula indice de agresión:**

`Ai = (bets + raises) / (bets + raises + calls + checks + passes) * 100`
`Mi = (0,1)`

| Expresión matematica       | Termino linguistico       | 
| ------------- |:-------------:|
| A = 1     				 | Absoluto      |
| A = (0.80, 1)     				 | Muy alto     |
| A = (0.60, 0.80)     				 | Alto     |
| A = (0.40, 0.60)     				 | Medio     |
| A = (0.20, 0.40)     				 | Bajo     |
| A = (0, 0.20)     				 | Muy Bajo     |
| A = (0,1)     				 | Impredecible    |

**Formula Indice de variabilidad:**

Coeficiente de varianza = Cv

` Vi = v/( Cv(Ai) * Cv(Mi) )`

`Vi = (0,1)`


| Expresión matematica       | Termino linguistico       | 
| ------------- |:-------------:|
| A = 1     				 | Absoluto      |
| A = (0.80, 1)     				 | Muy alto     |
| A = (0.60, 0.80)     				 | Alto     |
| A = (0.40, 0.60)     				 | Medio     |
| A = (0.20, 0.40)     				 | Bajo     |
| A = (0, 0.20)     				 | Muy Bajo     |
| A = (0,1)     				 | Impredecible    |

Tiene en cuenta: (A) Indice de mentira (Oportunidades que mintió sobre oportunidades que no lo hizo) , (B) Indice de agresión (Oportunidades que aumentó apuesta sobre oportunidades que no lo hizo) y (C) Indice de variabilidad (Frecuencia en la cambia el patrón de estrategia en función del resto)

| Nombre  | Descripción | Indice de mentira | Expresión Linguistica | Indice de agresión | Expresión Linguistica | Indice de variabilidad | Expresión Linguistica |  Tendencia a cantar con manos |
| ------------- |:-------------:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| Creativo  | Cambia sus tácticas con frecuencia, crea nuevas jugadas espontaneamente. | (0,1) | Impredecible | (0,1) | Impredecible | (0.80, 1)  | Muy Alta | Impredecible |
| Temerario | Miente con mucha frecuencia, y suele arriesgar muchos puntos teniendo cartas pobres.  | (0.80, 1) | Muy alto | (0.80, 1) | Muy alto | (0.20, 0.40) | Bajo | Malas |
| Tradicional | Miente seguido con cartas medias y malas, en alguna ocasión hace un gran aumento de apuestas con cartas malas.  | (0.60, 0.80) | Alto | (0.60, 0.80) | Alto | (0.20, 0.40) | Bajo | Medias o Malas |
| Pescador | Canta cuando tiene cartas buenas y medias, aunque cada tanto realiza una mentira teniendo cartas malas. | (0.40, 0.60) | Medio | (0.40, 0.60) | Medio | (0.20, 0.40) | Bajo | Buenas o Medias|
| Conservador | Canta cuando tiene buenas cartas. Suele decir que no quiere cuando tiene cartas malas. | (0.20, 0.40) | Bajo| (0.20, 0.40) | Bajo | (0.20, 0.40) | Bajo | Muy Buenas o Buenas |
| Miedoso | Solo canta cuando tiene cartas excelentes. Prácticamente renuncia a todos los aumentos de apuesta. | 0 | Nulo| (0, 0.20) | Muy Bajo | (0.20, 0.40) | Bajo | Muy Buenas |


Podriamos decir que tenemos 3 espectros de comportamiento:

1. Pasivo <-> Agresivo  
2. Conservador <-> Ariesgado
3. Estatico <-> Dinamico

**¿Se les ocurren otras clasificaciones?**

## Próximos pasos en el analísis

* Encontrar mejores formas de clasificar valor de las manos.
* Hacer una simulación para detectar el top de manos con más valor.
* Calcular probabilidad de ganar en función de la clasificación de la mano.
* Calcular probabilidad de las manos.¨
* Modelar estados del juego
* Clasificar jugadas (plays)
* Calcular valor esperado de jugadas y acciones segun diferentes estados.


## ¿Y vos, cómo encararias el desarrollo de un agente de aprendizaje reforzado para el truco Argentino?

¡No dudes en participar de este proyecto con tus ideas!

## Referencias y Bibliografía adicional

* David Sklansky (1987). The Theory of Poker. Two Plus Two Publications. ISBN 1-880685-00-0.
* Zadeh, L. A. (1965). Fuzzy sets. Information and control, 8(3), 338-353

### Más literatura cientifica:

* Billings, D., Schaeffer, J., & Szafron, D. (1999). Using probabilistic knowledge and simulation to play poker. In In AAAI National Conference. http://www.aaai.org/Papers/AAAI/1999/AAAI99-099.pdf
* Barone, L., & While, L. (2000, July). Adaptive learning for poker. In Proceedings of the 2nd Annual Conference on Genetic and Evolutionary Computation (pp. 566-573). Morgan Kaufmann Publishers Inc.. http://www.cs.bham.ac.uk/~wbl/biblio/gecco2000/RW179.pdf
* Johansson, U., Sonstrod, C., & Niklasson, L. (2006, December). Explaining Winning Poker--A Data Mining Approach. In Machine Learning and Applications, 2006. ICMLA'06. 5th International Conference on (pp. 129-134). IEEE. https://ieeexplore.ieee.org/abstract/document/4041481/