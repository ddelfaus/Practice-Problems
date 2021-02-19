import React, { useState, useEffect, useRef } from "react";
import { connect } from "react-redux"
import { createChart, TickMarkType } from 'lightweight-charts'
import ReactDOM from "react-dom";
import Chart from 'kaktana-react-lightweight-charts'

function FiveMinChart(props) {
    
   

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
        data: props.fiveMinData

    }]



    return (
        <>


            <Chart options={options} candlestickSeries={candlestickSeries} autoWidth height={320} />


        </>
    )
}

const mapStateToProps = state => {
    return {
        fiveMinData: state.ChartReducer.fiveMinData
    }
}

export default connect(
    mapStateToProps, {}
)(FiveMinChart)