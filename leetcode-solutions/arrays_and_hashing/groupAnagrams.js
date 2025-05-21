const strs = ["eat", "tea", "tan", "ate", "nat", "bat"];

function groupAnagrams(strs) {
  const anMap = new Map();
  let s;
  for (let i = 0; i < strs.length; i++) {
    s = strs[i].split("").sort().join("");
    if (s in anMap) {
      anMap[s] = [...anMap[s], strs[i]];
    } else {
      anMap[s] = [strs[i]];
    }
}

  return Object.values(anMap)
}
groupAnagrams(strs);
