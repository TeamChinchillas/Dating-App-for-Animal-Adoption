import React, { Component } from 'react'

export default class SignupFormShelter extends Component {
  constructor(props) {
    super(props)
    this.state = {
      shelterName: '',
      address: '',
      phoneNumber: '',
    }

    this.submitForm = this.submitForm.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  submitForm(event) {
    console.log('Shelter Form submitted')
    console.log(event.target.shelterName.value)
    console.log(event.target.address.value)
    console.log(event.target.phoneNumber.value)
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

  render() {
    return (
      <div>
        <form onSubmit={this.submitForm}>
          <h1>Shelter Registration Form</h1>
          <br />
          <input
            type="text"
            name="shelterName"
            placeholder="Shelter Name"
            value={this.state.shelterName}
            onChange={this.handleChange}
          />
          <br />
          <input
            type="text"
            name="address"
            placeholder="Shelter Address"
            value={this.state.address}
            onChange={this.handleChange}
          />
          <br />
          <input
            type="text"
            name="phoneNumber"
            placeholder="Shelter Phone Number"
            value={this.state.shelterPhoneNumber}
            onChange={this.handleChange}
          />
          <br />
          <button type="submit">Register</button>
        </form>
      </div>
    )
  }
}
