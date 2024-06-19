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

export function renderBarChart() {
  google.charts.load('current', { packages: ['bar'] });
  google.charts.setOnLoadCallback(() => {
    const data = google.visualization.arrayToDataTable(arr);
    const options = {
      chart: { title: 'Total Dispositivos - Barras' },
      bars: 'horizontal',
      colors: ['#1b9e77', '#d95f02', '#7570b3'],
      width: 300,
      hAxis: {
        title: 'Total',
        minValue: 0,
        textStyle: { color: '#333' },
        titleTextStyle: { color: '#1b9e77' },
      },
      vAxis: {
        title: 'Dispositivo',
        textStyle: { color: '#333' },
        titleTextStyle: { color: '#1b9e77' },
      },
      fontName: 'Arial',
      fontSize: 14,
    };
    const chart = new google.charts.Bar(document.getElementById('bar_chart'));
    chart.draw(data, google.charts.Bar.convertOptions(options));
  });
}

document.addEventListener('DOMContentLoaded', getData);