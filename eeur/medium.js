//https://edabit.com/challenge/N7PGFudDcNh5aueS3

// use cords to check for ones
function isAdjacent(matrix, node1, node2) {
    return matrix[node1][node2] === 1
}


//how much is true https://edabit.com/challenge/GLbuMfTtDWwDv2F73

function countTrue(arr) {
	var i
	var count = 0
	 for (i = 0; i < arr.length; i++) {
		 if (arr[i] == true) {
			 count++
		 }
	 }
	return count
}

//Finding the second largest number https://edabit.com/challenge/3zAT89ZAxg4CAQqsZ

//go thorugh and get the largerst number and pop it. Go through againg to get the max. 


function secondLargest(arr) {
	const largest = Math.max(...arr)
	const newArr = arr.filter(num=> num !== largest)

	return Math.max(...newArr)
}



// https://edabit.com/challenge/TDpT9tvwJK5uLn98h

function sameCase(str) {
	if (str === str.toUpperCase() || str === str.toLowerCase()){
		return true
	}
	else {
		return false
	}
}