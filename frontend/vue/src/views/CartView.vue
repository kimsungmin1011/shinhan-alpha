<template>
  <img src="../../../images/status.png" alt="My Image">
  <div id="app">
    <div id="top-wrapper">
      <font-awesome-icon icon="fa-solid fa-chevron-left" onclick=""/>
      <span><img src="../../../images/arrow.png" alt="My Image">  알파카트(일괄매수)</span>
      </div>
      <div class="scrollable" ref="scrollable" v-on:scroll="handleScroll">
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
          <tr v-for="(stock, index) in stocks" :key="index" :class="{ 'table-row-selected': stock.checked }">
              <td><input type="checkbox" v-model="stock.checked" @click="stockClick(stock)"></td>
              <td>{{ stock.name }}</td>
              <td>{{ stock.price }}</td>
              <td>
                <button type="button" @click="decrementQuantity(stock)">-</button>
                {{ stock.quantity }}
                <button type="button" @click="incrementQuantity(stock)">+</button>
              </td>
          </tr>
          </tbody>
      </table>
    </div>
      <div class="tabs">
        <div class="tab" @click="selectedTab = 'first'" :class="{ 'active': selectedTab === 'first' }">주식 포트폴리오</div>
        <div class="tab" @click="selectedTab = 'sec'" :class="{ 'active': selectedTab === 'sec' }">배당 포트폴리오</div>
        <div class="tab" @click="selectedTab = 'third'" :class="{ 'active': selectedTab === 'third' }">총자산 포트폴리오</div>
      </div>
      <div v-if="selectedTab == 'first'">
        <div style="display:inline-block; width:160px">
          <Pie :data="chartData" :options="options"/>
        </div>
        <div style="display:inline-block">
          기대수익률<br>
          {{ percent }}%<br><br>
          위험<br>
          {{ danger }}%<br><br>
        </div>
        <div id="size1">
        <!-- <h2>주문금액(합계) <span id="myValue">{{checkedStockPricesSum}}원</span></h2> -->
      </div>
      </div>
      <div v-else-if="selectedTab == 'sec'">
        <Bar :data="divchartData" :options="options"/>
      </div>
      <div v-else-if="selectedTab == 'third'">
        <div style="display:inline-block; width:100px">
          <b>보유 포트폴리오</b>        
          <Pie :data="chartData" :options="options"/>
        </div>
        <!-- <div style="display:inline-block; width:100px">
          <b>ㅁㄴㅇㄹ</b>
        </div> -->
        <div style="display:inline-block; width:100px">
          <b>목표 포트폴리오</b>
          <Pie :data="updatePort" :options="options"/>
        </div>
      </div>
      <button class="buy" type="button" @click="add" style="background-color:white; border-radius: 10px;">
        종목추가
      </button>
      <button class="buy" type="button" @click="modal" style="background-color:#117FE3; border-radius: 10px;">
        매수
      </button>
      <div style="margin:50px;"></div>
      
  </div>

</template>

<script>

