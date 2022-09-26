import React from "react";
import { useQuery } from 'react-query';
import Navbar from '../components/Navbar'
import VehicleDetail from '../components/VehicleDetail'

//Material UI Imports
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'


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
    console.log(data)
    const results = data.map((vehicle) => 
    <VehicleDetail
        key={vehicle.id}
        vehicleMake={vehicle.vehicle_make}
        vehicleModel={vehicle.vehicle_model}
        img={vehicle.image}
        pricePerDay={vehicle.price_per_day}
        seats={vehicle.seats}
        vehicleClass={vehicle.vehicle_class}
        vehicleType={vehicle.vehicle_type}
    />
        )
        
    return (
        <>
            <Navbar />
            <Box
            element='div'
            sx={{
                marginLeft: 20,
                marginTop: 2,
                marginBottom: 1,
            }}
            >
                <h1>Choose a Vehicle</h1>
            </Box>
            <Grid 
            container 
            justifyContent='center'
            alignItems='center'
            >
                <Grid item>
                    <Box>
                        {results}
                    </Box>
                </Grid>
            </Grid> 
        </>
    )
}
