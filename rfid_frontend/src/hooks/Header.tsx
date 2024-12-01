import React from 'react';
import {useNavigate} from 'react-router-dom';

const Header = ({username}) =>{
    const navigate = useNavigate();

    const handleLogout = async () => {
        // Send a POST request to the server to logout
        const username = localStorage.getItem('username');
        try {
            const response = await fetch('http://localhost:3001/log-out', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({name: username}),
            });
        } catch (error) {
        console.log(error.message);
        }
        localStorage.setItem('username', "");
        navigate("/")
    };

    username = username || "";
    return (
        <div className="flex flex-row sticky top-0 w-full bg-red-700 text-white py-4 px-6 shadow-md justify-between">
            <div className="px-10 font-source-code">RFID Dashboard</div>
            <div className='flex flex_row'>
                <div className="px-10 font-source-code pr-10">{username}</div>
                {username !== "" && (
                <div className="px-10 font-source-code cursor-pointer" onClick={handleLogout}>
                    Logout
                </div>
            )}
            </div>
        </div>
    );
};

export default Header;