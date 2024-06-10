
## consulta para grafico de pizza ou barras, usando funcoes de agregação
SELECT dispositivo, COUNT(dispositivo) as TotalRegistros
FROM monitoramento
GROUP BY dispositivo

## consulta para grafico, agrupando por data do registro das medições
SELECT DATE_FORMAT(dt_created,'%d/%m/%Y') as dia, COUNT(dispositivo) as TotalRegistros
FROM monitoramento
GROUP BY DATE_FORMAT(dt_created,'%d/%m/%Y')

## select com a data formata para padrão brasil
SELECT DATE_FORMAT(dt_created,'%d/%m/%Y') as dia, temperatura, umidade, luminosidade, dispositivo, presenca, distancia
FROM monitoramento


SELECT * 
FROM `monitoramento`
WHERE dt_created = '2024-04-20 15:50:41';


SELECT DATE_FORMAT(dt_created,'%d/%m/%Y'), temperatura
FROM `monitoramento`
WHERE dt_created = '2024-04-20 15:50:41';


SELECT DATE_FORMAT(dt_created,'%d/%m/%Y'), temperatura
FROM `monitoramento`
where DATE_FORMAT(dt_created,'%d/%m/%Y') BETWEEN '02/04/2024' AND '20/04/2024'  ;

SELECT DATE_FORMAT(dt_created,'%d/%m/%Y') AS DATA,  DATE_FORMAT(dt_created,'%d') AS DIA, DATE_FORMAT(dt_created,'%m') AS MES,  
DATE_FORMAT(dt_created,'%Y') AS ANO, temperatura
FROM `monitoramento`
where DATE_FORMAT(dt_created,'%d/%m/%Y') BETWEEN '02/04/2024' AND '20/04/2024'  ;

DATE_FORMAT(dt_created,'%d/%m/%Y')

SELECT DATE_FORMAT(dt_created,'%d/%m/%Y') AS DATA, 
DATE_FORMAT(dt_created,'%H:%i:%s') AS HORA,
DATE_FORMAT(dt_created,'%d') AS DIA, DATE_FORMAT(dt_created,'%m') AS MES,  
DATE_FORMAT(dt_created,'%Y') AS ANO,
temperatura
FROM `monitoramento`
where DATE_FORMAT(dt_created,'%d/%m/%Y') BETWEEN '02/04/2024' AND '20/04/2024'  ;