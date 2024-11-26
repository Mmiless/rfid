import React, {useEffect, useState} from 'react';
import { useNavigate } from "react-router-dom";

import Header from '../hooks/Header.tsx';

const AccessDenied = () => {
    const navigate = useNavigate();
    // Continuously poll the server to check if the user is logged in
    useEffect(() => {
        const poll = async () => {
            let running: boolean = true;

            while(running){
                try {
                    const response = await fetch('http://localhost:3000/api/isLoggedIn', {
                        method: 'POST',
                            headers: {
                                'Content-Type': 'application/json',
                            },
                    });
                    if(response.ok) {
                        const data = await response.json();
                        if(data.loggedIn === 1) {
                            running = false;
                            const uName: string = data.username;
                            localStorage.setItem('username', uName);
                            navigate('/Dashboard');
                        }
                        else continue;
                    }
                } catch (error){
                    console.log(error.message);
                }
                // 2 second delay to avoid request spam
                await new Promise((resolve) => setTimeout(resolve, 2000))
            }  
        };

        poll();

    }, [navigate]);

    return (
        <div>
            <Header username={""}/>
            <div className="flex flex-col items-center justify-center h-[calc(100vh-74px)] mx-auto">
                <div className="font-source-code text-3xl">Access Denied</div>
                <div className="font-source-code text-2xl">Scan ID</div>
            </div>
        </div>
    );
}

export default AccessDenied;