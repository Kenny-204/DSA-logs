// const nums = [2, 7, 11, 15];
// const target = 9;

// const twoSum = function (nums, target) {
//   const map = new Map();
//   for (let i = 0; i < nums.length; i++) {
//     map[nums[i]] = target - nums[i];
//   }
//   for (let i = 0; i < nums.length; i++) {
//     for (j = 0; j < nums.length; j++) {
//       if (i != j && nums[i] + nums[j] == target) {
//         return [i, j];
//       }
//     }
//   }

// };
// console.log(twoSum(nums,target))
const nums = [3,3]
const target = 6;

const twoSum = function (nums, target) {
    const map = new Map();
    for(let i = 0;i<nums.length;i++){
        if ((target-nums[i]) in map) return [map[target-nums[i]],i]
        map[nums[i]] = i
      }
};

console.log(twoSum(nums, target));
// const nums = [3,3]
// const target = 6;

// const twoSum = function (nums, target) {
//   const map = new Map();
//   for (let i = 0; i < nums.length; i++) {
//     map[i] = nums[i]
//   }
// // const entries = Object.entries(map)
//   console.log(map);
//   for(let [key,value] of map.entries()){

//   }
// //   for (let i = 0; i < nums.length; i++) {
// //     if ((target - nums[i]) in map && (target - nums[i]) != nums[i]) return [map[target-nums[i]],i]
// //   }
// };

// console.log(twoSum(nums, target));
