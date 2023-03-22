import { useState, useEffect} from 'react';
import api from "../../services/Api_service"
import Chart from "react-apexcharts"
import { Text, Center, Box, position } from '@chakra-ui/react'

const state = {
          
  series: [77, 2],
  options: {
    tooltip: {
      enabled: false,
    },
    chart: {
      width: 380,
      type: 'pie',
      animations: {
        enabled: false,
      }
    },
    title: {
      text: 'Resultado Geral',
      align: 'left'
    },
    labels: ['Aprovados', 'Reprovados'],
    colors:['#028f76', '#d14334']
  },
};

function MPO_0A(){
  
    const [date, setDate] = useState(0);
    if (date == 0){
      refresh()
    }
    ;
    
    function refresh(){
      api
      .get("/MPO_0A")
      .then((response) => setDate(response.data.MPO_0A))
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
        {console.log(date)}
        <Box border="2px" boxShadow='lg' borderRadius='lg' borderColor="#6F6" padding={'0 1em 0 1em'} height={300} width={450} m='1em 0 0 0'>
        <Center>
          <Text fontSize='1.5em' padding={'0.5em 0 0 0'} as='b'>MPO</Text>
        </Center>
      <Chart options={state.options} series={date} type="pie" height='75%' width='100%'/>
      </Box>
      </div>
      
    );

    }export default MPO_0A;