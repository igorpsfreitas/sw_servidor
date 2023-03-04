import { useState, useEffect} from 'react';
import api from "../../services/Api_service"
import Chart from "react-apexcharts"
import { Text, Center, Box } from '@chakra-ui/react'

const state = {
          
  series: [{
    name: 'Aprovados',
    data: []
  }, {
    name: 'Debug',
    data: []
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
      categories: [],
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

function T003(){
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
        <Text fontSize='2em'>$var0233</Text>

        </Center>
      <Chart options={state.options} series={state.series} type="bar" height={350} width={500}/>
      </Box>
      </div>
      
    );

    }export default T003;