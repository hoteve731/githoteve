let msg = 'Hello';

console.log('함수 호출 전');
console.log(msg) //당연히 Hello만 출력된다. 

function sayHello(name){
	if(name){
		msg += ', ' + name;
	}
    console.log('함수 내부');
    console.log(msg);//함수 밖에서 정의된 전역변수가 name을 Mike로 정의한다. 그렇기에 함수 내에서의 출력도 hello mike가 된다. 
}

sayHello('Mike'); //전역변수 정의

console.log('함수 호출 후');
console.log(msg); //함수 밖에서의 출력은 당연히 전역변수 mike를 받아 hello mike를 출력한다. 