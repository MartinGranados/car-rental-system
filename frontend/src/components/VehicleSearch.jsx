//Imports
import React from "react";
import {Link} from 'react-router-dom'

// Material.UI Imports
import Box from '@mui/material/Box'
import Grid from '@mui/material/Grid'
import Paper from '@mui/material/Paper'
import Button from '@mui/material/Button'
import TextField from '@mui/material/TextField'
import InputLabel from '@mui/material/InputLabel'
import MenuItem from '@mui/material/MenuItem'
import FormControl from '@mui/material/FormControl'
import Select from '@mui/material/Select'
// Icon Imports
import ArrowRightAltIcon from '@mui/icons-material/ArrowRightAlt'
// Date & Time Imports
import {AdapterDateFns} from '@mui/x-date-pickers/AdapterDateFns'
import {LocalizationProvider} from '@mui/x-date-pickers/LocalizationProvider'
import {TimePicker} from '@mui/x-date-pickers/TimePicker'
import {DesktopDatePicker} from '@mui/x-date-pickers/DesktopDatePicker'


export default function VehicleSearch() {
    const [value, setValue] = React.useState(new Date('2014-08-18T21:11:54'))
    const [vehicleType, setVehicleType] = React.useState('Show All')
    const [vehicleClass, setVehicleClass] = React.useState('Show All')
    const [seats, setSeats] = React.useState('Show All')

    const handleChange = (newValue) => {
        setValue(newValue)
    }

    const changeVehicleType = (event) => {
        setVehicleType(event.target.value)
    }

    const changeVehicleClass = (event) => {
        setVehicleClass(event.target.value)
    }

    const changeSeats = (event) => {
        setSeats(event.target.value)
    }

    return (
        <LocalizationProvider dateAdapter={AdapterDateFns}>
            <Box
            sx={{
                backgroundColor: 'white',
                height: 270,
                width: '80vw',
                zIndex: 1,
                borderRadius: 5,
                boxShadow: 10,
                borderBottom: 5,
                borderTop: 1,
                borderLeft: 2,
                borderRight: 2,
                borderColor: '#255dcc'
            }}>
                <Paper elevation={24} />
                <Grid container 
                sx={{
                    padding: 5,
                    alignItems: 'center',
                }}>
                    <Grid item>
                        <DesktopDatePicker 
                            label='Pick-up Date'
                            inputFormat='MM/dd/yyyy'
                            value={value}
                            onChange={handleChange}
                            renderInput={(params) => <TextField {...params} />}
                        />
                    </Grid>
                    <Grid item>
                        <TimePicker
                            label='Time'
                            value={value}
                            onChange={handleChange}
                            renderInput={(params) => <TextField {...params} />}
                        />
                    </Grid>
                    <Grid item>
                        <ArrowRightAltIcon 
                        sx={{
                            fontSize: 50,
                        }}/>
                    </Grid>
                    <Grid item>
                        <DesktopDatePicker 
                            label='Return Date'
                            inputFormat='MM/dd/yyyy'
                            value={value}
                            onChange={handleChange}
                            renderInput={(params) => <TextField {...params} />}
                        />
                    </Grid>
                    <Grid item>
                        <TimePicker
                            label='Time'
                            value={value}
                            onChange={handleChange}
                            renderInput={(params) => <TextField {...params} />}
                        />
                    </Grid>
                </Grid>
                <Grid container spacing={4}
                sx={{
                    paddingBottom: 10,
                    paddingLeft: 5,
                    alignItems: 'center',
                }}>
                    <Grid item>
                        <Box 
                        sx={{minWidth: 120}}>
                            <FormControl fullWidth>
                                <InputLabel>Vehicle Type</InputLabel>
                                <Select
                                    value={vehicleType}
                                    label='Vehicle Type'
                                    onChange={changeVehicleType}
                                >
                                    <MenuItem value='Show All'>Show All</MenuItem>
                                    <MenuItem value='Car'>Car</MenuItem>
                                    <MenuItem value='Truck'>Truck</MenuItem>
                                    <MenuItem value='Van'>Van</MenuItem>
                                    <MenuItem value='SUV'>SUV</MenuItem>
                                </Select>
                            </FormControl>
                        </Box>
                    </Grid>
                    <Grid item>
                        <Box 
                        sx={{minWidth: 120}}>
                            <FormControl fullWidth>
                                <InputLabel>Vehicle Class</InputLabel>
                                <Select
                                    value={vehicleClass}
                                    label='Vehicle Class'
                                    onChange={changeVehicleClass}
                                >
                                    <MenuItem value='Show All'>Show All</MenuItem>
                                    <MenuItem value='Economy'>Economy</MenuItem>
                                    <MenuItem value='Standard'>Standard</MenuItem>
                                    <MenuItem value='Sport'>Sport</MenuItem>
                                    <MenuItem value='Luxury'>Luxury</MenuItem>
                                </Select>
                            </FormControl>
                        </Box>
                    </Grid>
                    <Grid item>
                        <Box 
                        sx={{
                            minWidth: 120,
                        }}>
                            <FormControl fullWidth>
                                <InputLabel>Seats</InputLabel>
                                <Select
                                    value={seats}
                                    label='seats'
                                    onChange={changeSeats}
                                >
                                    <MenuItem value='Show All'>Show All</MenuItem>
                                    <MenuItem value={2}>2</MenuItem>
                                    <MenuItem value={4}>4</MenuItem>
                                    <MenuItem value={5}>5</MenuItem>
                                    <MenuItem value={6}>6</MenuItem>
                                    <MenuItem value={7}>7</MenuItem>
                                    <MenuItem value={12}>12</MenuItem>
                                </Select>
                            </FormControl>
                        </Box>
                    </Grid>
                    <Grid item>
                        <Link to='/results'>
                            <Button
                            sx={{
                                backgroundColor: '#255dcc',
                                color: 'white',
                                height: 55,
                                borderRadius: 5,
                            }}>Search Vehicles
                            </Button>
                        </Link>
                    </Grid>
                </Grid>
            </Box>
        </LocalizationProvider>
    )
}