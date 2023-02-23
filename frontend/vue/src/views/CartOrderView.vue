<template>
    <div>
      <img src="../../../images/status.png" alt="My Image" />
      <div id="app">
        <div id="top-wrapper">
          <font-awesome-icon icon="fa-solid fa-chevron-left" onclick="" />
          <div float="left">
            <img src="../../../images/arrow.png" alt="My Image" />
            알파카트(일괄매수)
          </div>
        </div>
        <div class="scrollable" ref="scrollable" v-on:scroll="handleScroll"></div>
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
            <tr v-for="(stock, index) in stocks" :key="index">
                    <td>
                        <input type="checkbox" v-model="stock.checked" @click="stockClick(stock)" />
                    </td>
                    <td>{{ stock.name }}</td>
                    <td>{{ stock.price }}</td>
                    <td>
                        <button type="button" @click="incrementQuantity(stock)">+</button>
                        {{ stock.quantity }}
                        <button type="button" @click="decrementQuantity(stock)">-</button>
                    </td>
                </tr>
</tbody>

        </table>
        <div id="app" style="width: 0.1vw; height: 0.1vh;">
          <Pie :data="chartData" :options="options" />
        </div>
        <div id="size1">
          <h2>주문금액(합계) <span id="myValue">{{ checkedStockPricesSum }}원</span></h2>
        </div>
        <button type="button" class="buyonce" id="show-checked-button" @click="showChecked">
          <h3 class="white">일괄매수</h3>
        </button>
        <div style="margin: 50px;"></div>

        <!-- 여기서부터 모달!!! -->
        <div v-if="showModal" class="modal">
          <div class="modal-content">
            <span class="close" @click="showModal = false">&times;</span>
            <p style="text-align:left"><b>주문 확인</b></p>
            <table>
          <thead>
          <tr>
              <th>종목</th>
              <th>주문수량</th>
              <th>주문단가</th>
          </tr>
          </thead>
          <tbody>
              <tr v-for="(stock, index) in checkedStocks" :key="index">
                <td>{{ stock.name }}</td>
                <td>{{ stock.quantity }}주</td>
              <td>{{ stock.price }}원</td>
              </tr> 
            </tbody>
            </table>
            <ul>
              <li><p class="opa" >주문금액(합계)</p></li>
              <li><p style="text-align:right;"><b>{{ checkedStockPricesSum }}원</b></p></li>
              <!-- <p style="text-align:left">주문금액(합계)</p>
              <p style="text-align:right"><b>{{ checkedStockPricesSum }}원</b></p> -->
            </ul>
              
              
                <p>위 내용으로 주문을 하시겠습니까?</p>
                <button type="button" @click="showCheckedplz">매수</button>
              
  
            
          </div>
        </div>
        <div v-if="completeOrderModal" class="modal">
          <div @click="completeOrderModal = false"></div>
          <div class="modal-content">
            <span class="close" @click="completeOrderModal = false">&times;</span>
            <img src="../../../images/lion.png" />
            <h3>주문이 완료되었습니다.</h3>
          <button>
            <router-link to="/">
              <button class="buy"><strong>확인</strong></button>
            </router-link>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { Chart as ChartJS, ArcElement, Tooltip, Legend } from 'chart.js'
import { Pie } from 'vue-chartjs'

ChartJS.register(ArcElement, Tooltip, Legend)

export default {
  name: 'App',
  components: {
    Pie,
  },
  data() {
    return {
      stocks: [
        { name: 'LG전자', price: '113,000', quantity: 1, checked: false },
        { name: '현대차', price: '179,200', quantity: 1, checked: false },
        { name: '삼성전자', price: '62,600', quantity: 1, checked: false },
        { name: '대우중공업', price: '100,000', quantity: 1, checked: false },
      ],
      options: {},
      showModal: false,
      completeOrderModal: false,
    }
  },
  computed: {
    checkedStocks() {
      if (this.stocks) {
        return this.stocks.filter((stock) => stock.checked)
      }
      return []
    },

    chartData() {
      /* eslint-disable */
      const checkedStocks = this.checkedStocks
      const checkedStockNames = checkedStocks.map((stock) => stock.name)
      const checkedStockPrices = checkedStocks.map(
        (stock) => Number(stock.price.replace(',', '')) * stock.quantity
      )

      return {
        labels: checkedStockNames,
        datasets: [
          {
            backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
            data: checkedStockPrices,
          },
        ],
      }
    },
  },
  watch: {
    chartData() {
      const checkedStocks = this.checkedStocks
      const checkedStockPrices = checkedStocks.map(
        (stock) => Number(stock.price.replace(',', '')) * stock.quantity
      )
      const sumValue = checkedStockPrices.reduce((acc, val) => acc + val, 0)

      this.checkedStockPricesSum = sumValue
    },
  },
  methods: {
    completeOrder() {
      window.alert('주문 완료!')
      setTimeout(() => {
        this.showModal = false
        this.completeOrderModal = false
      }, 1000)
    },
    stockClick(stock) {
      stock.checked = true
    },
    incrementQuantity(stock) {
      stock.quantity += 1
    },
    decrementQuantity(stock) {
      if (stock.quantity > 1) {
        stock.quantity -= 1
      }
    },
    showChecked() {
      this.showModal = true
    },
    showCheckedplz() {
      this.completeOrderModal = true
    },
  },
}
</script>

<style scoped>
table {
  border-collapse: collapse;
  width: 100%;
  font-size: 75%;
}

.opc {
  opacity: 0.5;
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

input[type='checkbox'] {
  cursor: pointer;
}

#buy {
  position: relative;
  max-width:200px;
}

.modal {
  display: block;
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  display: block;
  margin: 5% auto;
  padding: 20px;
  border: 1px solid #888;
  width: 90%;
  max-width: 800px;
  background-color: white;
}

.modal-overlay {
  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.4);
}

.close {
  color: #aaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}

.buy {
        padding: 10px 50px;
        margin: 2px;
        background-color:#117FE3;
        color:white
      }

.close:hover,
.close:focus {
  color: black;
  text-decoration: none;
  cursor: pointer;
}

#black {
  color: black;
}


#size1 {
  font-size: 12px;
}

/* .right {
  text-align: right;
}

.left {
  text-align: left;
} */


ul {
    list-style:none;
}
li {
    display: inline-block; 
} 
</style>

  