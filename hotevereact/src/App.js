import React from 'react';
import "./App.css";

import { Link, Route, Routes } from "react-router-dom";
import Page1 from './pages/Page1';
import Page2 from './pages/Page2';
import Home from './pages/Home';
// import menubar from './pages/Menubar';

const App = () => {
  return(
    <>
     <div className='nav'>
      <button className='navbutton'><Link to = '/page1'>페이지1</Link></button>
      <button className='navbutton'><Link to = '/page2'>페이지2</Link></button>
      <button className='navbutton'><Link to = '/home'>홈</Link></button>
    </div>
  

    <Routes>
        <Route path = '/home' element = {<Home/>} />
        <Route path = '/page1' element = {<Page1/>} />
        <Route path = '/page2' element = {<Page2/>}/>
    </Routes>

   
   
      
    </>
    
  );
}

export default App;








      
 