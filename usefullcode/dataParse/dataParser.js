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
