import { drawCharts } from '../charts.js';

let arr = [['Dispositivo', 'Total']];

function getData() {
  fetch('http://localhost:5000/monitoramento/graficobarra')
    .then((response) => response.json())
    .then((data) => {
      arr = [['Dispositivo', 'Total']];
      data.slice(0, 5).forEach((item) => {
        arr.push([item.dispositivo, item.TotalRegistros]);
      });
      drawCharts();
    })
    .catch((error) => console.error('Erro ao obter dados:', error));
}

export function renderLineChart() {
  google.charts.load('current', { packages: ['corechart'] });
  google.charts.setOnLoadCallback(() => {
    const data = google.visualization.arrayToDataTable(arr);
    const options = {
      title: 'Total Dispositivos - Linha',
      colors: ['#a52714', '#097138'],
      width: 300,
      hAxis: {
        title: 'Dispositivo',
        titleTextStyle: { color: '#333' },
      },
      vAxis: {
        title: 'Total',
        minValue: 0,
        titleTextStyle: { color: '#333' },
      },
      fontName: 'Arial',
      fontSize: 14,
      areaOpacity: 0.2,
      legend: { position: 'top', textStyle: { color: '#333', fontSize: 16 } },
    };
    const chart = new google.visualization.LineChart(
      document.getElementById('line_chart')
    );
    chart.draw(data, options);
  });
}

document.addEventListener('DOMContentLoaded', getData);