import {Heading, Box, Wrap, WrapItem, SimpleGrid, Center, Text, Grid, GridItem, Flex, Spacer } from "@chakra-ui/react"
import Clock from "../Clock"


function Header(){
    return (
        <Grid templateColumns='repeat(5, 1fr)' >
            <GridItem colSpan={4}>
                <Text fontSize='1em' padding='0 0em' bg='#121d96' color='#FFFFFF' maxWidth='100%'>
                    <Text as='b'fontSize='2em' padding='0 1em' bg='#121d96' color='#FFFFFF'maxWidth='100%'>
                        DASHBOARD
                    </Text>
                </Text>
            </GridItem>
            <GridItem colSpan={1}>

            <Box bg='#121d96' textAlign='right' padding='0 1em' maxWidth='100%'>
                <Clock/>   
            </Box>
            </GridItem>
        </Grid>
    )

}

export default Header