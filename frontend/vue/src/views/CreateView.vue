<template>
    <div class="container">
        <div id="top-wrapper">
            <font-awesome-icon icon="fa-solid fa-chevron-left" onclick="" />
            <span>포트폴리오 생성</span>
        </div>
        <!-- 메인 -->
        <div id="main">
            <button @click="selectedTab = 'first'">주식 포트폴리오</button>
            <button @click="selectedTab = 'sec'">배당 포트폴리오</button>
            <div v-if="selectedTab == 'first'">
                <div class="main-top">
                    <span>문민제</span>님의 목표 자산 포트폴리오
                    <div class="pie-chart">
                        <Pie :data="chartData" :options="options" />
                    </div>
                    <hr>
                </div>
                <div id="port-select">
                    <button>목표 비율 설정</button>
                    <button>내 자산 입력</button>
                </div>
                <div class="main-bottom">
                    <div>
                        <div class="my-box">
                            <table>
                                <thead>
                                    <colgroup>
                                        <col width="10%" />
                                        <col width="40%" />
                                        <col width="10%" />
                                        <col width="40%" />
                                    </colgroup>
                                </thead>
                                <tbody>
                                    <tr v-for="(stock, index) in stocks" :key="index">
                                        <td>{{ stock.name }}</td>
                                        <td><input type="text" class="percent" v-model="stock.percent" placeholder="%"
                                                @input="updatePrice(stock, $event.target.value)" /></td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>

                </div>
                <div id="save" @click=updatePort()>
                        <span>설정 완료</span>
                    </div>

            </div>
            <div v-else-if="selectedTab == 'sec'">
                <div class="main-top">
                    <span>김성민</span>님의 목표 자산 포트폴리오
                    <div class="pie-chart">
                        <Pie :data="chartData" :options="options" />
                    </div>
                    <hr>
                </div>
                <div id="port-select">
                    <button>목표 비율 설정</button>
                    <button>내 자산 입력</button>
                </div>
                <div class="main-bottom">
                    <div>
                        <div class="my-box">
                            <table>
                                <thead>
                                    <colgroup>
                                        <col width="10%" />
                                        <col width="40%" />
                                        <col width="10%" />
                                        <col width="40%" />
                                    </colgroup>
                                </thead>
                                <tbody>
                                    <h3>월별 목표 배당금</h3>
                                    <Bar :data="divchartData" :options="options"/>
                                </tbody>
                            </table>
                        </div>
                    </div>

                </div>
            
            </div>
            
        </div>
        </div>
        <div id="save" @click=updatePort()>
                        <span>설정 완료</span>
                    </div>
</template>

<script >
// import axios from 'axios';
import { Chart as ChartJS, ArcElement, Tooltip, Legend,Title,BarElement,CategoryScale,LinearScale } from 'chart.js'
import { Pie, Bar } from 'vue-chartjs'


ChartJS.register(ArcElement, Tooltip, Legend)
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)


export default {

    name: 'CreateView',
    components: {
        Bar,Pie
    },
    data() {
        return {
            stocks: [
                { name: "주식", percent: "" },
                { name: "채권", percent: "" },
                { name: "실물자산", percent: "" },
                { name: "가상화폐", percent: "" },
            ],
            selectedTab: "first",
            stock: '',
            bond: '',
            real_asset: '',
            crypto: '',
        }
    },
    computed: {
        chartData() {
            const checkedStockNames = this.stocks.map(stock => stock.name);
            const checkedStockPrices = this.stocks.map(stock => Number(stock.percent));
            return {
                labels: checkedStockNames,
                datasets: [
                    {
                        backgroundColor: ['#41B883', '#E46651', '#00D8FF', '#DD1B16'],
                        data: checkedStockPrices
                    }
                ],
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
      }
    },
    methods: {
    }
}
</script>

<style scoped>
tr:nth-child(odd) {
    background-color: #a5a5a5;
}

/* topbar */
#top-wrapper {
    text-align: left;
    height: 30px;
    font-size: 15px;
    padding-left: 5px;
}

/* main */
#main div {
    padding-top: 5px;
    font-size: 16px;
}

#main div span {
    font-weight: bold;
}

.main-top {
    text-align: center;
    height: 200px;
}

.pie-chart {
    display: inline-block;
    height: 150px;
    margin: 0;
}

.main-bottom {
    width: 100%;
}

#port-select {
    text-align: center;
}

#port-select button {
    float: left;
    border-radius: 8px;
    background-color: transparent;
    font-size: 12px;
    width: 100px;
    height: 30px;
    margin-right: 10px;
}

.my-box table {
    width: 100%;
}

.my-box table th {
    text-align: left;
    padding-top: 10px;
}

.question {
    padding-right: 10px;
}

.percent {
    width: 100px;
    height: 25px;
}

#save {
    position: fixed;
    width: 100%;
    bottom: 43px;
    left: 0px;
    text-align: center;
    padding-bottom: 8px;
    background-color: #4868E1;
    margin-top: 15px;
    color: white;
}</style>