import React from 'react';
import { Link, Outlet } from 'react-router-dom';

const Menubar = () => {
    return (
        <div>
            <button><link to = '/home'>홈</link></button>
            <button><link to = '/page1'>페이지1</link></button>
            <button><link to = '/page2'>페이지2</link></button>

            <Outlet />;
        </div>
    );
};

export default Menubar;