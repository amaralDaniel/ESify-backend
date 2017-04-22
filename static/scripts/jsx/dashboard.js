/**
 * Created by danielamaral on 21/04/2017.
 */
/**
 * Created by danielamaral on 21/04/2017.
 */

var $ = require('jquery');


var Dashboard = React.createClass({

    getInitialState: function () {
        return {
            pSong: []
        };
    },

    songActions: function () {
      <UploadSong></UploadSong>
    },

    componentDidMount: function () {
        var self = this;
        $.get(this.props.source, function (result) {
            var collection = result;
            //console.log(collection)
            if (this.isMounted()) {
                this.setState({
                    pSong: collection
                });
            }
        }.bind(this));
    },

    render: function () {
        songs = this.state.pSong || [];
        return (
            <div>

                <button onClick={this.songActions}>Songs Actions</button>
            </div>

        );
    }
});

var UploadSong = React.createClass({
    doUpload: function () {
        fetch('/api/song/upload', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                album: document.getElementById('album').value,
                title: document.getElementById('title').value,
                artist: document.getElementById('artist').value,
                release_year: document.getElementById('release_year').value,
                song: document.getElementById('file').files[0],

            })
        }).then(response => {
           if(response.status != 200) {
               alert("something went wrong.")
               return
           }
           response.json()
               .then(json => {
                   alert("Upload successful!");

               })
        });
    },

    render: function () {
        songs = this.state.pSong || [];
        return (
            <div>
                <input type="text" id="title" placeholder="Song Title"/>
                <input type="text" id="album" placeholder="Album"/>
                <input type="text" id="release_year" placeholder="Release Year"/>
                <input type="text" id="artist" placeholder="Artist"/>
                <input type="file" id="file" size="60" />

                <button onClick={this.doUpload}>Upload</button>
            </div>

        );
    }
})

var LogoutButton = React.createClass({
    doLogout: function () {
        fetch('/api/authentication/logout', {
            method: 'GET',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            }
        }).then(function (data) {
            alert("logout done!")
        })
    },

    render: function () {
        return (
            <button type="submit" onClick={this.doLogout}></button>
        )
    }
});

ReactDOM.render(
    <Dashboard source="/api/song/"/>,
    document.getElementById('dashboard')
);