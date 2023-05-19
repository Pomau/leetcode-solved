/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    chunks = []
    count = 0
    for (let i = 0; i < arr.length; i++) {
        if (count == 0) {
            chunks.push([])
        }
        chunks[chunks.length - 1].push(arr[i])
        count = (count + 1) % size
    }
    return chunks
};
