import { useState, useEffect} from 'react';
import api from "../../services/Api_service"
import Chart from "react-apexcharts"
import { Text, Center, Box, position } from '@chakra-ui/react'

const state = {
          
  series: [{
    name: "Ocupado",
    data: [10, 41, 35, 51]
    },
    {name: "Espera",
    data: [41, 35, 51, 49]}],
    options: {
      tooltip: {
        enabled: false,
      },
    chart: {
    
      height: 350,
      type: 'line',
      zoom: {
        enabled: false
      },
      animations: {
        enabled: false,
      },
      toolbar: {
        show: false
      } 
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight'
    },
    title: {
      text: 'Ocupação e Espera',
      align: 'left'
    },
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['09:00', '10:00', '11:00', '12:00'],
    },
    yaxis: {
      title: {
        text: 'Segundos',
        style: {
          fontSize: '1em',
          fontWeight: 900
        }
      }
    },
    colors:['#028f76', '#b8b040']
  },


};



function MPO_0C(){
  
    const [date, setDate] = useState(0);
    if (date == 0){
      refresh()
    }
    ;
    
    function refresh(){
      api
      .get("/MPO_0C")
      .then((response) => setDate(response.data.MPO_0C))
      .catch((err) => {
        console.error("ops! ocorreu um erro" + err);
    })}

    useEffect(() =>{
      const timerId = setInterval(refresh, 1000);
      return function cleanup() {
        clearInterval(timerId);
      };
    }, []); 
    
    return(
      <div>
        <Box border="2px" boxShadow='lg' borderRadius='lg' borderColor="#6F6" padding={'0 1em 0 1em'} height={300} width={450} m='1em 0 0 0'>
        <Center>
          <Text fontSize='1.5em' padding={'0.5em 0 0 0'} as='b'>MPO</Text>
        </Center>
      <Chart options={state.options} series={date} type="line" height='75%' width='100%'/>
      </Box>
      </div>
      
    );

    }export default MPO_0C;