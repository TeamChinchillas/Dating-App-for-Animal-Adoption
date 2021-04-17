export default class User {
  constructor(data) {
    this.id = data.id_users
    this.username = data.username
    this.firstName = data.first_name
    this.lastName = data.last_name
    this.emailAddress = data.email_address
    this.userType = data.user_type
  }
}
