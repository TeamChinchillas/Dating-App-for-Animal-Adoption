import React from 'react'
import SignupFormUser from '../components/SignupFormUser'
import SignupFormShelter from '../components/SignupFormShelter'

function SignupPage() {
  const [showAdopter, setAdopterState] = React.useState(false)
  const [showShelter, setShelterState] = React.useState(false)

  return (
    <div>
      <h1> Sign up Page </h1>

      <button
        type="button"
        onClick={() => {
          setAdopterState(true)
          setShelterState(false)
        }}
      >
        Register as Adopter
      </button>
      <br />
      <button
        type="button"
        onClick={() => {
          setShelterState(true)
          setAdopterState(false)
        }}
      >
        Register as Shelter
      </button>
      <br />

      {showAdopter ? <SignupFormUser /> : null}

      {showShelter ? <SignupFormShelter /> : null}
    </div>
  )
}

export default SignupPage
