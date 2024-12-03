import React, {useEffect, useState} from 'react'
import Header from '../hooks/Header.tsx'
import { Bar } from 'react-chartjs-2';
// big import statement for chart.js
import {Chart as ChartJS, CategoryScale,  LinearScale, BarElement, Title, Tooltip, Legend,} from 'chart.js';
ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);


async function fetchDates() {
    try {
        const response = await fetch('https://api.nasa.gov/DONKI/FLR?startDate=yyyy-MM-dd&endDate=yyyy-MM-dd&api_key=ie1u4oQ3dmPsFT8RbgQIXwbSpo0pg8d733WuRss3');
        const data = await response.json();
        
        const flareTimes = data.map((flare: any) => flare.beginTime);
        console.log(flareTimes);
        return flareTimes;

    } catch (error) {
        console.log(error.message);
    }
}

const Dashboard = () => {
    const username: string = localStorage.getItem('username') || "";
    const [occurrences, setOccurrences] = useState<Map<string, number>>(new Map())

    // ensure flare data is fetched once upon page load
    useEffect(() => {
        async function pageLoad() {
            const times = await fetchDates();
            let occurrences_: Map<string, number> = new Map();
            for (let time of times) {
                const formattedTime: string = new Date(time).toLocaleDateString('en-US');
                if (occurrences_.has(formattedTime)) {
                    // ! is a non-null assertion operator to appease TS
                    occurrences_.set(formattedTime, occurrences_.get(formattedTime)! + 1);
                } 
                else {
                    occurrences_.set(formattedTime, 1);
                }
            }
            setOccurrences(occurrences_);

        }
        pageLoad();
        console.log(occurrences);
    }, []);

    const chartData = {
        labels: Array.from(occurrences.keys()),
        datasets: [{
            label: 'Flare Occurrences',
            data: Array.from(occurrences.values()),
            backgroundColor: 'rgba(60, 60, 60, 1)',
        }]
    };

    const chartOptions = {
        plugins: {
            title: {
                display: true,
                text: 'Solar Flare Occurrences',
            },
        },
    };


    return (
        <div>
            <Header username={username}/>
            <div className="font-source-code">
                <Bar data={chartData} options={chartOptions}/>
            </div>
        </div>
    )
}

export default Dashboard;