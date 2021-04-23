import React, { Component } from 'react'

export default class Login extends Component {
  constructor(props) {
    super(props)

    this.state = {
      email: '',
      password: '',
    }

    this.submitForm = this.submitForm.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  submitForm(event) {
    const { email, password } = this.state
    console.log('Submit Form Fired')
    console.log(event.target.email.value)
    console.log(event.target.password.value)
    // To view any field we enter "event.target.{field_name}.value"
    // Add code to connect to Flask API
    event.preventDefault()
  }

  handleChange(event) {
    console.log('Handle Change')
    this.setState({
      [event.target.name]: event.target.value,
    })
    console.log(event.target.name)
  }

  // Add handle successful login function

  render() {
    return (
      <div>
        <h1>Login Page</h1>
        <br />
        <form onSubmit={this.submitForm}>
          <input
            type="email"
            name="email"
            placeholder="Email"
            value={this.state.email}
            onChange={this.handleChange}
          />
          <br />
          <input
            type="password"
            name="password"
            placeholder="Password"
            value={this.state.password}
            onChange={this.handleChange}
          />
          <br />
          <button type="submit">Login</button>
        </form>
      </div>
    )
  }
}
