console.log("hello world")

let x = 10

console.log("X is ", x)


// Variable Declaration Practice
const name = "kalyan";
console.log(name);
let age = 31;
console.log(age)

let skills = ['python', 'rust']
console.log(skills)

let kalyan = {
    "name": name,
    "age": age,
    "skills": skills
}

console.log(kalyan)


// Type conversions

let a = 10
console.log("a as a number: ", a);
let b = String(a)
console.log("a as a string: ", b);
let c = Number(b)
console.log("b as a number: ", c);
console.log(`Type of a: ${typeof a}, Type of b: ${typeof b}, Type of c: ${typeof c}`)


// Playing with lists

let fruits = ['apple', 'banana', 'mango', 'orange']

console.log(fruits)

fruits.push("grapes")
console.log("After pushing grapes", fruits)

fruits.unshift("kiwi")
console.log("After unshifting kiwi", fruits)

fruits.pop()
console.log("After popping", fruits)

fruits.shift()
console.log("After shifting", fruits)

console.log("Length of fruits: ", fruits.length)

console.log("value at index 0", fruits[0])

console.log("Value at index len - 1", fruits[fruits.length - 1])

let array1 = [1, 2, 3]
let array2 = [4, 5, 6]

let combined = array1.concat(array2)
