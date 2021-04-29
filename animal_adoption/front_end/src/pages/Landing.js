import { useContext } from 'react'
import UserContext from '../components/users/UserContext'
import LandingBeforeLogin from '../components/landing/LandingBeforeLogin'
import LandingForAdopters from '../components/landing/LandingForAdopters'
import LandingForShelters from '../components/landing/LandingForShelters'
import LandingForAdmins from '../components/landing/LandingForAdmins'

export default function Landing() {
  const { user } = useContext(UserContext)

  if (user?.isAdopter) {
    return <LandingForAdopters />
  }
  if (user?.isShelterWorker) {
    return <LandingForShelters />
  }
  if (user?.isAdministrator) {
    return <LandingForAdmins />
  }

  return <LandingBeforeLogin />
}
