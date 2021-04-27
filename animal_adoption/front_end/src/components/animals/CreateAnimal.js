import { Container, Heading, Button } from '@chakra-ui/react'
import { useState } from 'react'
import { useHistory } from 'react-router-dom'
import Animal from '../../models/Animal'
import FormEditAnimal from './FormEditAnimal'

export default function CreateAnimal() {
  const [animal, setAnimal] = useState(new Animal())

  const history = useHistory()
  /**
   * TODO: Send new animal profile to the server
   * TODO: Validation
   */
  const submit = () => {
    history.push('/') // back to home page
  }

  return (
    <Container mt="2" centerContent>
      <Heading mb="2">Create new animal profile</Heading>
      <FormEditAnimal animal={animal} setAnimal={setAnimal} />
      <Button mt="5" colorScheme="teal" onClick={submit}>
        Submit
      </Button>
    </Container>
  )
}
