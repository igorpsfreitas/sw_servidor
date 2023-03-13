import {Heading, Box, Wrap, WrapItem, SimpleGrid, Center, Text, Grid, GridItem, Flex, Spacer } from "@chakra-ui/react"
import Clock from "../Clock"


function Header(){
    return (
        <Box boxShadow='dark-lg'>
            <Grid templateColumns='repeat(5, 1fr)' >
                <GridItem colSpan={4}>
                    <Text fontSize='1em' padding='0 0em' bg='#09456c' color='#FFFFFF' maxWidth='100%'>
                        <Text textShadow='2px 2px #9b0800' as='b'fontSize='2em' padding='0 1em' bg='#09456c' color='#FFFFFF'maxWidth='100%'>
                            DASHBOARD
                        </Text>
                    </Text>
                </GridItem>
                <GridItem colSpan={1}>

                <Box textShadow='2px 2px #9b0800' bg='#09456c' textAlign='right' padding='0 1em' maxWidth='100%'>
                    <Clock/>   
                </Box>
                </GridItem>
            </Grid>
        </Box>
    )

}

export default Header