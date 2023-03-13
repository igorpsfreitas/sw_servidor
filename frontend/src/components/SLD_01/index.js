import { useState, useEffect} from 'react';
import api from "../../services/Api_service"
import Chart from "react-apexcharts"
import { Text, Center, Box } from '@chakra-ui/react'

const state = {
          
  series: [{
    name: 'Baia 01',
    data: [44, 55, 41]
  }, {
    name: 'Baia 02',
    data: [13, 23, 20]
  }, {
    name: 'Baia 03',
    data: [11, 17, 15]
  }],
  options: {
    chart: {
      type: 'bar',
      height: 350,
      stacked: true,
      toolbar: {
        show: true
      },
      zoom: {
        enabled: true
      },
      animations: {
        enabled: false
      },
      toolbar: {
        show: false
      },
      tooltip: {
        show: false,
        enabled: false
      }

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
    yaxis: {
      title: {
        text: 'Segundos',
        style: {
          fontSize: '1em',
          fontWeight: 900
        }
      }
    },
    plotOptions: {
      bar: {
        horizontal: false,
        borderRadius: 10,
        dataLabels: {
          total: {
            enabled: true,
            style: {
              fontSize: '13px',
              fontWeight: 900
            }
          }
        }
      },
    },
    xaxis: {
      type: 'text',
      categories: ['Posto-01', 'Posto-02', 'Posto-03'],
    },
    legend: {
      position: 'right',
      offsetY: 40
    },
    fill: {
      opacity: 1
    }
  }
}


function SLD_01(){
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
        <Box border="1px" borderColor="gray.200" padding={'0 1em 0 1em'} height={300} width={450}>
        <Center>
          <Text fontSize='1.5em' padding={'0.5em 0 0 0'}>SLD</Text>
        </Center>
        <Center>
          <Text fontSize='1em' padding={'0'}>Tempo médio de trabalho por posto</Text>
        </Center>
      <Chart options={state.options} series={state.series} type="bar" height='75%' width='100%'/>
      </Box>
      </div>
      
    );

    }export default SLD_01;