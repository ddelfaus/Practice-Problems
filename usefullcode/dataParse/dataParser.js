function parseData(data){   
    const headers = ["date", "open", "high", "low", "close", "volume"].splice(',')
    let i = 0
    const test = data[0][0]
    const dataObject =[]
    console.log(new Date(test* 1000), "date")

    for (i = 0; i < data.length; i++) {
        
        const newData = data[i].splice(',')
        const newObj = {}
     
        for(let j = 0; j< newData.length; j++){
            newData[0] =(new Date(newData[0] * 1000))
            newObj[headers[j]] = newData[j]
        }
       dataObject.push(newObj);
    }

    return dataObject





    
]

console.log(new Date(1612362600), "Date")

useEffect(() => {
    axios
    .get(`http://192.168.1.7:62500/api/stocks/GOOG/minutes`)
    .then(res =>{
        console.log(res.data, "data")
       
        // parseData(res.data,dataArray)
        // console.log(stockData, "stock data")
        // console.log(dataArray, "efaa")
    })  
    .catch(err => {
        console.log("There was an error, ", err)
    })

}, []);




return (
    <>
        <VictoryChart
            theme={VictoryTheme.material}
            domainPadding={{ x: 25 }}
            scale={{ x: "time" }}
        >
        <VictoryAxis tickFormat={(t) => `${t.getDate()}/${t.getMonth()}`}/>
        <VictoryAxis dependentAxis/>
        <VictoryCandlestick
            candleColors={{ positive: "#5f5c5b", negative: "#c43a31" }}
            data={data}
        />
        </VictoryChart>
     
    </>

)
}



const dataArray = []
const options = {
    chart: {
        type: 'candlestick',
        height: 350,
        animations: {
            enabled: false
        }
      },

      series: [{
        data: dataArray
          
      }],
      xaxis: {
        type: 'datetime'
      }

}

const dataArray =[]
const [loading, setLoading] = useState(true)
const [stockData, setStockData] = useState([])
const [stockArray, setStockArray] = useState([])
useEffect(() => {
    
    axios
    .get(``)
    .then(res =>{
        setStockData(res.data)
        
      
        
      return(stockData)
    }).then((res)=>{
        
        parseData(res,dataArray)
     

       return(setLoading(false))
        
    })  
    .catch(err => {
        console.log("There was an error, ", err)
    })
   
}, [loading]);


},[])
console.log(props)
const options = {
    alignLabels: true,
    // localization: {
    //     timeFormatter: function(TimeStamp) {
            
    //             return Date(TimeStamp)
          
    //     }
    // },
    timeScale: {
      rightOffset: 12,
      barSpacing: 3,
      fixLeftEdge: true,
      lockVisibleTimeRangeOnResize: false,
      rightBarStaysOnScroll: true,
      borderVisible: false,
      borderColor: "#fff000",
      visible: true,
      timeVisible: true,
      secondsVisible: false,
    //   tickMarkFormatter: (time, TickMarkType, locale => {
    //       console.log(time, TickMarkType, locale)
    //       const intraDay = LightweightCharts.isBusinessDay(time) ? time.intraDay
    //   })
    }
}
const candlestickSeries = [{
        data: props.dataArray

      }]
    