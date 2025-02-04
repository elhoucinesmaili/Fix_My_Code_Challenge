var React = require('react/addons');
var Navbar = require('react-bootstrap').Navbar;
var NavBrand = require('react-bootstrap').NavBrand;
var Link = require('react-router').Link;

var Header = React.createClass({

    contextTypes: {
        router: React.PropTypes.func
    },

    render: function() {
        return (
            <Navbar>
                <NavBrand><Link to={`/`}>React Blog</Link></NavBrand> {/* Fixed Link usage */}
            </Navbar>
        );
    }
});

module.exports = Header;
