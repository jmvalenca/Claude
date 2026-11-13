# Capítulo 4: Verificação de Modelos baseada em SAT (2ª parte)

# Transformadores de Predicados

Vamos considerar um SFOTS  e o seu dual 

                    $$\Sigma\;\equiv\;\langle\,\mathsf{X}\,,\,\mathsf{I}\,,\,\mathsf{T}\,,\,\mathsf{E}\rangle\qquad$$  ,$$\qquad\Sigma^\top\;\equiv\;\langle\,\mathsf{X}\,,\,\mathsf{E}\,,\,\mathsf{T}^{-1}\,,\,\mathsf{I}\rangle$$

e assumir implícita, na especificação  dos tipos das variáveis, a SMT  $$\,\mathcal{T}\,$$(que se assume ter quantificadores)  para ambos  os sistemas, assim como a criação de “clones” **next**.  Finalmente vamos restringir o conjunto dos valores de $$\;\mathsf{X}\;$$  a um domínio infinito e enumerável $$\;\mathcal{X}\;$$  (e.g. domínio das strings de bits).
Assim todo o predicado $$\,\mathsf{P}\,$$ em $$\;\mathcal{T}\;$$,  usando $$\,n\,$$ clones de $$\,\mathsf{X}\,$$ como variáveis livres (aqui designado por $$\,n$$-ário),  tem um conjunto de modelos 

                                $$\lbrack \mathsf{P}\rbrack\;\equiv\;\{\,x\in \mathcal{X}^n\,|\,x \models \mathsf{P}\,\}$$  

que se identifica com um subconjunto de $$\,\mathcal{X}\,.$$ 

| Por hipótese $$\,\mathcal{X}\,$$ é infinito e enumerável; então, para todo $$\,n\geq 0\,$$, $$\,\mathcal{X}^n\,$$ identifica-se com um subconjunto do    próprio $$\,\mathcal{X}\,$$.  Nomeadamente cada $$\;p\in \mathsf{2}^\mathcal{X}\;$$ determina uma classe, eventualmente vazia,  de predicados  semanticamente equivalentes. |

