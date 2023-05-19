/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    nums = []
    // console.log(fn(arr[0]))
    for (let i = 0; i < arr.length; i++) {
        //console.log(fn(arr[i]))
        if (fn(arr[i], i)) {
            nums.push(arr[i])
        }
    }
    return nums
};