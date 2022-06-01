import React, { useState } from 'react';

function Music() {
  let [music, setMusic] = useState(["I've - Love Dive",'(G)-Idle - Tomboy','Le Sserafim - FEARLESS']);
  return(
    <div className='musiclist'>
      <h1 className='hi'>저의 최애 곡들을 소개합니다!</h1>
      <div className='musicname'>
        <li>{music[0]}</li>
        <li>{music[1]}</li>
        <li>{music[2]}</li>
      </div>
      

      <button className='button' onClick = {()=>{
          setMusic(["이걸 클릭하네",'(G)-Idle - Tomboy','Le Sserafim - FEARLESS']);
      }}>클릭해보세요</button>
    </div>
  );
};

export default Music;