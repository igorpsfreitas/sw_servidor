import { useState, useEffect} from 'react';
import api from "../../services/Api_service"
import Chart from "react-apexcharts"
import { Text, Center, Box, position } from '@chakra-ui/react'

const state = {
          
  series: [{
    name: 'Aprovados',
    data: [23, 17, 19, 13, 15]
  }, {
    name: 'Reprovados',
    data: [8, 5, 6, 4, 2],
  }],
  options: {
    chart: {
      type: 'bar',
      height: 430,
      toolbar: {
        show: false
      },
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
    colors:['#2fd12a', '#d12a2a']
  },


};



function SLD_02(){
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
        <Box border="1px" borderColor="gray.200">
        <Center>
          <Text fontSize='1.5em' padding={'0.5em 0 0 0'}>SLD</Text>
        </Center>
        <Center>
          <Text fontSize='1em' padding={'0'}>Taxa de Aprovação e Reprovação</Text>
        </Center>
      <Chart options={state.options} series={state.series} type="bar" height={350} width={500}/>
      </Box>
      </div>
      
    );

    }export default SLD_02;