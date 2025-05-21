const s = "Was it a car or a cat i saw?";

function isPalindrome(s) {
  let ss = s.replaceAll(/\W/g, "").toLowerCase();
  let start = 0;
  let end = ss.length - 1;
  while (start < end) {
    if (ss[start] !== ss[end]) {
      return false;
    } else {
      start++;
      end--;
    }
    return true;
  }
}

console.log(isPalindrome(s));
