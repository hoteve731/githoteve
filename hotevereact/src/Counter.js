import React, { useState } from 'react';

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
