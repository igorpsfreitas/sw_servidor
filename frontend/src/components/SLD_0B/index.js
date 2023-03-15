import { useState, useEffect} from 'react';
import api from "../../services/Api_service"
import Chart from "react-apexcharts"
import { Text, Center, Box } from '@chakra-ui/react'

const state = {
          
  series: [{
    name: 'Aprovados',
    data: [77, 44, 66]
  }, {
    name: 'Reprovados',
    data: [33, 66, 33]
  }],
  options: {
  /*  title: {
      text: 'Grouped Labels on the X-axis'
    }, */
    chart: {
      type: 'bar',
      height: 350,
      stacked: true,
      stackType: '100%',
      zoom: {
        enabled: true
      },
      animations: {
        enabled: false
      },
      toolbar: {
        show: false
      },
      

    },
    tooltip: {
        show: false,
        enabled: false
      },
    responsive: [{
      breakpoint: 480,
      options: {
        legend: {
          position: 'bottom',
          offsetX: -10,
          offsetY: 0
        }
      }
    }],
    xaxis: {
      title: {
        text: 'Segundos',
        style: {
          fontSize: '0.8em',
          fontWeight: 900
        }
      }
    },
    plotOptions: {
      bar: {
        horizontal: true,
        borderRadius: 10
      },
    },
    xaxis: {
      type: 'text',
      categories: ['Posto-01', 'Posto-02', 'Posto-03'],
    },
    legend:{
      position: 'bottom',
          offsetX: -10,
          offsetY: 0,
    },
          fill: {
      opacity: 1
    },
    title: {
      text: 'Resultados Geral por Posto',
      align: 'left'
    },
    colors:['#028f76', '#d14334']
  }
}


function SLD_0B(){
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

    }export default SLD_0B;