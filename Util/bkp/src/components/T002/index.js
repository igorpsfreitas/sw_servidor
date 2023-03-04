import { useState, useEffect} from 'react';
import api from "../../services/Api_service"
import Chart from "react-apexcharts"
import { Text, Center, Box } from '@chakra-ui/react'

const state = {
          
  series: [{
    name: 'Aprovados',
    data: [76, 85, 101, 98, 87]
  }, {
    name: 'Debug',
    data: [44, 55, 57, 56, 61]
  }],
  options: {
    
    colors:['#008000', '#BB0000'],
    chart: {
      animations: {
        enabled: false
      },
      toolbar:{
        show: false
      },
      type: 'bar',
      height: 350
    },
    toolbar: {
      show: false
    },
    plotOptions: {
      bar: {
        horizontal: false,
        columnWidth: '55%',
        endingShape: 'rounded'
      },
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      show: true,
      width: 2,
      colors: ['transparent']
    },
    xaxis: {
      categories: ['8:00', '8:30', '9:00', '9:30', '10:00'],
    },
    yaxis: {
      title: {
        text: 'Unidades'
      }
    },
    fill: {
      opacity: 1
    },
    tooltip: {
      enabled: false
    }

  }
};

function T002(){
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
        <Text fontSize='2em'>Saida MPO</Text>

        </Center>
      <Chart options={state.options} series={state.series} type="bar" height={350} width={500}/>
      </Box>
      </div>
      
    );

    }export default T002;