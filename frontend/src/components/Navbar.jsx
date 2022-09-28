// Imports
import React from 'react';
import {Link} from 'react-router-dom';

// Material.UI Imports
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Paper from '@mui/material/Paper'
import Appbar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import AppBar from '@mui/material/AppBar';
import CarRentalIcon from '@mui/icons-material/CarRental';


export default function Navbar () {
    const barHeight = window.innerHeight / 10

       return (
        <Box
        sx={{
            flexgrow: 1,
            boxShadow: 1,
        }}>
            <AppBar 
            position='static'
            elevation={24}
            square={false}
            sx={{
            width: 'auto',
            height: barHeight,
            backgroundColor: '#255dcc',
            borderBottomLeftRadius: 5,
            borderBottomRightRadius: 5,
            }}>
                <Toolbar>
                    <CarRentalIcon 
                    sx={{
                        fontSize: 50,
                    }}/>
                    <Typography
                    className='logo-title'
                    variant='h1'
                    component='div'
                    sx={{
                        flexGrow: 1,
                        fontSize: 50,
                    }}>
                        <Link to='/'
                        style={{
                            textDecoration: 'none',
                            color: 'white',
                            backgroundColor: null,
                        }}>
                            Bronco Rental System
                        </Link>
                    </Typography>
                    <Button
                    sx={{
                        color: 'white',
                        backgroundColor: null,
                    }}>
                        Login
                    </Button>
                    <Button
                    sx={{
                        color: 'white',
                        backgroundColor: null,
                    }}>
                        Sign Up
                    </Button>
                </Toolbar>
            </AppBar>
            {/* <Grid container 
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
            </Grid> */}
        </Box>
       )
}

