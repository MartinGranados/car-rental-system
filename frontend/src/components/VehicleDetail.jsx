//Imports
import React from "react";

//Material.UI Imports
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'



export default function VehicleDetail(props) {
    
    return (
        <>
            <Box 
            sx={{
                borderTop: 2,
                borderColor: '#255dcc',
                width: '50vw',
            }}>
                <Grid 
                container
                direction='row'
                justifyContent='space-between'
                alignItems='center'>
                    <Grid item>
                        <Box 
                            component='img'
                            alt='Image of car'
                            src={props.img}
                            xs={4}
                        sx={{
                            height: '30vh'
                        }}>
                        </Box>
                    </Grid>
                    <Grid item>
                        <Box>
                            <h2>{props.vehicleMake}</h2>
                            <h3>{props.vehicleModel}</h3>
                            <br/>
                            <h6>Seats/{props.seats} | Class/{props.vehicleClass}</h6>
                        </Box>
                    </Grid>
                    <Grid 
                    item
                    sx={{
                        marginLeft: 5,
                    }}>
                        <Box>
                            <h4>Price Per Day | {props.pricePerDay}</h4>
                            <Button
                            sx={{
                                backgroundColor: '#255dcc',
                                color: 'white',
                                height: 40,
                                borderRadius: 5,
                                marginLeft: 10,
                                marginTop: 1,
                            }}>Select</Button>
                        </Box>
                    </Grid>
                </Grid>
            </Box>
        </>
    )
}
