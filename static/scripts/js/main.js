(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
/**
 * Created by danielamaral on 21/04/2017.
 */
var InitialPage = React.createClass({displayName: "InitialPage",

    updateEmail: function (event) {
        this.setState({value1: event.target.value});
    },
    updatePassword: function (event) {
        this.setState({value2: event.target.value});
    },
    updateUsername: function (event) {
        this.setState({value3: event.target.value});
    },
    getInitialState: function () {
        return {
            showInitialPage : false
        }
    },
    // sets state, triggers render method
    handleChange: function (event) {
        // grab value form input box
        this.setState({searchString: event.target.value});
        console.log("scope updated!");
    },
    componentWillMount: function () {
        this.setState({value: this.state.value})
    },
    doLogin: function () {
        fetch('/api/authentication/login', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: this.state.value1,
                password: this.state.value2,
                username: this.state.value3
            })
        }).then(response => {
           if(response.status != 200) {
               alert("something went wrong.")
               return
           }
           response.json()
               .then(json => {
                   alert("Login successful!");

               })
        });
    },
    doRegister: function () {
        fetch('/api/authentication/register', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email: this.state.value1,
                password: this.state.value2,
                username: this.state.value3
            })
        }).then(response => {
           if(response.status != 200) {
               alert("something went wrong.")
               return
           }
           response.json()
               .then(json => {
                   alert("Registration successful!");

               })
        });
    },

    render: function () {

        return (
            React.createElement("div", {className: "update-label"}, 
                React.createElement("div", {class: "vcenter"}, 
                    React.createElement("input", {type: "text", placeholder: "Email", onChange: this.updateEmail}), 
                    React.createElement("input", {type: "password", placeholder: "Password", onChange: this.updatePassword}), 
                    React.createElement("input", {type: "text", placeholder: "Username", onChange: this.updateUsername})
                ), 
                React.createElement("button", {onClick: this.doLogin}, "Login"), 
                React.createElement("button", {onClick: this.doRegister}, "Register"), 

                React.createElement(Label, {value: this.state.value1}), 
                React.createElement(Label, {value: this.state.value2}), 
                React.createElement(Label, {value: this.state.value3})
            )

        )
    }
});



var Label = React.createClass({displayName: "Label",

    render: function () {
        return (
            React.createElement("div", {class: "my-label"}, 
                React.createElement("h2", null, this.props.value)
            )
        )
    }
});




ReactDOM.render(
    React.createElement(InitialPage, null),
    document.getElementById('main')

);

},{}]},{},[1]);
