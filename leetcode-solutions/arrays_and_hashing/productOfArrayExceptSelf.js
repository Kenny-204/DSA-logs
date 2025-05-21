const nums = [-1, 1, 0, -3, 3];
// const nums = [1, 2, 3, 4];

const productExceptSelf = function (nums) {
  let output = [];
  for (let i = 0; i < nums.length; i++) {
    let trim = nums.slice(0, i).concat(nums.slice(i + 1));
    output.push(trim);
  }
  return output.map((el) => el.reduce((a, b) => a * b));
};

console.log(productExceptSelf(nums));
