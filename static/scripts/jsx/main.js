/**
 * Created by danielamaral on 21/04/2017.
 */
var InitialPage = React.createClass({

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
            <div className="update-label">
                <div class="vcenter">
                    <input type="text" placeholder="Email" onChange={this.updateEmail}/>
                    <input type="password" placeholder="Password" onChange={this.updatePassword}/>
                    <input type="text" placeholder="Username" onChange={this.updateUsername}/>
                </div>
                <button onClick={this.doLogin}>Login</button>
                <button onClick={this.doRegister}>Register</button>

                <Label value={this.state.value1}/>
                <Label value={this.state.value2}/>
                <Label value={this.state.value3}/>
            </div>

        )
    }
});



var Label = React.createClass({

    render: function () {
        return (
            <div class="my-label">
                <h2>{this.props.value}</h2>
            </div>
        )
    }
});




ReactDOM.render(
    <InitialPage/>,
    document.getElementById('main')

);