import { Chart as ChartJS, ArcElement, Tooltip, Legend,Title,BarElement,CategoryScale,LinearScale } from 'chart.js'
import { Pie, Bar } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)
export default {
  name: 'App',
  components: {
    Pie, Bar
  },
  data() {
    return {
      categoryList: ['주식포트폴리오'],
      stocks: [
      { name: "LG전자", price: "113,000", quantity: 1, checked: false },
      { name: "현대차", price: "179,200", quantity: 1, checked: false },
      { name: "삼성전자", price: "62,600", quantity: 1, checked: false },
      { name: "대우중공업", price: "100,000", quantity: 1, checked: false },
      { name: "LG전자", price: "113,000", quantity: 1, checked: false },
      { name: "현대차", price: "179,200", quantity: 1, checked: false },
      { name: "삼성전자", price: "62,600", quantity: 1, checked: false },
      { name: "대우중공업", price: "100,000", quantity: 1, checked: false },
      ],
      selectedTab: "first",
      posts:{labels: [ '01', '02', '03','04', '05', '06','07', '08', '09','10', '11', '12'],
        datasets: [
          {
            label:'Dividend',
            backgroundColor: '#f87979',
            data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11],
          },
        ]},
    }
  },
  computed:{
      checkedStocks() {
        if(this.stocks){
          return this.stocks.filter(stock => stock.checked);
        }
        return [];

  },
  /* eslint-disable */
  chartData() {
    const checkedStocks = this.checkedStocks;
    const checkedStockNames = checkedStocks.map(stock => stock.name);
    const checkedStockPrices = checkedStocks.map(stock => Number(stock.price.replace(',', ''))*stock.quantity);
    const sum = checkedStockPrices.reduce((acc, val) => acc + val, 0);
    this.checkedStockPricesSum = sum;
    return {
      labels: checkedStockNames,
      datasets: [
        {
          backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
          data: checkedStockPrices
        }
      ],
      checkedStockPricesSum: 0,
    };
  },
  divchartData() {
    // const checkedStocks = this.checkedStocks;
    // const checkedStockdiv = checkedStocks.map(stock => Number(dividend)*stock.quantity);
      return{
        labels: [ '01', '02', '03','04', '05', '06','07', '08', '09','10', '11', '12'],
        datasets: [
          {
            label:'Dividend',
            backgroundColor: '#f87979',
            data: [40, 20, 12, 39, 10, 40, 39, 80, 40, 20, 12, 11],
          }
        ]
      }
    },
    dartchartData() {
      return{
        
      }
    }
  },
  methods: {
    updatePort() {
            const headers = { 'Authorization': `JWT ${localStorage.getItem('access_token')}` };
            /* eslint-disable */
            axios
                .get("http://127.0.0.1:8000/api/portfolio/", { headers })
                  .then(response => {
                    this.dartchartDataresponse.data.results[0].keys;
                  })
                  .catch(error => {
                    console.log(error);
                  });
    },
    stockClick(stock) {
      stock.checked = true;
    },
    incrementQuantity(stock) {
      stock.quantity += 1;
    },
    decrementQuantity(stock) {
      if (stock.quantity > 1){
        stock.quantity -= 1;
      }
    },
    handleScroll() {
        const scrollable = this.$refs.scrollable;
        if (scrollable.scrollTop + scrollable.offsetHeight >= scrollable.scrollHeight) {
          console.log('맨 아래 도달');
        }
      }
  }
}
</script>
<style scoped>
.scrollable {
    height: 170px;
    overflow-y: scroll;
  }
 .tabs {
    display: flex;
    justify-content: space-between;
    border-bottom: 1px solid #ccc;
    font-size:10px;
  }
  
  .tab {
    padding: 10px;
    cursor: pointer;
  }
  
  .tab.active {
    background-color: #ccc;
    font-weight: 900;
    text-decoration : underline;
  }
  
  .tab-content {
    margin-top: 10px;
  }
      table {
          border-collapse: collapse;
          width: 100%;
          border: 1px solid #444444;
          font-size:75%
      }

      td {
          text-align: left;
          padding: 8px;
          border: 1px solid #444444;
          padding: 4px;
      }

      th {
          background-color: #eeeeee;
          color: #5f5f5f;
          border: 1px solid #444444;
          padding: 4px;
      }
      /* tr:nth-child(odd) {
          background-color: #a5a5a5;
      }
      tr:nth-child(even) {
          background-color: #f2f2f2;
      } */

      input[type=checkbox] {
          cursor: pointer;
      }
      button img{
        width: 100px;
        height: 30px;
        object-fit: cover;
      }
      #chart {
        display: inline-block;
      }
      .buy {
        padding: 10px 50px;
        margin: 2px;
        background-color:#117FE3;
        
      }
      .table-row-selected {
  background-color: #e6f7ff;
}

      /* topbar */
#top-wrapper {
    text-align: left;
    height: 30px;
    font-size: 15px;
    padding-left: 5px;
}
#top-wrapper span {
  margin-left: 10px;
}
#size1 {font-size:12px;}
</style>