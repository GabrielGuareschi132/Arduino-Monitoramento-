let gaugeData = [['Label', 'Value']];

function getData() {
  fetch('http://localhost:5000/monitoramento/graficomedidor')
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
      console.log(data[0].MED_LUMINOSIDADE);
      gaugeData = [
        ['Label', 'Value'],
        ['Temperatura', data[0].MED_TEMPERATURA],
        ['Umidade', data[0].MED_UMIDADE],
        ['Luz', data[0].MED_LUMINOSIDADE],
      ];
      drawCharts();
    })
    .catch((error) => console.error('Erro ao obter dados:', error));
}

function loadGoogleCharts(callback) {
  google.charts.load('current', { packages: ['corechart', 'bar', 'gauge'] });
  google.charts.setOnLoadCallback(callback);
}

function drawCharts() {
  loadGoogleCharts(() => {
    renderGauge();
  });
}

function renderGauge() {
  const data = google.visualization.arrayToDataTable(gaugeData);
  console.log(data);
  const options = {
    width: 400,
    height: 120,
    redFrom: 90,
    redTo: 100,
    yellowFrom: 75,
    yellowTo: 90,
    minorTicks: 5,
  };

  const chart = new google.visualization.Gauge(
    document.getElementById('gauge_chart')
  );

  chart.draw(data, options);


}

document.addEventListener('DOMContentLoaded', getData);