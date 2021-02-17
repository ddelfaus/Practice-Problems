import React, { useState, useEffect,useRef} from "react";

import { createChart, TickMarkType } from 'lightweight-charts'
import ReactDOM from "react-dom";
import Chart from 'kaktana-react-lightweight-charts'

function FiveMinChart(props) {
    
    const [fiveMinData, setFiveMinData] = useState([])

    useEffect(()=> {
        fiveMin(props.dataArray)

        
    },[])

    function fiveMin(data){
        let i = 0 
        let count = 1
        const fiveMinArray = []
        let open
        let close
        let time
        for (i =0; i < data.length; i++) {
            let high = 1
            let low = 99999
            let fiveMinCandle = {}
            if (data[i].high >= high){
                high = data[i].high
               
            }
            if (data[i].low <= low){
                low = data[i].low
            }
            
            if(count < 5){
                
                if(count == 1){
                   
                    open = data[i].open
                    time = data[i].time
                }
                
                count += 1 
            }else{
                count = 1
                close = data[i].close
    
                fiveMinCandle = {
                    time: time,
                    open : open,
                    high : high,
                    low : low,
                    close : close
                }
                
                high = null
                low = null
                open = null
                close = null
                time = null

           
                fiveMinArray.push(fiveMinCandle)
            }
        }
        console.log(fiveMinArray)
        setFiveMinData(fiveMinArray)
        console.log(fiveMinData, "test")
    }

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
            data: fiveMinData

          }]



    return (
        <>
        <Chart options={options} candlestickSeries={candlestickSeries} autoWidth height= {320}/>
        </>
    )
}

export default FiveMinChart