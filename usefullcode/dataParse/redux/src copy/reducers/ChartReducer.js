import {types} from '../actions/index'

const {
GET_STOCK_DATA_START,
GET_STOCK_DATA_SUCCESS,
GET_STOCK_DATA_FAILURE,
} =types

const initialState = {
    
    OneMinData: [],
    isLoading: false
}


const ChartReducer = (state = initialState, {type, payload}) => {
    switch(type){
        //Get stock data
        case GET_STOCK_DATA_START:
            return {
                ...state,
                isLoading: true,
                error: '',
            }
        case GET_STOCK_DATA_SUCCESS:
            return {
                ...state,
                oneMinData: payload,
                
                isLoading: false,
                error: '',
                };
        case GET_STOCK_DATA_FAILURE:
            return {
                ...state,
                isLoading: false,
                error: payload,
            };
        default:
            return state


    }
}


export default ChartReducer 