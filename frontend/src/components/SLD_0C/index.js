import { useState, useEffect} from 'react';
import api from "../../services/Api_service"
import Chart from "react-apexcharts"
import { Text, Center, Box, position } from '@chakra-ui/react'

const state = {
          
  series: [{
    name: 'Aprovados',
    data: [5, 13, 10, 10]
  }, {
    name: 'Reprovados',
    data: [2, 4, 1, 5],
  }],
  options: {
    tooltip: {
      enabled: false,
    },
    chart: {
      type: 'bar',
      height: 430,
      toolbar: {
        show: false
      },
      animations: {
        enabled: false,
      }      
    },
    plotOptions: {
      bar: {
        horizontal: false,
        dataLabels:{ 
          position: 'top'
        }
      }
    },
    dataLabels: {
      enabled: true,
      offsetX: 0,
      style: {
        fontSize: '12px',
        colors: ['#fff']
      }
    },
    title: {
      text: 'Resultado Hora',
      align: 'left'
    },
    stroke: {
      show: true,
      width: 1,
      colors: ['#fff']
    },
    xaxis: {
      categories: ['09:00', '10:00', '11:00', '12:00'],
    },
    yaxis: {
      title: {
        text: 'Unidades',
        style: {
          fontSize: '1em',
          fontWeight: 900
        }
      }
    },
    colors:['#028f76', '#d14334']
  },


};



function SLD_0C(){
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
        <Box border="2px" boxShadow='lg' borderRadius='lg' borderColor="#9cadf7" padding={'0 1em 0 1em'} height={300} width={450} m='1em 0 0 0'>
        <Center>
          <Text fontSize='1.5em' padding={'0.5em 0 0 0'} as='b'>SLD</Text>
        </Center>
      <Chart options={state.options} series={state.series} type="bar" height='75%' width='100%'/>
      </Box>
      </div>
      
    );

    }export default SLD_0C;