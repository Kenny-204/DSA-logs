const nums = [2, 3, 5];

// 235
// 127
// 21
// 157
// 22
class Nodel {
  prev;
  value;
  next;
  constructor(value) {
    this.value = value;
  }
}
const node = new Nodel(5)
const node3 = new Nodel(3)
node.next =node3
node3.prev = node


const map = new Map([])
map.set(5,node)
console.log(map.has(5))