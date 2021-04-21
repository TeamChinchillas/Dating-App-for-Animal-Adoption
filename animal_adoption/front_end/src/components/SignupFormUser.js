import React, { Component } from 'react'

export default class SignupFormUser extends Component {
  constructor(props) {
    super(props)
    this.state = {
      first_name: '',
      last_name: '',
      email_address: '',
      animal_type: '',
      user_role: '',
    }

    this.submitForm = this.submitForm.bind(this)
    this.handleChange = this.handleChange.bind(this)
  }

  submitForm(event) {
    console.log('Form submitted')
    console.log(event.target.first_name.value)
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
        <h1> Registration Form</h1>
        <form onSubmit={this.submitForm}>
          <input
            type="text"
            name="first_name"
            placeholder="First Name"
            value={this.state.firstName}
            onChange={this.handleChange}
            required
          />
          <br />
          <input
            type="text"
            name="last_name"
            placeholder="Last Name"
            value={this.state.lastName}
            onChange={this.handleChange}
            required
          />
          <br />
          <input
            type="email"
            name="email"
            placeholder="Email Address"
            value={this.state.email}
            onChange={this.handleChange}
            required
          />
          <br />
          <label>Select Desired Animal Type:</label>
          <select value={this.state.animalType} onChange={this.handleChange} required>
            <option value="dog">Dog</option>
            <option value="cat">Cat</option>
            <option value="other">Other</option>
          </select>
          <br />
          <label>
            Select Animal Disposition:
            <br />
            <input
              type="checkbox"
              name="good_with_animals"
              checked={this.state.goodWithAnimals}
              onChange={this.handleChange}
            />
            Good with other animals
            <br />
            <input
              type="checkbox"
              name="good_with_children"
              checked={this.state.goodWithChildren}
              onChange={this.handleChange}
            />
            Good with other children
            <br />
            <input
              type="checkbox"
              name="animal_leashed"
              checked={this.state.animalLeashed}
              onChange={this.handleChange}
            />
            Animal must be leashed at all times
            <br />
            <br />
          </label>
          <button type="submit">Register</button>
        </form>
      </div>
    )
  }
}
