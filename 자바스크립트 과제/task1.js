function sayHello(name){ //sayHello라는 함수 정의, 매개변수 name 그러나 정의되어 호출되지 않음-> undefined
	let msg = `Hello`; //msg 변수 안에 'Hello' 스트링 삽입
	if(name){ //name이 정의되지 않았다. 
		msg = `Hello, ${name}`; //if의 조건이 정의되지 않기에 실행되지 않는다. 지역변수?
	}
	console.log(msg);//'Hello'를 출력한다. 함수 내에서 출력 명령-> 함수 내에서 따로 지역변수(name)가 정의되지 않았기 때문
}

sayHello(); //전역변수에서도 name이 정의되지 않았다

/*결국 이 함수는 msg 안에 hello를 넣고 그것을 출력하는 역할만 한다.
그래서 Hello만 출력된다.*/