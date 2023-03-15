import { useState, useEffect} from 'react';
import api from "../../services/Api_service"
import Chart from "react-apexcharts"
import { Text, Center, Box, position } from '@chakra-ui/react'

const state = {
          
  series: [77, 33],
  options: {
    labels: ['Reparados', 'Scrap'],
    chart: {
      type: 'donut',
      animations: {
        enabled: false,
      }
    },
    responsive: [{
      breakpoint: 480,
      options: {
        chart: {
          width: 200,
        },
        legend: {
          position: 'bottom'
        }
      }
    }],
    tooltip: {
      enabled: false,
    },
    title: {
      text: 'Resultado Geral',
      align: 'left'
    },
    colors:['#028f76', '#d14334']
  },


};



function SLD_DEBUG(){
  /*
    const [date, setDate] = useState(0);
    if (date == 0){
      refresh()
    }
    ;
    
    function refresh(){
      api
      .get("/teste")
      .then((response) => setDate(response.data.teste))
      .catch((err) => {
        console.error("ops! ocorreu um erro" + err);
    })}

    useEffect(() =>{
      const timerId = setInterval(refresh, 1000);
      return function cleanup() {
        clearInterval(timerId);
      };
    }, []); 
    */
    return(
      <div>
        <Box border="2px" boxShadow='lg' borderRadius='lg' borderColor="#c9f241" padding={'0 1em 0 1em'} height={300} width={450} m='1em 0 0 0'>
        <Center>
          <Text fontSize='1.5em' padding={'0.5em 0 0 0'} as='b'>DEBUG_SLD</Text>
        </Center>
      <Chart options={state.options} series={state.series} type="donut" height='75%' width='100%'/>
      </Box>
      </div>
      
    );

    }export default SLD_DEBUG;