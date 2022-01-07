function minSubArrayLen(arr, target){
    let minLen = 0;
    let total = 0;
    let tempLen = 0;
    
    let i = 0;
    while(i < arr.length){
        total += arr[i];
        tempLen++;
        i++;

        if(total >= target){
            if(!minLen) minLen = tempLen;
            minLen = Math.min(minLen, tempLen);
            total -= arr[i - tempLen];
            tempLen--;
            i--;
        }
    }
    return minLen;
}

console.log(minSubArrayLen([2,3,1,2,4,3], 7))