import { drawCharts } from '../charts.js';

let arr = [['Dispositivo', 'Total']];

function getData() {
  fetch('http://localhost:5000/monitoramento/graficopizza')
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

export function renderPieChart() {
  google.charts.load('current', { packages: ['corechart'] });
  google.charts.setOnLoadCallback(() => {
    const data = google.visualization.arrayToDataTable(arr);
    const options = { 
      title: 'Total Dispositivos - Pizza',
      width: 300,
     };
    const chart = new google.visualization.PieChart(
      document.getElementById('pie_chart')
    );
    chart.draw(data, options);
  });
}

document.addEventListener('DOMContentLoaded', getData);