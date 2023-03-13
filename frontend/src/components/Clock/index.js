import { useState, useEffect } from 'react';
import { Text } from '@chakra-ui/react'

function Clock(){
    const [date, setDate] = useState(new Date());
    
    function refreshClock() {
      setDate(new Date());
    }  useEffect(() => {
      const timerId = setInterval(refreshClock, 1000);
      return function cleanup() {
        clearInterval(timerId);
      };
    }, []);  return (
      <Text bg='#09456c' fontSize='2em' color='#ffffff' h='100%'>
        {date.toLocaleTimeString()}
      </Text>
      
    );
  }export default Clock;

