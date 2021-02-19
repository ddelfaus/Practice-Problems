import React, { useState, useEffect} from "react";
import { connect } from "react-redux"
import {getStockData, parseFiveMinData} from "../actions/StockActions"
import OneMinChart from "../components/OneMinChart"
import FiveMinChart from "../components/FiveMinChart"

function ChartDashboard(props){
    

    useEffect(() => {
        props.getStockData()
        // parseData()
        console.log(props, "Data please")
        props.parseFiveMinData(props.oneMinData)
    }, []);
    
   
    return (
        <>
            <OneMinChart oneMinData = {props.oneMinData} />
            <FiveMinChart/>
        </>
    )
}

const mapStateToProps = state => {
    return {
        oneMinData: state.ChartReducer.oneMinData,
   

    }
}


export default connect(
    mapStateToProps, {getStockData, parseFiveMinData}
)(ChartDashboard)