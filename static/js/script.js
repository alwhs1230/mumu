Chart.defaults.global.defaultFontColor = '#333';



const CHART_COLORS = {
  red: 'rgb(255, 99, 132)',
  orange: 'rgb(255, 159, 64)',
  yellow: 'rgb(255, 205, 86)',
  green: 'rgb(75, 192, 192)',
  blue: 'rgb(54, 162, 235)',
  purple: 'rgb(153, 102, 255)',
  1: 'rgb(255, 99, 132)',
  2: 'rgb(255, 159, 64)',
  3: 'rgb(255, 205, 86)',
  4: 'rgb(75, 192, 192)',
  5: 'rgb(54, 162, 235)',
  6: 'rgb(153, 102, 255)',
  7: 'rgb(255, 99, 132)',
  8: 'rgb(255, 159, 64)',
  9: 'rgb(255, 205, 86)',
};



var chart;

function makeChart(param) {

  var location = param.map(function(d) {return d[group]});

  var number = param.map(function(d) {return d[group_value]});

    chart = new Chart(ctx, {
    type: 'bar',
    options: {
      responsive: false,
      maintainAspectRatio: false,
      legend: {
        display: false
      },
      scales: {
      },

              
      sortBy: 'number',
      order: 'asc',
      sortFunction: (a, b) => {
        if (a.label < b.label) return -1
        if (a.label > b.label) return 1
        return 0
        }
      
    },
    data: {
      labels: location,
      datasets: [
        {
          data: number,
          backgroundColor: Object.values(CHART_COLORS)
        }
      ]
    },
  })
}
