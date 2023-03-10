import { useState, useEffect} from 'react';
import api from "../../services/Api_service"
import Chart from "react-apexcharts"
import { Text, Center, Box, position } from '@chakra-ui/react'

const state = {
          
  series: [{
    name: 'Aprovados',
    data: [13, 10, 10, 11, 8]
  }, {
    name: 'Reprovados',
    data: [4, 1, 5, 3, 2],
  }],
  options: {
    chart: {
      type: 'bar',
      height: 430,
      toolbar: {
        show: false
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
    stroke: {
      show: true,
      width: 1,
      colors: ['#fff']
    },
    tooltip: {
      shared: true,
      intersect: false
    },
    xaxis: {
      categories: ['10:00','10:30', '11:00', '11:30', '12:00'],
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
    colors:['#2fd12a', '#d12a2a']
  },


};



function MPO_01(){
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
        <Box border="1px" boxShadow='lg' borderRadius='lg' borderColor="gray.200" padding={'0 1em 0 1em'} height={300} width={450} m='1em 0 0 0'>
        <Center>
          <Text fontSize='1.5em' padding={'0.5em 0 0 0'} as='b'>MPO</Text>
        </Center>
        <Center>
          <Text fontSize='1em' padding={'0'}>Taxa de Aprovação e Reprovação</Text>
        </Center>
      <Chart options={state.options} series={state.series} type="bar" height='75%' width='100%'/>
      </Box>
      </div>
      
    );

    }export default MPO_01;