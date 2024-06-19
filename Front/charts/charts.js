import { renderBarChart } from './GraficoBarra/bar.js';
import { renderLineChart } from './GraficoLinha/line.js';
import { renderPieChart } from './GraficoTorta/pie.js';

export function drawCharts() {
  loadGoogleCharts(() => {
    if (document.getElementById('pie_chart')) renderPieChart();
    if (document.getElementById('bar_chart')) renderBarChart();
    if (document.getElementById('line_chart')) renderLineChart();
  });
}

function loadGoogleCharts(callback) {
  google.charts.load('current', { packages: ['corechart', 'bar', 'gauge'] });
  google.charts.setOnLoadCallback(callback);
}