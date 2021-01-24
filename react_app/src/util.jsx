import config from './config.json'
import uuid from "uuid";

export const SESSION_ID = uuid.v4();

export const SERVER = "http://" + config.Deployment.HOST + ":" + config.Deployment.FLASK_PORT + "/"

export const getRequestOptions = (formData) => {
    const options = {
        mode: "cors",
        credentials: "same-origin",
        method: "POST",
        headers: {"Accept": "application/json"},
        dataType: "json"
    }

    if (formData != null){
        options["body"] = formData
    }

    return options
}

export const createSelectOptions = (optionList, labelFunction) => {
    if (optionList == null){
        return []
    }
    if (labelFunction == null){
        return optionList.map(opt => { return { "value": opt, "label": opt } })
    } else {
        return optionList.map(opt => { return { "value": opt, "label": labelFunction(opt) } })
    }
}