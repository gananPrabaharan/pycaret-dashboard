import React from 'react';
import { BrowserRouter, Route, Switch, Redirect } from 'react-router-dom';
import Navigation from './navigation';
import ImportWizard from "./import"
import Models from "./model"
import { SERVER, SESSION_ID } from "./util"

const App = () => {
    window.onbeforeunload = function() {
        const url = SERVER + "api/removeSession"
        let formData = new FormData();
        formData.append("sessionId", JSON.stringify(SESSION_ID));

        const options = {
            mode: "cors",
            credentials: "same-origin",
            method: "POST",
            headers: {"Accept": "application/json"},
            dataType: "json",
            body: formData
        };

        fetch(url, options)
            .then((response) => {
                if (response.status === 200) {
                    console.info('Logged Out')
                }
            });
    }

    return (
        <div id="automl">
            <BrowserRouter>
                <Navigation/>
                <Switch>
                    <Redirect exact from='/' to='/import'/>,
                    <Route exact path='/import' render={(props) => <ImportWizard />}/>
                    <Route exact path='/model' render={(props) => <Models />}/>
                </Switch>
            </BrowserRouter>
        </div>
    );
}

export default App;