<template>
  <div>
    <h1>알파카트(일괄매수)</h1>
    <table>
      <thead>
        <tr>
          <th>선택</th>
          <th>종목</th>
          <th>현재가</th>
          <th>수량</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><input type="checkbox" v-model="checked[0]" /></td>
          <td>LG전자</td>
          <td>113,000</td>
          <td>1</td>
        </tr>
        <tr>
          <td><input type="checkbox" v-model="checked[1]" /></td>
          <td>현대차</td>
          <td>179,200</td>
          <td>1</td>
        </tr>
        <tr>
          <td><input type="checkbox" v-model="checked[2]" /></td>
          <td>삼성전자</td>
          <td>62,600</td>
          <td>1</td>
        </tr>
        <tr>
          <td><input type="checkbox" v-model="checked[3]" /></td>
          <td>대우중공업</td>
          <td>100,000</td>
          <td>1</td>
        </tr>
      </tbody>
    </table>
    <h1>주식 포트폴리오</h1>
    <div class="chart-container" style="position: relative; height:80vh; width:80vw">
      <canvas id="myChart"></canvas>
    </div>
    <h2>주문금액(합계) <span>{{ sum }}</span></h2>
    <button type="button" @click="order"><img src="images/매수버튼.PNG" alt="매수버튼"></button>
  </div>
</template>

<script>
import Chart from 'chart.js';

export default {
  data() {
    return {
      checked: [false, false, false, false],
      stockPrices: [113000, 179200, 62600, 100000],
      stockNumber: [1, 1, 1, 1],
      sum: 0,
      myChart: null
    };
  },
  mounted() {
    this.createChart();
  },
  methods: {
    createChart() {
      const ctx = document.getElementById('myChart').getContext('2d');
      this.myChart = new Chart(ctx, {
        type: 'pie',
        data: {
          labels: ['LG전자', '현대차', '삼성전자', '대우중공업'],
          datasets: [
            {
              data: [0, 0, 0, 0],
              backgroundColor: [
                '#' + Math.floor(Math.random() * 16777215).toString(16),
                '#' + Math.floor(Math.random() * 16777215).toString(16),
                '#' + Math.floor(Math.random() * 16777215).toString(16),
                '#' + Math.floor(Math.random() * 16777215).toString(16)
              ]
            }
          ]
        }
      });
      for (let i = 0; i < this.checked.length; i++) {
        if(this.checked[i]) {
      this.myChart.data.datasets[0].data[i] += this.stockNumber[i] * this.stockPrices[i];
    }
  }
  this.myChart.update();
},
order() {
  let checkedItems = [];
  for (let i = 0; i < this.checked.length; i++) {
    if (this.checked[i]) {
      checkedItems.push(`${this.myChart.data.labels[i]} 현재가: ${this.stockPrices[i]} 수량: ${this.stockNumber[i]} 총금액: ${this.stockNumber[i] * this.stockPrices[i]}`);
    }
  }
  let myWindow = window.open("", "myWindow", "width=400,height=200,modal=yes");
  myWindow.document.write("<p>" + "주문확인:<br>" + checkedItems.join('<br>') + "</p>" + "주문금액(합계): " + this.myChart.data.datasets[0].data.reduce((a, b) => a + b, 0) + "원");
  let moveButton = myWindow.document.createElement("button");
  moveButton.innerText = "취소";
  moveButton.onclick = function () {
    window.location.href = "alapha_cart_order.html";
    myWindow.close();
  };
  myWindow.document.body.appendChild(moveButton);
}
},
watch: {
checked: function(newChecked) {
for (let i = 0; i < newChecked.length; i++) {
if (newChecked[i]) {
this.myChart.data.datasets[0].data[i] += this.stockNumber[i] * this.stockPrices[i];
} else {
this.myChart.data.datasets[0].data[i] -= this.stockNumber[i] * this.stockPrices[i];
}
}
this.myChart.update();
this.sum = this.myChart.data.datasets[0].data.reduce((a, b) => a + b, 0) + "원";
}
}
};
</script>

<style scoped>
table {
  border-collapse: collapse;
  width: 100%;
}

th,
td {
  text-align: left;
  padding: 8px;
}

th {
  background-color: #333;
  color: white;
}

tr:nth-child(even) {
  background-color: #f2f2f2;
}

input[type='checkbox'] {
  cursor: pointer;
}
</style>
