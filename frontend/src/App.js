import './App.css';
import Header from './components/Header';
import { ChakraProvider, Box, Wrap, WrapItem, SimpleGrid } from '@chakra-ui/react'
import MPO_0A from './components/MPO_0A';
import MPO_0B from './components/MPO_0B';
import MPO_0C from './components/MPO_0C';

import SLD_0A from './components/SLD_0A';
import SLD_0B from './components/SLD_0B';
import SLD_0C from './components/SLD_0C';
import SLD_0D_1 from './components/SLD_0D_1';
import SLD_0D_2 from './components/SLD_0D_2';
import SLD_0D_3 from './components/SLD_0D_3';

import MPO_DEBUG from './components/MPO_DEBUG';
import MPO_DEBUG_2 from './components/MPO_DEBUG_2';
import SLD_DEBUG from './components/SLD_DEBUG';
import SLD_DEBUG_2 from './components/SLD_DEBUG_2';

function App() {
  
  return (
    <ChakraProvider>
      <Header />
      <Wrap justify='center' spacing='1em' padding={['0.2em', '0.2em', '0.2em', '0.2em']}>
        <WrapItem>
          <MPO_0A/>
        </WrapItem>
        <WrapItem>
          <MPO_0B/>
        </WrapItem>
        <WrapItem>
          <MPO_0C/>
        </WrapItem>

        <WrapItem>
          <SLD_0B/>
        </WrapItem>
        <WrapItem>
          <SLD_0C/>
        </WrapItem>
        <WrapItem>
          <SLD_0D_1/>
        </WrapItem>
        <WrapItem>
          <SLD_0D_2/>
        </WrapItem>
        <WrapItem>
          <SLD_0D_3/>
        </WrapItem>

        <WrapItem>
          <SLD_DEBUG/>
        </WrapItem>
        <WrapItem>
          <SLD_DEBUG_2/>
        </WrapItem>
        <WrapItem>
          <MPO_DEBUG/>
        </WrapItem>
        <WrapItem>
          <MPO_DEBUG_2/>
        </WrapItem>

      </Wrap>
    </ChakraProvider> 
    
  );
}

export default App;