// const s = "ccac";
// const t = "aaca";

const s = "anagram";
const t = "naaragm";

// const validAnagram = function(s,t){
// return (s.split('').sort().join('') == t.split('').sort().join(''))
// }

const validAnagram = function (s, t) {
  const map = {};
  if (s.length !== t.length) return false;
  for (let i = 0; i < s.length; i++) {
    if (map[s[i]]) map[s[i]] = map[s[i]] + 1;
    else map[s[i]] = 1;
  }
  for (let i = 0; i < t.length; i++) {
    if (!map[t[i]]) return false;
    else map[t[i]] = map[t[i]] - 1;
  }
  return true;
};

console.log(validAnagram(s, t));
