const nums = [1, 1, 1, 2, 2, 3];
const k = 2;

const topKFrequent = function (nums, k) {
  const map = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] in map) {
      map[nums[i]]++;
    } else {
      map[nums[i]] = 1;
    }
  }
  const arr = Object.entries(map);
  const values = Object.values(map);
  const output = [];

  while (output.length < k) {
    let max = Math.max(...values);
    for (let [key, value] of arr) {
      if (value == max) {
        output.push(key);
      let i =   values.findIndex((el)=>el == value)
        values[i] = 0;

      }
    }
  }
  return(output);
};
topKFrequent(nums, k);


/*  const map = new Map();

    nums.forEach(n => {
        if (!map.has(n)) {
            return map.set(n, 1);
        }

        map.set(n, map.get(n) + 1);
    });

    let counters = Array.from(map.values());
    const numbers = Array.from(map.keys());
    let maxCount = Math.max(...counters);
    let result = [];

    while (result.length < k) {
        result = result.concat(numbers.filter(n => map.get(n) === maxCount));
        counters = counters.filter(c => c !== maxCount);
        maxCount = Math.max(...counters);
    }

    return result.slice(0, k); */