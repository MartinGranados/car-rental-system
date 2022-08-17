//Imports
import React from "react";

// Material.UI Imports
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid'
import Paper from '@mui/material/Paper'
import TextField from '@mui/material/TextField'
import {AdapterDateFns} from '@mui/x-date-pickers/AdapterDateFns'
import {LocalizationProvider} from '@mui/x-date-pickers/LocalizationProvider'
import {TimePicker} from '@mui/x-date-pickers/TimePicker'
import {DesktopDatePicker} from '@mui/x-date-pickers/DesktopDatePicker'

export default function VehicleSearch() {
    const [value, setValue] = React.useState(new Date('2014-08-18T21:11:54'))

    const handleChange = (newValue) => {
        setValue(newValue)
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
                <Grid container>
                    <Grid item>
                        <DesktopDatePicker 
                            label='Date desktop'
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
                        <DesktopDatePicker 
                            label='Date desktop'
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
            </Box>
        </LocalizationProvider>
    )
}