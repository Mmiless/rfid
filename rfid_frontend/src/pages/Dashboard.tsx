import React from 'react'
import Header from '../hooks/Header.tsx'

const Dashboard = () => {
    const username: string = localStorage.getItem('username') || "";

    return (
        <div>
            <Header username={username}/>
            <div className="font-source-code">Dashboard</div>
        </div>
    )
}

export default Dashboard;