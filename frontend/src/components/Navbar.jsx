// Imports
import React from 'react';
import {Link} from 'react-router-dom'

// Material.UI Imports
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Grid from '@mui/material/Grid'
import ButtonGroup from '@mui/material/ButtonGroup';


export default function Navbar () {
       return (
        <Box
        sx={{
            width: 'auto',
            height: (window.innerHeight / 10),
            backgroundColor: '#255dcc',
        }}>
            <Grid container 
            sx={{
                alignItems: 'center',
                padding: 1,
                justifyContent: 'space-between'
            }}>
                <Grid item>
                    <ButtonGroup 
                    sx={{
                        justifyContent: 'space-between',
                        marginLeft: 10,
                    }}>
                        <Button 
                        sx={{
                            color: 'white',
                            backgroundColor: null,
                            fontWeight: 'bold',
                            fontSize: 18
                        }}>Bronco Rental System
                        </Button>
                        <Link to='/'>
                            <Button
                            sx={{
                                color: 'white',
                                backgroundColor: null,
                            }}>Home
                            </Button>
                        </Link>
                    </ButtonGroup>
                </Grid>
                <Grid item>
                    <ButtonGroup
                    sx={{
                        marginRight: 10,
                        justifyContent: 'space-between'
                    }}>
                        <Button 
                        sx={{
                            color: 'white',
                            backgroundColor: null,
                        }}>Sign In</Button>
                        <Button 
                        sx={{
                            color: 'white',
                            backgroundColor: null,
                        }}>Register</Button>
                    </ButtonGroup>
                </Grid>
            </Grid>
        </Box>
       )
}

