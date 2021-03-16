GET_STOCK_DATA_SUCCESS,
GET_STOCK_DATA_FAILURE,
PARSE_FIVE_MIN_DATA
} = types;



const {

    GET_STOCK_DATA_START,
    GET_STOCK_DATA_SUCCESS,
    GET_STOCK_DATA_FAILURE,
    PARSE_FIVE_MIN_DATA
    } = types;
    
    
    
    
    
    
    export const getStockData =(stock) => dispatch => {
        
        dispatch({type: GET_STOCK_DATA_START});
        return axios
            .get(`http://192.168.1.7:62500/api/stocks/${stock}/minutes?period_start=1614004205`)
            .then(res => {
                dispatch({type:GET_STOCK_DATA_SUCCESS, payload: parseData(res.data)},console.log(stock, "eee"))
            })
            .catch(err => {
                dispatch({type:GET_STOCK_DATA_FAILURE, payload: err})
            })
    }
    
    export const parseFiveMinData =(data) => dispatch => {
        dispatch({type:PARSE_FIVE_MIN_DATA, payload: fiveMin(data)})
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
    
    
    
    
    function fiveMin(data){
        



export const getStockData =() => dispatch => {
    dispatch({type: GET_STOCK_DATA_START});
    return axios
        .get(`http://192.168.1.7:62500/api/stocks/TSLA/minutes?period_start=1614004205`)
        .then(res => {
            dispatch({type:GET_STOCK_DATA_SUCCESS, payload: parseData(res.data)},console.log(res.data))
        })
        .catch(err => {
            dispatch({type:GET_STOCK_DATA_FAILURE, payload: err})
        })
}

export const parseFiveMinData =(data) => dispatch => {
    dispatch({type:PARSE_FIVE_MIN_DATA, payload: fiveMin(data)})
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




function fiveMin(data){
    
    let i = 0 
    let count = 1
    const fiveMinArray = []
    let open
    let close
    let time
    for (i =0; i < data.length; i++) {
        if(data.time == null){
            console.log("pppooooop[popoop")
        }
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
  return(fiveMinArray)
    