# Descricao  
A classe Temposinc foi desenvolvida como uma ferramenta versatil para a obtencao e analise de dados de previsao do tempo. Com funcionalidades abrangentes, ela permite nao apenas a recuperacao das coordenadas de uma cidade, mas tambem a obtencao detalhada da previsao do tempo para os proximos 7 dias. Alem disso, oferece recursos para calcular medias diarias, visualizar probabilidades de precipitacao de chuva atraves de graficos interativos e ate mesmo compartilhar essas informacoes meteorologicas por e-mail.  

# Funcionalidades  
-> Obter cordenadas de uma cidade.  
-> Obter previsao de tempo para os proximos sete dias.  
-> Obter a media de temperatura para os proximos sete dias.   
-> Obter previsao da temperatura atual.  
-> Obter previsao da temperatura por hora para os proxímos sete dias.  
-> Obter previsao da temperatura por hora de um dia em especifico.  
-> Elaboracao de um grafico que representa a probabilidade de ocorrencia de chuva nos proximos sete dias.  
-> Elaboracao de um grafico que representa a probabilidade de ocorrencia de chuva por hora de um dia em especifico.  
-> Envio de dados climaticos por e-mail.  

# Como usar  
### Importar a biblioteca <br>  
```python
    pip install TempoSinc
```

### Cria a instância da classe passando o nome da cidade como parametro 
```python
    a = Temposinc("picos")
```

# Usando metodos:  
### Obter cordenadas de uma cidade  
```python
    aa = a.obter_coordenadas()
    print(aa)
```
Vai retornar a latitude e longitude da cidade escolhida.  

### Obter previsso de tempo para os proximos sete dias
```python
  aa = a.dados_diarios_prox_7_dias()
  print(aa)
```
Vai retornar dados como temperatura maxima, temperatura minima, indice UV, probabilidade de chuva e velocidade do vento.  

### Obter a media de temperatura para os proximos sete dias  
```python
  aa = a.calcular_media_por_dia()
  print(aa)
```
Vai retornar a media de todas as unidades citadas acima.  

### Obter previsao da temperatura atual   
```python
    aa = a.obter_dados_cli_atual()
    print(aa)
```
Vai retornar os dados climaticos atuias de uma cidade. 

### Obter previsao da temperatura por hora para os proxímos sete dias  
```python
    aa = a.obter_previsao_hora_prox_7_dias()
    print(aa)
```
Vai retornar dados climaticos da semana por hora.  

### Obter previsao da temperatura por hora de um dia em especifico  
```python
    aa = a.obter_dados_do_dia_atual_por_hora("2024-01-28")
    print(aa)
```
Vai retornar os dados climaticos por hora de um dia em especifico.  
O parametro da funcao e a data em especifico começando pelo ano, mes e dia. Utilizando aspas simples ou duplas.  

### Elaboracao de um grafico que representa a probabilidade de ocorrencia de chuva nos próximos sete dias  
```python
    aa = a.visualizar_grafico_de_media_precipitacao()
```
Vai retornar um grafico com as medias de chances de chuva para os sete dias.  

### Elaboracao de um grafico que representa a probabilidade de ocorrencia de chuva por hora de um dia em especifico  
```python
    aa = a.obter_dados_do_dia_atual_por_hora("2024-01-28")
    bb = a.visualizar_grafico_de_hora_precipitacao(aa)
```
Vai retornar um grafico com as medias de chances de chuva por hora de um dia em especifico.  
O parametro da funcao sao os dados da funcao obter_dados_do_dia_atual_por_hora("2024-01-28"). 
 
### Envio de dados climaticos por e-mail  
```python
    aa = a.obter_previsao_hora_prox_7_dias()
    bb = a.enviar_email("seu e-mail", aa)
```
Envia os dados para um e-mail em especifico.  
O primeiro parâmetro é o e-mail que deseja enviar e o segundo parâmetro e o dado que deseja enviar.
