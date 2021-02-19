import React, { useState, useEffect,useRef} from "react";
import axios from "axios"
import { createChart, TickMarkType } from 'lightweight-charts'
import ReactDOM from "react-dom";
import Chart from 'kaktana-react-lightweight-charts'



function OneMinChart(props){
    
    
    console.log(props, "One MIn Chart")
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
            data: props.oneMinData

          }]
        
    
  
        
    return(
        <>
        <Chart options={options} candlestickSeries={candlestickSeries} autoWidth height= {320}/>
        
        </>
    )
}


export default OneMinChart