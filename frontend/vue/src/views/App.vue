<template>
    <div class="container">
        <div id="main">
            <button @click="selectedTab = 'first'">차트 비교</button>
            <button @click="selectedTab = 'sec'">주식 포트폴리오 평가</button>
            <!-- <div v-if="selectedTab == 'first'"> -->
                <div>
                    <Pie :data="data1" :options="options" />
                </div>
                <div>
                    <Line :data="data" :options="options" />
                </div>
            <!-- </div> -->
        </div>
    </div>
</template>
  
<script>
import {
    Chart as ChartJS,
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
} from 'chart.js'
import { Line, Pie } from 'vue-chartjs'
import * as chartConfig from '../components/chartConfig.js'

ChartJS.register(
    CategoryScale,
    LinearScale,
    PointElement,
    LineElement,
    Title,
    Tooltip,
    Legend
)

export default {
    name: 'App',
    components: {
        Line, Pie
    },
    data() {
        return chartConfig
    },
    data1() {
        return chartConfig
    },

}
</script>