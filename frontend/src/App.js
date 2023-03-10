import './App.css';
import Header from './components/Header';
import { ChakraProvider, Box, Wrap, WrapItem, SimpleGrid } from '@chakra-ui/react'
import T001 from './components/T001'
import SLD_01 from './components/SLD_01';
import SLD_02 from './components/SLD_02';
import MPO_01 from './components/MPO_01';

function App() {
  
  return (
    <ChakraProvider>
     
      <Header />
    
      <Wrap justify='center' spacing='1em' padding={['0.2em', '0.2em', '0.2em', '0.2em']}>
        <WrapItem>
          <SLD_01/>
        </WrapItem>
        <WrapItem>
          <SLD_02/>
        </WrapItem>
        <WrapItem>
          <MPO_01/>
        </WrapItem>
        <WrapItem>
          <SLD_01/>
        </WrapItem>
        <WrapItem>
          <SLD_01/>
        </WrapItem>
        <WrapItem>
          <SLD_01/>
        </WrapItem>
        <WrapItem>
          <SLD_01/>
        </WrapItem>
        <WrapItem>
          <SLD_01/>
        </WrapItem>
        <WrapItem>
          <SLD_01/>
        </WrapItem>
        <WrapItem>
          <SLD_01/>
        </WrapItem>
        <WrapItem>
          <SLD_01/>
        </WrapItem>
        <WrapItem>
          <SLD_01/>
        </WrapItem>
      </Wrap>
    </ChakraProvider> 
    
  );
}

export default App;