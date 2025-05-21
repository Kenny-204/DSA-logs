// what i tried that worked

var containsDuplicate = function (nums) {
  const set = new Set();

  return !(set.size === nums.length);
};

// the solution thats faster
var containsDuplicate = function (nums) {
  const set = new Set();

  for (i = 0; i < nums.length; i++) {
    if (set.has(nums[i])) return true;

    set.add(nums[i]);
  }
  return false;
};
