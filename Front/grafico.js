google.charts.load("current", { packages: ["corechart"] });

// Define a função de callback para executar quando a API de Visualização do Google for carregada.
google.charts.setOnLoadCallback(drawChart);

// Função de callback que cria e preenche uma tabela de dados,
// instancia o gráfico de pizza, passa os dados e desenha.
async function drawChart() {
  try {
    const response = await fetch("http://192.168.1.7:5000/monitoramento");
    const result = await response.json();

    console.log("Dados buscados:", result);

    if (!Array.isArray(result)) {
      throw new Error("Os dados buscados não são um array");
    }

    // Verifica se todos os itens são arrays e têm exatamente dois elementos
    const transformedResult = result.map(row => {
      if (Array.isArray(row) && row.length === 2) {
        return row;
      }
      throw new Error("Cada linha deve ser um array com exatamente dois elementos");
    });

    var data = new google.visualization.DataTable();
    data.addColumn("string", "Tarefa");
    data.addColumn("number", "Horas por Dia");

    data.addRows(transformedResult);

    var options = {
      title: "Distribuição das Tarefas por Dia",
      width: 400,
      height: 300,
    };

    var chart = new google.visualization.PieChart(
      document.getElementById("chart_div")
    );
    chart.draw(data, options);
  } catch (error) {
    console.error("Erro ao buscar ou analisar os dados:", error);
  }
}
