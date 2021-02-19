import React, { useState, useEffect} from "react";
import { connect } from "react-redux"
import {getStockData} from "../actions/StockActions"
import OneMinChart from "../components/OneMinChart"


function ChartDashboard(props){
    

    useEffect(() => {
        props.getStockData()
        // parseData()
        console.log(props, "Data please")
    }, []);
    
   
    return (
        <>
            <OneMinChart oneMinData = {props.oneMinData} />
        </>
    )
}

const mapStateToProps = state => {
    return {
        oneMinData: state.ChartReducer.oneMinData,
        

    }
}


export default connect(
    mapStateToProps, {getStockData}
)(ChartDashboard)