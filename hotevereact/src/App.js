import React, { useState} from 'react';
import "./App.css";

function Counter () {
    const [num, setNum] = useState(0);
    function onClick(){
        setNum(num+1)
    };
    function onclick2(){
      setNum(num-1)
    };
    return(
      <>
        <div className='p1'>
            <h1 className='hi'>숫자세기 : {num} </h1>
            <button className='button' onClick={onClick}>+1</button>
            <button className='button' onClick={onclick2}>-1</button>
              
        </div>
      </>
    );
};
export default Counter;



// function musiclist() {
//   let [music, setMusic] = useState(["I've - Love Dive",'(G)-Idle - Tomboy','Le Sserafim - FEARLESS']);
//   return(
//     <div>
//       <h1>저의 최애 곡들을 소개합니다!</h1>
//       {setMusic}
//     </div>
//   );
// };




      
 