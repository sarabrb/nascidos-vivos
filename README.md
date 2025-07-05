#### Fonte: o código pode rodar na sua máquina localmente e o dataset está disponível nesse [link aqui.](https://opendatasus.saude.gov.br/dataset/sistema-de-informacao-sobre-nascidos-vivos-sinasc/resource/61145247-d2bb-463a-befc-01dd5a86ff34?inner_span=True)

___

### Nascidos Vivos - Janeiro a Agosto de 2024
#### Análise Exploratória de Dados sobre os nascidos vivos de janeiro a agosto de 2024. Dataset disponibilizado pelo DataSUS.

___

### Objetivo
##### O objetivo deste estudo é constatar algumas estatísticas básicas sobre os nascidos vivos no Brasil de janeiro a agosto de 2024, com base nos registros do DataSUS. Informações como idade dos pais, anomalias registradas, escolaridade e estado civil das mães, tipos de partos, semanas de gestação e número de consultas pré-natal e as relações que essas variáveis podem ter entre si.

___
### Estatística sobre a idade das mães:
##### A média é de 27 anos com um desvio padrão de 6 anos;
##### A idade mínima constatada na base de dados foi 8 anaos e a máxima de 99 anos, mas foram poucos registros e passei a contabilizar de 10 a 65 anos;
##### O primeiro quartil (Q1) conta que até 25% das mães possuem até 25 anos, o segundo quartial (Q2) informa que a mediana é de 27 anos e o terceiro quartil (Q3) revela que até 75% das mães possuem 33 anos.
![image](https://github.com/user-attachments/assets/b974d639-207f-4a09-aaa7-028dd41dd40a)


### Outliers na coluna 'Idade da Mãe'
##### A base, que possui mais de um milhão de linhas, informa que há 305 outliers, representado 0.025% da base de dados.

___
### Estatística sobre a idade dos pais:
##### A idade média é de 32 anos, com um desvio padrão de 7 anos;
##### A idade mínima na base é de 9 anos e a máxima de 99 anos, mas novamente as considero outliers;
##### O primeiro quartil (Q1) informa que até 25% dos pais possuem 26 anos, o segundo quartil (Q2) nos traz que a mediana de idade é de 32 anos, o terceiro quartil (Q3) informa que até 75% dos pais possuem 37 anos;.

![image](https://github.com/user-attachments/assets/3ba3c001-2bda-4c15-836b-9b457887f2da)

<br>

### Outliers na coluna 'Idade dos Pais'
##### A base contém 4401 registros de pais acima de 52 anos, o que é consideravelmente maior que o número de outliers na idade das mães, representando 1.11% do total.

___

### Há mais anomalias registradas em nascidos de pais ou mães de mais idade?
![image](https://github.com/user-attachments/assets/ccc4fb83-9245-4a3a-a120-31635d051430)


![image](https://github.com/user-attachments/assets/11fdad47-49b7-401f-9f34-15d270a4e827)

##### É possível observar que, até os 30 anos, tanto a idade dos pais quanto a das mães influenciam de forma semelhante na porcentagem de anomalias registradas. A partir dos 31 anos, a idade da mãe passa a ter um impacto maior, especialmente após os 40 anos. Por outro lado, a porcentagem de anomalias relacionada à idade dos pais se mantém praticamente constante, mesmo após os 60 anos, permanecendo em torno de 1.25%.


___
### Locais de nascimento e partos

![image](https://github.com/user-attachments/assets/1768cd5c-c781-494f-92ff-c7f0af9ee25a)
<br>
##### A grande maioria dos partos tem sido realizada em hospitais, motivo pelo qual o gráfico está em escala logarítmica, o que indica que atualmente as pessoas têm mais acesso a hospitais em comparação com décadas passadas.

___

### Gestações normais e prematuras por tipo de parto
<br>

![image](https://github.com/user-attachments/assets/7df35739-dad3-46ef-a6d2-b7b497e8db32)

<br>

![image](https://github.com/user-attachments/assets/ca20d7a7-b08f-4499-bbb0-f24cd424b355)
<br>
##### As semanas mínimmas indicam que as mulheres têm partos prematuros, geralmente por volta de 35 semanas de gestação.
##### A mediana dos dados mostra que, para partos cesáreos, a gestação ocorre por volta de 37 semanas, enquanto para partos comuns, a mediana está em torno de 38 semanas.
##### O terceiro quartil (Q3) revela que 75% das mulheres que optam por ou necessitam de uma cesárea têm seus filhos entre 37 e 38 semanas de gestação, enquanto para partos comuns, essa faixa é de 38 a 40 semanas.
#### As semanas máximas informam que os 25% restantes das mulheres têm seus filhos entre 38 a 42 semanas em partos cesáreos, enquanto em partos naturais, a faixa se estende de 40 a 43 semanas.
##### Os outliers representam uma minoria, mas são mais frequentes em partos cesáreos.

___

### Escolaridade e estado civil das mães

<br>

![image](https://github.com/user-attachments/assets/d60298b6-2796-4bd1-90a1-633230726966)

<br>

![image](https://github.com/user-attachments/assets/59896bed-d713-4c1b-bde7-c68f5c2f459e)

<br>

### Tabela de Escolaridade das Mães por Faixa de Idade
##### Na tabela de Escolaridade das Mães por Faixa de Idade, é possível notar que uma porcentagem considerável das mães na faixa etária de 10 a 30 anos possui de 8 a 11 anos de escolaridade, o que compreende o ensino fundamental e médio. Em seguida, 25% das mães chegaram ao menos ao ensino superior ou técnico. De 7 anos de escolaridade à nenhuma escolaridade, compreendem 6,88% das mães.

##### Entre as mães de 31 a 40 anos, a escolaridade é mais elevada, com 55% delas atingindo o ensino superior ou técnico. Em segundo lugar, vem a escolaridade de 8 a 11 anos, representando quase 40% das mães. A baixa escolaridade nessa faixa é menor, representando apenas 5,21% das mães.

##### Na faixa etária de 41 a 50 anos, 54% das mães possuem 12 ou mais anos de escolaridade, e 36% delas têm entre 8 a 11 anos de escolaridade, o que é semelhante à faixa anterior. No entanto, há um salto na baixa escolaridade, representando 9% das mães com menos de 7 anos de escolaridade.

##### Entre as mães de 51 a 60 anos, observa-se um aumento significativo na porcentagem de mães com escolaridade superior a 12 anos, atingindo 66%. Enquanto 25% concluíram pelo menos o ensino fundamental ou médio, 8% possuem menos de 7 anos de escolaridade.dade.
<br>

### Tabela de Estado Civil das Mães por Faixa de Idade
<br>

##### Nas estatísticas de estado civil por faixa de idade, no grupo de 10 a 30 anos, aproximadamente 52% das mães são solteiras, seguidas por 32% de casadas e 14% em união estável.


##### Na faixa etária de 31 a 40 anos, 58% das mães são casadas, e o número de solteiras diminui para 26%, enquanto as uniões estáveis caem para 11%. Isso indica que as pessoas tendem a se casar após os 30 anos. Além disso, o número de divorciadas aumenta, de 1,06% na faixa anterior para 2,7% na faixa dos 31-40 anos.


##### Entre as mães de 41 a 50 anos, a taxa de casadas diminui para 52%, enquanto o número de divorciadas aumenta para 4,7%. As mães solteiras caem para 25%, enquanto as que estão em união estável aumentam para 12%, o que pode sugerir que algumas mulheres se separam e, em seguida, iniciam outro relacionamento.


##### Na faixa etária de 51 a 60 anos, a taxa de casadas permanece em torno de 58%, enquanto o número de divorciadas se mantém estável (cerca de 4%). As mães solteiras caem ainda mais para 15%, enquanto as uniões estáveis aumentam para 20%, representando um padrão de busca por estabilidade em relacionamentos mais tarde na vida.
##### A taxa de viúvez também aumenta com a idade, passando de 0,10% na faixa de 10-30 anos para 1,38% na faixa de 51-60 anos.

___

### O nível de escolaridade influencia na quantidade de consultas pré-natal?
<br>

![image](https://github.com/user-attachments/assets/12a1ff88-7125-432b-842f-25a29ae3f77b)
<br>

##### É possível observar que no grupo com maior escolaridade (12 anos ou mais de estudo), a maioria das gestantes realizou 7 ou mais consultas pré-natal, representando 88,6%.
##### Grupos com 8 a 11 anos e 4 a 7 anos de escolaridade também apresentam altas concentrações nessa faixa de consultas, mas em níveis menores quando comparados ao grupo com maior escolaridade.
##### No grupo com nenhuma escolaridade, o maior percentual está na faixa de 7 ou mais consultas (46,1%), uma redução de 47% em relação ao grupo com maior escolaridade. Além disso, esse grupo apresenta o maior percentual (16,4%) de gestantes realizando apenas 1 a 3 consultas, o que pode indicar possíveis barreiras, como falta de acesso a serviços de saúde ou desconhecimento da importância do acompanhamento pré-natal.

___

### Conclusões finais
##### A maioria das mães tem idades mais jovens, com uma concentração significativa de gestantes entre 24 e 33 anos. A partir dos 31 anos, a idade das mães passa a impactar mais a ocorrência de anomalias, especialmente após os 40 anos. As mães com idades mais avançadas têm uma maior chance de anomalias, o que é esperado devido ao aumento dos riscos biológicos associados à idade gestacional.

##### A idade dos pais também impacta as anomalias, embora de maneira mais constante. Os pais mais velhos (acima dos 50 anos) representam outliers, com uma alta concentração de idades que variam entre 52 a 85 anos, um fator que pode ser relevante em análises sobre saúde paterna.

___

### Partos e gestações
##### A maioria dos partos ocorre em hospitais, refletindo a melhora no acesso à saúde ao longo dos anos.
##### Os partos cesáreos acontecem um pouco mais cedo (37-38 semanas), enquanto os partos comuns tendem a ocorrer entre 38-40 semanas. Isso reflete a tendência de antecipação de partos via cesárea por razões médicas ou logísticas.
##### A maioria dos partos ocorre dentro da janela de tempo saudável (37-40 semanas), mas ainda existe uma porcentagem considerável de partos prematuros (antes de 37 semanas), especialmente para partos cesáreos.

___

### Escolaridade
##### Existe uma alta incidência de mães com baixa escolaridade (menos de 7 anos de estudo) nas faixas etárias mais jovens. Esse dado pode indicar uma falta de acesso à educação ou, possivelmente, um ciclo intergeracional de baixo acesso à educação.
##### Mães com 12 ou mais anos de escolaridade tendem a realizar mais consultas pré-natal e têm melhores condições para acompanhar a gestação. A escolaridade tem uma relação direta com o número de consultas, indicando a importância do acesso à educação para o cuidado gestacional.

___

### Estado civil
##### Na faixa etária de 10 a 30 anos, há uma maior concentração de mães solteiras. Isso diminui conforme as mulheres envelhecem, com um aumento significativo no número de mães casadas ou em união estável a partir dos 31 anos.
##### A taxa de divórcios aumenta com a idade. Isso pode indicar mudanças nas dinâmicas de relacionamento ao longo do tempo, refletindo as escolhas pessoais e as mudanças nas expectativas de vida.
##### A viúvez também aumenta com a idade, especialmente após os 50 anos, o que é esperado devido ao avanço da idade.

___

### Consultas pré-natal e escolaridade
##### A relação entre escolaridade e número de consultas pré-natal é clara: mães com maior escolaridade têm mais acesso e realizam mais consultas. Isso pode ser uma indicação de que a educação contribui para a conscientização sobre a importância do acompanhamento pré-natal e o acesso ao sistema de saúde.
##### Mães com nenhuma escolaridade ou baixa escolaridade (até 7 anos) têm menos consultas, com um percentual maior de gestantes realizando apenas 1 a 3 consultas. Esse dado sugere que mães em situação de vulnerabilidade educacional podem ter dificuldades para acessar cuidados médicos adequados durante a gestação, o que pode ser agravado por fatores socioeconômicos.
<br><br>
___

### Final
##### Este projeto oferece uma análise básica dos fatores que influenciam a gestação e os resultados associados a diferentes faixas etárias, escolaridade e estado civil. A análise sugere que o aumento da escolaridade, o acesso à saúde e o casamento ou união estável podem ser fatores protetores para as mães, contribuindo para melhores resultados durante a gestação. Além disso, os dados destacam a importância de abordar as desigualdades educacionais e de saúde para melhorar o acesso ao cuidado pré-natal e reduzir as disparidades nas condições de saúde materna e infantil.




