import './App.css';
import Header from './components/Header';
import { ChakraProvider, Box, Wrap, WrapItem, Flex } from '@chakra-ui/react'
import T001 from './components/T001'
import T002 from './components/T002';
import T003 from './components/T003'
import T004 from './components/T004'



function App() {
  
  return (
    <ChakraProvider>
     
        <Header />
      
      
      
       <Wrap justify='center' spacing='1em' padding={['3em', '1em', '1em', '1em']}>
        <WrapItem>
          

            <T002/>
          
         
        </WrapItem>
        <WrapItem>
          

            <T003/>
          
         
        </WrapItem>
        <WrapItem>

            <T003/>
         
        </WrapItem>
        <WrapItem>
          

            <T003/>
          
         
        </WrapItem>
        <WrapItem>
          

          <T003/>
        
       
      </WrapItem>
      </Wrap>
      
      

    </ChakraProvider> 
    
  );
}

export default App;
