import axios from 'axios'
import {types} from './index'


const {

GET_STOCK_DATA_START,
GET_STOCK_DATA_SUCCESS,
GET_STOCK_DATA_FAILURE
} = types;






export const getStockData =() => dispatch => {
    dispatch({type: GET_STOCK_DATA_START});
    return axios
        .get(`http://192.168.1.7:62500/api/stocks/TSLA/minutes?period_start=1613019600&period_end=1613106000/`)
        .then(res => {
            dispatch({type:GET_STOCK_DATA_SUCCESS, payload: parseData(res.data)},console.log(res.data))
        })
        .catch(err => {
            dispatch({type:GET_STOCK_DATA_FAILURE, payload: err})
        })
}


function parseData(data){   
    const headers = ["time", "open", "high", "low", "close"].splice(',')   
    
    const dataArray = []
    let i = 0
    if (data.length <= 0 ) {
        return
    } 
    for (i = 0; i < data.length; i++) {
        const newData = data[i].splice(',')
        let newObj = {}
        for(let j = 0; j< newData.length -1  ; j++){

            newData[0] = parseInt(newData[0])
            if(j > 0){

                newData[0] =(new Date(newData[0] * 1000))
                newData[j] = Number(newData[j])
                newObj[headers[j]] = newData[j]
            
            }else{
                newObj[headers[j]] = newData[j]    }     
        }
        dataArray.push(newObj);

    }
    return dataArray
}