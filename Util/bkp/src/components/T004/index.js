import { useState, useEffect} from 'react';
import api from "../../services/Api_service"
import Chart from "react-apexcharts"
import { Text, Center, Box, Spacer } from '@chakra-ui/react'

const state = {
          
  series: [{
    name: "Baia 01",
    data: [10, 41, 35, 51, 49, 62, 69]
},
{
  name: "Baia 02",
  data: [50, 51, 49, 62, 69, 91, 3]
},{
  name: "Baia 03",
  data: [40, 41, 35, 49, 62, 41, 25]
},{
  name: "Baia 04",
  data: [10, 41, 35, 51, 5, 62, 91]
},{
  name: "Baia 05",
  data: [32, 41, 49, 62, 69, 91, 80]
},{
  name: "Baia 06",
  data: [41, 35, 51, 49, 69, 42, 42]
},{
  name: "Baia 07",
  data: [38, 4, 35, 11, 49, 62, 69,]
},{
  name: "Baia 08",
  data: [13, 35, 49, 62, 69, 91, 14]
},{
  name: "Baia 08",
  data: [15, 41, 35, 62, 69, 11, 72]
}],

  options: {
    chart: {
      height: 350,
      type: 'line',

    toolbar: {
      show: false
    },
      zoom: {
        enabled: false
      }
    },
    dataLabels: {
      enabled: false
    },
    stroke: {
      curve: 'straight'
    },
  
    grid: {
      row: {
        colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
        opacity: 0.5
      },
    },
    xaxis: {
      categories: ['8:00', '8:30', '9:00', '9:30', '10:00', '10:30', '11:00'],
    },
    yaxis: {
      title: {
        text: 'Segundos'
      }
    }
    ,
    tooltip: {
      enabled: false
    }
  },


};;

function T004(){
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
        <Box border="1px" borderColor="gray.200"  minWidth={1000} >
        <Center>
        <Text fontSize='2em'>SLD</Text>

        </Center>
        <Center>
        <Text fontSize='1em'>Tempo de teste por baia</Text>

        </Center>
        

      <Chart options={state.options} series={state.series} type="line" height={350}  width="100%"/>
        
      </Box>
      </div>
      
    );

    }export default T004;