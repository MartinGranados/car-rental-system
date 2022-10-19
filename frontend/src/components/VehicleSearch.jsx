//Imports
import React from "react";
import { Link } from 'react-router-dom';

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
import { AdapterDateFns } from '@mui/x-date-pickers/AdapterDateFns'
import { LocalizationProvider } from '@mui/x-date-pickers/LocalizationProvider'
import { TimePicker } from '@mui/x-date-pickers/TimePicker'
import { DesktopDatePicker } from '@mui/x-date-pickers/DesktopDatePicker'


export default function VehicleSearch() {
    
    const date = new Date();
    const currentDate = `${date.getMonth()+1}/${date.getDate()}/${date.getFullYear()}`;
    
    const [pickUpDate, setPickUpDate] = React.useState(currentDate)
    const [vehicleType, setVehicleType] = React.useState('showAll')
    const [vehicleClass, setVehicleClass] = React.useState('showAll')
    const [seats, setSeats] = React.useState('showAll')

    const [filters, setFilters] = React.useState({pickUpDate:pickUpDate, vehicleType:vehicleType, vehicleClass:vehicleClass, seats:seats})
    

    const changePickUpDate = (newValue) => {
        setPickUpDate(newValue)
        setFilters({
            pickUpDate: newValue,
            vehicleType: vehicleType,
            vehicleClass: vehicleClass,
            seats: seats,
        })
    }

    const changeVehicleType = (event) => {
        setVehicleType(event.target.value)
        setFilters({
            pickUpDate: pickUpDate,
            vehicleType: (event.target.value),
            vehicleClass: vehicleClass,
            seats: seats,
        })
    }

    const changeVehicleClass = (event) => {
        setVehicleClass(event.target.value)
        setFilters({
            pickUpDate: pickUpDate,
            vehicleType: vehicleType,
            vehicleClass: (event.target.value),
            seats: seats,
        })
    }

    const changeSeats = (event) => {
        setSeats(event.target.value)
        setFilters({
            pickUpDate: pickUpDate,
            vehicleType: vehicleType,
            vehicleClass: vehicleClass,
            seats: (event.target.value)
        })
    }
    
    const handleSubmit = (event) => {
        setFilters({
            pickUpDate: pickUpDate,
            vehicleType: vehicleType,
            vehicleClass: vehicleClass,
            seats: seats,
        })
        console.log(filters)
    }

    return (
        <LocalizationProvider dateAdapter={AdapterDateFns}>
            <Box
            sx={{
                backgroundColor: 'white',
                height: 270,
                width: '80vw',
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
                            value={pickUpDate}
                            onChange={changePickUpDate}
                            renderInput={(params) => <TextField {...params} />}
                        />
                    </Grid>
                    <Grid item>
                        <TimePicker
                            label='Time'
                            value={pickUpDate}
                            onChange={changePickUpDate}
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
                            value={pickUpDate}
                            onChange={changePickUpDate}
                            renderInput={(params) => <TextField {...params} />}
                        />
                    </Grid>
                    <Grid item>
                        <TimePicker
                            label='Time'
                            value={pickUpDate}
                            onChange={changePickUpDate}
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
                                    <MenuItem value='showAll'>Show All</MenuItem>
                                    <MenuItem value='car'>Car</MenuItem>
                                    <MenuItem value='truck'>Truck</MenuItem>
                                    <MenuItem value='van'>Van</MenuItem>
                                    <MenuItem value='suv'>SUV</MenuItem>
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
                                    <MenuItem value='showAll'>Show All</MenuItem>
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
                                    <MenuItem value='showAll'>Show All</MenuItem>
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
                        <Link to='/results' state={filters} className='search-button'>
                            <Button
                            onClick={handleSubmit}
                            sx={{
                                backgroundColor: '#255dcc',
                                color: 'white',
                                height: 55,
                                borderRadius: 4,
                            }}>Search Vehicles
                            </Button>
                        </Link>
                    </Grid>
                </Grid>
            </Box>
        </LocalizationProvider>
    )
}