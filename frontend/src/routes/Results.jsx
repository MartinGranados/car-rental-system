import React from "react";
import { useQuery } from 'react-query';


async function fetchVehicles() {
    const res = await fetch('http://127.0.0.1:8000/api/')
    return res.json()
  }

export default function Results() {

    const { data, status} = useQuery('vehicles', fetchVehicles)

    if (status === 'loading') {
        return <p>Loading...</p>
    }
    
    if (status === 'error') {
        return <p>Error!</p>
    }

    return (
        <ul>
            {data.map((vehicle) => (
                <li key={vehicle.id}>`{vehicle.vehicle_make}, {vehicle.vehicle_model}, <img src={vehicle.image} />`</li>
            ))}
        </ul>
    )
}