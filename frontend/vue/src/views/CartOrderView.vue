<template>
    <div id="app">
        <h2>알파카트(일괄매수)</h2>
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
        <h2>주문금액(합계) <span id="myValue">{{ checkedStockPricesSum }}원</span></h2>
        <button type="button" class="buyonce" id="show-checked-button" @click="showChecked">
            <h3 class="white">일괄매수</h3>
        </button>
        <div style="margin: 50px;"></div>
        <div v-if="showModal" class="modal">
            <div class="modal-content">
                <span class="close" @click="showModal = false">&times;</span>
                <h3>매수 확인</h3>
                <li>
                    가능금액: {{ charge }}원
                </li>
                <ul>
                    <li v-for="(stock, index) in checkedStocks" :key="index">
                        {{ stock.name }} - {{ stock.price }}원 x {{ stock.quantity }}
                    </li>
                    <li>
                        총 {{ checkedStockPricesSum }}원
                    </li>
                    <li>
                        <h3>위 내용으로 주문을 하시겠습니까?</h3>
                        <button type="button" @click="completeOrder">매수</button>
                    </li>
                </ul>
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
            window.alert('주문이 완료되었습니다.')
            setTimeout(() => {
                this.showModal = false
            }, 2000)
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
    },
}
</script>

<style scoped>
table {
    border-collapse: collapse;
    width: 100%;
}

td {
    text-align: left;
    padding: 8px;
}

th {
    background-color: #333;
    color: white;
}

tr:nth-child(odd) {
    background-color: #a5a5a5;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

input[type='checkbox'] {
    cursor: pointer;
}

#buy {
    position: relative;
    max-width: 200px;
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
    /* 넓이 증가 */
    max-width: 800px;
    /* 너무 커지는걸 방지함 */
    background-color: white;
}


.close {
    color: #aaa;
    float: right;
    font-size: 28px;
    font-weight: bold;
}

.close:hover,
.close:focus {
    color: black;
    text-decoration: none;
    cursor: pointer;
}</style>

  