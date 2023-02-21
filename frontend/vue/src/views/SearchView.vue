<template>
  <div>
    <input type="text" id="stockName" v-model="searchText" @input="fetchData">
    <ul v-show="searchResults.length">
      <li v-for="(result, index) in searchResults" :key="index" @click="selectResult(result)">
        {{ result.label }}
      </li>
    </ul>
    <input type="hidden" id="stockCode" v-model="selectedResult.value">
    <div>Price: <span id="stockPrice">{{ selectedResult.price }}</span></div>
    <div>Market: <span id="market">{{ selectedResult.market }}</span></div>
    <div>Changes: <span id="changes">{{ selectedResult.changes }}</span></div>
    <div>Change Percentage: <span id="changepct">{{ selectedResult.changepct }}</span></div>
    <div>Stock Time: <span id="stockTime">{{ selectedResult.stockTime }}</span></div>
  </div>
</template>

<script>
import $ from 'jquery'
export default {
  data() {
    return {
      searchText: '',
      searchResults: [],
      selectedResult: {
        label: '',
        value: '',
        price: '',
        market: '',
        changes: '',
        changepct: '',
        stockTime: '',
        IndustryCode: '',
      },
      searchRequest: null,
    }
  },
  methods: {
    fetchData() {
      if (this.searchRequest) {
        this.searchRequest.abort()
      }
      if (this.searchText.length < 2) {
        this.searchResults = []
        return
      }
      this.searchRequest = $.ajax({
        url: "https://sedaily.com/Stock/Quote/JsonSearchData",
        type: "get",
        data: { text: this.searchText },
        success: (data) => {
          this.searchResults = data.Items.map((item) => {
            return {
              label: item.StockName + '(' + item.StockCode + ')',
              value: item.StockCode,
              price: item.CurrentPrice,
              market: (item.Market == 1) ? '코스피' : '코스닥',
              changes: (item.PreRate.indexOf('-') > 0) ? -item.PreGap : item.PreGap,
              changepct: item.PreRate,
              stockTime: item.StockTime,
              IndustryCode: item.IndustryCode,
            }
          })
        },
        dataType: "json",
      })
    },
    selectResult(result) {
      this.selectedResult = result
    },
  },
}
</script>
