function sayHello(name){ //sayHello라는 함수 정의, 매개변수 name
	let msg = `Hello`; //msg 변수 안에 'Hello' 스트링 삽입
	if(name){ //?? if의 조건이 정의되지 않는다.
		msg = `Hello, ${name}`; //if의 조건이 만족되지 않기에 실행되지 않는다
	}
	console.log(msg);//콘솔에 'Hello'를 출력한다
}

sayHello(); 
/*결국 이 함수는 msg 안에 hello를 넣고 그것을 출력하는 역할만 한다.
그래서 Hello가 실행된다.*/