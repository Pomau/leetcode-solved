/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    ans = init;
    nums.forEach(function(el) {
        ans = fn(ans, el);
    });
    return ans
};