function onloadFunction() {
    // Bind Switches (on/off)
    var switches = document.getElementsByClassName('pluggy-switch-bind');

    for (var i = 0; i < switches.length; i++) {
        switches[i].addEventListener('click', pluggyClick, false);
    }

    // Bind actions
    var actions = document.getElementsByClassName('pluggy-action-bind');

    for (var i = 0; i < actions.length; i++) {
        actions[i].addEventListener('click', actionClick, false)
    }

    /**
     * Handle Plug on/off button click
     * @param  {event} e The Event
     */
    function pluggyClick(e) {
        var switchId = e.target.dataset.plug;
        var checked  = e.target.dataset.plugMethod;
        var channel  = e.target.dataset.plugChannel;

        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'switch');
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.send('switch='+switchId+'&on='+checked+'&channel='+channel);
        
        xhr.onreadystatechange = _xhrFinish(xhr);
    }

    /**
     * Handle Action button click
     * @param  {event} e The Event
     */
    function actionClick(e) {
        var action = e.target.dataset.action;

        var xhr = new XMLHttpRequest();
        xhr.open('POST', 'action');
        xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
        xhr.send('action='+encodeURIComponent(action));

        xhr.onreadystatechange = _xhrFinish(xhr);
    }

    /**
     * Generic method for on xhr finish
     */
    function _xhrFinish(xhr) {
        var DONE = 4; // readyState 4 means the request is done.
        var OK = 200; // status 200 is a successful return.
        if (xhr.readyState === DONE) {
            if (xhr.status === OK) { 
                console.log(xhr.responseText); // 'This is the returned text.'
            } else {
                console.log('Error: ' + xhr.status); // An error occurred during the request.
            }
        }
    }
}

document.addEventListener('DOMContentLoaded', onloadFunction, false);