Vamos representar por $$\;\mathcal{P}_\mathsf{X}\;$$ (ou simplesmente $$\;\mathcal{P}\;$$) o conjunto dos predicados unários  (que podem ser definidos  em $$\;\mathcal{T}\;$$ com variáveis livres$$\;\mathsf{X}\,$$) . Igualmente vamos representar por $$\;\mathcal{P}_{\mathsf{X},\mathsf{X'}}\;$$(ou simplesmente $$\,\mathcal{P}'\;$$) o conjunto dos predicados binários  definidos em $$\,\mathcal{T}\,$$ com variáveis livres $$\,\mathsf{X}\,\text{e}\,\mathsf{X}'\;$$.


| Neste contexto recorde-se que o predicado $$\,\mathsf{T}^{-1}\,$$ , que faz parte da definição de $$\,\Sigma^\top\;$$, se obtém de $$\,\mathsf{T}\,$$ trocando o papel das variáveis $$\,\mathsf{X}\,$$e $$\,\mathsf{X}'\,$$; isto é,    $$\mathsf{T}^{-1}\;\equiv\;\mathsf{T}[\mathsf{X}/\mathsf{X}'\,,\,\mathsf{X}'/\mathsf{X}]$$  em substituições simultâneas. |

Por  **transformador de predicados (t.p.)** designamos uma transformação   $$\;\mathsf{op}\,\colon\,\mathcal{P}\,\to\,\mathcal{P}\,$$ ou  $$\;\mathsf{op}\,\colon\,\mathcal{P}'\,\to\,\mathcal{P}'\,$$ que é possível definir aumentando $$\;\mathcal{T}\;$$com o operador “substituição de variáveis por termos”.

| A substituição de $$\,\mathsf{X}\,$$ por um “clone” arbitrário  (distinto de $$\,\mathsf{X}$$)  não é um transformador de predicados unários porque o resultado  passa a conter variáveis que não estão em $$\,\mathsf{X}\,$$. |

O FOTS $$\,\Sigma\,$$ cria dois transformadores de predicados que representam a relação $$\,\mathsf{T}$$  em $$\,\Sigma\,$$:


1. O transformador de predicados $$\;\mathsf{wp}_\Sigma\;$$, designado por **universal weakest pre-condition** mapeia um  $$\,\mathsf{Q}\in\mathcal{P}\,$$ no  predicado $$\;\mathsf{wp}_\Sigma(\mathsf{Q})\in \mathcal{P}\;$$que verifica, para todo  $$\;\mathsf{P}\,\in\,\mathcal{P}\;$$,


             $$\mathsf{P}\,\to\,\mathsf{wp}_\Sigma(\mathsf{Q})\quad$$é tautologia se e só se é tautologia
                            $$\quad\forall\,Z\,\centerdot\,\mathsf{P}\,\land\,\mathsf{T}[\mathsf{X}'/Z]\,\to\,\mathsf{Q}[X/Z]\quad$$ 
    
2. O transformador de predicados $$\;\mathsf{sp}_\Sigma\;$$, designado por **existencial strongest post-condition** mapeia um  $$\,\mathsf{P}\in\mathcal{P}\,$$ no  predicado $$\;\mathsf{sp}_\Sigma(\mathsf{P})\;$$que verifica, para todo  $$\;\mathsf{Q}\,\in\,\mathcal{P}\;$$,


            $$\mathsf{sp}_\Sigma(\mathsf{P})\,\to\,\mathsf{Q}\quad$$ é tautologia se e só se é tautologia
                            $$\quad\forall\,Z\,\centerdot\,\mathsf{P}\,\land\,\mathsf{T}[\mathsf{X}'/Z]\,\to\,\mathsf{Q}[X/Z]\quad$$ 


> É essencial explicitar que estas definições axiomáticas definem univocamente (a menos de equivalência semântica)  $$\,\mathsf{wp}_\Sigma(\mathsf{Q})\,$$ e $$\,\mathsf{sp}_\Sigma(\mathsf{P})\,$$  caso existam em $$\,\mathcal{P}\,$$. Com quantificadores, existem sempre. Nomeadamente
>                              $$\mathsf{wp}_\Sigma(\mathsf{Q}) \;\equiv\quad\forall\,Z\,\centerdot\,\mathsf{T}[\mathsf{X}'/Z]\,\to\,\mathsf{Q}[\mathsf{X}/Z]\quad$$
>                          $$\quad\mathsf{sp}_\Sigma(\mathsf{P})\quad\equiv\quad\exists\,Z\,\centerdot\,\mathsf{T}^{-1}[\mathsf{X}'/Z]\,\land\,\mathsf{P}[\mathsf{X}/Z]\,$$
> Sem quantificadores, a existência depende da SMT $$\mathcal{T}$$.
> 
> A vantagem da  descrição do comportamento de $$\,\Sigma\,$$  por transformadores de predicados reside no facto de, em muitos casos,  evitar a introdução de novas variáveis distintas das de $$\,\mathsf{X}\,$$. Note-se que a relação $$\,\mathsf{T}\,$$ já usa as variáveis  $$\,\mathsf{X}\,$$ e um seu clone $$\,\mathsf{X}'\,$$ ;  enquanto a verificação de que    $$\mathsf{P}\,\to\,\mathsf{wp}_\Sigma(\mathsf{Q})\quad$$ou  $$\mathsf{sp}_\Sigma(\mathsf{P})\,\to\,\mathsf{Q}\quad$$é tautologia exige apenas a variável livre $$\,\mathsf{X}\,$$,  já a verificação direta de que $$\;\mathsf{P}\land\mathsf{T}\to\mathsf{Q}'\;$$ é tautologia necessita dos dois conjuntos de variáveis. 
> 
> Qualquer das metodologias apresentadas na 1ª parte deste capítulo (BMC, indução, SMT-based, etc.) usa não só estes dois conjuntos de variáveis mas também vários outros clones: um clone para cada estado que seja representado explicitamente.  Como consequência  o típico algoritmo SMT  que implementa esta verificação  tem uma dimensão do espaço de procura que é enorme. Em alternativa, em situações em que   $$\mathsf{P}\,\to\,\mathsf{wp}_\Sigma(\mathsf{Q})\quad$$e     $$\mathsf{sp}_\Sigma(\mathsf{P})\,\to\,\mathsf{Q}\quad$$não têm quantificadores,  só se usam as variáveis $$\;\mathsf{X}\;$$; isto torna  mais simples a sua verificação SMT. 
> 
> É essencial  ter em atenção que cada quantificador introduz necessariamente uma nova variável cuja presença retorna a verificação com t.p.  à formulação original  
                                            $$\quad\forall\,Z\,\centerdot\,\mathsf{P}\,\land\,\mathsf{T}[\mathsf{X}'/Z]\,\to\,\mathsf{Q}[X/Z]$$     é tautologia



| Pode-se definir em $$\,\mathcal{P}\,$$ uma pré-ordem<br>                                                $$\;A \geq B\quad$$sse     $$\, B \to A\;$$ é tautologia.  <br>Na representação em $$\,\mathsf{2}^\mathcal{X}\,$$ a pré-ordem transforma-se numa ordem parcial.                                          <br>Então, para todos $$\;\mathsf{P},\mathsf{Q}\,\in\,\mathcal{P}$$, tem-se<br>                                              $$\mathsf{wp}_\Sigma(\mathsf{Q})\,\geq\,\mathsf{P}\;\quad\text{sse}\quad\; \mathsf{Q}\,\geq\,\mathsf{sp}_\Sigma(\mathsf{P})$$<br>em que ambas as asserções acima são equivalentes a    “$$\mathsf{P}\,\land\,\mathsf{T}\,\to\,\mathsf{Q}'\quad$$é tautologia”.<br><br>Este é um exemplo de um conceito muito importante em Ciências da Computação designado por *conexão*  *de Galois* (“[Galois connection](https://en.wikipedia.org/wiki/Galois_connection)”). Neste exemplo, $$\mathsf{sp}_\Sigma\,$$ é um adjunto inferior (preserva disjunções) e $$\,\textsf{wp}_\Sigma\,$$ é um adjunto superior (preserva conjunções). |

----------

Predicados e transformadores de predicados podem ser descritos por conjuntos e funções sobre conjuntos. No que se segue, salvo ambiguidade, usaremos predicados  $$\,\mathsf{P}\,,\,\mathsf{Q}\,$$ e os símbolos $$\,P,Q\,$$para representar os conjuntos de modelos $$\;[\mathsf{P}]\,$$ e $$\,[\mathsf{Q}]\,$$;  usaremos $$\;\mathsf{T}\;$$ para o predicado que define a relação de transição em $$\;\Sigma\;$$ e usaremos $$\,T\in \mathsf{2}^{\mathcal{X}^2}\,$$ para representar a relação formada pelos modelos de $$\,\mathsf{T}\,$$.

Todo o t.p. interpreta-se por uma função   $$\,\mathsf{2}^\mathcal{X}\,\to\,\mathsf{2}^\mathcal{X}$$ ; em particular, 


    - $$\quad x\models \mathsf{wp}_{\Sigma}(\mathsf{Q}) \qquad\text{se e só se}\qquad \forall\,z\,\centerdot\,(x,z)\in {T}\,\Rightarrow\,z\in {Q}$$
    - $$\quad x\models \mathsf{sp}_\Sigma(\mathsf{P})\qquad\;\,\text{se e só se}\qquad\exists\,z\,\centerdot\, (z,x)\in {T} \;\land\;z\in {P}$$
| Note-se que, se se verificar $$\;\forall\,y\centerdot(x,y)\,\notin{T}\;$$ (i.e. $$\,x\,$$ não tem sucessores; é um estado de bloqueio), então para todo $$\,\mathsf{Q}\,$$ verifica-se $$\,x\models \mathsf{wp}_\Sigma(\mathsf{Q})$$ . |

Frequentemente é necessário introduzir duais da “weakest pre-condition” e da “strongest post-condition”  representadas respetivamente por $$\;\mathsf{pre}_\Sigma(\mathsf{Q})\;$$ e $$\;\mathsf{post}_\Sigma(\mathsf{P})\;$$; são definidas como


    - $$\quad \mathsf{pre}_\Sigma(\mathsf{Q})\;\equiv\; \neg\,\mathsf{wp}_\Sigma(\neg \mathsf{Q})\quad$$  equivalente a  
                                $$\quad x\models \mathsf{pre}_\Sigma(\mathsf{Q})\quad\text{sse}\quad \exists\,z\,\centerdot\,(x,z)\in{T}\,\land\,z\in {Q}$$
                            
    - $$\quad \mathsf{post}_\Sigma(\mathsf{P})\;\equiv\; \neg\,\mathsf{sp}_\Sigma(\neg \mathsf{P})\quad$$ equivalente a  
                                $$\quad x\models \mathsf{post}_\Sigma(\mathsf{P})\quad\text{sse}\quad \forall\,z\,\centerdot\, (z,x) \in {T}\,\Rightarrow\, z\in {P}\,$$



### Um quadro resumo das propriedades definidoras 


| Interpretando a transição  $$\;{T}\;$$ como um subconjunto de $$\,\mathcal{X}^2\,$$, para cada $$\,x\in\mathcal{X}\,$$ representamos por $$\;{T}(x)\;$$ o conjunto $$\,\{y\in\mathcal{X}\,|\,(x,y)\in{T}\}\;$$. A relação $$\;T^{-1}\;\equiv\;\{(y,x)\in\mathcal{X}^2\,|\,(x,y)\in T\}\;$$é a *inversa* de $$\,{T}\,$$. Tem-se $$\,{T}^{-1}(y)\,\equiv\,\{x\,|\,(x,y)\in{T}\}\,$$ para todo $$\,y\,$$. Para conjuntos define-se $$\,T(A)\equiv \bigcup_{x\in A}\,T(x)$$. |

|                             | existe um (∃)         | todos (∀)           |
| --------------------------- | --------------------- | ------------------- |
| sobre o estado de partida x | pre(Q): T(x) ∩ Q ≠ ∅  | wp(Q): T(x) ⊆ Q     |
| sobre o estado de chegada y | sp(P): T⁻¹(y) ∩ P ≠ ∅ | post(P): T⁻¹(y) ⊆ P |



### Propriedades dos t.p. duais
1. Para todos os  predicados $$\;\mathsf{Q}\;,\;\mathsf{P}\;$$  verifica-se
                    $$\quad\mathsf{pre}_\Sigma(\mathsf{Q})\;\;\equiv\;\;\mathsf{sp}_{\Sigma^\top}(\mathsf{Q})\quad$$e $$\quad \mathsf{post}_\Sigma(\mathsf{P})\;\;\equiv\;\;\mathsf{wp}_{\Sigma^\top}(\mathsf{P})\;$$
2. Interpretação em conjuntos:          
                        $$\;\lbrack\mathsf{pre}_\Sigma(\mathsf{Q})\rbrack\;=\; {T}^{-1}(\lbrack\mathsf{Q}\rbrack)\quad$$   e $$\quad [\mathsf{sp}_\Sigma(\mathsf{P})]\;=\;T([\mathsf{P}])$$
    em que $$\;T\,\equiv\,[\mathsf{T}]\;$$ e  $$\,T^{-1}\,$$ designa a relação inversa da  $$\,T\,$$.
3. Conexão de Galois (em conjuntos): $$\;[\mathsf{sp}_\Sigma(\mathsf{P})]\subseteq [\mathsf{Q}] \;\text{sse}\; \lbrack\mathsf{P}\rbrack\subseteq \lbrack\mathsf{wp}_\Sigma(\mathsf{Q})\rbrack$$
4. Como consequência de 1.  e 3. conclui-se que
    1.   o par $$\;(\mathsf{pre}_\Sigma\,,\,\mathsf{post}_\Sigma)\;$$ também define uma conexão de Galois ou, equivalentemente,
    2. $$\;\mathsf{pre}_\Sigma(\mathsf{Q})\,\to\,\mathsf{P}\;\;$$ é  tautologia se e só se  $$\;\mathsf{Q}\,\to\,\mathsf{post}_\Sigma(\mathsf{P})\;$$ é  tautologia.


## Alguns exemplos de transformadores de predicados 

Em “model checking” o aspeto negativo do uso de transformadores de predicados $$\,\mathsf{wp}_\Sigma\,$$ e $$\,\mathsf{sp}_\Sigma\,$$ em vez da relação de transição $$\,\mathsf{T}\,$$ é a dificuldade em os calcular a partir de $$\,\mathsf{T}\,$$.

Vendo  $$\;{P}, {Q}\,$$  como conjuntos de estados, então um transformador de predicados (t.p.) é uma função $$\;F\colon \mathsf{2}^\mathcal{X}\,\to\,\mathsf{2}^\mathcal{X}\;$$ que atua sobre tais conjuntos e dá origem a relações da forma

                                           $${Q}\;=\;F({P})\,$$

Se os conjuntos $$\,{P}\,,\,{Q}\,$$  forem descritos por predicados,  representados por $$\,\mathsf{P}\,$$ e $$\,\mathsf{Q}\,$$, 

                                $${x}\models \mathsf{P} \;\Leftrightarrow\; x\in {P}\quad,\quad  x\models\mathsf{Q}\;\Leftrightarrow\; x\in {Q}$$

então idealmente o t.p. deve ser descrito por uma transformação $$\;\phi_F\;$$ que atua sobre predicados para produzir outros predicados de tal forma que se verifica   $${Q}\,=\,F({P})\quad$$se e só se   os predicados $$\;\mathsf{Q}\;\text{e}\;\phi_F(\mathsf{P})$$ são semanticamente equivalentes.

Da definição de $$\,\mathsf{sp}_\Sigma(\mathsf{P})\;$$ e de $$\;\mathsf{wp}_\Sigma(\mathsf{Q})\;$$ vimos que 
                                           $$y \models \mathsf{sp}_{\Sigma}(\textsf{P})\quad\text{sse}\quad\exists\,x\in{P}\,\centerdot\,(x,y)\in T$$$$\quad\text{sse}\quad T^{-1}(y)\,\cap\,P\,\neq\,\emptyset$$ 
Isto é, o conjunto dos modelos de  $$\;\mathsf{sp}_\Sigma(\textsf{P})\;$$ coincide com o conjunto de todos os estados acessíveis num passo de transição a partir de um $$\;x\in{P}\;$$. Em princípio esta relação determina  a semântica de $$\;\mathsf{sp}_\Sigma(\mathsf{P})\,$$  mas, no caso geral, recorre a quantificadores.

Analogamente tem-se

                 $$x\models\mathsf{wp}_\Sigma(\mathsf{Q})\quad\Leftrightarrow\quad\forall\,y \,\centerdot\,y\in{T}(x)\Rightarrow y\in Q\quad\Leftrightarrow\quad {T}(x) \subseteq Q$$


                            

Os predicados  $$\,\mathsf{wp}_\Sigma(\mathsf{Q})\,$$ e $$\,\mathsf{sp}_\Sigma(\mathsf{P})\;$$ são predicados dependentes das fórmulas $$\,\mathsf{Q},\mathsf{P}\,$$ mas que têm a forma de fórmulas quantificadas. O transformador existe sempre, mas em geral não admite uma forma livre de quantificadores; obtê-la é um problema de eliminação de quantificadores, decidível só em certas teorias e geralmente caro. No caso geral, não é possível inferir delas um transformador de predicados que seja útil em “model checking”.



### Transição determinística  

Considere-se um FOTS onde a relação de transição, interpretada como conjunto, verifica 

                                                  $${T}\;\equiv\;\{(x,y)\,|\,y = f(x)\}$$

para alguma *função total  e computável* $$\,f\,\colon\,\mathcal{X}\,\to\,\mathcal{X}$$.
Neste caso, como conjunto,  $$\,\mathsf{wp}_\Sigma\;$$ pode-se definir facilmente  através de

                                 $$\;x\models\mathsf{wp}_\Sigma(\mathsf{Q})\quad\Leftrightarrow\quad \forall\,z\,\centerdot (z = f(x)) \,\Rightarrow\,z\models \mathsf{Q}$$ $$\quad\Leftrightarrow\quad f(x)\models \mathsf{Q}$$

A pós-condição mais forte tem de verificar

                                   $$\;x \models \mathsf{sp}_\Sigma(\mathsf{P}) \quad\Leftrightarrow\quad \exists\,z\,\centerdot\,(x = f(z)) \,\land\,z\models \mathsf{P}\;$$ 

Enquanto a primeira condição não exige  quantificadores, a 2ª condição, no caso geral, necessita desses quantificadores. Uma exceção ocorre quando $$\;\forall\,x\,\centerdot\,\exists_\mathsf{1}\,z\,\centerdot\,x = f(z)\,$$ é válido; isto é, a  função $$\,f\,$$ é invertível; agora a  condição $$\;x\models\mathsf{sp}_\Sigma(\mathsf{P})\;$$ escreve-se simplesmente como

                                 $$\;x \models \mathsf{sp}_\Sigma(\mathsf{P}) \quad\Leftrightarrow\quad f^{-1}(x)\models \mathsf{P}\;$$ 

Assumindo que $$\,\Sigma\,$$ está definido sobre um fragmento $$\,\mathcal{T}\,$$  da LPO com igualdade, então o predicado $$\,\mathsf{T}\,$$ exige variáveis livres $$\,\mathsf{X},\mathsf{X}'\,$$ e escreve-se

                                              $$\mathsf{T}\,\equiv\,(\mathsf{X}' = e(\mathsf{X}))$$

sendo $$\,e(\mathsf{X})\,$$ um tuplo de termos **em **$$\,\mathcal{T}\,$$  com a variável livre $$\,\mathsf{X}\,$$.  Note-se que nem todas as funções $$\,f\colon\mathcal{X}\to\mathcal{X}\,$$ totais e computáveis são modelos de tuplos de termos $$\,e(\mathsf{X})\,$$ em $$\,\mathcal{T}\,$$. Vamos assumir, porém, que $$\,\mathcal{T}\,$$ é tal que

    - todo o tuplo de termos $$\,e(\mathsf{X})\,$$ em $$\,\mathcal{T}\,$$ tem como modelo uma função total e computável $$\,f\,$$.
    - se $$\,f\,$$ for invertível existe  em $$\,\mathcal{T}\,$$ um tuplo de termos $$\;e^{-1}(\mathsf{X})\;$$ que tem  $$\,f^{-1}\,$$ como modelo.

Pretende-se verificar se $$\,\mathsf{wp}_\Sigma\,$$ e $$\;\mathsf{sp}_\Sigma\;$$ podem ser escritos como transformadores de predicados, preferivelmente livres de quantificadores. Para $$\;\mathsf{wp}_\Sigma(\mathsf{Q})\;$$(sempre) e $$\,\mathsf{sp}_\Sigma(\mathsf{P})\,$$ (quando $$\,f\,$$ é invertível)  pode-se realizar um t.p. sem quantificadores
                           $$\mathsf{wp}_\Sigma(\mathsf{Q})\;\equiv\;\mathsf{Q}[\mathsf{X}/e(\mathsf{X})]\qquad$$e $$\qquad \mathsf{sp}_\Sigma(\mathsf{P})\;\equiv\;\mathsf{P}[\mathsf{X}/e^{-1}(\mathsf{X})]$$
Quando $$\;f\;$$ não é invertível, em geral,  já são necessários quantificadores; pode-se escrever

                                       $$\mathsf{sp}_\Sigma(\mathsf{P})\;\equiv\quad\exists\,Z\,\centerdot\,(\mathsf{X} = e[\mathsf{X}/Z])\,\land\,\mathsf{P}[\mathsf{X}/Z]$$

**Atribuição**

A forma mais simples de transição de estados é a que, numa linguagem  imperativa, deriva do comando *atribuição* 

                                                $$\mathsf{X}\,\gets\,e(\mathsf{X})$$

A relação de transição   que a representa  é

                                             $$\mathsf{T}(\mathsf{X},\mathsf{X}')\;\equiv\quad (\mathsf{X}' = e(\mathsf{X}))$$

Portanto estamos dentro das condições que definimos atrás para a transição determinística.

**Havoc**

A transição $$\;\mathsf{havoc}(X)\;$$ é uma **atribuição não-determinística**. Essencialmente é equivalente a 
                                                                 $$\bigvee\,a\,\centerdot \;\mathsf{X} \,\gets\, a$$
A transição será  $$\;\exists\,a\,\centerdot\,(X'=a)\;$$ que é, simplesmente,   $$\,\mathtt{true}$$ .
  
A pré-condição mais fraca é

                              $$\,\mathsf{wp}_\Sigma(\mathsf{Q})\,\equiv\,\forall\,a\,\centerdot\,\;\mathsf{Q}[\mathsf{X}/a]\quad\equiv\quad\left\{\begin{array}{lr} \mathtt{true} & \text{se} \;\mathsf{Q}\;\text{é tautologia} \\ \mathtt{false} & \text{em caso contrário}\end{array}\right.$$                                                                                           

e a pós-condição mais forte é

                         $$\,\mathsf{sp}_\Sigma(\mathsf{P})\,\equiv\,\exists\,a\,\centerdot\,\;\mathsf{P}[\mathsf{X}/a]\quad\equiv\quad\left\{\begin{array}{lr}\mathtt{true} &\text{se}\;\mathsf{P}\;\text{é satisfazível} \\ \mathtt{false} & \text{em caso contrário}\end{array}\right.$$

                          
Estas fórmulas são ambas quantificadas mas são fórmulas fechadas.

**Guarda**

Em uma transição da forma
                                     $$\;\mathsf{T}(X,X')\;\equiv \mathsf{G}(X)\,\land\, \mathsf{S}(X,X')\,$$ 
o predicado $$\,\mathsf{G}\,$$ é uma “guarda” de uma outra transição $$\;\mathsf{S}\;$$.
Tem-se  $$\;\mathsf{P}\,\land\,\mathsf{T}\,\to\,\mathsf{Q}'\;\equiv\; \mathsf{P} \to (\mathsf{G}\land \mathsf{S} \to \mathsf{Q}')\;$$;      portanto

                              $$\mathsf{wp}_{\mathsf{T}}(\mathsf{Q})\;\equiv\; \mathsf{G} \to \,\mathsf{wp}_\mathsf{S}(\mathsf{Q})$$
                                

Da mesma forma 

                                $$\mathsf{sp}_\mathsf{T}(\mathsf{P})\;\equiv\;\mathsf{sp}_S(\mathsf{G}\land \mathsf{P})$$

**Escolha**

É frequente  a relação de transição de um FOTS  ser composta pela disjunção de várias outras relações de transição; vamos aqui considerar apenas duas mas obviamente esta análise estende-se para qualquer número. Temos por hipótese
                                       $$\mathsf{T}(X,X') \quad\equiv\; \mathsf{T}_0(X,X') \;\lor\;\mathsf{T}_1(X,X')$$
                                       
É vulgar designar $$\;\mathsf{T}\;$$ como a **escolha** entre  $$\;\mathsf{T}_0\;$$ e  $$\;\mathsf{T}_1\;$$ e representá-la  por   $$\mathsf{T}_0\,\|\,\mathsf{T}_1$$  .

Cada uma das transições $$\;\mathsf{T}_i\;$$, com  $$i\in\{0,1\}\,$$, pode ser vista como descrevendo um FOTS “local” que representa uma componente do sistema global. Cada uma destas componentes é definida por um par de transformadores de predicados $$\;\langle\, \mathsf{wp}_{\mathsf{T}_i}(\cdot)\,,\,\mathsf{sp}_{\mathsf{T}_i}(\cdot)\,\rangle\;$$ . Então em seguida prova-se que


>                 $$\mathsf{wp}_{\mathsf{T}}\;\equiv\; \mathsf{wp}_{\mathsf{T}_0}\,\land\,\mathsf{wp}_{\mathsf{T}_1}\qquad\text{e que}\qquad\mathsf{sp}_{\mathsf{T}}\;\equiv\; \mathsf{sp}_{\mathsf{T}_0}\,\lor\,\mathsf{sp}_{\mathsf{T}_1}$$
| **Justificação**<br>Para todo $$P,Q\;$$ ,     $$P\land\neg\,\mathsf{wp}_i(Q)\;\text{é unsat}\quad\Leftrightarrow\quad \mathsf{sp}_i(P)\land\neg\, Q\;\text{é unsat}\quad\Leftrightarrow\quad P\land\mathsf{T}_i\land\neg\,Q'\;\text{é unsat}$$.<br>Por outro lado  $$P\land\mathsf{T}\land\neg\, Q' \;\equiv\; (P\land\mathsf{T}_0\land \neg Q')\,\lor\,(P\land\mathsf{T}_1\land \neg Q')$$  e, por isso ,<br>        $$P\land\mathsf{T}\land\neg\,Q'\;\text{é unsat}\quad\Leftrightarrow\quad P\land\mathsf{T}_0\land\neg\,Q'\;\text{é unsat}\quad\mathbf{\&}\quad P\land\mathsf{T}_1\land\neg\,Q'\;\text{é unsat}$$<br>Equivalentemente<br>                                      $$P\leq\mathsf{wp}_{\mathsf{T}}(Q)\quad\Leftrightarrow\quad P\leq \mathsf{wp}_{\mathsf{T}_0}(Q)\;\; \mathbf{\&}\;\; P\leq \mathsf{wp}_{\mathsf{T}_1}(Q)$$<br>e portanto $$\;\mathsf{wp}_{\mathsf{T}} \,=\,\mathsf{wp}_{\mathsf{T}_0}\,\land\,\mathsf{wp}_{\mathsf{T}_1}$$ . <br>Também<br>                                       $$\mathsf{sp}_{\mathsf{T}}(P)\leq Q\quad\Leftrightarrow\quad\mathsf{sp}_{\mathsf{T}_0}(P)\leq Q\quad\mathbf{\&}\quad\mathsf{sp}_{\mathsf{T}_1}(P)\leq Q$$<br>o que implica $$\;\mathsf{sp}_{\mathsf{T}} \,=\,\mathsf{sp}_{\mathsf{T}_0}\,\lor\,\mathsf{sp}_{\mathsf{T}_1}$$ . |


**Composição**

Uma segunda construção para combinar duas transições $$\;\mathsf{T}_0\,$$e $$\,\mathsf{T}_1\;$$usa a noção de **composição** (ou **sequenciação**) que captura a ação de transitar $$\;\mathsf{T}_1\;$$imediatamente a seguir à transição $$\,\mathsf{T}_0$$.
Pode-se representar por $$\;\mathsf{T}\;\equiv\;\mathsf{T}_0\,;\,\mathsf{T}_1\,$$ e a sua definição é
                                       $$\mathsf{T}(X,X')\;\equiv\;\exists\,Z\,\centerdot\,\mathsf{T}_0(X,Z)\land\mathsf{T}_1(Z,X')$$
Os transformadores de predicados da composição vão ser construídos por composição dos operadores
                     $$\mathsf{sp}_{\mathsf{T}}(\mathsf{P})\;\equiv\; \mathsf{sp}_{\mathsf{T}_1}(\mathsf{sp}_{\mathsf{T}_0}(\mathsf{P}))\quad$$    e       $$\quad\mathsf{wp}_{\mathsf{T}}(\mathsf{Q})\;\equiv\; \mathsf{wp}_{\mathsf{T}_0}(\mathsf{wp}_{\mathsf{T}_1}(\mathsf{Q}))\quad$$                                     

**Invariantes indutivos**

Num FOTS com uma relação de transição $$\,\mathsf{T}\,$$ o predicado $$\,\mathsf{P}\,$$ é  invariante indutivo quando $$\,\mathsf{I}\,\to\,\mathsf{P}\,$$é tautologia  e  $$\;\mathsf{P}\land\mathsf{T}\to \mathsf{P}'\,$$ também é tautologia. Em termos de transformadores de predicados a última asserção equivale  à afirmação de que qualquer uma das seguintes asserções (equivalentes entre si) é tautologia.
                                    $$\;\mathsf{sp}_\mathsf{T}(\mathsf{P})\to \mathsf{P}\;\quad$$ ou  $$\quad\;\mathsf{P}\to\mathsf{wp}_\mathsf{T}(\mathsf{P})\;$$


## Acessibilidade e Segurança

Os quatro operadores $$\;\mathsf{wp}_\Sigma\,,\,\mathsf{sp}_\Sigma\,,\,\mathsf{wp}_{\Sigma^\top}\,,\,\mathsf{sp}_{\Sigma^\top}\,$$  podem ser aplicados múltiplas vezes e usados para caracterizar a segurança de $$\,\Sigma\,$$.  Nesta secção  vamos focar a construção no par de operadores $$\;(\mathsf{sp}_\Sigma\,,$$ $$\,\mathsf{sp}_{\Sigma^\top})\;$$mas uma análise semelhante é possível no par $$\;(\mathsf{wp}_{\Sigma^\top}\,,\,\mathsf{wp}_\Sigma)\;$$.


1. $$\;\mathsf{sp}_\Sigma^n(\mathsf{I})\;$$é a pós-condição mais forte  após a aplicação $$\,n\,$$ vezes da transição $$\,\mathsf{T}\,$$ a partir do predicado  “estado inicial” $$\,\mathsf{I}\;$$ .  
    Visto como conjunto  este predicado determina  essencialmente os estados que são acessíveis (“reachable”) a partir de $$\,\mathsf{I}\,$$ em exatamente $$\,n\,$$passos. 
    Genericamente, para qualquer predicado, $$\,\mathsf{P}\,$$, o conjunto $$\;[\mathsf{sp}_\Sigma^n(\mathsf{P})]\;$$ identifica os estados que são acessíveis em exatamente $$\,n\,$$ passos a partir de um modelo de $$\,\mathsf{P}\,$$.


2. De forma análoga, no SFOTS dual $$\,\Sigma^\top\;$$ *,* o predicado $$\;\mathsf{sp}_{\Sigma^\top}^m(\mathsf{E})\;$$ caracteriza os estados que são inseguros (“unsafe”) em exatamente $$\,m\,$$ passos. Isto é, os estados a partir dos quais algum estado de erro é $$\,\Sigma$$-acessível em $$\,m\,$$ passos. 


3. Desta forma $$\,\Sigma\,$$ é seguro se, para todo $$\,n\,$$ e todo $$\,m\,$$ os conjuntos  $$\;[\mathsf{sp}_\Sigma^n(\mathsf{I})]\;$$ e  $$\;[\mathsf{sp}_{\Sigma^\top}^m(\mathsf{E})]\;$$ não se intersectam. Formalmente $$\;\Sigma\;$$ **é seguro** se e só se
                                         $$\forall\,n\geq 0,m\geq 0\,\centerdot\;\text{SAT}(\mathsf{sp}_\Sigma^n(\mathsf{I})\;\land\;\mathsf{sp}_{\Sigma^\top}^m(\mathsf{E}))\;=\;\emptyset$$


4. É óbvio que, dadas as relações entre os vários t.p.s, esta mesma condição pode ser reescrita de várias formas. Por exemplo, dado que $$\,\mathsf{sp}_{\Sigma^\top}\,$$coincide com  $$\;\mathsf{pre}_\Sigma\,$$, poderíamos escrever a mesma noção de segurança como:  ****$$\;\Sigma\;$$ **é seguro** se e só se
                                $$\forall\,n\geq0,m\geq 0\,\centerdot\, \text{SAT}(\mathsf{sp}_\Sigma^n(\mathsf{I})\;\land\;\mathsf{pre}_\Sigma^m(\mathsf{E})) \;=\;\emptyset$$


5. Podemos também formular a segurança em termos de “menores invariantes indutivos”.
    Define-se, se existir, $$\;\mathsf{sp}_\Sigma^\ast(\mathsf{I})\,$$ como o “menor” $$\,\mathsf{R}\,$$  que verifica :$$\;\mathsf{I}\,\to\,\mathsf{R}\quad$$e $$\quad \mathsf{sp}_\Sigma(\mathsf{R})\,\to\,\mathsf{R}\;$$ são ambos tautologias. 
    Identicamente $$\;\mathsf{pre}^\ast_\Sigma(\mathsf{E})\;$$ define-se, se existir,  como o “menor” $$\;\mathsf{U}\;$$ em que $$\,\mathsf{E}\,\to\,\mathsf{U}\;$$e $$\; \mathsf{pre}_\Sigma(\mathsf{U})\,\to\,\mathsf{U}\,$$ são ambos tautologias. 
    Neste caso, se existirem $$\;\mathsf{sp}_\Sigma^\ast(\mathsf{I})\;$$ e $$\;\mathsf{pre}^\ast_\Sigma(\mathsf{E})\;$$, então $$\;\Sigma\;$$ é seguro se e só se
    
                                                          $$\;\mathsf{sp}_\Sigma^\ast(\mathsf{I})\;\land\;\mathsf{pre}_\Sigma^\ast(\mathsf{E})\qquad$$é insatisfazível

Esta condição é  necessária e suficiente para segurança mas o seu uso exige que seja possível determinar os predicados $$\;\mathsf{sp}_\Sigma^\ast(\mathsf{I})\;$$e $$\;\mathsf{pre}_\Sigma^\ast(\mathsf{E})\;$$. Na maior parte dos casos, calcular estes predicados exatamente via  a definição (como disjunções infinitas ou como pontos fixos)  não é computável em domínios infinitos e, mesmo em domínios finitos, é muito difícil.  
Por isso os algoritmos que se baseiam nestes critérios usam sobre-aproximações  $$\,\mathsf{R}\,$$ e $$\,\mathsf{U}\;$$ para respetivamente $$\;\mathsf{sp}_\Sigma^\ast(\mathsf{I})\;$$ e $$\;\mathsf{pre}_\Sigma^\ast(\mathsf{E})\;$$  e testam a condição
                                                                     $$\;\mathsf{R}\,\land\,\mathsf{U}\quad$$é insatisfazível
Nestas sobre-aproximações  força-se que sejam  tautologias   $$\;\mathsf{I}\,\to\,\mathsf{R}\;$$,  $$\;\mathsf{E}\,\to\,\mathsf{U}\;$$   e que os predicados $$\;\mathsf{R}\;\text{e}\;\mathsf{U}\;$$ sejam indutivos;  esta última condição exige que $$\;\mathsf{sp}_\Sigma(\mathsf{R})\,\to\,\mathsf{R}\;$$ e $$\,\mathsf{pre}_\Sigma(\mathsf{U})\,\to\,\mathsf{U}\,$$ sejam tautologias.  
A condição testada é apenas suficiente para segurança e é tanto mais “precisa” quanto “menores” forem $$\,\mathsf{R}\,$$ e $$\,\mathsf{U}\,$$. Pode-se verificar que a condição “$$\,\mathsf{R}\land\mathsf{U}\;$$é insatisfazível” é suficiente para segurança mesmo que apenas um dos predicados $$\;\mathsf{R}\,\text{ou}\,\mathsf{U}\;$$ seja indutivo; neste caso só o predicado que for indutivo é majorante do respetivo ponto fixo.


# Control Flow Automata (CFA)


CFA’s  segundo “[Conditional Model Checking](https://arxiv.org/html/1109.6926v1)”, *Beyer D. et al*  (aqui referidos como “clássicos”) são modelos de programas imperativos, usados em alternativa aos FOTS em circunstâncias em que estes últimos são  de difícil aplicação. Para isso introduzem modelos de uma forma estruturada, colocam o controlo do fluxo explicitamente no centro de cada modelo e, como consequência,  tornam mais simples  codificar grandes porções de código. Apesar de, em princípio, qualquer CFA clássico poder ser descrito por um FOTS, o CFA introduz uma disciplina que torna viável lidar com sistemas dinâmicos de dimensões realistas.

Neste curso pretende-se estender a noção de CFA clássico para algo que designaremos, à falta de melhor alternativa, também como CFA. A generalização é feita em dois sentidos:

- Extensão para além dos programas imperativos. Pretende-se modelar sistemas dinâmicos genéricos usando muitos dos conceitos dos autómatos híbridos (a.h.); nomeadamente tempo tanto discreto como contínuo (e neste caso não têm correspondente FOTS), a noção de “local” (modo nos a.h.) como subsistema com comportamento próprio, e fluxo   guiado/controlado por “guardas”.
- Ênfase na composicionalidade.  A dinâmica está atomicamente  distribuída pelos “locais” e pelas “guardas”; regras de composição permitem construir a dinâmica global do sistema a partir dessas dinâmicas atómicas.

 
Um FOTS é um **modelo global** de comportamento: através de uma relação de transição e de estados iniciais fica completamente determinado o comportamento global do sistema.  
Ao invés um CFA é um **modelo local** do comportamento: o sistema é formado por um conjunto de **locais** (também designados por **modos** de funcionamento) com comportamento próprio que, em grande medida, é  independente do comportamento dos restantes locais. 

Nomeadamente, o modelo de comportamento usado num local pode ter uma natureza completamente distinta do modelo usado noutro local. Por exemplo um local pode usar um  FOTS e, no mesmo sistema, outro local usar transformadores de predicados.

O comportamento de um local só não é completamente independente do comportamento nos restantes locais porque, dentro de um mesmo sistema, os locais precisam de trocar informação. Para tal, o sistema define um conjunto de **variáveis do sistema** que  podem ser lidas e escritas por cada um dos seus locais.

Uma noção central num CFA, como o nome indica, é a noção de **controlo**. O controlo num CFA é um atributo booleano de local que, em cada instante, privilegia um e só um local do sistema:  em cada instante um e só um local tem controlo do sistema.
Só quando um local tem controlo do sistema ele pode ler ou escrever nas variáveis do sistema. 

O **controlo de fluxo** é determinado por um conjunto de regras, designadas por **guardas,**  que definem em que circunstâncias um local transfere o controlo para outro;  “guardas” podem  ler as variáveis do sistema mas, ao contrário dos ramos em CFA clássicos, não podem nelas escrever .

A descrição do controlo de fluxo assume a forma de um multigrafo orientado tal que:

    1. os nodos  identificam-se com os locais do sistema,
    2. os ramos representam a relação “transferência de controlo”:  um ramo
                                                                  $$\,\ell\,\stackrel{s}{\to}\,\ell'\,$$    
        representa a transferência de controlo do local $$\,\ell\,$$para o local $$\,\ell'\,$$ que ocorre só quando a condição $$\,s\,$$ se verifica no presente estado. Vários ramos com a mesma origem  $$\,\ell\,$$ e com guardas que são satisfeitas no presente estado, representam sob o ponto de vista de $$\,\ell\,$$, uma escolha não determinística de locais para onde o controlo é transferido.  Uma visão alternativa da mesma semântica, considera  os vários ramos com o mesmo destino $$\,\ell'\,$$ e satisfazendo as respetivas guardas no presente estado;   agora, sob o ponto de vista de $$\,\ell'\,$$,   o conjunto de ramos identifica  os locais $$\,\ell\,$$ de onde não é proibido assumir que o controlo proveio. Vista da origem, a escolha não determinística dos ramos traduz-se numa conjunção do que é fornecido aos diversos destinos (todos os ramos “ativos” têm de garantir a pós-condição do destino respetivo). Sob o ponto de vista do destino, as pré-condições em $$\,\ell'$$ são a disjunção do que chega em cada ramo (i.e. a pós-condição da origem e a guarda respetiva).

As **regras de composição**  estabelecem a forma como o comportamento global é construído a partir dos comportamentos locais e das guardas e como esse comportamento se traduz em formalizações que podem ser verificadas numa SMT. 
O tipo dessas formalizações depende crucialmente do modo como o comportamento de cada local é descrito. Um exemplo típico é o de um sistema em que o comportamento do local $$\,\ell\,$$ é descrito por um transformador de predicados $$\,\mathsf{tp}_\ell$$ e o local tem associados dois predicados: uma pré-condição $$\,\mathsf{P}_\ell\,$$ e uma pós-condição $$\,\mathsf{Q}_\ell$$. O t.p. $$\,\mathsf{tp}_\ell$$  estabelece uma ligação dentro do mesmo local entre estas duas condições. Por seu  lado, cada ramo   $$\,\ell\,\stackrel{s}{\to}\,\ell'\,$$  do controlo de fluxo, estabelece uma ligação entre  a pós-condição de $$\,\ell\,$$, a guarda $$\,s\,$$ e a pré-condição de $$\,\ell'\,$$.  Os  vários $$\,\mathsf{P}_\ell$$ e $$\,\mathsf{Q}_\ell\,$$ são incógnitas, descritas por variáveis de predicado,  e as relações $$\,\mathsf{tp}_\ell\,$$assim como as ligações $$\;\ell\,\stackrel{s}{\to}\,\ell'\;$$ determinam um conjunto de condições verificáveis na SMT de base.


| Veremos na 3ª parte deste capítulo mecanismos (como as CHC’s, “Constrained Horn Clauses”) que permitem formalizar rigorosamente estas condições. |


Como foi dito atrás, os diversos modelos de comportamento $$\,\mathcal{M}_\ell\;$$ dependem do tipo de CFA e mesmo dentro do mesmo CFA, a natureza do modelo depende do local $$\;\ell\;$$. Exemplos típicos são sistemas de transições, transformadores de predicados e, para o caso em que o CFA descreve um *autómato híbrido*, sistemas de equações diferenciais.

Sobre este modelo genérico várias outras componentes podem ser adicionadas formando-se assim classes dentro da classe de modelos CFA. Nomeadamente,


    - A subclasse **Timed Control Flow Automata** (TCFA) acrescenta ao modelo CFA  uma representação explícita do **tempo**. Essa representação é feita através de  uma variável de sistema $$\;t\;$$, real ou inteira, que pode ser manipulada  desde que tenha sempre valores não-negativos e nunca seja decrementada. O comportamento $$\,\mathcal{M}_\ell\,$$ determina no local $$\,\ell\,$$ a forma como $$\,t\,$$ evolui. Nomeadamente a variável  $$\;t\;$$ permite medir a duração do intervalo de tempo em que cada local tem controlo  (por exemplo guardando à entrada de $$\,\ell\,$$ o valor $$\,\tau \gets t\;$$; a duração do controlo de $$\,\ell\,$$ é $$\,t-\tau$$) e, com essa informação, proceder  a uma transferência desse controlo.


    - A subclasse **Sync Control Flow Automata** (SyncCFA) acrescenta ao modelo CFA  a noção de **evento** e a **sincronização** de eventos  entre dois ou mais CFA’s. Essencialmente nestes sistemas estende-se a noção de produto, herdada da sincronização de autómatos híbridos. Aqui a condição de unicidade do controlo aplica-se individualmente a cada componente e as variáveis do sistema são também específicas de cada componente. 
        Os eventos são marcas que podem ser associadas aos ramos do multigrafo “controlo de fluxo” e são a única informação partilhada pelas componentes; cada ramo  pode ter zero ou mais eventos associados;  o mesmo evento pode estar associado a vários ramos.  Ramos sem eventos executam de forma independente, intercalada com outras componentes. Um ramo com vários eventos é equivalente a vários ramos com um evento cada.
        Quando dois (ou mais) CFA’s   que partilham os mesmos eventos estão agrupados, o controlo de fluxo dentro de cada um é condicionado por **regras de sincronismo**; em  particular uma determinada transferência de controlo dentro de um dos CFA’s, marcada como um evento $$\;e\;$$, só ocorre se também ocorrer, em cada um dos  CFA’s que contenha $$\,e\,$$,  transferências de controlo marcadas com o mesmo evento.

Resumidamente a descrição de um CFA genérico compreende:

    1. A SMT $$\;\mathcal{T}\;$$ usada na verificação de propriedades temporais, na definição das guardas, e na definição de comportamentos locais,
    2. O conjunto finito $$\;\mathcal{L}\;$$ dos locais do sistema, e o “local inicial” que tem controlo do sistema no instante zero.
    3. O conjunto $$\;\mathcal{V}\;$$ das variáveis do sistema,
    4. O controlo de fluxo descrito pelo multigrafo referido atrás; nomeadamente faz parte da descrição do controlo de fluxo a definição das “guardas” associadas a cada ramo.
    5. O modelo de comportamento $$\,\mathcal{M}_\ell\;$$ associado a cada local $$\;\ell\in\mathcal{L}\,$$. Noções como estados iniciais admissíveis,  estados de erro e potenciais invariantes fazem parte de $$\,\mathcal{M}_\ell\,$$.
    6. As regras de composição.
# Exemplo
## Multiplicação de inteiros com  erros 

Neste exemplo quase todos os locais podem ser identificados com valores específicos de um “program counter” $$\;\mathsf{pc}\;$$num programa imperativo que implemente este algoritmo. 
A única exceção é o local  $$\;\mathsf{error}\;$$que não pode ser identificado com nenhuma posição do $$\;\mathsf{pc}\;$$ porque o erro de “overflow”  pode surgir de várias formas. Isso é por si uma indicação de que um FOTS clássico captura mal o comportamento deste sistema.

| **Nota**<br>Obviamente, neste caso particular, onde o “overflow” só ocorre em duas situações distintas, é possível escrever um sistema de transições que descreva essas situações particulares.<br>Não seria “limpo” porque requer inventar um valor fictício  do $$\;\mathsf{pc}\;$$que represente o estado de erro.<br>Para além do facto, já de si negativo, de  destruir o significado próprio do $$\;\mathsf{pc}\;$$ atribuindo-lhe valores fictícios (fonte provável de “bugs” futuros),  este esforço é, em grande medida, inútil porque não se tem a certeza que essas são as duas únicas situações onde aparece o “overflow”. |

Por isso se optou por uma descrição do comportamento através de predicados e transformadores de predicados.

Vamos considerar  o exemplo da multiplicação de dois inteiros positivos. O algoritmo foi modelado por um CFA (“control flow automaton”) sumariamente descrito no seguinte diagrama.


![](https://paper-attachments.dropboxusercontent.com/s_1562376E63EDCC265F35577DF1C34F9DF37F938151FDBDFFBFC6409E7F23005F_1669924804269_multiplicacao-overflow-2.png)


O diagrama introduz alguma notação adicional em relação à apresentada anteriormente:

1. Todos os locais estão identificados com um nome
2. A inicialização é descrita por uma transição $$\;\mathsf{havoc}\;$$, que atribui às variáveis $$\,a,b\,$$ valores arbitrários, seguida de uma guarda $$\;(x=a)\land(y=b)\land(z=0)\,$$que deixa passar apenas valores apropriados para o nosso problema.

Nestas circunstâncias pode-se assumir que o predicado dos estados iniciais  é

                                           $$\mathsf{I}\;\equiv\;\mathtt{True}$$

e que o 1º estado de acessibilidade $$\;\mathsf{sp}(\mathsf{I})\;$$  é determinado por este comando  $$\;\mathsf{havoc}\;$$ seguido pela guarda referida. Por isso 
                                     $$\mathsf{sp}_{\mathsf{havoc}(a,b)}(\mathsf{I}) \;=\;\mathtt{True}$$

Todos os restantes locais  vão ser representados por pré-condições mais fracas. Nomeadamente o local $$\;\mathsf{do}\,$$ é representado por $$\;\mathsf{wp}(\mathsf{do})\;$$. O sistema será seguro quando é tautologia

                                                     $$\;\mathsf{sp}_{\mathsf{havoc}(a,b)}(\mathsf{I})\,\land\,(x=a)\land(y=b)\land(z=0)\;\to\,\mathsf{wp}(do)\quad$$

ou, equivalentemente, é insatisfazível

                       $$(x=a)\land(y=b)\land(z=0)\,\land\,\neg \mathsf{wp}(\mathsf{do})\quad$$

Podemos associar um predicado a cada um dos locais do sistema de acordo com os seguintes princípios.

    - Ao local $$\;\mathsf{system}\,$$ associamos a condição de segurança atrás referida
    - Aos restantes locais com exceção de $$\;\mathsf{stop}\;$$e $$\;\mathsf{error}\;$$associamos a pré-condição mais fraca.
    - Aos locais $$\;\mathsf{stop}\;$$e $$\;\mathsf{error}\;$$associamos predicados constantes que vão depender do tipo de problema que vamos tentar modelar. 

Ignorando por momentos a semântica pode-se escrever num sistema de equações

----------

$$\mathsf{system}\;=\;(x=a)\land(y=b)\land(z=0)\,\to\,\mathsf{do}\,$$
$$\mathsf{do}\;=\;(y=0\,\to\,\mathsf{stop})\,\land\,(y\neq 0 \land \mathit{even}(y)\,\to\,\mathsf{even})\,\land\,(y\neq 0\land\mathit{odd}(y)\,\to\,\mathsf{odd})$$
$$\mathsf{even}\;=\;\mathsf{wp}_\mathsf{even}((\mathsf{overflow}\to\mathsf{error})\,\land\,(\neg\,\mathsf{overflow}\to\mathsf{do}))$$
$$\mathsf{odd}\;\,=\;\mathsf{wp}_\mathsf{odd}((\mathsf{overflow}\to\mathsf{error})\,\land\,(\neg\,\mathsf{overflow}\to\mathsf{do}))$$

----------

Os predicados $$\,\mathsf{overflow}, \mathsf{stop}, \mathsf{error}\,$$ não estão especificamente definidos nesta especificação; devem ser concretizados de acordo com as particularidades de cada  sistema.

Se for possível encontrar uma solução para este sistema de equações então pode-se resolver vários tipos de problemas. Por exemplo

    - Para determinar, se o programa terminar, termina sempre em erro faz-se $$\;\mathsf{error}\,\equiv\,\mathsf{True}\,$$ e  $$\;\mathsf{stop}\,\equiv\,\mathtt{False}\,$$ e verifica-se se $$\;\mathsf{system}\;$$ é tautologia.
    - Para determinar se o programa está *parcialmente* *correto*, (i.e. se terminar,  calcula em $$\,z\,$$ o valor  $$\,a*b\,$$  e não termina em “overflow”)  basta introduzir  $$\;\mathsf{stop}\,\equiv\,(z = a*b)\,$$ e $$\;\mathsf{error}\,\equiv\,\mathtt{False}\,$$ e verificar se $$\;\mathsf{system}\;$$ é tautologia.

Esta formalização porém tem dois problemas:

1. É necessário encontrar uma solução para o sistema de equações. Uma tal solução pode ser obtida de forma iterativa através das definições recursivas
----------

$$\mathsf{system}_n\;\equiv\; (x=a)\land(y=b)\land(z=0)\,\to\,\mathsf{do}_n\,$$
$$\mathsf{do}_n\quad\equiv\;(y=0\,\to\,\mathsf{stop})\,\land\,(y\neq 0 \land \mathit{even}(y)\,\to\,\mathsf{even}_n)\,\land\,(y\neq 0\land\mathit{odd}(y)\,\to\,\mathsf{odd}_n)$$
$$\mathsf{even}_n\;\equiv\;\mathsf{wp}_\mathsf{even}((\mathsf{overflow}\to\mathsf{error})\,\land\,(\neg\,\mathsf{overflow}\to\mathsf{do}_{n-1}))$$
$$\mathsf{odd}_n\;\,\equiv\;\mathsf{wp}_\mathsf{odd}((\mathsf{overflow}\to\mathsf{error})\,\land\,(\neg\,\mathsf{overflow}\to\mathsf{do}_{n-1}))$$

----------
    É importante notar que, aqui, temos um sistema de definições enquanto anteriormente tínhamos um sistema de equações.  O sistema é inicializado com

           $$\mathsf{do}_0 \;\equiv\;\mathtt{True}$$

    e iterativamente usa as definições acima para produzir uma sequência decrescente de  sucessivos valores $$\,\{\mathsf{do}_n\}\,$$; o algoritmo  termina com sucesso se for possível  construir  $$\,\mathsf{do}_n\,$$ tal que      $$\mathsf{do}_n \,\to\,\mathsf{do}_{n+1}$$ é tautologia. Isto é equivalente a calcular **o maior ponto fixo** da definição recursiva acima.


    É evidente que se pode sempre assumir uma abordagem análoga à do BMC, colocando um limite ao número de iterações efetuadas. Com isto o algoritmo termina sempre; porém  tem todos os problemas inerentes a um BMC com um pequeno limite.
    
2. O 2º problema é potencialmente mais sério e deriva do modo como o CFA usa o comando $$\;\mathsf{havoc}(a,b)\;$$. Operacionalmente o comando $$\,\mathsf{havoc}(a,b)\,$$ gera dois inteiros arbitrários; porém só existe garantia que o algoritmo termina quando ocorrer $$\;(b\geq 0)\;$$. Por isso o CFA  produz  um programa parcialmente correcto que não é correcto.
    A solução passa pela modificação da guarda no ramo  $$\,\mathsf{system}\,\to\,\mathsf{do}\,$$ para 
                                $$(x=a)\,\land\,(y=b)\,\land\,(z=0)\,\land\,(a\geq 0)\,\land(b\geq 0)$$
    A condição $$\,(a\geq 0)\,$$ , apesar de não ser nececessária para a garantia de terminação, está incluída porque a especificação do problema fala de “inteiros positivos”.

          

# CFA’s e Transformadores de Predicados

Essencialmente um CFA é descrito por um grafo orientado $$\,\langle \mathcal{N},\mathcal{E}\rangle\,$$ em que os vértices/nodos $$\,a\in\mathcal{N}\,$$ representam os locais  e os ramos $$\,e\in\mathcal{E}\,$$ representam as “guardas”  (ou “switches”). 
Existe um nodo marcado com $$\,\mathsf{system}\,$$ que é o único local que não tem antecessores. Existem nodos que são “sinks” (i.e. não têm sucessores) que são marcados com os identificadores $$\,\mathsf{stop}\,$$ ou $$\,\mathsf{error}\,$$. A verificação da correção é estabelecida por um predicado $$\,\varphi\,$$ designado por *pós-condição*  que tem de ser válida nos locais $$\,\mathsf{stop}\,$$.

O comportamento do sistema  é gerado a partir de interpretações  semânticas dos locais segundo uma de duas abordagens:  orientada às pré-condições e orientada às pós-condições.


**Representação orientada às pré-condições mais fracas (**$$\{\mathsf{wp}_a\}_{a\in \mathcal{N}}\,$$**)**


1. Cada nodo $$\,a\in\mathcal{N}\,$$ tem associado um transformador de predicados  $$\,\mathsf{wp}_a\,$$ e cada ramo  $$\,(a,b)\in \mathcal{E}\,$$ tem associado um predicado $$\,\mathsf{sw}_{a,b}\,$$.
2. O comportamento global do sistema é determinado por um conjunto de  predicados $$\,\{Q_a\}_{a\in \mathcal{N}}\,$$, um para cada local $$\,a\,$$. O predicado $$\,Q_a\,$$ é a pós-condição associada ao fluxo de informação do local $$\,a\,$$. 
3. As relações que determinam o comportamento descrevem a relação entre cada local $$\,a\,$$e os seus sucessores (locais que são destino de ramos com origem em $$\,a\,$$).  Para todo $$\,a\,$$ são tautologias
                                  $$Q_a \,\equiv\,\bigwedge_{b\in \mathsf{succ}(a)}\,\mathsf{sw}_{a,b}\,\to\,\mathsf{wp}_b(Q_b)$$
                        
![](https://paper-attachments.dropboxusercontent.com/s_1562376E63EDCC265F35577DF1C34F9DF37F938151FDBDFFBFC6409E7F23005F_1730738703577_wp_cfa.png)

4. O grafo tem uma única fonte (local sem antecessores) marcada como $$\,\mathsf{system}\,$$ e  sem condições iniciais; por isso verifica-se se é tautologia
                                       $$\mathtt{True}\,\to\,\mathsf{wp}_\mathsf{system}(Q_\mathsf{system})\quad\leftrightarrow\quad\mathsf{wp}_\mathsf{system}(Q_\mathsf{system})$$
5. A configuração pode ser usada para verificar a **correção**  ou a **segurança** do sistema**.** 
    1. A correção é definida por uma pós-condição $$\,\varphi\,$$ que tem que ser válida nos locais $$\,\mathsf{stop}\,$$. Adicionalmente nos locais $$\,\mathsf{error}\,$$ não devem existir estados acessíveis. Axiomaticamente estabelecem-se as condições
                                                 $$Q_\mathsf{stop} \,\equiv\,\varphi\qquad,\qquad Q_\mathsf{error}\,\equiv\,\mathtt{False}$$
        e a verificação de que $$\;\mathsf{SAT}(\neg\,\mathsf{wp}_\mathsf{system}(Q_\mathsf{system}))$$  é  **unsat**.
    2. A insegurança é detetada pela verificação da condição de inicialização quando os locais terminais são 
                            $$Q_\mathsf{stop}\,\equiv\,\mathtt{True}\qquad,\qquad Q_\mathsf{error}\,\equiv\,\mathtt{False}$$ 
        e o sistema é inseguro se e só se $$\;\mathsf{wp}_\mathsf{system}(Q_\mathsf{system})\;$$ *não é*  tautologia.

**Representação orientada às pós-condições mais fortes**

1. Cada nodo $$\,a\in\mathcal{V}\,$$ tem associado um transformador de predicados  $$\,\mathsf{sp}_a\,$$ e cada ramo  $$\,(a,b)\in \mathcal{E}\,$$ tem associado um predicado $$\,\mathsf{sw}_{a,b}\,$$.
2. O comportamento global do sistema é determinado por um conjunto de  predicados $$\,\{P_a\}_{a\in \mathcal{N}}\,$$, um para cada local $$\,a\,$$. O predicado$$\,P_a\,$$ é a pré-condição  do fluxo de informação associado a $$\,a\,$$. 
3. As relações que determinam o comportamento descrevem a relação entre cada local $$\,a\,$$e os seus antecessores (locais que são origem de ramos que terminam em $$\,a\,$$).  Para todo $$\,a\,$$ são tautologias
                                  $$P_a \,\equiv\,\bigvee_{b\in \mathsf{pred}(a)}\,\mathsf{sw}_{b,a}\,\land\,\mathsf{sp}_b(P_b)$$
                    
![](https://paper-attachments.dropboxusercontent.com/s_1562376E63EDCC265F35577DF1C34F9DF37F938151FDBDFFBFC6409E7F23005F_1730738757943_sp_cfa.png)

4. O grafo tem uma única fonte (local sem antecessores) marcada como $$\,\mathsf{system}\,$$ e  condições iniciais definidas por um predicado $$\,\mathsf{init}\,$$ que coincide com $$\;\mathtt{True}\;$$ dado que o local $$\;\mathsf{system}\;$$ não tem antecedentes. Temos assim  
                                       $$P_\mathsf{system} \,\equiv\,\mathsf{True}\,$$


5. A configuração pode ser usada para verificar a **correção**  ou a **segurança** do sistema**.** 
    1. A correção é definida por uma pós-condição $$\,\varphi\,$$ que tem que ser válida nos locais $$\,\mathsf{stop}\,$$. Adicionalmente nos locais $$\,\mathsf{error}\,$$ não devem existir estados acessíveis. Axiomaticamente estabelecem-se as tautologias
                                                 $$P_\mathsf{stop} \,\to\,\varphi\qquad,\qquad P_\mathsf{error}\,\to\,\mathtt{False}$$
    2. A insegurança é detetada pela verificação da condição de inicialização quando
                                           $$\quad P_\mathsf{error}\;$$é satisfazível 


----------

O problema computacional está na determinação do vetor de predicados $$\,\mathcal{P} \equiv \{P_a\}_{a\in\mathcal{N}}$$  ou $$\,\mathcal{Q} \equiv \{Q_a\}_{a\in\mathcal{N}}$$ . Uma abordagem consiste em definir   variáveis de predicados $$\,\mathsf{Q}_a\,$$ (ou $$\,\mathsf{P}_a\,$$) , considerar as várias equivalências como “equações” e, tal como no exemplo anterior , calcular uma solução como um ponto fixo. 


    A completar
# “Property Directed Reachability (PDR)”

O algoritmo PDR (“property directed reachability”) é um algoritmo eficiente para verificar segurança em sistemas dinâmicos. Foi introduzido inicialmente na verificação de “hardware” , em FSM, mas tem sido generalizado para outras formas de sistemas dinâmicos nomeadamente autómatos híbridos e programas imperativos ambos objeto dos próximos capítulos.

Neste capítulo vamos apresentar o PDR na sua forma original  o que requer alguma adaptação da terminologia e notação que introduzimos anteriormente.

Em primeiro lugar o nosso sistema dinâmico é descrito por um SFOTS

                                                  $$\Sigma \,\equiv\, \langle\,\,{X}\,,\,\mathsf{I}\,,\,\mathsf{T}\,,\,\neg\mathsf{P}\,\rangle\,$$

em que as variáveis têm  sempre  domínios finitos.  Sem perda de generalidade vamos considerar que as variáveis $$\,{X} \,=\,\langle\,x_1\,,\,\cdots\,,\,x_n\,\rangle\,$$ são todas booleanas. 
Neste modelo a propriedade $$\;\mathsf{P}\;$$ designa os “bons estados”: assim a  propriedade de erro é a negação $$\;\neg\,\mathsf{P}\,$$.

Assim 

    - o espaço de estados é o domínio $$\,\mathcal{B}_n\,\equiv\;\{0,1\}^n\,$$.  
    - os predicados $$\,\mathsf{I}\,,\,\mathsf{P}\,$$ e quaisquer outros predicados unários, são descritos por fórmulas proposicionais nas variáveis $$\,X\,$$. 
    - a relação de transição $$\,\mathsf{T}\,$$  é descrita por uma fórmula proposicional nas variáveis $$\,X,X'\,$$. 

Para representar estes estados, predicados e relações vamos recuperar a terminologia das formas normais fazendo algumas alterações:


    - Um *literal* é uma variável $$\,x_i\,$$ ou a sua negação $$\,\neg\,x_i\,$$
    
    - *Cláusulas conjuntivas* (conjunções de literais) são aqui designadas por **cubos,** enquanto que as cláusulas disjuntivas (disjunções de literais) são designadas simplesmente por **cláusulas**. Note-se que uma cláusula é sempre a negação de um cubo.
    
    - *Conjuntos de cubos interpretados disjuntivamente* (DNF’s) são designados por **frames.**
    
    - *Conjuntos de cláusulas interpretados conjuntivamente* (CNF’s) são designados como **propriedades**.

**Notas sobre “cubos” como extensões de estados**


1. Um **cubo determinado** é um conjunto de literais onde ocorrem todas as variáveis. Se faltarem variáveis ao conjunto de literais este designa-se por **cubo indeterminado.**
    Cada estado é representado por um cubo determinado. Cubos indeterminados representam conjuntos de estados.
| **Exemplo**<br><br>1. Considere-se $$\,n=8\,$$ e o estado $$\,s\,\equiv\,\mathtt{(\,0,1,1,0,1,1,1,0\,)}\,\in \mathcal{B}_8\,$$. <br><br>Este é o único estado que satisfaz  (“é modelo de”)  o cubo<br>                                     $$s\,\equiv\,\neg x_0 \land x_1\land x_2\land \neg x_3\land x_4\land x_5\land x_6\land \neg x_7\,$$<br><br>2. A fórmula     $$\alpha\,\equiv\,x_1\land x_2\land \neg x_3\land x_5\,$$     é um  cubo indeterminado que representa o conjunto de $$16$$ estados<br><br>                             $$\alpha \,\equiv\,\{\, (\,x_0,1,1,0,x_4,1,x_6,x_7\,)\;\;|\;\; x_0,x_4,x_6,x_7\in \{0,1\}\,\}$$ |

                              
                          

2. O cubo     $$\alpha\,\equiv\,x_1\land x_2\land \neg x_3\land x_5\,$$    pode também ser representado por um único vetor de $$n$$ componentes pertencentes ao conjunto de três símbolos  $$\,\{0,1,?\}$$  

                                                 $$\mathtt{(\,?,1,1,0,?,1,?,?\,)}$$

    Aqui, na chamada *lógica de três símbolos*,  $$\,?\,$$ é o símbolo escolhido para designar  “valor indeterminado”.
3.  Genericamente cada cubo  na lógica de dois símbolos $$\,\{0,1\}\,$$   é representado por um único vetor  $$\,c \,\in\,\{0,1,?\}^n\,$$.  Nessa notação, um estado é o caso particular de um cubo em que nenhuma componente é o  símbolo $$\,?\,$$.        
    Um cubo  onde ocorrem  $$\,m\leq n\,$$ variáveis  descreve um  conjunto de estados  com  $$\,2^{n-m}\,$$  elementos.


4. A semântica da lógica de três valores aumenta a da lógica proposicional de dois valores com as seguintes regras pertinentes ao  símbolo $$\,?\,$$:

           $$? \land a\;=\;\left\{\begin{array}{ccc}0 & \text{se} & a = 0\\ ? &\text{se}& a\neq 0 \end{array}\right.\quad$$,     $$\quad ? \lor a\;=\;\left\{\begin{array}{ccc}1 & \text{se} & a = 1\\ ? &\text{se}& a\neq 1 \end{array}\right.$$ , $$\quad\neg ? = ?$$          


**Problema da expansão  de um cubo.**


> Um cubo $$\,\tilde{c}\,$$ que se obtém do cubo $$\,c\,$$ eliminando alguns  literais diz-se uma **expansão** de $$\,c\,$$.  Isto ocorre quando $$\,c,\tilde{c}\,$$ são ambos cubos e   $$\,c \to \tilde{c}\,$$ é uma tautologia.

 
 O *problema da expansão*  de um cubo $$\,c\,$$ limitado a uma proposição $$\,f\,$$  define-se como
 

> Dados uma fórmula proposicional $$\,f\,$$ e um cubo $$\,c\,$$ tal que $$\,c \land \neg\,f\,$$ é insatisfazível (equivalente, em conjuntos, a $$\;c \subseteq f\;$$)  determinar uma expansão maximal $$\,\tilde{c}\,$$tal que       $$\,\tilde{c}\,\land\, \neg\,f$$  seja insatisfazível (equivalente, em conjuntos de estados, a $$\,\tilde{c} \subseteq f\,$$).


| Um algoritmo trivial para resolver aproximadamente este problema consiste em percorrer todos os literais de $$\,c\,$$até encontrar um que, eliminado de $$\,c\,$$, produza uma expansão $$\,\tilde{c}\,$$ tal que  $$\,\tilde{c}\land \neg f\,$$  é insatisfazível. Substitui-se $$\,c\,$$ por $$\,\tilde{c}$$ e o processo repete-se iterativamente, retirando literais  até que nenhuma remoção mantenha $$\,\tilde{c}\land \neg f\,$$ insatisfazível. <br><br>Este não é o melhor algoritmo de expansão. Existem melhores algoritmos e a eficiência do PDR  depende fortemente do algoritmo de expansão usado. No entanto detalhes desses algoritmos não são relevantes nesta fase introdutória . |




**Algoritmo PDR**

Neste algoritmo  PDR  usam-se as seguintes representações


    - os predicados $$\,\mathsf{I}\,$$ e $$\,\mathsf{P}\,$$ são descritos por propriedades (conjunções de cláusulas).
    Consequentemente  $$\,\neg\,\mathsf{I}\,$$ e $$\,\neg\,\mathsf{P}\,$$ são descritas  por “frames”  (disjunções de cubos).
    
    - A relação de transição é descrita por uma “frame” nas variáveis $$\,X,X'\,$$.


    - Nenhum estado inicial é inseguro; isto é, a proposição $$\,\mathsf{I}\to \mathsf{P}\,$$ é uma tautologia.


O algoritmo  cria e gere uma sequência de conjuntos de cubos $$\,\langle F_0\,,\,F_1\,,\,\cdots\,F_N\rangle\,$$ que devem verificar , para todo $$\,k\,\leq N\,$$ ,  as seguintes condições:


1. Nenhum estado $$\,s\in c\,$$ de qualquer cubo $$\,c\in F_k\,$$  pode ser alcançado, a partir de um
    estado inicial,  em  $$\,k\,$$ ou menos passos de transição.  Tais estados dizem-se **bloqueados** pela “frame”  $$\,F_k$$. 
    
2. Para $$\,k\neq N\,$$, todo o estado inseguro $$\,s\in \neg\mathsf{P}\,$$ pertence a algum cubo da “frame” $$\, F_k\,$$; equivalentemente,     $$\,\neg\mathsf{P}\to F_k\,$$ tem de ser uma tautologia.
    
3. São tautologias   $$\,F_0 \;\leftrightarrow\; \neg\,\mathsf{I}\quad$$e     $$\; F_{k+1}\to \, F_k\;$$, para $$\,k< N$$.
    
4. A propriedade $$\,R_k \equiv \neg\,F_k\;\equiv\;\bigwedge_{c\in F_k}\,\neg\,c\,$$  é sobre-aproximação do conjunto de estados que podem ser alcançados em $$\,k\,$$ ou menos passos a partir de um estado inicial. Verifica-se sempre
                            $$R_k\,\land \,\mathsf{T}\,\to\,R'_{k+1}\quad$$é tautologia

**algoritmo de bloqueio**

A sequência de “frames” deve verificar a propriedade (1.). Por isso uma componente essencial do algoritmo PDR  é um **bloqueio** que, dado um cubo $$\,c\,$$ e um número de “frame” $$\,k\,$$ , decide se:


> Para todo o estado acessível em $$k$$ passos, $$\,s\,\in\,R_k\,$$  que não pertence ao cubo $$\,c\,$$, e para toda a transição $$\,s\to s'\,$$, o cubo $$\,c\,$$ também não contém $$s'$$.  Um tal cubo $$\,c\,$$ diz-se **indutivo** para $$\,R_k\,$$.

Para bloquear um cubo $$\,c\,$$ é preciso verificar primeiro que não contém nenhum estado inicial. Para isso testa-se  se  $$\;\mathsf{SAT}(c\,\land\,\mathsf{I})\,$$ é  **unsat**.   Em seguida verifica-se se o cubo $$\,c\,$$ é indutivo  para propriedade $$\,R_{k-1}\,$$  testando se é tautologia

                                   $$\,R_{k-1}\,\land\,\mathsf{T}\,\land\,\neg\,c\,\to\,\neg\, c'$$ 

Para  isso usa-se o algoritmo de SAT  com a “query”

                                                $$\, \mathsf{SAT}\{\,R_{k-1}\,\land\,\mathsf{T}\,\land\,\neg\,c\,\land\, c'\,\}$$

A eventual tautologia acima verifica-se se e só se a resposta é **unsat**.

O significado associado a um cubo $$\,c\,$$indutivo para $$\,R_{k}\,$$  é o de estar **bloqueado**  na “frame”  $$\,k\,$$. Ou seja,  para todo $$\,s\in R_{k-1}\,$$ (i.e. $$\,s\,$$ não foi excluído da “frame” $$\,k-1\,$$ ), se o cubo $$\,c\,$$ não contém $$\,s\,$$   então, após uma transição adicional  $$\,s\to s'\,$$, o cubo $$\,c\,$$ também não contém $$\,s'\,$$ .

Um tal cubo $$\,c\,$$ pode ser adicionado  a $$\,F_k\,$$ e a todos os “frames”  $$\,F_i\,$$, com $$0<i\leq k\,$$ e o processo de bloqueio termina em sucesso.

Se a resposta for **sat (**i.e**.** $$\,c\,$$ o cubo não for indutivo), então existe uma testemunha $$\,s\,$$ que valida a fórmula submetida ao SAT. Suponhamos que $$\,\tilde{s}\,$$ é a expansão do cubo $$\,s\,$$ limitada à pré-imagem de $$\,c\,$$ — i.e. $$\,\mathsf{T}^{-1}(c)\;$$. Então, recursivamente, vai-se repetir este algoritmo de bloqueio com o cubo $$\,\tilde{s}\,$$ e no “frame”  $$\,k-1\,$$. Se se atingir o “frame”  $$F_0$$ com um cubo que interseta $$\,\mathsf{I}\,$$ , então o processo de bloqueio falha, porque não se pode bloquear um estado inicial. Senão, depois de bloquear o predecessor, volta-se a tentar o mesmo cubo $$\,c\,$$.

**get_bad_cube**

Um “bad cube”  no “frame”  $$\,k\,$$  é um cubo que contém um estado inseguro e não pertence a qualquer cubo de $$\,F_k\,$$. Para o detetar temos apenas de submeter ao SAT a “query”

                                                              $$\, \mathsf{SAT}\{\,\neg\,F_k\,\land\,\neg\,\mathsf{P}\,\}$$

Se a resposta for **unsat** não existe um “mau cubo”. Se a resposta for **sat**  recolhe-se uma testemunha $$\,s\,$$ e expande-se esse estado para um cubo que se devolve como resultado.

Com estas componentes podemos  construir o algoritmo PDR


----------

$$\mathsf{PDR}(X,I,T,P)$$ 

1. Inicializa a lista de frames com a lista singular $$\,[\neg\,I]$$ ; inicializar $$\,k = 0\,$$
2. $$\mathbf{while}\;\mathsf{True}$$ 
3. $$\quad \text{bad} = \mathbf{get\_bad\_cube}(P,k)$$
4.     se  $$\text{bad}$$  não existe então
5.               se  $$\,k\geq 1\,$$ e  $$F_{k-1}\leftrightarrow F_{k}\,$$  então o algoritmo termina com a mensagem **safe**  
6.               em caso contrário aumenta-se a sequência criando um novo “frame” 
              $$F_{k+1} = \mathsf{False}$$,  faz-se $$\,k = k+1\,$$ e o ciclo continua
7.     se $$\,\mathsf{bad}\,$$ existe  então corre-se o algoritmo $$\,\mathbf{bloqueio}(\text{bad},k)$$
8.            se a resposta de **bloqueio**(bad,*k*) for **sucesso**  o ciclo continua
9.            em caso contrário o ciclo termina com a mensagem **unsafe** 


----------

O seguinte código usando a interface `pysmt`  dá uma implementação muito simples deste algoritmo. O exemplo consta da lista de tutoriais na documentação [do](https://pysmt.readthedocs.io/en/latest/tutorials.html) `[pysmt](https://pysmt.readthedocs.io/en/latest/tutorials.html)`[.](https://pysmt.readthedocs.io/en/latest/tutorials.html)


    # Implementação simplificada do PDR (sem expansão de cubos nem propagação)
    
    from pysmt.shortcuts import Symbol, Not, And, Or, EqualsOrIff, Implies
    from pysmt.shortcuts import is_sat, is_unsat, Solver, TRUE
    from pysmt.typing import BOOL
    def next_var(v):
        """Returns the 'next' of the given variable"""
        return Symbol("next(%s)" % v.symbol_name(), v.symbol_type())
    def at_time(v, t):
        """Builds an SMT variable representing v at time t"""
        return Symbol("%s@%d" % (v.symbol_name(), t), v.symbol_type())
    
    class TransitionSystem(object):
        """Trivial representation of a Transition System."""
        def __init__(self, variables, init, trans):
            self.variables = variables
            self.init = init
            self.trans = trans
    # EOC TransitionSystem
    
    


    class PDR(object):
        def __init__(self, system):
            self.system = system
            self.frames = [system.init]
            self.solver = Solver()
    
        def check_property(self, prop):
            """Property Directed Reachability approach without optimizations."""
            print("Checking property %s..." % prop)
            while True:
                cube = self.get_bad_state(prop)
                if cube is not None:
                    # Blocking phase of a bad state
                    if self.recursive_block(cube):
                        print("--> Bug found at step %d" % (len(self.frames)-1))
                        break
                    else:
                        print("   [PDR] Cube blocked '%s'" % str(cube))
                else:
                    # Checking if the last two frames are equivalent i.e., are inductive
                    if self.inductive():
                        print("--> The system is safe!")
                        break
                    else:
                        print("   [PDR] Adding frame %d..." % (len(self.frames)))
                        self.frames.append(TRUE())
    
        def get_bad_state(self, prop):
            """Extracts a reachable state that intersects the negation
            of the property and the last current frame"""
            return self.solve(And(self.frames[-1], Not(prop)))
    
        def solve(self, formula):
            """Provides a satisfiable assignment to the state variables that are consistent with the input formula"""
            if self.solver.solve([formula]):
                return And([EqualsOrIff(v, self.solver.get_value(v)) for v in self.system.variables])
            return None
    
        def recursive_block(self, cube):
            """Blocks the cube at each frame, if possible.
            Returns True if the cube cannot be blocked.
            """
            for i in range(len(self.frames)-1, 0, -1):
                cubeprime = cube.substitute(dict([(v, next_var(v)) for v in self.system.variables]))
                cubepre = self.solve(And(self.frames[i-1], self.system.trans, Not(cube), cubeprime))
                if cubepre is None:
                    for j in range(1, i+1):
                        self.frames[j] = And(self.frames[j], Not(cube))
                    return False
                cube = cubepre
            return True
    
        def inductive(self):
            """Checks if last two frames are equivalent """
            if len(self.frames) > 1 and \
               self.solve(Not(EqualsOrIff(self.frames[-1], self.frames[-2]))) is None:
                return True
            return False
    
        def __del__(self):
            self.solver.exit()
    
    


    def counter(bit_count):
        """Counter example with n bits and reset signal."""
        # Example Counter System (SMV-like syntax)
        #
        # VAR bits: word[bit_count];
        #     reset: boolean;
        #
        # INIT: bits = 0 & reset = FALSE;
        #
        # TRANS: next(bits) = bits + 1
        # TRANS: next(bits = 0) <-> next(reset)
        from pysmt.typing import BVType
        bits = Symbol("bits", BVType(bit_count))
        nbits = next_var(bits)
        reset = Symbol("r", BOOL)
        nreset = next_var(reset)
        variables = [bits, reset]
        init = bits.Equals(0) & Not(reset)
        trans = nbits.Equals(bits + 1) &\
                (nbits.Equals(0)).Iff(nreset)
        # A true invariant property: (reset -> bits = 0)
        true_prop = reset.Implies(bits.Equals(0))
        # A false invariant property: (bits != 2**bit_count-1)
        false_prop = bits.NotEquals(2**bit_count -1)
        return (TransitionSystem(variables, init, trans), [true_prop, false_prop])
    
    def main():
        example = counter(4)
        pdr = PDR(example[0])
        for prop in example[1]:
            pdr.check_property(prop)
            print("")
    if __name__ == "__main__":
        main()

