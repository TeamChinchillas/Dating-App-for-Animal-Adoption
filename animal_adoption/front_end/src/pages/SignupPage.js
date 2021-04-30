import React from 'react'
import SignupFormUser from '../components/SignupFormUser'
import SignupFormShelterWorker from '../components/SignupFormShelterWorker'

function SignupPage() {
  const [showAdopter, setAdopterState] = React.useState(false)
  const [showShelterWorker, setShelterWorkerState] = React.useState(false)

  return (
    <div>
      <h1> Sign up Page </h1>

      <button
        type="button"
        onClick={() => {
          setAdopterState(true)
          setShelterWorkerState(false)
        }}
      >
        Register as Adopter
      </button>
      <br />
      <button
        type="button"
        onClick={() => {
          setShelterWorkerState(true)
          setAdopterState(false)
        }}
      >
        Register as Shelter
      </button>
      <br />

      {showAdopter ? <SignupFormUser /> : null}

      {showShelterWorker ? <SignupFormShelterWorker /> : null}
    </div>
  )
}

export default SignupPage
