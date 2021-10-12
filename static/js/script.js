//import {CHART_COLORS} from './utils.js';
Chart.defaults.global.defaultFontFamily = 'Roboto';
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
  10: 'rgb(75, 192, 192)',
  11: 'rgb(54, 162, 235)',
  12: 'rgb(153, 102, 255)',
  13: 'rgb(255, 99, 132)',
  14: 'rgb(255, 159, 64)',
  15: 'rgb(255, 205, 86)',
  16: 'rgb(75, 192, 192)',
  17: 'rgb(54, 162, 235)',
  18: 'rgb(153, 102, 255)',
  19: 'rgb(255, 99, 132)'
};






function getParams() {
  // 파라미터가 담길 배열
  var param = new Array();

  // 현재 페이지의 url
  var url = decodeURIComponent(location.href);
  // url이 encodeURIComponent 로 인코딩 되었을때는 다시 디코딩 해준다.
  url = decodeURIComponent(url);

  var params;
  // url에서 '?' 문자 이후의 파라미터 문자열까지 자르기
  params = url.substring( url.indexOf('?')+1, url.length );
  // 파라미터 구분자("&") 로 분리
  params = params.split("&");

  // params 배열을 다시 "=" 구분자로 분리하여 param 배열에 key = value 로 담는다.
  var size = params.length;
  var key, value;
  for(var i=0 ; i < size ; i++) {
      value = params[i].split("=")[0];
  

      param[i] = value;
  }

  return param;
}


var chart;

function makeChart(param) {
  // players is an array of objects where each object is something like:
  // {
  //   "Name": "Steffi Graf",
  //   "Weeks": "377",
  //   "Gender": "Female"
  // }

  //var temp= '평균';
  var location = param.map(function(d) {return d[group]});

  var number = param.map(function(d) {/*console.log(d[1])*/;return d[group_value]});
  //var chart_color = param.map(function(d) {return '#19A0AA';});

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

/*
var parameter = getParams();
console.log(parameter[0]);

var ctx = document.getElementById("chart1");
d3.csv('static/data/전국환경2.csv')
.then(makeChart);
*/

// Request data using D3
/*
for(let i=0; i<parameter.length;i++){
  var test = "chart" + (i+1).toString();
  console.log(test);
  var ctx = document.getElementById(test);

  d3.csv('static/data/전국환경.csv')
  .then(makeChart);
}
*/