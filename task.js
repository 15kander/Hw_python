// N1:
console.log("Hello, JavaScript!");


// N2:
let name = 'Iskander'
let age = 16
let city = 'Nukus'
console.log(`Name: ${name}   |   Age: ${age}   |   City: ${city}`);

// N3:
let a = 0;
let b = 1;
[a, b] = [b, a];
console.log(a, b);

// N4:
let n1 = 25;
let n2 = 11;
console.log(`sum of n1 and n2 == ${n1+n2}`);

// N5:
let na = 25;
let nb = 11;
console.log(na-nb);

// N6:
let nc = 25;
let ne = 11;
console.log(nc*ne);

// N7:
let q = 25;
let p = 11;
console.log((q/p).toFixed(2));

// N8:
let n = 16
let nn = 5
console.log(n%nn);

// N9:
let number = 123
console.log(number%2==0);

// N10:
let num = 5;
if (num > 0) {
    console.log("Положительное");
} else if (num < 0) {
    console.log("Отрицательное");
} else {
    console.log("Ноль");
}

// N11:
let a11 = 10, b11 = 20;
console.log(Math.max(a11, b11));

// N12:
let a12 = 5, b12 = 12, c12 = 8;
console.log(Math.max(a12, b12, c12));

// N13:
let age2 = 20;
console.log(age >= 18 ? "Совершеннолетний" : "Несовершеннолетний");

// N14:
let n14 = 15;
console.log(n14 % 3 === 0 && n14 % 5 === 0);

// N15:
let month = 3;
const months = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"];
console.log(months[month - 1]);

// N16:
let day = 1;
const days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"];
console.log(days[day - 1]);

// N17:
let year = 2024;
console.log((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0));

// N18:
let x18 = 10, y18 = 5, op = '+';
let res18 = op === '+' ? x18 + y18 : op === '-' ? x18 - y18 : op === '*' ? x18 * y18 : x18 / y18;
console.log(res18);

// N19:
let val = 45;
console.log(val >= 10 && val <= 100);

// N20:
let score = 75;
let grade = score >= 90 ? 'A' : score >= 70 ? 'B' : score >= 50 ? 'C' : 'F';
console.log(grade);

// N21:
for (let i = 1; i <= 100; i++) { console.log(i); }

// N22:
for (let i = 100; i >= 1; i--) { console.log(i); }

// N23:
for (let i = 2; i <= 100; i += 2) { console.log(i); }

// N24:
for (let i = 1; i <= 100; i += 2) { console.log(i); }

// N25:
let sum25 = 0; 
for (let i = 1; i <= 100; i++) sum25 += i; 
console.log(sum25);

// N26:
let sumEven = 0; 
for (let i = 2; i <= 100; i += 2) sumEven += i; 
console.log(sumEven);

// N27:
let base = 5; 
for (let i = 1; i <= 10; i++) console.log(`${base} * ${i} = ${base * i}`);

// N28:
for (let i = 1; i <= 10; i++) { 
    for (let j = 1; j <= 10; j++) { 
        console.log(`${i} * ${j} = ${i * j}`); 
    } 
}

// N29:
let numFact = 5, fact = 1; 
for (let i = 1; i <= numFact; i++) fact *= i; 
console.log(fact);

// N30:
let numDigits = 12345; 
console.log(String(numDigits).length);

// N31:
let arr31 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]; 
arr31.forEach(el => console.log(el));

// N32:
let sumArr = [1, 2, 3, 4, 5].reduce((a, b) => a + b, 0); 
console.log(sumArr);

// N33:
let nums33 = [10, 20, 30, 40]; 
let avg = nums33.reduce((a, b) => a + b, 0) / nums33.length; 
console.log(avg);

// N34:
let maxArr = [5, 12, 3, 8]; 
console.log(Math.max(...maxArr));

// N35:
let minArr = [5, 12, 3, 8]; 
console.log(Math.min(...minArr));

// N36:
let countArr = [1, 2, 3, 4, 5, 6].filter(n => n % 2 === 0).length; 
console.log(countArr);

// N37:
let posArr = [-2, 5, 0, 10, -3].filter(n => n > 0); 
console.log(posArr);

// N38:
let orig = [1, 2, 3, 4]; 
let rev = []; 
for (let i = orig.length - 1; i >= 0; i--) rev.push(orig[i]); 
console.log(rev);

// N39:
let duplicates = [1, 2, 2, 3, 4, 4, 5]; 
let unique = [...new Set(duplicates)]; 
console.log(unique);

// N40:
let arrNums = [10, 5, 20, 8, 20]; 
let uniqueArr = [...new Set(arrNums)].sort((a, b) => b - a); 
console.log(uniqueArr[1]);

// N41:
const add = (x, y) => x + y; 
console.log(add(5, 3));

// N42:
const isEven = n => n % 2 === 0; 
console.log(isEven(4));

// N43:
const maxInArr = arr => Math.max(...arr); 
console.log(maxInArr([1, 5, 3]));

// N44:
const reverseStr = str => str.split('').reverse().join(''); 
console.log(reverseStr("hello"));

// N45:
const isPalindrome = str => str === str.split('').reverse().join(''); 
console.log(isPalindrome("radar"));

// N46:
let str = 'Js is one of popular lang for programing';
const vowels = 'aoeuiAOEUI';

const countVowels = () => {
    let c =0;
    for (let ch of str) {
        if (vowels.includes(ch)) {
            c++;
        }
    }
    return c;
}
console.log(countVowels());

// N47:
let str47 = 'Js is one of popular lang for programing';
let sentns = str47.split(' ')
const LongestWord = ()=>{
    let longW = sentns.reduce((a,b)=>b.length>a.length? b:a,"")
    return longW
}   
console.log(LongestWord());

// N48:
let user = { 
    name: "Alex", 
    age: 25, 
    email: "alex@mail.com", 
    info() { console.log(`${this.name}, ${this.age}, ${this.email}`); } 
}; 
user.info();

// N49:
let products = [
    {name: 'laptop', price: 159, category: 'technique'},
    {name: 'sofa', price:79, category:'furniture'}
]
let cheap = products.filter(p=>p.price<100)
console.log(cheap);

// N50:
let users = [
    { name: "Anna", age: 22 }, 
    { name: "Bob", age: 17 }, 
    { name: "Charlie", age: 30 }
]
let adults = users.filter(u=>u.age>18).map(u=>u.name)
console.log(adults);
