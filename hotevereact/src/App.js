import React from 'react';
import "./App.css";
import Counter from './Counter';
import Music from './Music';
import { Link, Route, Routes } from "react-router-dom";
import page1 from './pages/page1';
import page2 from './pages/page2';
import Home from './pages/Home';
import menubar from './pages/menubar';

const App = () => {
  return(
    <>
     <div className='navbutton'>
      <button><Link to = '/page1'>페이지1</Link></button>
      <button><Link to = '/page2'>페이지2</Link></button>
      <button><Link to = '/home'>홈</Link></button>
  
    </div>
    <Routes>
      <Route path = '/' element = {<menubar />}>
        <Route path = '/home' element = {<Home />}></Route>
        <Route path = '/page1' element = {<page1 />}></Route>
        <Route path = '/page2' element = {<page2 />}></Route>
      </Route>
    </Routes>

   
    
    <Counter />
    <Music />
      
    </>
    
  );
}

export default App;








      
 