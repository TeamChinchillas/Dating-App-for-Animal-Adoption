export default class User {
  constructor(data) {
    this.username = data.username
    this.firstName = data.first_name
    this.lastName = data.last_name
    this.emailAddress = data.username
    this.userType = data.user_type
  }

  get isShelterWorker() {
    return this.userType === 'shelter worker'
  }

  get isAdopter() {
    return this.userType === 'adopter'
  }

  get isAdministrator() {
    return this.userType === 'administrator'
  }
}
