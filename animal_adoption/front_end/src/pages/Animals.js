import { Switch, Route, useRouteMatch } from 'react-router-dom'
import AnimalDetail from '../components/animals/AnimalDetail'

export default function Animals() {
  const match = useRouteMatch()

  return (
    <Switch>
      <Route path={`${match.path}/create`}>
        <div>Create New Animal Profile</div>
      </Route>
      <Route path={`${match.path}/:animalId/edit`}>
        <div>Edit Animal Profile</div>
      </Route>
      <Route path={`${match.path}/:animalId`}>
        <AnimalDetail />
      </Route>
    </Switch>
  )
}
