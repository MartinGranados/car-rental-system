// Imports
import React, { useState, useRef } from "react";

// Material.UI Imports
import Button from '@mui/material/Button'
import Grid from '@mui/material/Grid'
import Box from '@mui/material/Box'
import TextField from '@mui/material/TextField'
import Popover from '@mui/material/Popover'


export default function Login() {
    const [anchorEl, setAnchorEl] = useState(null)
    const form = useRef();

    const handleClick = (e) => {
        setAnchorEl(e.currentTarget)
    }
    
    const handleClose = () => {
        setAnchorEl(null)
    }

    const open = Boolean(anchorEl)
    const id = open ? 'login-popover' : undefined
    return (
        <>
            <Button
            onClick={handleClick}
            size='large'
            sx={{
                color: 'white',
                backgroundColor: null,
                border: 1,
                borderRadius: 5,
            }}>
                Sign In / Join
            </Button>
            <Popover
            id={id}
            open={open}
            anchorEl={anchorEl}
            onClose={handleClose}
            anchorOrigin={{
                vertical: 'bottom',
                horizontal: 'center'
            }}
            transformOrigin={{
                vertical: 'top',
                horizontal: 'right',
            }}>
                <Box
                sx={{
                    padding: 3,
                }}>
                    <Grid container>
                        <Grid item>
                            <h3>
                                Sign In to Bronco Rental System
                            </h3>
                            <Grid item>
                                <TextField 
                                label='Email'
                                sx={{
                                    marginTop: 3,
                                    marginBottom: 1,
                                }}>
                                </TextField>
                            </Grid>
                            <Grid item>
                                <TextField label='Password'></TextField>
                            </Grid>
                            <Button
                            sx={{
                                backgroundColor: '#255dcc',
                                color: 'white',
                                height: 55,
                                borderRadius: 4,
                                margin: 1,
                            }}>
                                Sign In
                            </Button>
                            <Grid item>
                                <p>Dont have an account yet? <Button>Click Here</Button></p>
                            </Grid>
                        </Grid>
                    </Grid>
                </Box>
            </Popover>
        </>
    )
}